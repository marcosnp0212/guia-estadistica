import json
T=[]
def mc(tema,q,opts,ok,exp,where): T.append({'tema':tema,'q':q,'opts':opts,'ok':ok,'exp':exp,'where':where})
# ---- Tema 1
mc(1,'Tienes una tabla de frecuencias con los valores xᵢ en A2:A6, las frecuencias nᵢ en B2:B6 y la media en D1. ¿Qué fórmula da la varianza S²?',
 ['=SUMAPRODUCTO(A2:A6^2;B2:B6)/SUMA(B2:B6)-D1^2','=VAR.S(A2:A6)','=SUMAPRODUCTO(A2:A6;B2:B6)/SUMA(B2:B6)-D1^2','=VAR.P(B2:B6)'],0,
 'Es la fórmula práctica S² = Σxᵢ²nᵢ / n − x̄². VAR.S y VAR.P no sirven con una tabla de frecuencias: tratarían cada valor una sola vez. La C olvida elevar al cuadrado.','1.7 (varianza)')
mc(1,'¿Qué función de Excel calcula la cuasivarianza (la que divide entre n − 1)?',['VAR.P','VAR.S','DESVEST.P','COVARIANZA.P'],1,
 'VAR.S divide entre n − 1 (cuasivarianza). VAR.P divide entre n (varianza). DESVEST son las raíces.','1.7 (cuasivarianza)')
mc(1,'«Número de hijos» y «nivel de estudios (primaria, secundaria, universitaria)» son, respectivamente:',
 ['Cuantitativa discreta y cualitativa ordinal','Cuantitativa continua y cualitativa nominal','Cuantitativa discreta y cualitativa nominal','Cuantitativa continua y cualitativa ordinal'],0,
 'Los hijos se cuentan (0, 1, 2…): discreta. Los estudios son palabras con un orden: ordinal.','1.2')
mc(1,'X tiene media 10 y desviación típica 3. Si Y = 2X − 5, entonces:',['ȳ = 15 y Sᵧ = 6','ȳ = 15 y Sᵧ = 1','ȳ = 20 y Sᵧ = 6','ȳ = 15 y S²ᵧ = 12'],0,
 'ȳ = 2·10 − 5 = 15. La desviación solo nota la multiplicación: Sᵧ = 2·3 = 6 (la varianza sería 4·9 = 36). El −5 no cambia la dispersión.','1.5 y 1.7 (cambios de origen y escala)')
mc(1,'Salarios: 1200, 1300, 1350, 1400 y 9000 €. ¿Qué medida representa mejor el salario «típico»?',['La media','La mediana','El rango','El coeficiente de variación'],1,
 'El 9000 es un atípico que arrastra la media hasta 2850 €. La mediana (1350 €) es robusta y no se deja arrastrar.','1.5 (¿cuál uso?)')
mc(1,'Intervalos 0–10 con 20 datos y 10–40 con 30 datos. ¿Cuál es el intervalo modal?',
 ['10–40, porque tiene más datos','0–10, porque su densidad es 2 frente a 1','Los dos, porque hay empate','No se puede saber sin la media'],1,
 'Las amplitudes son distintas: hay que comparar densidades. 20/10 = 2 y 30/30 = 1. Gana 0–10.','1.5 (moda con intervalos)')
mc(1,'Grupo A: media 50 y S = 5. Grupo B: media 10 y S = 2. ¿Cuál es más homogéneo?',
 ['B, porque su S es menor','A, porque su CV es 0,10 frente a 0,20','Los dos igual','No se puede comparar porque las medias son distintas'],1,
 'Con medias distintas se compara el CV: A = 5/50 = 0,10, B = 2/10 = 0,20. Menor CV, más homogéneo: A.','1.7 (CV)')
mc(1,'Al descomponer la varianza de una empresa por departamentos, la varianza «entre» es el 5 % de la total. Eso significa que:',
 ['Los departamentos tienen medias muy distintas','Casi toda la variabilidad está dentro de cada departamento: sus medias son muy parecidas','La varianza dentro es el 5 %','Hay un error, porque la entre siempre es mayor'],1,
 'Si «entre» es solo el 5 %, las medias de los grupos apenas se separan. El 95 % de las diferencias está dentro de cada grupo.','1.7 (subpoblaciones)')
