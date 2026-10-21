# Crea voz_nuevos/<t>_guion.json solo con fragmentos sin audio de v1
import json,hashlib,os,glob
os.makedirs('/home/claude/video/voz_nuevos',exist_ok=True)
tot=0;chars=0
for g in sorted(glob.glob('/home/claude/video/out/*_guion.json')):
    t=os.path.basename(g)[:-11]
    old=set()
    v1=f'/home/claude/video/guion_v1/{t}_guion.json'
    if os.path.exists(v1):
        old={'f'+hashlib.sha1(x['texto'].encode()).hexdigest()[:12] for x in json.load(open(v1))}
    new=[x for x in json.load(open(g)) if x['id'] not in old]
    json.dump(new,open(f'/home/claude/video/voz_nuevos/{t}_guion.json','w'),ensure_ascii=False,indent=1)
    c=sum(len(x['texto']) for x in new);tot+=len(new);chars+=c
    print(t,len(new),'fragmentos',c,'car.')
print('TOTAL',tot,chars)
