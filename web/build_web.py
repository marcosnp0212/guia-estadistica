import os,subprocess,sys,re,json,base64
X='/home/claude/xl2/'
FILES=['Solucionario_estadistica.xlsx','Practicas_autocorregidas.xlsx','Simulacros_autocorregidos.xlsx','Plantillas_estadistica.xlsx','Estadistica_ejercicios_resueltos.xlsx']
def sheet_lib():
    d='/home/claude/web/sheet/'
    # la hoja de cálculo (1,7 MB) va en un archivo aparte, assets/sheet.js, que solo se descarga
    # la primera vez que una práctica la necesita (loadSheetLib); el navegador la guarda para la próxima
    os.makedirs('/home/claude/web/assets',exist_ok=True)
    open('/home/claude/web/assets/sheet.js','w').write('\n;\n'.join(open(d+f).read() for f in ['hot.js','hf-es.js','hfsetup.js']))
    loader=("window.loadSheetLib=function(cb){if(window.Handsontable){if(cb)cb();return;}var q=window._shq=window._shq||[];if(cb)q.push(cb);if(window._shl)return;window._shl=1;"
            "var e=document.createElement('script');e.src='assets/sheet.js';function done(){q.splice(0).forEach(function(f){f();});}e.onload=done;e.onerror=function(){window._shl=0;done();};document.head.appendChild(e);};")
    open('/home/claude/web/sheetlib.html','w').write('<style>'+open(d+'hot.css').read()+'</style><script>'+loader+'</script>')
def data_script(lang='es'):
    d={'practicas':json.load(open(X+'practicas.json')),'simulacros':json.load(open(X+'simulacros.json'))+json.load(open('/home/claude/xl3/sim_papel.json')),'checks':{**json.load(open(X+'checks.json')),**json.load(open('/home/claude/xl3/checks_papel.json'))},'tests':json.load(open('/home/claude/xl3/sim_test.json'))}
    if lang=='zh':
        # traducciones: cada archivo de web/zh/ sustituye por completo al original; checks se mezcla por apartado
        Z='/home/claude/web/zh/'
        for k,f in [('practicas','practicas.json'),('tests','sim_test.json')]:
            if os.path.exists(Z+f): d[k]=json.load(open(Z+f,encoding='utf-8'))
        if os.path.exists(Z+'simulacros.json'): d['simulacros']=json.load(open(Z+'simulacros.json',encoding='utf-8'))
        if os.path.exists(Z+'checks.json'): d['checks'].update(json.load(open(Z+'checks.json',encoding='utf-8')))
    p=base64.b64encode(json.dumps(d,ensure_ascii=False).encode()).decode()
    # los Excel de descarga van como archivos normales en assets/
    import shutil
    os.makedirs('/home/claude/web/assets',exist_ok=True)
    for n in FILES: shutil.copy('/home/claude/entrega/'+n,'/home/claude/web/assets/'+n)
    fs={n:round(os.path.getsize('/home/claude/entrega/'+n)/1024) for n in FILES}
    open('/home/claude/web/'+('data_zh.html' if lang=='zh' else 'data.html'),'w').write('<script>(function(){var b=atob("'+p+'"),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);window.GUIA_DATA=JSON.parse(new TextDecoder().decode(u));window.GUIA_DATA.fsize='+json.dumps(fs)+';})();</script>')
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
def headers(blocks,out):
    """lista de los títulos del documento (pandoc JSON), en orden"""
    for b in blocks:
        if b['t']=='Header':out.append(b)
        c=b.get('c')
        if b['t'] in ('Div','BlockQuote'):headers(c[-1] if b['t']=='Div' else c,out)
    return out
def js_zh(name):
    """copia del .js con los textos de la interfaz en chino (web/zh/ui.py)"""
    import importlib.util
    sp=importlib.util.spec_from_file_location('ui','/home/claude/web/zh/ui.py');ui=importlib.util.module_from_spec(sp);sp.loader.exec_module(ui)
    src=open('/home/claude/web/'+name,encoding='utf-8').read()
    for a,b in ui.RAW:src=src.replace(a,b)
    for a,b in sorted(ui.UI,key=lambda x:-len(x[0])):
        src=src.replace("'"+a+"'","'"+b.replace("'","\\'")+"'")
    os.makedirs('/home/claude/web/zh/out',exist_ok=True)
    open('/home/claude/web/zh/out/'+name,'w',encoding='utf-8').write(src)
    return 'zh/out/'+name