mc(1,'Una distribución tiene media 30 y mediana 25. Lo más probable es que:',
 ['Sea simétrica','Tenga asimetría positiva (cola a la derecha, CA > 0)','Tenga asimetría negativa','Sea platicúrtica'],1,
 'Unos pocos valores altos tiran de la media hacia arriba y la dejan por encima de la mediana: cola a la derecha.','1.8')
mc(1,'En un diagrama de caja, C₁ = 20 y C₃ = 30. ¿Es atípico un dato de 47?',
 ['No, porque está por debajo de 50','Sí, porque el límite superior es 30 + 1,5·10 = 45','No, porque el límite es 30 + 10 = 40 y el 47 está cerca','Solo si la media es menor que 25'],1,
 'IQR = 30 − 20 = 10. Límite superior = 30 + 15 = 45. Como 47 > 45, es atípico.','1.10')
# ---- Tema 2
mc(2,'En una tabla de doble entrada, fᵢⱼ es:',['nᵢⱼ / n','nᵢ. / n','nᵢⱼ / nᵢ.','nᵢ. · n.ⱼ'],0,
 'La frecuencia relativa conjunta es la absoluta conjunta entre el total. nᵢⱼ / nᵢ. sería una condicionada.','2.1')
mc(2,'n = 100. La fila A suma 40 y la columna «Sí» suma 50. Si X e Y fueran independientes, ¿qué frecuencia esperaríamos en la casilla (A, Sí)?',['20','90','45','2000'],0,
 'Frecuencia esperada = nᵢ. · n.ⱼ / n = 40 · 50 / 100 = 20. Si la tabla tiene 20 en esa casilla (y en todas cuadra), son independientes.','2.4')
mc(2,'La distribución condicionada Y | X = A se obtiene:',
 ['Dividiendo la fila A entre su total nᵢ.','Dividiendo la fila A entre n','Sumando la columna A','Multiplicando las marginales'],0,
 'Condicionar a X = A es quedarte solo con la fila A y repartirla en porcentajes de esa fila: se divide entre el total de la fila.','2.3')
mc(2,'¿Qué gráfico es adecuado para dos variables cualitativas?',['Histograma','Nube de puntos','Barras apiladas o mosaico','Diagrama de caja'],2,
 'Para dos cualitativas: barras agrupadas o apiladas, o mosaico. La nube de puntos es para dos cuantitativas.','2.1 (gráficos)')
mc(2,'Si las distribuciones condicionadas de Y cambian mucho según el valor de X:',
 ['Las variables son independientes','Hay relación (dependencia) entre X e Y','La covarianza es 0','Las marginales son iguales'],1,
 'Si saber X cambia lo que esperas de Y, están relacionadas. Con independencia, todas las condicionadas serían iguales.','2.3 y 2.4')
# ---- Tema 3
mc(3,'En una nube de puntos, los puntos bajan de izquierda a derecha. Entonces:',['S_XY > 0','S_XY < 0 y r < 0','r = 0','R² < 0'],1,
 'Si baja, la relación es inversa: covarianza, pendiente y r negativas. R² nunca es negativo.','3.1 y 3.2')
mc(3,'¿Cuál es la fórmula del coeficiente de correlación lineal de Pearson?',['r = S_XY / (Sₓ · Sᵧ)','r = S_XY / S²ₓ','r = Sₓ · Sᵧ / S_XY','r = S²_XY'],0,
 'r = covarianza entre el producto de las desviaciones típicas. S_XY / S²ₓ es la pendiente b.','3.4')
mc(3,'x̄ = 5, ȳ = 20, S²ₓ = 4 y S_XY = 8. La recta de Y sobre X es:',['Ŷ = 10 + 2X','Ŷ = 20 + 2X','Ŷ = 10 + 0,5X','Ŷ = 2 + 10X'],0,
 'b = 8/4 = 2. a = 20 − 2·5 = 10. Ŷ = 10 + 2X.','3.3')
mc(3,'En la recta Ŷ = 300 + 3X, el 3 significa que:',
 ['Cuando X = 0, Y vale 3','Por cada unidad más de X, Y aumenta de media 3 unidades','La recta explica el 3 %','Y es 3 veces X'],1,
 'La pendiente es lo que cambia Y, de media, por cada unidad más de X. El 300 es el valor cuando X = 0.','3.3')
