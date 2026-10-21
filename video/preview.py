import sys,importlib,os;sys.path.insert(0,'/home/claude/video/content');sys.path.insert(0,'/home/claude/video')
from engine import *
m=importlib.import_module(sys.argv[1]);picks=[(int(a.split(':')[0]),int(a.split(':')[1])) for a in sys.argv[2:]]
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=br.new_page(viewport={'width':W,'height':H})
    base=os.path.join(ROOT,'base.html');open(base,'w').write(page(m.TEMA,m.S[0],0,'',0));pg.goto('file://'+base);pg.evaluate('()=>document.fonts.ready');pg.wait_for_timeout(200)
    for si,k in picks:
        sc=m.S[si];seg=[s for s in sc.segs if s[0]==k] or sc.segs[-1:]
        cls,inner=body(m.TEMA,sc,k,split_cues(seg[0][1])[0],0.4)
        z=pg.evaluate(FIT_JS,[cls,inner]);print(si,k,round(z,2));pg.evaluate('()=>Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r})))');pg.wait_for_timeout(100)
        pg.screenshot(path=f'/tmp/claude-0/-home-claude/5ed45f48-7a6a-525a-9769-23012da0dd80/scratchpad/pv_{si}_{k}.png')
    br.close()
