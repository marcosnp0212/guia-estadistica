import json, math
from collections import Counter
def tol(k,dec): return max(0.5*10**-dec*1.02, abs(k)*0.001)
def ask(label,key,dec=2,kind='num',alts=None,accept=None):
    if kind=='text': return {'t':'ask','label':label,'key':key,'dec':0,'tol':0,'kind':'text','accept':accept or [key],'alts':alts or []}
    al=[[a,h] for a,h in (alts or []) if abs(a-key)>1.5*tol(key,dec)]
    return {'t':'ask','label':label,'key':float(key),'dec':dec,'tol':tol(key,dec),'kind':kind,'accept':None,'alts':al}
def receta_q(vals,p):
    v=sorted(vals);n=len(v);k=p*n
    if abs(k-round(k))<1e-9:
        k=int(round(k));return (v[k-1]+v[k])/2
    return v[math.ceil(k)-1]
def grouped(L,U,ns,p):
    n=sum(ns);k=p*n;N=0
    for l,u,ni in zip(L,U,ns):
        if N+ni>=k-1e-9: return l+(k-N)/ni*(u-l)
        N+=ni
sims=[]
# P1
d=[0,1,1,2,2,2,3,1,0,2,4,2,1,3,2,1,0,2,3,5]
n=len(d);m=sum(d)/n;S2=sum(x*x for x in d)/n-m*m;c=Counter(d)
me=receta_q(d,.5);c1=receta_q(d,.25);c3=receta_q(d,.75);mo=max(c,key=lambda k:c[k])
P1=[{'t':'p','text':'Número de cursos de formación que han hecho en el último año 20 empleados de una empresa.','b':True,'i':False},
 {'t':'datos','values':d},{'t':'hint','text':'Hazlo en papel: tabla de frecuencias con xᵢ, nᵢ, Nᵢ, xᵢ·nᵢ y xᵢ²·nᵢ. Usa la receta de los apuntes para la mediana y los cuartiles.'},
 {'t':'h','text':'Preguntas'},
 ask('Media',m,2,alts=[(sum(set(d))/len(set(d)),'Has hecho la media de los valores distintos. Cada valor cuenta tantas veces como se repite.')]),
 ask('Mediana (receta de los apuntes)',me,2),
 ask('Moda',mo,0,alts=[(c[mo],'Eso es la frecuencia más alta. La moda es el VALOR que tiene esa frecuencia.')]),
 ask('Primer cuartil C₁ (receta de los apuntes)',c1,2),
 ask('Tercer cuartil C₃ (receta de los apuntes)',c3,2,alts=[(sorted(d)[14],'Con 3n/4 = 15 exacto, la receta dice: media del dato 15.º y el 16.º.')]),
 ask('Varianza S² (dividiendo entre n)',S2,3,alts=[(S2*n/(n-1),'Esa es la cuasivarianza (entre n − 1). Te piden la varianza S², entre n.'),(sum(x*x for x in d)/n,'Te falta restar la media al cuadrado.')]),
 ask('Coeficiente de variación (en decimal)',math.sqrt(S2)/m,3,alts=[(S2/m,'El CV usa la desviación típica S (la raíz de la varianza), no la varianza.')]),
 ask('En Excel, ¿qué función usarías para la varianza S² (la que divide entre n)? Escribe solo su nombre.','VAR.P',kind='text',accept=['VAR.P','VARP'],alts=[('VAR.S','VAR.S divide entre n − 1: es la cuasivarianza.'),('VAR','VAR es la antigua VAR.S (entre n − 1).'),('DESVEST.P','Esa es la desviación típica, no la varianza.')]),
]
sims.append(('P1',P1,'Cursos de formación de 20 empleados'))
# P2
L=[1000,1200,1400,1800];U=[1200,1400,1800,2400];ns=[10,25,30,15];N=sum(ns)
mk=[(a+b)/2 for a,b in zip(L,U)];mean=sum(x*k for x,k in zip(mk,ns))/N
med=grouped(L,U,ns,.5);p90=grouped(L,U,ns,.9)
den=[k/(u-l) for k,l,u in zip(ns,L,U)];i=den.index(max(den))
mo=L[i]+(den[i]-den[i-1])/((den[i]-den[i-1])+(den[i]-den[i+1]))*(U[i]-L[i])
mas1600=(ns[2]*(1800-1600)/400+ns[3])/N
mo_wrong_i=ns.index(max(ns));mo_w=L[mo_wrong_i]+(ns[mo_wrong_i]-ns[mo_wrong_i-1])/((ns[mo_wrong_i]-ns[mo_wrong_i-1])+(ns[mo_wrong_i]-ns[mo_wrong_i+1]))*(U[mo_wrong_i]-L[mo_wrong_i])
P2=[{'t':'p','text':'Salario mensual (€) de 80 trabajadores de una cadena de tiendas.','b':True,'i':False},
 {'t':'tabla','headers':['Salario (€)','nᵢ'],'rows':[['[1000, 1200]',10],['(1200, 1400]',25],['(1400, 1800]',30],['(1800, 2400]',15]]},
 {'t':'hint','text':'Ojo: los intervalos no miden lo mismo. Para la moda, densidades.'},
 {'t':'h','text':'Preguntas'},
 ask('Salario medio',mean,2),
 ask('Mediana',med,2),
 ask('Moda (con densidades)',mo,2,alts=[(mo_w,'Has usado las frecuencias. Con amplitudes distintas, el intervalo modal es el de mayor DENSIDAD (nᵢ ÷ aᵢ).')]),
 ask('Percentil 90',p90,2),
 ask('Proporción de trabajadores que ganan más de 1600 € (en decimal)',mas1600,4,kind='pct'),
 ask('En Excel, ¿qué función cuenta cuántos datos caen en cada intervalo (la que se escribe en varias celdas a la vez)?','FRECUENCIA',kind='text',accept=['FRECUENCIA'],alts=[('CONTAR.SI','CONTAR.SI cuenta un valor concreto. Para intervalos, FRECUENCIA (o CONTAR.SI.CONJUNTO).'),('CONTAR.SI.CONJUNTO','También vale para un intervalo, pero la que hace todos a la vez es FRECUENCIA.')]),
]
sims.append(('P2',P2,'Salarios en intervalos'))
# P3
tab=[[18,12,10],[12,22,26]]  # filas: Hombre, Mujer ; columnas: completa, parcial, por horas? 
rows=['Hombre','Mujer'];cols=['Completa','Parcial','Por horas']
rt=[sum(r) for r in tab];ct=[sum(c) for c in zip(*tab)];NN=sum(rt)
esp=rt[1]*ct[1]/NN
P3=[{'t':'p','text':'100 trabajadores según su sexo (filas) y su tipo de jornada (columnas).','b':True,'i':False},
 {'t':'tabla','headers':['Sexo \\ Jornada']+cols,'rows':[[rows[k]]+tab[k] for k in range(2)]},
 {'t':'h','text':'Preguntas'},
 ask('¿Cuántos trabajadores tienen jornada parcial? (marginal)',ct[1],0),
 ask('Porcentaje de mujeres con jornada parcial, sobre el total de mujeres (en decimal)',tab[1][1]/rt[1],4,kind='pct',alts=[(tab[1][1]/NN,'Has dividido entre el total (100). La condicionada se divide entre el total de su grupo: las mujeres.'),(tab[1][1]/ct[1],'Has dividido entre el total de la columna. «De las mujeres» = fila de mujeres.')]),
 ask('Porcentaje de los de jornada completa que son hombres (en decimal)',tab[0][0]/ct[0],4,kind='pct',alts=[(tab[0][0]/rt[0],'Has dividido entre los hombres. «De los de jornada completa» = columna de completa.')]),
 ask('Frecuencia esperada de la casilla Mujer–Parcial si fueran independientes',esp,2),
 ask('¿Son independientes? Escribe SI o NO.','NO',kind='text',accept=['NO'],alts=[('SI','Compara la casilla Mujer–Parcial (22) con su esperada: no coinciden, así que no son independientes.')]),
 ask('En Excel, ¿qué herramienta usas para construir la tabla de doble entrada a partir de los datos?','TABLA DINAMICA',kind='text',accept=['TABLA DINAMICA','TABLAS DINAMICAS','TABLA DINÁMICA']),
]
sims.append(('P3',P3,'Sexo y tipo de jornada'))
# P4
n4=10;Sx,Sy,Sxx,Syy,Sxy=50,300,290,9300,1580
mx,my=Sx/n4,Sy/n4;vx=Sxx/n4-mx*mx;vy=Syy/n4-my*my;cv=Sxy/n4-mx*my;b=cv/vx;a=my-b*mx;r=cv/math.sqrt(vx*vy)
P4=[{'t':'p','text':'Horas de formación (X) y puntuación en una evaluación de desempeño (Y) de 10 trabajadores. Solo te dan las sumas:','b':True,'i':False},
 {'t':'tabla','headers':['n','Σx','Σy','Σx²','Σy²','Σxy'],'rows':[[n4,Sx,Sy,Sxx,Syy,Sxy]]},
 {'t':'h','text':'Preguntas'},
 ask('Covarianza S_XY',cv,3,alts=[(Sxy/n4,'Te falta restar x̄·ȳ.')]),
 ask('Pendiente b de la recta de Y sobre X',b,3,alts=[(cv/vy,'Has dividido entre la varianza de Y. Para Y sobre X se divide entre S²ₓ.')]),
 ask('Término independiente a',a,3),
 ask('Coeficiente de correlación r',r,3),
 ask('Coeficiente de determinación R² (en decimal)',r*r,3,kind='pct'),
 ask('Puntuación prevista para 7 horas de formación',a+b*7,2),
 ask('En Excel, ¿qué función da la pendiente de la recta?','PENDIENTE',kind='text',accept=['PENDIENTE'],alts=[('INTERSECCION.EJE','Esa da el término independiente a, no la pendiente.')]),
]
sims.append(('P4',P4,'Regresión a partir de las sumas'))
# P5
i3=100*1.20*0.90*1.15;tm=(i3/100)**(1/3)-1
real=1650/108*100;vreal=real/1500-1
lp=(1.3*50+2.6*20)/(1.2*50+2.0*20)*100
P5=[{'t':'p','text':'Índices y deflactar.','b':True,'i':False},
 {'t':'p','text':'Las ventas de una empresa variaron +20 % en 2023, −10 % en 2024 y +15 % en 2025. Base 2022 = 100.','b':False,'i':False},
 {'t':'p','text':'Un salario pasa de 1500 € (2022) a 1650 € (2025). El IPC de 2025 con base 2022 es 108.','b':False,'i':False},
 {'t':'tabla','headers':['Producto','p₂₀₂₂','q₂₀₂₂','p₂₀₂₅'],'rows':[['A',1.2,50,1.3],['B',2.0,20,2.6]]},
 {'t':'h','text':'Preguntas'},
 ask('Índice de ventas de 2025 (base 2022 = 100)',i3,2,alts=[(125,'Has sumado los porcentajes. Se multiplican: 1,20 × 0,90 × 1,15.')]),
 ask('Tasa media anual de crecimiento 2022-2025 (en decimal)',tm,4,kind='pct',alts=[(0.25/3,'Has dividido entre 3. La tasa media es la raíz cúbica del crecimiento total, menos 1.')]),
 ask('Salario de 2025 en euros de 2022 (real)',real,2,alts=[(1650*1.08,'Has multiplicado por el IPC. Para deflactar se DIVIDE: 1650 ÷ 108 × 100.')]),
 ask('Variación real del salario 2022-2025 (en decimal)',vreal,4,kind='pct',alts=[(0.1,'Esa es la variación nominal (1650 ÷ 1500 − 1). La real usa el salario deflactado.')]),
 ask('Índice de precios de Laspeyres 2025 (base 2022 = 100)',lp,2),
 ask('En Excel, ¿qué función calcula la media geométrica?','MEDIA.GEOM',kind='text',accept=['MEDIA.GEOM','MEDIAGEOM']),
]
sims.append(('P5',P5,'Índices y deflactar'))
out=[]
for k,(pid,blocks,sub) in enumerate(sims,1):
    out.append({'id':'S3_'+pid,'title':f'Simulacro 3 · Pregunta {k} (2 puntos)','color':'tx','subtitle':sub,'blocks':blocks,'paper':True})
json.dump(out,open('/home/claude/xl3/sim_papel.json','w'),ensure_ascii=False,indent=1)
for o in out:
    print(o['id'],[ (b['label'][:30],round(b['key'],4) if isinstance(b['key'],float) else b['key']) for b in o['blocks'] if b['t']=='ask'])
