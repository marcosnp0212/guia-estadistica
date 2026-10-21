from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.style import WD_STYLE_TYPE
d=Document('ref_default.docx')
st0=d.styles
class G:
    def __getitem__(self,n):
        for x in st0:
            if x.name==n: return x
        raise KeyError(n)
    def add_style(self,*a): return st0.add_style(*a)
    def __iter__(self): return iter(st0)
st=G()
def font(s,size=None,color=None,bold=None,name='Calibri'):
    s.font.name=name
    rpr=s.element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
    if rf is None: rf=OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ['w:ascii','w:hAnsi','w:cs','w:eastAsia']: rf.set(qn(a),name)
    for a in ['w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme']:
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: s.font.size=Pt(size)
    if color: s.font.color.rgb=RGBColor.from_string(color)
    if bold is not None: s.font.bold=bold
for n in ['Normal','Body Text','First Paragraph','Compact']:
    s=st[n]; font(s,11.5)
    pf=s.paragraph_format; pf.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY; pf.space_after=Pt(7); pf.line_spacing=1.2
    if n in ('Body Text','First Paragraph'): pf.left_indent=Cm(0.6)
st['Compact'].paragraph_format.space_after=Pt(3)
cols={'Heading 1':('1F4E79',20),'Heading 2':('2E75B6',15.5),'Heading 3':('1F7A5C',13),'Heading 4':('7A4E1F',12)}
for n,(c,sz) in cols.items():
    s=st[n]; font(s,sz,c,True); s.font.italic=False
    s.paragraph_format.space_before=Pt(16 if n=='Heading 1' else 12); s.paragraph_format.space_after=Pt(6); s.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
    s.paragraph_format.keep_with_next=True
st['Heading 1'].paragraph_format.page_break_before=True
font(st['Title'],26,'1F4E79',True); font(st['Subtitle'],14,'2E75B6',False)
def shade(p,fill,border):
    ppr=p.element.get_or_add_pPr()
    sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),fill); 
    bd=OxmlElement('w:pBdr')
    for side in ['top','left','bottom','right']:
        b=OxmlElement('w:'+side); b.set(qn('w:val'),'single'); b.set(qn('w:sz'),'24' if side=='left' else '4'); b.set(qn('w:space'),'6'); b.set(qn('w:color'),border); bd.append(b)
    ppr.append(bd); ppr.append(sh)
boxes={'Truco':('E8F5E9','2E7D32'),'Ojo':('FFF3E0','E65100'),'Excel':('E3F2FD','1565C0'),'Resultado':('FFFDE7','F9A825'),'Idea':('F3E5F5','6A1B9A'),'Enunciado':('F2F2F2','7F7F7F')}
for name,(fill,border) in boxes.items():
    s=st.add_style(name,WD_STYLE_TYPE.PARAGRAPH); s.base_style=st['Normal']; font(s,11)
    s.paragraph_format.left_indent=Cm(0.6); s.paragraph_format.right_indent=Cm(0.3); s.paragraph_format.space_after=Pt(2); s.paragraph_format.space_before=Pt(2)
    s.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
    shade(s,fill,border)
s=st['Verbatim Char']; font(s,10.5,'0D47A1',True,'Consolas')
rpr=s.element.get_or_add_rPr(); sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),'EEF4FB'); rpr.append(sh)
t=st['Table']; tpr=t.element.find(qn('w:tblPr'))
if tpr is None: tpr=OxmlElement('w:tblPr'); t.element.append(tpr)
b=OxmlElement('w:tblBorders')
for side in ['top','left','bottom','right','insideH','insideV']:
    e=OxmlElement('w:'+side); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:space'),'0'); e.set(qn('w:color'),'A6A6A6'); b.append(e)
tpr.append(b)
for n in ['Image Caption','Table Caption']:
    font(st[n],10,'595959')
# tables
d.save('reference.docx')
print('ok')
