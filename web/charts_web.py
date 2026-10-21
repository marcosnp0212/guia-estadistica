import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'font.family':'DejaVu Sans','svg.fonttype':'none','axes.edgecolor':'#5B6770','axes.labelcolor':'#26323A','xtick.color':'#5B6770','ytick.color':'#5B6770','text.color':'#26323A'})
B='#2F5FD0';G='#0F8A68';O='#C2185B';P='#B07A00'
def save(n): plt.tight_layout(); plt.savefig('img/'+n+'.svg',transparent=True); plt.close()
# hermanos bar
x=[0,1,2,3,4,5];n=[21,12,6,2,2,1]
plt.figure(figsize=(6,3.4));b=plt.bar(x,n,color=B,width=0.6)
for xi,ni in zip(x,n): plt.text(xi,ni+0.4,f'{ni} ({ni/44*100:.1f}%)'.replace('.',','),ha='center',fontsize=9)
plt.xlabel('Número de hermanos');plt.ylabel('Nº de personas (nᵢ)');plt.title('Diagrama de barras (variable discreta)');save('t1_barras_hermanos')
# histogram alturas + polygon
plt.figure(figsize=(6,3.4));plt.bar([165,175,185,195],[3,6,5,2],width=10,color=G,edgecolor='white',alpha=.85)
plt.plot([155,165,175,185,195,205],[0,3,6,5,2,0],'o-',color=O,label='Polígono de frecuencias');plt.xticks([160,170,180,190,200]);plt.xlabel('Altura (cm)');plt.ylabel('Frecuencia');plt.legend(frameon=False);plt.title('Histograma: las barras se tocan');save('t1_histograma_alturas')
# boxplot anatomy
fig,ax=plt.subplots(figsize=(7,2.6))
ax.add_patch(plt.Rectangle((173.5,0.6),11,0.8,fc='#BBDEFB',ec=B,lw=2));ax.plot([178.5,178.5],[0.6,1.4],color='k',lw=3)
ax.plot([163,173.5],[1,1],'k--');ax.plot([184.5,198],[1,1],'k--');ax.plot([163,163],[.8,1.2],'k');ax.plot([198,198],[.8,1.2],'k')
for xv,t,yv in [(163,'Mínimo\n163',1.55),(173.5,'C₁ = 173,5\n(25 %)',1.55),(178.5,'Mediana 178,5',-0.25),(184.5,'C₃ = 184,5\n(75 %)',1.55),(198,'Máximo\n198',1.55)]:
    ax.text(xv,yv,t,ha='center',fontsize=9)
ax.annotate('',xy=(173.5,0.45),xytext=(184.5,0.45),arrowprops=dict(arrowstyle='<->',color=O));ax.text(179,0.3,'',ha='center')
ax.text(191,0.35,'Caja = 50 % central (IQR = 11)',fontsize=9,color=O)
ax.set_xlim(158,203);ax.set_ylim(-0.4,2.1);ax.set_yticks([]);ax.set_xlabel('Altura (cm)');ax.spines['left'].set_visible(False);ax.set_title('Anatomía de un diagrama de caja');save('t1_caja_anatomia')
# skew shapes
fig,axs=plt.subplots(1,3,figsize=(8,2.3));xs=np.linspace(0,10,200)
from math import gamma
def gpdf(x,k,t): return x**(k-1)*np.exp(-x/t)
axs[0].fill_between(xs,gpdf(10-xs,2.2,1.4),color=O,alpha=.6);axs[0].set_title('Asimetría negativa\n(cola a la izquierda)',fontsize=10)
axs[1].fill_between(xs,np.exp(-(xs-5)**2/3),color=G,alpha=.6);axs[1].set_title('Simétrica',fontsize=10)
axs[2].fill_between(xs,gpdf(xs,2.2,1.4),color=B,alpha=.6);axs[2].set_title('Asimetría positiva\n(cola a la derecha)',fontsize=10)
for a in axs: a.set_yticks([]);a.set_xticks([])
save('t1_asimetria')
fig,axs=plt.subplots(1,3,figsize=(8,2.3));xs=np.linspace(-5,5,300)
for a,(s,t,c) in zip(axs,[(0.6,'Leptocúrtica (CC > 0)\npicuda',B),(1,'Mesocúrtica (CC = 0)\ncomo la normal',G),(1.8,'Platicúrtica (CC < 0)\naplanada',O)]):
    a.fill_between(xs,np.exp(-xs**2/(2*s*s))/s,color=c,alpha=.6);a.set_title(t,fontsize=10);a.set_yticks([]);a.set_xticks([]);a.set_ylim(0,1.8)
