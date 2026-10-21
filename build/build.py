import re,sys,os,hashlib,subprocess
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
os.makedirs('eq',exist_ok=True)
def render(tex):
    h=hashlib.md5(tex.encode()).hexdigest()[:10];fn=f'eq/{h}.png'
    if not os.path.exists(fn):
        fig=plt.figure(figsize=(0.01,0.01));fig.text(0,0,'$'+tex.replace(chr(92)+'frac',chr(92)+'dfrac')+'$',fontsize=18,color='#1a1a1a')
        fig.savefig(fn,dpi=200,bbox_inches='tight',pad_inches=0.06,transparent=False,facecolor='white');plt.close(fig)
    from PIL import Image
    w,hh=Image.open(fn).size
    return fn,hh/200*0.95
def boxes(md):
    out=[];inbox=False
    for line in md.split('\n'):
        if line.startswith('::: {custom-style='): inbox=True; out.append(line); continue
        if line.strip()==':::' : inbox=False; out.append(line); continue
        if inbox:
            m=re.match(r'^(\d+)\. (.*)',line)
            if m: line=f'**{m.group(1)}.** {m.group(2)}'
            elif line.startswith('- '): line='→ '+line[2:]
            if line.strip() and not line.startswith('|'): out.append(line); out.append(''); continue
        out.append(line)
    return '\n'.join(out)
def pre(md):
    md=boxes(md)
    def rep(m):
        fn,hin=render(m.group(1).strip())
        return f'\n::: {{custom-style="Formula"}}\n![]({fn}){{height={hin:.2f}in}}\n:::\n'
    return re.sub(r'^\$\$(.+?)\$\$\s*$',rep,md,flags=re.M)
def build(folder,out,title):
    parts=sorted(f for f in os.listdir(folder) if f.endswith('.md'))
    md='\n\n'.join(open(os.path.join(folder,p),encoding='utf-8').read() for p in parts)
    md=pre(md)
    open(out+'.md','w').write(md)
    fmt='markdown-tex_math_dollars-tex_math_single_backslash'
    subprocess.run(['pandoc','-f',fmt,out+'.md','-o',out+'.docx','--reference-doc=reference.docx'],check=True)
    subprocess.run(['pandoc','-f',fmt,out+'.md','-s','--toc','--toc-depth=2','--embed-resources','--css=guia.css','--metadata','pagetitle='+title,'-o',out+'.html'],check=True)
if __name__=='__main__':
    build(sys.argv[1],sys.argv[2],sys.argv[3])
