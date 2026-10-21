import sys,time,importlib;sys.path.insert(0,'/home/claude/video/content');sys.path.insert(0,'/home/claude/video')
from engine import build
for name in sys.argv[1:]:
    m=importlib.import_module(name);t=time.time()
    print(name,build(m.TEMA,m.S),round(time.time()-t,1),flush=True)