mc(3,'Si r = 0:',
 ['No hay ningún tipo de relación entre X e Y','No hay relación lineal, pero podría haber una relación curva','La recta es perfecta','La pendiente es 1'],1,
 'r solo mide relación lineal. Una relación en forma de U puede tener r = 0.','3.4')
mc(3,'R² = 0,64 y la pendiente de la recta es negativa. ¿Cuánto vale r?',['0,64','−0,8','0,8','−0,64'],1,
 'r = ±√0,64 = ±0,8, con el signo de la pendiente: −0,8.','3.4 y 3.6')
mc(3,'La pendiente de la recta de X sobre Y es:',['b′ = S_XY / S²ᵧ','b′ = S_XY / S²ₓ','b′ = S²ᵧ / S_XY','b′ = r · S²ₓ'],0,
 'Para X sobre Y se divide entre la varianza de Y (la variable que explica en esa recta).','3.3')
mc(3,'Con Ŷ = 500 + 20X, ¿qué valor se predice para X = 12?',['520','740','760','6240'],1,
 '500 + 20·12 = 500 + 240 = 740.','3.5')
# ---- Tema 4
mc(4,'Un índice de precios vale 92 (base = 100). Significa que:',['Los precios han subido un 92 %','Los precios han bajado un 8 %','Los precios han bajado un 92 %','Los precios valen 92 €'],1,
 '92 − 100 = −8: han bajado un 8 % respecto al año base.','4.1')
mc(4,'Un precio sube un 10 % y al año siguiente un 20 %. En total ha subido:',['30 %','32 %','15 %','2 %'],1,
 'Los porcentajes se multiplican: 1,10 · 1,20 = 1,32 → +32 %.','4.3 (encadenamiento)')
mc(4,'Con base 2020, el índice de 2022 es 125 y el de 2024 es 150. ¿Cuánto vale el de 2024 con base 2022?',['120','25','187,5','150'],0,
 'Cambio de base: 150 / 125 · 100 = 120.','4.4')
mc(4,'Una magnitud crece un 3 % cada trimestre. Su tasa anual equivalente es:',['12 %','(1,03)⁴ − 1 ≈ 12,55 %','(1,03)^(1/4) − 1 ≈ 0,74 %','0,75 %'],1,
 'Un año son 4 trimestres encadenados: 1,03⁴ − 1 = 12,55 %. Sumar (12 %) es la trampa.','4.5')
mc(4,'El índice de Paasche de precios pondera con:',['Las cantidades del periodo actual (qₜ)','Las cantidades del año base (q₀)','Los precios del año base','La media de los dos índices'],0,
 'Paasche usa la cesta actual: Σpₜqₜ / Σp₀qₜ. Laspeyres usa la del año base.','4.6')
mc(4,'Un salario nominal sube un 5 % y el IPC sube un 3 %. El salario real:',['Sube un 2 %','Sube un 1,94 %','Sube un 8 %','Baja un 2 %'],1,
 'Real = 1,05 / 1,03 − 1 = 0,0194 → +1,94 %. Restar (2 %) es una aproximación, no la cuenta exacta.','4.7')
mc(4,'El índice de Fisher es:',['La media aritmética de Laspeyres y Paasche','La media geométrica de Laspeyres y Paasche','El cociente entre Laspeyres y Paasche','El mayor de los dos'],1,
 'F = √(L · P). Queda entre los dos.','4.6')
