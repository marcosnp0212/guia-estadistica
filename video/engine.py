"""Motor de vídeos: escenas -> fotogramas (HTML + Playwright) -> subtítulos -> vídeo (ffmpeg).
Cada escena tiene una diapositiva (bloques) y segmentos de locución (k bloques visibles, texto).
Sin audio: duración estimada. Con audio (audio/<tema>/<seg>.wav): duración real."""
import html, json, os, re, subprocess, math, wave, contextlib
ROOT = '/home/claude/video'
CHARS_PER_SEC = 14.5   # ritmo estimado de una voz TTS en español
PAD = 0.45             # silencio tras cada segmento
W, H = 1920, 1080

# ---------- bloques ----------
def esc(s): return html.escape(s, quote=False)
def md(s):
    """**negrita**, `código`, _subrayado_ y saltos."""
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'__(.+?)__', r'<u>\1</u>', s)
    s = re.sub(r'S_XY', 'S<sub>XY</sub>', s).replace(' %', '\u00a0%')
    return s.replace('\n', '<br>')
def P(t, cls=''): return f'<p class="p {cls}">{md(t)}</p>'
def Li(t): return f'<div class="li">{md(t)}</div>'
def Step(n, t): return f'<div class="step"><span class="n">{n}</span><span>{md(t)}</span></div>'
def F(t, cls=''): return f'<div class="f {cls}">' + re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t) + '</div>'          # html ya preparado
def frac(a, b): return f'<span class="fr"><span>{a}</span><span>{b}</span></span>'
def Big(t): return f'<div class="big">{md(t)}</div>'
def Enun(t): return f'<div class="enun">{md(t)}</div>'
def Res(t): return f'<div class="res">{md(t)}</div>'
def Ojo(t): return f'<div class="ojo">{md(t)}</div>'
def Truco(t): return f'<div class="truco">{md(t)}</div>'
def XL(formula, note=''):
    n = f'<span class="xn">{md(note)}</span>' if note else ''
    return f'<div class="xl"><span class="fx">fx</span><code>{esc(formula)}</code>{n}</div>'
def T(headers, rows, hl_col=None, hl_row=None, small=False):
    isn = lambda v: bool(re.fullmatch(r'[−\-+]?[\d.,\s]+%?|—', str(v).replace('**', '').strip()))
    ncol = [sum(isn(r[ci]) for r in rows if ci < len(r)) * 2 > len(rows) for ci in range(len(headers))]
    h = ''.join(f'<th class="{"num" if ncol[ci] else ""}">{md(str(x))}</th>' for ci, x in enumerate(headers))
    body = ''
    for ri, r in enumerate(rows):
        tds = ''
        for ci, v in enumerate(r):
            c = []
            if hl_col is not None and ci in (hl_col if isinstance(hl_col, (list, tuple)) else [hl_col]): c.append('hc')
            if hl_row is not None and ri in (hl_row if isinstance(hl_row, (list, tuple)) else [hl_row]): c.append('hr')
            if re.fullmatch(r'[−\-+]?[\d.,\s]+%?|—', str(v).replace('**', '').strip()): c.append('num')
            tds += f'<td class="{" ".join(c)}">{md(str(v))}</td>'
        body += f'<tr style="--r:{ri+1}">{tds}</tr>'
    return f'<table class="t{" sm" if small else ""}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>'
def Img(name, w=1100): return f'<div class="img"><img src="file:///home/claude/web/img/{name}" style="width:{w}px"></div>'
def Row(*blocks): return '<div class="row">' + ''.join(f'<div class="col">{b}</div>' for b in blocks) + '</div>'

# ---------- escenas ----------
class Scene:
    def __init__(self, sec, title, kind='teo', blocks=None, segs=None, layout=''):
        self.sec, self.title, self.kind, self.blocks, self.segs, self.layout = sec, title, kind, blocks or [], segs or [], layout
KIND_LABEL = {'enun': 'Enunciado', 'teo': 'Teoría', 'mano': 'A mano, con calculadora', 'xl': 'En Excel', 'int': 'Cómo se interpreta', 'res': 'Resumen', 'card': '', 'title': ''}

CSS = open(os.path.join(ROOT, 'video.css')).read() if os.path.exists(os.path.join(ROOT, 'video.css')) else ''

def page(tema, scene, k, sub, prog):
    cls, inner = body(tema, scene, k, sub, prog)
    css = open(os.path.join(ROOT, 'video.css')).read()
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body class="{cls}">{inner}</body></html>'