save('t1_curtosis')
# Ej3 hijos
plt.figure(figsize=(5.5,3.2));n=[4,7,4,3,2];plt.bar(range(5),n,color=B,width=.6)
for i,v in enumerate(n): plt.text(i,v+.15,f'{v} ({v*5} %)',ha='center',fontsize=9)
plt.xlabel('Número de hijos');plt.ylabel('Nº de familias');plt.title('Ejercicio 3: número de hijos');save('b3_hijos')
# Ej4
fig,axs=plt.subplots(1,2,figsize=(8,3),sharey=True);x=range(1,8)
axs[0].bar(x,np.array([1,3,5,7,5,3,1])/25,color=G,width=.6);axs[0].set_title('Fútbol (X)');axs[1].bar(x,[.24,.16,.08,.04,.08,.16,.24],color=O,width=.6);axs[1].set_title('Baloncesto (Y)')
for a in axs: a.set_xlabel('Nº de lesiones')
axs[0].set_ylabel('Frecuencia relativa');save('b4_lesiones')
# Ej5 histogram unequal
plt.figure(figsize=(6,3.3));L=[7,8,9,10,12,15];d=[3,6,9,4.5,1]
for i in range(5): plt.bar(L[i],d[i],width=L[i+1]-L[i],align='edge',color=B,edgecolor='white');plt.text((L[i]+L[i+1])/2,d[i]+.2,str(d[i]).replace('.',','),ha='center',fontsize=9)
plt.xticks(L);plt.ylabel('Densidad dᵢ = nᵢ / aᵢ');plt.title('Ejercicio 5: histograma con amplitudes distintas');save('b5_hist')
# Ej9
plt.figure(figsize=(6,3.3));L=[5,9,13,17,21,25,29,33];p=[3.75,12.5,17.5,31.25,21.25,11.25,2.5]
plt.bar(L[:-1],p,width=4,align='edge',color=G,edgecolor='white');plt.xticks(L);plt.xlabel('Toneladas de óxido de azufre');plt.ylabel('% de días');plt.title('Ejercicio 9');save('b9_hist')
# Ej20 radial
cats=['Alimentación','Vivienda','Sanidad','Transporte','Educ./Cultura','Vestido/Calzado','Mobiliario']
ponte=[11684.90,7441.24,806.27,5462.74,2057.68,4180.55,2161.11]
ang=np.linspace(0,2*np.pi,len(cats),endpoint=False).tolist();vals=ponte+[ponte[0]];ang2=ang+[ang[0]]
fig=plt.figure(figsize=(4.6,4.6));ax=fig.add_subplot(111,polar=True);ax.set_theta_offset(np.pi/2);ax.set_theta_direction(-1)
ax.plot(ang2,vals,'o-',color=P);ax.fill(ang2,vals,color=P,alpha=.25);ax.set_xticks(ang);ax.set_xticklabels(cats,fontsize=9);ax.set_ylim(0,12000);ax.set_yticks([3000,6000,9000,12000]);ax.set_yticklabels(['3000','6000','9000','12000'],fontsize=7)
ax.set_title('Pontevedra (máximo del gráfico = 12000)',fontsize=10);save('b20_radial_pontevedra')
# T3 scatter antiguedad
x=np.array([1,2,3,5,6,7,9,10,12,15]);y=np.array([1400,1600,1700,1700,1800,1850,2200,2400,2250,2500])
plt.figure(figsize=(6,3.4));plt.scatter(x,y,color=B,zorder=3);xx=np.linspace(0,16,10);plt.plot(xx,1390.27+78.53*xx,color=O,label='Ŷ = 1390,27 + 78,53·X');plt.scatter([11],[1390.27+78.53*11],marker='*',s=180,color=G,zorder=4,label='Predicción para 11 años');plt.xlabel('Antigüedad (años)');plt.ylabel('Salario (€)');plt.legend(frameon=False,fontsize=9);plt.title('Nube de puntos y recta de regresión');save('t3_antig')
# relation types
rng=np.random.default_rng(3);fig,axs=plt.subplots(1,4,figsize=(9,2.3));x=rng.uniform(0,10,30)
for a,(yv,t) in zip(axs,[(2*x+rng.normal(0,2,30),'Directa (r > 0)'),(-2*x+rng.normal(0,2,30),'Inversa (r < 0)'),(rng.normal(5,2,30),'Sin relación (r ≈ 0)'),((x-5)**2+rng.normal(0,1.5,30),'No lineal (curva)')]):
    a.scatter(x,yv,s=12,color=B);a.set_title(t,fontsize=10);a.set_xticks([]);a.set_yticks([])
save('t3_tipos')
# Ej3 talleres
x=np.array([20.4,21.8,22,23,23.6]);y=np.array([80,64,46,50,51]);plt.figure(figsize=(6,3.4));plt.scatter(x,y,color=B,zorder=3);xx=np.linspace(20,24,10);plt.plot(xx,263.05-9.244*xx,color=O,label='Ŷ = 263,05 − 9,244·X');plt.xlabel('Precio (€/hora)');plt.ylabel('Nº de clientes');plt.legend(frameon=False);plt.title('Ejercicio 3 (Tema 3)');save('r3_talleres')
x=np.array([.5,1,1.5,2,2.5,3,3.5]);y=np.array([100,300,500,800,1100,1500,2400]);plt.figure(figsize=(6,3.4));plt.scatter(x,y,color=B,zorder=3);xx=np.linspace(0.3,3.7,10);plt.plot(xx,-457.14+707.14*xx,color=O,label='Ŷ = −457,14 + 707,14·X');plt.scatter([2.2],[1098.57],marker='*',s=180,color=G,zorder=4,label='Predicción para 2,2');plt.xlabel('Miles de litros vertidos');plt.ylabel('Sanción (miles de €)');plt.legend(frameon=False,fontsize=9);plt.title('Ejercicio 5 (Tema 3)');save('r5_vertidos')
# T4 nominal vs real
yrs=np.arange(2015,2026);nom=np.array([100,102,104.67,106.67,110,113.33,116.67,120,123.33,126.67,130]);real=np.array([100,100.79,102.11,102.56,103.77,104.45,105.87,107.14,107.71,108.26,109.24])
plt.figure(figsize=(6,3.3));plt.plot(yrs,nom,'o-',color=B,label='Índice nominal');plt.plot(yrs,real,'o-',color=O,label='Índice real (sin inflación)');plt.legend(frameon=False);plt.ylabel('Índice (2015 = 100)');plt.title('Salario nominal vs. real');save('t4_nominal_real')
# boxplot ej19 recreated? skip
print('ok')