def build_zh():
    """versión en chino: mismos apartados y mismos id que la española, para que el progreso y los enlaces valgan en los dos idiomas"""
    es='/home/claude/build/alumna';zh='/home/claude/build/alumna_zh'
    parts=sorted(f for f in os.listdir(es) if f.endswith('.md'))
    def md_of(folder,fallback):
        md='\n\n'.join(open(os.path.join(folder if os.path.exists(os.path.join(folder,p)) else fallback,p),encoding='utf-8').read() for p in parts)
        md=md.replace('](img/','](/home/claude/web/img/')
        return re.sub(r'^\$\$(.+?)\$\$[ \t]*$',lambda m:'$$'+re.sub(r'(\d+)\{,\}(\d+)',r'\\text{\1,\2}',m.group(1))+'$$',md,flags=re.M)
    def ast(md):
        return json.loads(subprocess.run(['pandoc','-f','markdown','-t','json'],input=md,capture_output=True,text=True,check=True).stdout)
    # los id salen de la versión española ya montada (pandoc con --section-divs da los mismos id que aquí)
    A_es=ast(md_of(es,es));A_zh=ast(md_of(zh,es))
    H_es=headers(A_es['blocks'],[]);H_zh=headers(A_zh['blocks'],[])
    if len(H_es)!=len(H_zh):raise SystemExit(f'La versión china tiene {len(H_zh)} títulos y la española {len(H_es)}: tienen que coincidir uno a uno.')
    ids={}
    for he,hz in zip(H_es,H_zh):
        if he['c'][0]!=hz['c'][0]:raise SystemExit('Nivel de título distinto: '+json.dumps(hz['c'][2],ensure_ascii=False)[:120])
    # pandoc pone los id al convertir; con -t json ya vienen calculados
    for he,hz in zip(H_es,H_zh):hz['c'][1][0]=he['c'][1][0]
    tmp='/home/claude/web/alumna_zh.json';open(tmp,'w',encoding='utf-8').write(json.dumps(A_zh,ensure_ascii=False))
    data_script('zh')
    tb=open('/home/claude/web/tbar_alumna.html',encoding='utf-8').read()
    for a,b in [('Estadística<small>Temas 1 a 4</small>','统计学<small>Tema 1 到 4</small>'),('aria-label="Secciones"','aria-label="栏目"'),('>Inicio<','>首页<'),('>Mi plan<','>我的计划<'),
                ('>Temas<span','>Tema<span'),('>Examen<','>考试<'),('<span class="lg">Herramientas</span><span class="sh">Más</span>','<span class="lg">工具</span><span class="sh">更多</span>'),
                ('aria-label="Índice completo"','aria-label="完整目录"'),('<span>Índice</span>','<span>目录</span>'),('aria-label="Buscar en la guía"','aria-label="在指南中搜索"'),
                ('aria-label="Mis notas"','aria-label="我的笔记"'),('aria-label="Cambiar entre modo claro y oscuro"','aria-label="切换浅色或深色模式"'),
                ('href="#" data-to="zh" lang="zh-CN" title="中文版">中文</a>','href="#" data-to="es" lang="es" title="Versión en español">ES</a>')]:
        assert a in tb,a;tb=tb.replace(a,b)
    env=dict(os.environ,GUIA_LANG='zh')
    js=[js_zh(n) for n in ['guia.js','features.js','course.js','plan.js','nav.js']]
    args=['pandoc','-f','json',tmp,'-t','html5','-s','--template=template.html','--lua-filter=guia.lua','--section-divs','--toc','--toc-depth=2',
          '--mathml','--embed-resources','--css=guia.css','--css=zh/zh.css','--include-after-body='+js[0],'--include-after-body=data_zh.html','--include-after-body=sheetlib.html',
          '--include-after-body='+js[1],'--include-after-body='+js[2],'--include-after-body='+js[3],'--include-after-body='+js[4],
          '-V','tbar='+tb,'-V','htmllang=zh-CN','-M','pagetitle=统计学（Tema 1 到 4）','-V','shorttitle=统计学','-V','endnote=统计学学习指南，Tema 1 到 4（RRLL y RRHH，UVigo）。非官方学习资料。','-V','guide=alumna',
          '--include-before-body','zh/hero_zh.html','-o','/home/claude/web/alumna_zh.html']
    subprocess.run(args,check=True,cwd='/home/claude/web',env=env)
    h=open('/home/claude/web/alumna_zh.html',encoding='utf-8').read()
    for a,c in [('>Saltar al contenido<','>跳到正文<'),('class="to-top">Volver al principio<','class="to-top">回到顶部<'),('aria-label="Cambiar entre modo claro y oscuro"','aria-label="切换浅色或深色模式"')]:h=h.replace(a,c)
    open('/home/claude/web/alumna_zh.html','w',encoding='utf-8').write(h)
if __name__=='__main__':
    data_script()
    sheet_lib()
    build('/home/claude/build/alumna','alumna','Estadística (Temas 1 a 4)','Estadística','hero_alumna.html','Guía de estudio de Estadística, Temas 1 a 4 (RRLL y RRHH, UVigo). Material de estudio no oficial.')
    build_zh()
    build('/home/claude/build/tutor','tutor','Guía del tutor · Estadística con Excel','Guía del tutor','hero_tutor.html','Guía del tutor · Estadística con Excel',guide='tutor')
