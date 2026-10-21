import sys,time,importlib,shutil;sys.path.insert(0,'/home/claude/video/content');sys.path.insert(0,'/home/claude/video')
from engine_anim import build_anim
for name in sys.argv[1:]:
    m=importlib.import_module(name);t=time.time()
    r=build_anim(m.TEMA,m.S)
    print(name,round(r[0]/60,1),'min',r[2],round(time.time()-t),'s',flush=True)