def body(tema, scene, k, sub, prog):
    tb = [b for b in scene.blocks if b.startswith('<table')]
    split = 'split' in scene.layout or ('full' not in scene.layout and len(tb) == 1 and len(scene.blocks) - 1 >= 3 and scene.kind in ('mano', 'teo', 'int'))
    if split and 'split' not in scene.layout: scene.layout += ' split'
    def L(b): return ' L' if split and (b.startswith('<table') or b.startswith('<div class="img"')) else ''
    blocks = ''.join(f'<div class="b{L(b)}{" on" if i < k else ""}{" cur" if i == k - 1 and scene.kind not in ("card","title") else ""}">{b}</div>' for i, b in enumerate(scene.blocks))
    lab = KIND_LABEL.get(scene.kind, '')
    head = '' if scene.kind in ('card', 'title') else f'<header><span class="tab">{esc(tema["tab"])}</span><span class="sec">{esc(scene.sec)} {esc(scene.title)}</span><span class="kind k-{scene.kind}">{esc(lab)}</span></header>'
    subh = f'<div class="sub"><span><em>{esc(sub)}</em></span></div>' if sub else ''
    return f"t-{tema['color']} kind-{scene.kind} {scene.layout}", f'{head}<main><div class="inner">{blocks}</div></main><div class="prog"><span style="width:{prog*100:.2f}%"></span></div>{subh}'

FIT_JS = '''([c,h])=>{document.body.className=c;document.body.innerHTML=h;
 const m=document.querySelector('main'),i=document.querySelector('main .inner');if(!i)return 1;let z=1;i.style.zoom=1;
 const H=m.clientHeight,W=m.clientWidth;
 while((i.getBoundingClientRect().height>H+2||i.scrollWidth*z>W+2)&&z>0.5){z-=0.03;i.style.zoom=z;}return z;}'''

# ---------- subtítulos ----------
def split_cues(text, maxlen=84):
    """Corta el texto en trozos de como mucho 2 líneas (~42 c/línea), por frases y comas."""
    text = re.sub(r'\s+', ' ', text.strip())
    parts = re.split(r'(?<=[.!?…:;])\s+', text)
    out = []
    for p in parts:
        while len(p) > maxlen:
            cut = max(p.rfind(', ', 0, maxlen), p.rfind(' y ', 0, maxlen), p.rfind(' que ', 0, maxlen))
            if cut < maxlen * 0.45: cut = p.rfind(' ', 0, maxlen)
            out.append(p[:cut + 1].strip()); p = p[cut + 1:].strip()
        if p: out.append(p)
    # junta trozos muy cortos
    res = []
    for c in out:
        if res and len(res[-1]) + len(c) + 1 <= maxlen and (len(c) < 28 or len(res[-1]) < 24): res[-1] += ' ' + c
        else: res.append(c)
    return res

def wav_dur(p):
    with contextlib.closing(wave.open(p)) as w: return w.getnframes() / float(w.getframerate())

def spoken(text):
    """Texto que dirá la voz: igual que el subtítulo, pero con símbolos leídos."""
    t = text
    for a, b in [('x̄', 'equis barra'), ('ȳ', 'y barra'), ('S²', 'ese cuadrado'), ('s²', 'ese minúscula al cuadrado'), ('R²', 'erre cuadrado'),
                 ('Σ', 'suma de '), ('nᵢ', 'ene sub i'), ('fᵢ', 'efe sub i'), ('Nᵢ', 'ene mayúscula sub i'), ('Fᵢ', 'efe mayúscula sub i'), ('xᵢ', 'equis sub i'),
                 ('C₁', 'C uno'), ('C₃', 'C tres'), ('%', ' por ciento'), ('≥', 'mayor o igual que'), ('÷', 'entre'), ('×', 'por'), ('−', 'menos'), ('√', 'raíz de '), ('Sx', 'ese de equis'), ('Sy', 'ese de y'), (' + ', ' más '), (' = ', ' igual a '), ('…', '...')]:
        t = t.replace(a, b)
    return t