C=[
 {'q':'¿Qué es una variable cualitativa ordinal? Pon un ejemplo.','kind':'open','model':'Es una variable que toma categorías (palabras, no números) que tienen un orden natural. Ejemplo: nivel de satisfacción (bajo, medio, alto) o nivel de estudios.','where':'1.2'},
 {'q':'Datos: 4, 6, 8, 10, 12. Calcula la varianza S² (dividiendo entre n).','kind':'num','key':8,'dec':2,'alts':[[10,'Has dividido entre n − 1: eso es la cuasivarianza.'],[72,'Te falta restar la media al cuadrado (8² = 64).']],'explain':'x̄ = 40/5 = 8. Σx² = 16 + 36 + 64 + 100 + 144 = 360. S² = 360/5 − 64 = 8.','where':'1.7'},
 {'q':'Intervalos 0–10 con 8 datos y 10–30 con 12 datos. ¿Cuál es la densidad del intervalo modal?','kind':'num','key':0.8,'dec':2,'alts':[[0.6,'Esa es la densidad de 10–30. Compara: 8/10 = 0,8 es mayor.'],[12,'Eso es la frecuencia. Te piden la densidad (frecuencia entre amplitud).']],'explain':'Densidades: 8/10 = 0,8 y 12/20 = 0,6. El modal es 0–10, con densidad 0,8.','where':'1.5'},
 {'q':'Grupo A: 10 personas, media 20, varianza 4. Grupo B: 30 personas, media 24, varianza 9. Calcula la varianza total.','kind':'num','key':10.75,'dec':2,'alts':[[3,'Esa es solo la varianza entre. Súmale la de dentro.'],[7.75,'Esa es solo la varianza dentro. Súmale la de entre.'],[6.5,'Has hecho la media simple de las varianzas. Hay que ponderar por el tamaño y sumar la varianza entre.']],'explain':'Media global = (200 + 720)/40 = 23. Dentro = (4·10 + 9·30)/40 = 7,75. Entre = ((20−23)²·10 + (24−23)²·30)/40 = 3. Total = 10,75.','where':'1.7'},
 {'q':'En un diagrama de caja, C₁ = 12 y C₃ = 20. ¿Cuál es el límite superior a partir del cual un dato es atípico?','kind':'num','key':32,'dec':1,'alts':[[28,'Has sumado el IQR (8), pero hay que sumar 1,5 · IQR = 12.'],[8,'Eso es el IQR. Ahora: C₃ + 1,5 · IQR.']],'explain':'IQR = 20 − 12 = 8. Límite = 20 + 1,5·8 = 32.','where':'1.10'},
 {'q':'Si r = 0,6, ¿qué porcentaje de la variabilidad de Y explica la recta? (escribe el número del %)','kind':'pct','key':0.36,'dec':2,'alts':[[0.6,'Ese es r. El porcentaje explicado es R² = r².']],'explain':'R² = 0,6² = 0,36 → 36 %.','where':'3.4'},
 {'q':'Escribe el nombre de la función de Excel que calcula el coeficiente de correlación r.','kind':'text','key':'COEF.DE.CORREL','accept':['COEF.DE.CORREL','PEARSON'],'alts':[['COEFICIENTE.R2','Esa da R², no r.'],['COVARIANZA.P','Esa da la covarianza.'],['PENDIENTE','Esa da la pendiente b.']],'explain':'=COEF.DE.CORREL(A2:A11;B2:B11). PEARSON hace lo mismo.','where':'3.4'},
 {'q':'La recta es Ŷ = 2 + 0,5X y x̄ = 10. ¿Cuánto vale ȳ?','kind':'num','key':7,'dec':2,'alts':[[5,'Te falta sumar el término independiente: 2 + 0,5·10.']],'explain':'La recta pasa por (x̄, ȳ): ȳ = 2 + 0,5·10 = 7.','where':'3.6'},
 {'q':'Una inversión crece un 10 %, baja un 5 % y crece un 8 % en tres años. ¿Cuál es la tasa media anual? (en %)','kind':'pct','key':0.04115,'dec':2,'alts':[[0.04333,'Eso es la media aritmética de las tasas. Hay que usar la geométrica: (1,10·0,95·1,08)^(1/3) − 1.'],[0.1286,'Esa es la tasa total de los tres años. Ahora haz la raíz cúbica y resta 1.']],'explain':'1,10 · 0,95 · 1,08 = 1,1286. Raíz cúbica: 1,0412. Tasa media: 4,12 % anual. En Excel: =MEDIA.GEOM(1,10;0,95;1,08)-1.','where':'4.5'},
 {'q':'Un salario nominal es de 1800 € y el IPC (en base 1) vale 1,20. ¿Cuál es el salario real?','kind':'num','key':1500,'dec':0,'alts':[[2160,'Has multiplicado. Para deflactar se divide entre el IPC.'],[15,'Con el IPC en base 1 no hay que dividir entre 100.']],'explain':'Real = 1800 / 1,20 = 1500 € del año base.','where':'4.7'},
]
json.dump({'S4':{'tests':T,'cortas':C}},open('/home/claude/xl3/sim_test.json','w'),ensure_ascii=False,indent=1)
print(len(T),len(C))
