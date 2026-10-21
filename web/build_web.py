import os,subprocess,sys,re,json,base64
X='/home/claude/xl2/'
FILES=['Solucionario_estadistica.xlsx','Practicas_autocorregidas.xlsx','Simulacros_autocorregidos.xlsx','Plantillas_estadistica.xlsx','Estadistica_ejercicios_resueltos.xlsx']
def sheet_lib():
    d='/home/claude/web/sheet/'
    # la hoja de cálculo pesa 1,7 MB: va como texto y solo se ejecuta la primera vez que una práctica la necesita (loadSheetLib)
    js='\n;\n'.join(open(d+f).read() for f in ['hot.js','hf-es.js','hfsetup.js'])
    loader="window.loadSheetLib=function(){if(window.Handsontable)return;var s=document.getElementById('sheetlib-src');if(!s)return;var e=document.createElement('script');e.textContent=s.textContent;document.head.appendChild(e);};"
    open('/home/claude/web/sheetlib.html','w').write('<style>'+open(d+'hot.css').read()+'</style><script type="text/plain" id="sheetlib-src">'+js+'</script><script>'+loader+'</script>')
def data_script():
    d={'practicas':json.load(open(X+'practicas.json')),'simulacros':json.load(open(X+'simulacros.json'))+json.load(open('/home/claude/xl3/sim_papel.json')),'checks':{**json.load(open(X+'checks.json')),**json.load(open('/home/claude/xl3/checks_papel.json'))},'tests':json.load(open('/home/claude/xl3/sim_test.json'))}
    p=base64.b64encode(json.dumps(d,ensure_ascii=False).encode()).decode()
    f={n:base64.b64encode(open('/home/claude/entrega/'+n,'rb').read()).decode() for n in FILES}
    # los Excel de descarga van como texto aparte y solo se leen al pulsar «Descargar»
    fs={n:round(len(v)*0.75/1024) for n,v in f.items()}
    open('/home/claude/web/data.html','w').write('<script>(function(){var b=atob("'+p+'"),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);window.GUIA_DATA=JSON.parse(new TextDecoder().decode(u));window.GUIA_DATA.fsize='+json.dumps(fs)+';})();</script><script type="application/json" id="guia-files">'+json.dumps(f)+'</script>')
def build(folder,out,title,short,hero=None,endnote='',guide='alumna'):
    parts=sorted(f for f in os.listdir(folder) if f.endswith('.md'))
    md='\n\n'.join(open(os.path.join(folder,p),encoding='utf-8').read() for p in parts)
    md=md.replace('](img/','](/home/claude/web/img/')
    md=re.sub(r'^\$\$(.+?)\$\$[ \t]*$',lambda m:'$$'+re.sub(r'(\d+)\{,\}(\d+)',r'\\text{\1,\2}',m.group(1))+'$$',md,flags=re.M)
    tmp=f'/home/claude/web/{out}.md';open(tmp,'w').write(md)
    args=['pandoc','-f','markdown',tmp,'-t','html5','-s','--template=template.html','--lua-filter=guia.lua','--section-divs','--toc','--toc-depth=2',
          '--mathml','--embed-resources','--css=guia.css','--include-after-body=guia.js']+(['--include-after-body=data.html','--include-after-body=sheetlib.html'] if guide=='alumna' else [])+['--include-after-body=features.js']+(['--include-after-body=course.js','--include-after-body=plan.js','--include-after-body=nav.js'] if guide=='alumna' else [])+(['-V','tbar='+open('/home/claude/web/tbar_alumna.html',encoding='utf-8').read()] if guide=='alumna' else [])+['-M','pagetitle='+title,'-V','shorttitle='+short,'-V','endnote='+endnote,'-V','guide='+guide,'-o',f'/home/claude/web/{out}.html']
    if hero: args+=['--include-before-body',hero]
    subprocess.run(args,check=True,cwd='/home/claude/web')
if __name__=='__main__':
    data_script()
    sheet_lib()
    build('/home/claude/build/alumna','alumna','Estadística (Temas 1 a 4)','Estadística','hero_alumna.html','Guía de estudio de Estadística, Temas 1 a 4 (RRLL y RRHH, UVigo). Material de estudio no oficial.')
    build('/home/claude/build/tutor','tutor','Guía del tutor · Estadística con Excel','Guía del tutor','hero_tutor.html','Guía del tutor · Estadística con Excel',guide='tutor')