# ---------- construcción ----------
def build(tema, scenes, render=True, video=True):
    tid = tema['id']
    fdir = os.path.join(ROOT, 'frames', tid); os.makedirs(fdir, exist_ok=True)
    adir = os.path.join(ROOT, 'audio', tid)
    segs = []
    for si, sc in enumerate(scenes):
        for gi, (k, text) in enumerate(sc.segs):
            import hashlib
            sid = 'f' + hashlib.sha1(spoken(text).encode('utf-8')).hexdigest()[:12]
            a = os.path.join(adir, sid + '.wav')
            dur = wav_dur(a) + PAD if os.path.exists(a) else len(text) / CHARS_PER_SEC + PAD
            dur = max(dur, 1.6)
            segs.append({'id': sid, 'scene': si, 'k': k, 'text': text, 'dur': dur, 'audio': a if os.path.exists(a) else None})
    # guion para la voz
    with open(os.path.join(ROOT, 'out', f'{tid}_guion.json'), 'w') as f:
        json.dump([{'id': s['id'], 'texto': spoken(s['text']), 'subtitulo': s['text']} for s in segs], f, ensure_ascii=False, indent=1)
    total = sum(s['dur'] for s in segs)
    # cues
    frames, srt, t = [], [], 0.0
    for s in segs:
        cues = split_cues(s['text']) or ['']
        L = sum(len(c) for c in cues) or 1
        speak = s['dur'] - PAD
        for ci, c in enumerate(cues):
            d = speak * len(c) / L
            if ci == len(cues) - 1: d += PAD
            frames.append({'scene': s['scene'], 'k': s['k'], 'sub': c, 'dur': d, 't': t})
            srt.append((t, t + d - (PAD if ci == len(cues) - 1 else 0), c)); t += d
    def ts(x):
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s_, ms = divmod(ms, 1000)
        return f'{h:02d}:{m:02d}:{s_:02d},{ms:03d}'
    with open(os.path.join(ROOT, 'out', f'{tid}.srt'), 'w') as f:
        for i, (a, b, c) in enumerate(srt, 1): f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{c}\n\n')
    if render:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            br = p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
            pg = br.new_page(viewport={'width': W, 'height': H})
            base = os.path.join(ROOT, 'base.html'); open(base, 'w').write(page(tema, scenes[0], 0, '', 0))
            pg.goto('file://' + base, wait_until='load'); pg.evaluate('()=>document.fonts.ready'); pg.wait_for_timeout(200)
            last = None
            for i, fr in enumerate(frames):
                cls, inner = body(tema, scenes[fr['scene']], fr['k'], fr['sub'], (fr['t'] + fr['dur']) / total)
                pg.evaluate(FIT_JS, [cls, inner])
                if fr['scene'] != last:
                    pg.evaluate('()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r})))'); last = fr['scene']
                pg.screenshot(path=os.path.join(fdir, f'{i:05d}.png'))
            br.close()
    if video:
        lst = os.path.join(fdir, 'list.txt')
        with open(lst, 'w') as f:
            for i, fr in enumerate(frames):
                f.write(f"file '{i:05d}.png'\nduration {fr['dur']:.3f}\n")
            f.write(f"file '{len(frames)-1:05d}.png'\n")
        silent = os.path.join(ROOT, 'out', f'{tid}_sinvoz.mp4')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-vf', 'fps=10,format=yuv420p',
                        '-c:v', 'libx264', '-tune', 'stillimage', '-crf', '22', '-preset', 'veryfast', silent], check=True, cwd=fdir)
        if all(s['audio'] for s in segs):
            # pista de audio: cada segmento + silencio hasta su duración
            alst = os.path.join(adir, 'alist.txt'); parts = []
            for s in segs:
                padded = os.path.join(adir, s['id'] + '_p.wav')
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', s['audio'], '-af', f"apad=whole_dur={s['dur']:.3f}", '-ar', '44100', '-ac', '1', padded], check=True)
                parts.append(padded)
            with open(alst, 'w') as f:
                for p_ in parts: f.write(f"file '{p_}'\n")
            final = os.path.join(ROOT, 'out', f"{tid}.mp4")
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', silent, '-f', 'concat', '-safe', '0', '-i', alst, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', final], check=True)
    return total, len(frames)

def card(tab, t, s): return [f'<span class="card-tab">{esc(tab)}</span>', f'<h1 class="card-t">{esc(t)}</h1>', f'<p class="card-s">{md(s)}</p>']
def sec_card(num, t, s=''): return [f'<div class="card-num">{esc(num)}</div>', f'<h1 class="card-t">{esc(t)}</h1>'] + ([f'<p class="card-s">{md(s)}</p>'] if s else [])
def toc(items): return '<div class="toc">' + ''.join(f'<div><b>{a}</b><span>{esc(b)}</span></div>' for a, b in items) + '</div>'
