"""Versión animada del motor: transiciones suaves al aparecer cada bloque, al cambiar de escena y de subtítulo.
Usa las mismas escenas, audios y subtítulos que engine.build; solo cambia cómo se dibujan los fotogramas."""
import os, json, re, subprocess, hashlib
from engine import *
import engine

FPS = 25
MAXT = 3.4  # segundos máximos de animación por cambio

def body_anim(tema, scene, k, sub, prog, new=(), enter=False, subnew=False, prev_k=0):
    cls, inner = engine.body(tema, scene, k, sub, prog)
    order = {i: n for n, i in enumerate(sorted(new))}
    def rep(m):
        rep.i += 1; i = rep.i
        tag = m.group(0); extra = ''
        if i < k - 1: extra += ' dim'
        if i in order: extra += ' new'
        elif not enter and i == prev_k - 1 and k > prev_k: extra += ' justdim'
        tag = tag.replace('class="b', 'class="b' + extra, 1)
        if i in order: tag = tag[:-1] + f' style="--i:{order[i]}">'
        return tag
    rep.i = -1
    inner = re.sub(r'<div class="b[^"]*">', rep, inner)
    if subnew: inner = inner.replace('<div class="sub">', '<div class="sub new">')
    if enter:
        if scene.kind in ('card', 'title'): inner += '<div class="wipe"></div>'
        else: inner += f'<div class="wipe"><b>{esc(KIND_LABEL.get(scene.kind, ""))}</b><i>{esc((scene.sec + " " + scene.title).strip())}</i></div>'
    cls += ' anim' + (' enter' if enter else '')
    return cls, inner

def cue_times(seg, cues):
    import numpy as np, wave as _w
    n = len(cues); L = sum(len(c) for c in cues) or 1
    if not seg['audio']:
        sp = seg['dur'] - PAD; acc = 0; out = []
        for c in cues: out.append(sp * acc / L); acc += len(c)
        return out
    w = _w.open(seg['audio']); a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float); sr = w.getframerate()
    hop = sr // 100
    e = np.sqrt(np.convolve(a ** 2, np.ones(hop) / hop, 'same'))[::hop]; on = e > 400
    if not on.any(): return [seg['dur'] * i / n for i in range(n)]
    st = on.argmax() * .01; en = (len(on) - on[::-1].argmax()) * .01
    pauses = []; i = 0
    while i < len(on):
        if not on[i]:
            j = i
            while j < len(on) and not on[j]: j += 1
            if j - i >= 12 and i * .01 > st and j * .01 < en: pauses.append((i * .01, j * .01))
            i = j
        else: i += 1
    out = [0.0]; acc = 0; used = set()
    for ci in range(1, n):
        acc += len(cues[ci - 1]); est = st + (en - st) * acc / L
        best = None
        for pi, (p0, p1) in enumerate(pauses):
            if pi in used: continue
            d = abs((p0 + p1) / 2 - est)
            if d < 1.5 and (best is None or d < best[0]) and p1 - .08 > out[-1] + .5: best = (d, pi, p1 - .08)
        if best: used.add(best[1]); out.append(best[2])
        else: out.append(max(est - .05, out[-1] + .5))
    return out

PREP_JS = '''()=>{const A=document.getAnimations();A.forEach(a=>a.pause());window.__A=A;
 let e=0;A.forEach(a=>{const t=a.effect.getComputedTiming();e=Math.max(e,t.endTime||0)});return e/1000;}'''
SEEK_JS = '''(t)=>{window.__A.forEach(a=>a.currentTime=t*1000);}'''

def build_anim(tema, scenes, name=None, render=True):
    tid = tema['id']; name = name or tid
    fdir = os.path.join(ROOT, 'frames_a', name); os.makedirs(fdir, exist_ok=True)
    for f in os.listdir(fdir): os.remove(os.path.join(fdir, f))
    adir = os.path.join(ROOT, 'audio', tid)
    segs = []
    for si, sc in enumerate(scenes):
        for k, text in sc.segs:
            sid = 'f' + hashlib.sha1(spoken(text).encode('utf-8')).hexdigest()[:12]
            a = os.path.join(adir, sid + '.wav')
            dur = max((wav_dur(a) if os.path.exists(a) else len(text) / CHARS_PER_SEC) + PAD, 1.6)
            segs.append({'id': sid, 'scene': si, 'k': k, 'text': text, 'dur': dur, 'audio': a if os.path.exists(a) else None})
    total = sum(s['dur'] for s in segs)
    frames, t = [], 0.0
    srt = []
    for s_ in segs:
        cues = split_cues(s_['text']) or ['']
        bounds = cue_times(s_, cues)  # instantes (relativos al segmento) en que empieza cada cue
        for ci, c in enumerate(cues):
            st = bounds[ci]; en = bounds[ci + 1] if ci + 1 < len(cues) else s_['dur']
            frames.append({'scene': s_['scene'], 'k': s_['k'], 'sub': c, 'dur': en - st, 't': t + st})
            srt.append((t + st, t + en, c))
        t += s_['dur']
    def ts(x):
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); q, ms = divmod(ms, 1000)
        return f'{h:02d}:{m:02d}:{q:02d},{ms:03d}'
    os.makedirs(os.path.join(ROOT, 'out_a'), exist_ok=True)
    with open(os.path.join(ROOT, 'out_a', f'{name}.srt'), 'w') as f:
        for i, (x, y, c) in enumerate(srt, 1): f.write(f'{i}\n{ts(x)} --> {ts(y)}\n{c}\n\n')
    lst = []  # (fichero, duración)
    if render:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
            pg = br.new_page(viewport={'width': W, 'height': H})
            base = os.path.join(ROOT, 'base.html'); open(base, 'w').write(page(tema, scenes[0], 0, '', 0))
            pg.goto('file://' + base, wait_until='load'); pg.evaluate('()=>document.fonts.ready'); pg.wait_for_timeout(200)
            prev = (None, 0, None); n = 0
            carry = None  # (t0, new, end) de una entrada de escena que aún no ha terminado
            def shot(d):
                nonlocal n
                fn = f'{n:06d}.jpg'; pg.screenshot(path=os.path.join(fdir, fn), type='jpeg', quality=92); n += 1
                lst.append((fn, d))
            for fr in frames:
                sc, k, sub = fr['scene'], fr['k'], fr['sub']
                enter = sc != prev[0]
                subnew = sub != prev[2]
                if carry and not enter and k == prev[1]:
                    t0, cnew, cend = carry; off = fr['t'] - t0
                    cls, inner = body_anim(tema, scenes[sc], k, sub, (fr['t'] + fr['dur']) / total, cnew, True, False, 0)
                else:
                    carry = None; off = 0.0
                    new = range(0, k) if enter else range(prev[1], k)
                    cls, inner = body_anim(tema, scenes[sc], k, sub, (fr['t'] + fr['dur']) / total, new, enter, subnew, prev[1])
                pg.evaluate(FIT_JS, [cls.replace(' anim', '').replace(' enter', ''), inner.replace(' new', ' ')])
                pg.evaluate('([c,h])=>{const z=document.querySelector("main .inner").style.zoom;document.body.className=c;document.body.innerHTML=h;const i=document.querySelector("main .inner");if(i)i.style.zoom=z;}', [cls, inner])
                if enter: pg.evaluate('()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r})))')
                end = min(pg.evaluate(PREP_JS), MAXT)
                if enter and not carry: carry = (fr['t'], range(0, k), end)
                todo = max(0.0, end - off); nt = min(int(todo * FPS), int(fr['dur'] * FPS))
                for j in range(nt):
                    pg.evaluate(SEEK_JS, off + j / FPS); shot(1 / FPS)
                if nt * 1 / FPS < fr['dur'] - 1e-3:
                    pg.evaluate(SEEK_JS, off + nt / FPS if todo > fr['dur'] else 30.0); shot(fr['dur'] - nt / FPS)
                if carry and off + fr['dur'] >= carry[2]: carry = None
                prev = (sc, k, sub)
            br.close()
    lf = os.path.join(fdir, 'list.txt')
    with open(lf, 'w') as f:
        for fn, d in lst: f.write(f"file '{fn}'\nduration {d:.4f}\n")
        f.write(f"file '{lst[-1][0]}'\n")
    silent = os.path.join(ROOT, 'out_a', f'{name}_sinvoz.mp4'); os.makedirs(os.path.dirname(silent), exist_ok=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lf, '-vf', f'fps={FPS},format=yuv420p',
                    '-c:v', 'libx264', '-crf', '21', '-preset', 'veryfast', silent], check=True, cwd=fdir)
    final = None
    if all(s['audio'] for s in segs):
        parts = []
        for s in segs:
            padded = os.path.join(adir, s['id'] + '_p.wav')
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', s['audio'], '-af', f"apad=whole_dur={s['dur']:.3f}", '-ar', '44100', '-ac', '1', padded], check=True)
            parts.append(padded)
        alst = os.path.join(fdir, 'alist.txt')
        with open(alst, 'w') as f:
            for p_ in parts: f.write(f"file '{p_}'\n")
        final = os.path.join(ROOT, 'out_a', f'{name}.mp4')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent, '-f', 'concat', '-safe', '0', '-i', alst, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', final], check=True)
    return total, len(lst), final
