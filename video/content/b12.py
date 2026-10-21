import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 'b12', 'tab': 'Boletín T1-2', 'color': 't2'}
S = []
def E(n, t): return (f'Ej. {n}.', t)
S.append(Scene('', '', 'title', card('Boletín', 'Ejercicios de los Temas 1 y 2', 'Los 22 ejercicios, resueltos a mano y en Excel'), [
    (3, 'En este vídeo resolvemos los 22 ejercicios del boletín de los Temas 1 y 2. Para cada uno: el enunciado, la resolución a mano paso a paso, cómo se haría en Excel y la frase de interpretación. Un consejo: antes de ver cada solución, para el vídeo e inténtalo tú en papel.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:72px">Antes de cada ejercicio, 3 preguntas</h1>',
    Step(1, '¿Qué **variable** es y de qué **tipo**?'), Step(2, '¿Los datos vienen **sueltos**, en **tabla de valores** o en **intervalos**?'), Step(3, '¿Qué me piden: **centro, dispersión, posición, forma o relación**?')], [
    (2, 'Antes de empezar cualquier ejercicio, hazte tres preguntas. Primera: ¿qué variable es y de qué tipo?'),
    (3, 'Segunda: ¿los datos vienen sueltos, en una tabla de valores o en intervalos?'),
    (4, 'Y tercera: ¿qué me piden exactamente? ¿El centro, la dispersión, una posición, la forma o la relación entre dos variables?'),
]))
# ---- Ej 1
S.append(Scene(*E(1, 'Medias, varianzas y datos tipificados'), 'enun', [
    Enun('Primer conjunto: 1, 2, 3, 4, 5, 6. Segundo: 1, 1, 1, 6, 6, 6. Tercero: −13, 2, 3, 4, 5, 20.\na) Medias y varianzas. b) Datos tipificados del primer conjunto.')], [
    (1, 'Ejercicio 1. Tres conjuntos de seis datos. Nos piden la media y la varianza de cada uno, y tipificar el primero.'),
]))
S.append(Scene(*E(1, 'Medias, varianzas y datos tipificados'), 'mano', [
    T(['', 'Σxᵢ', 'x̄', 'Σxᵢ²', 'S² = Σxᵢ²/6 − x̄²'], [['1.º', 21, '3,5', 91, '15,167 − 12,25 = **2,917**'], ['2.º', 21, '3,5', 111, '18,5 − 12,25 = **6,25**'], ['3.º', 21, '3,5', 623, '103,833 − 12,25 = **91,583**']], small=True),
    Res('Misma media (3,5), pero dispersión muy distinta: **la media sola no basta**.'),
    Step(1, 'b) S = √2,917 = 1,708. Para cada dato: z = (x − 3,5) ÷ 1,708'),
    T(['x', 1, 2, 3, 4, 5, 6], [['z', '−1,464', '−0,878', '−0,293', '0,293', '0,878', '1,464']], small=True),
    XL('=NORMALIZACION(A2;PROMEDIO($A$2:$A$7);DESVEST.P($A$2:$A$7))'),
], [
    (1, 'A mano: la suma de cada conjunto es 21, así que los tres tienen media 21 entre 6, 3,5. Para la varianza usamos la fórmula práctica: la suma de los cuadrados entre 6, menos 3,5 al cuadrado. En el primero, 91 entre 6 menos 12,25: 2,917. En el segundo, 6,25. En el tercero, por los valores extremos menos 13 y 20, 91,58.'),
    (2, 'Moraleja: los tres tienen la misma media, pero su dispersión es muy distinta. La media sola no basta para describir unos datos.'),
    (3, 'Para tipificar el primero: la desviación típica es la raíz de 2,917, 1,708. Y a cada dato le restas 3,5 y divides entre 1,708.'),
    (4, 'Salen estos valores. Comprobación: suman 0, porque los datos tipificados tienen media 0.'),
    (5, 'En Excel: PROMEDIO, VAR.P, y para tipificar, NORMALIZACION con el dato, la media y la desviación típica fijadas con dólares, y arrastrar.'),
]))
# ---- Ej 2
S.append(Scene(*E(2, 'Preguntas de teoría'), 'int', [
    Enun('a) ¿Qué significa estar en el percentil 98? b) Diferencias entre medidas de posición, dispersión y forma. c) Asimetría frente a curtosis.'),
    Res('a) El **98 %** de los trabajadores tiene una renta **menor o igual**; solo el **2 %** gana más.'),
    Res('b) **Posición:** dónde están los datos (media, mediana, cuartiles). **Dispersión:** cuánto se separan (varianza, S, CV, IQR). **Forma:** el dibujo (asimetría y curtosis).'),
    Res('c) **Asimetría:** si hay una cola más larga hacia un lado. **Curtosis:** si es más picuda o más plana que la normal.'),
], [
    (1, 'Ejercicio 2: tres preguntas de teoría.'),
    (2, 'a) Que la renta de un trabajador esté en el percentil 98 significa que el 98 por ciento de los trabajadores tiene una renta menor o igual que la suya, y solo un 2 por ciento gana más.'),
    (3, 'b) Las medidas de posición dicen dónde están los datos: el centro o puntos de corte. Las de dispersión, cuánto se separan. Y las de forma describen el dibujo de la distribución.'),
    (4, 'c) La asimetría mira si la distribución tiene una cola más larga hacia un lado. La curtosis, si es más picuda o más plana que la normal.'),
]))
# ---- Ej 3
S.append(Scene(*E(3, 'Número de hijos'), 'enun', [
    Enun('Hijos por familia: 0, 2, 2, 2, 4, 3, 3, 0, 0, 0, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1.\na) Tamaño muestral. b) Tabla de frecuencias. c) Comenta los gráficos. d) Interpreta: Min 0 · 1st Qu. 1 · Median 1 · Mean 1,6 · 3rd Qu. 2,5 · Max 4.')], [
    (1, 'Ejercicio 3: el número de hijos de varias familias. Nos piden el tamaño de la muestra, la tabla de frecuencias, comentar unos gráficos e interpretar unas medidas.'),
]))
S.append(Scene(*E(3, 'Número de hijos'), 'mano', [
    Step(1, 'a) Contamos: **n = 20** familias. Variable cuantitativa **discreta**.'),
    T(['xᵢ', 'nᵢ', 'fᵢ', '%', 'Nᵢ'], [[0, 4, '0,20', 20, 4], [1, 7, '0,35', 35, 11], [2, 4, '0,20', 20, 15], [3, 3, '0,15', 15, 18], [4, 2, '0,10', 10, 20]], small=True),
    Step(2, 'Comprobación: Me: n/2 = 10 → N = 11 → **1** · C₃: 15 → N = 15 **igual** → (2 + 3)/2 = **2,5** · x̄ = 32/20 = **1,6**'),
    Res('c) Tres gráficos de barras con la **misma forma** (absolutas, relativas y %): solo cambia la escala. Lo más frecuente es **1 hijo**; ligera cola a la derecha.'),
    Res('d) Todas son de **posición**. Media (1,6) > mediana (1): las familias con 3 y 4 hijos tiran de ella → asimetría positiva.'),
    Ojo('En Excel, `CUARTIL.INC` da C₃ = **2,25**, no 2,5: es el otro método.'),
], [
    (1, 'a) Contando los datos, n es 20 familias. Es una variable cuantitativa discreta.'),
    (2, 'b) Ordenamos y contamos con palotes. 4 familias sin hijos, 7 con uno, 4 con dos, 3 con tres y 2 con cuatro. Las relativas y las acumuladas salen como siempre.'),
    (3, 'Con la tabla comprobamos las medidas que nos dan. La mediana: n entre 2 es 10, la primera acumulada que llega es 11, valor 1. C3: 15, y la acumulada es justo 15, así que la media entre 2 y 3: 2,5. Y la media, 32 entre 20, 1,6. Coinciden.'),
    (4, 'c) Los tres gráficos son diagramas de barras con la misma forma: uno con frecuencias absolutas, otro con relativas y otro con porcentajes. Solo cambia la escala. Lo más frecuente es tener un hijo, y a partir de ahí las barras bajan.'),
    (5, 'd) Todas son medidas de posición. La media es mayor que la mediana porque las familias con 3 y 4 hijos tiran de ella hacia arriba: hay asimetría positiva.'),
    (6, 'Ojo: en Excel, CUARTIL.INC da 2,25 para el tercer cuartil, por la diferencia de método. En papel, la receta.'),
]))
# ---- Ej 4
S.append(Scene(*E(4, 'Lesiones en fútbol y baloncesto'), 'enun', [
    Enun('Fútbol (X): valores 1 a 7 con frecuencias **absolutas** 1, 3, 5, 7, 5, 3, 1.\nBaloncesto (Y): valores 1 a 7 con frecuencias **relativas** 0,24 · 0,16 · 0,08 · 0,04 · 0,08 · 0,16 · 0,24.\nMedia, moda, gráficos, medianas y ¿dónde hay más variabilidad?')], [
    (1, 'Ejercicio 4: lesiones de jugadores de fútbol, con frecuencias absolutas, y de baloncesto, con frecuencias relativas. Ojo a esa diferencia, que cambia cómo se calcula la media.'),
]))
S.append(Scene(*E(4, 'Lesiones en fútbol y baloncesto'), 'mano', [
    Step(1, 'Media fútbol (absolutas, n = 25): Σxᵢnᵢ = 100 → 100 ÷ 25 = **4**'),
    Step(2, 'Media baloncesto (relativas): Σxᵢfᵢ = **4** (se multiplica por fᵢ y **no se divide**)'),
    Step(3, 'Moda: fútbol **4** · baloncesto **1 y 7** (bimodal)'),
    Step(4, 'Mediana fútbol: n/2 = 12,5 → acumuladas 1, 4, 9, **16** → **Me = 4** · baloncesto: Fᵢ 0,24 · 0,40 · 0,48 · **0,52** → **Me = 4**'),
    Step(5, 'S²ₓ = 452/25 − 4² = **2,08** · S²ᵧ = 21,76 − 4² = **5,76**'),
    Res('Misma media, pero baloncesto tiene casi el **triple** de varianza: **más variabilidad en baloncesto**.'),
    XL('=SUMAPRODUCTO(A2:A8;C2:C8)', 'media con relativas, sin dividir'),
], [
    (1, 'La media de fútbol: valor por frecuencia, sumado, da 100; entre 25 jugadores, 4 lesiones.'),
    (2, 'En baloncesto nos dan frecuencias relativas, así que se multiplica cada valor por su frecuencia relativa y se suma, sin dividir, porque las relativas ya suman 1. También da 4.'),
    (3, 'La moda: en fútbol, 4, la frecuencia más alta. En baloncesto, la más alta, 0,24, está en el 1 y en el 7: es bimodal.'),
    (4, 'Lo que piden de las medianas: con 4 lesiones o más estás en la mitad de futbolistas que más se lesiona. Las acumuladas llegan a 12,5 en el valor 4. En baloncesto, la acumulada relativa pasa de 0,5 también en el 4.'),
    (5, 'Para comparar la variabilidad, las varianzas: fútbol, 452 entre 25 menos 16, 2,08. Baloncesto, 21,76 menos 16, 5,76.'),
    (6, 'Las dos tienen media 4, pero la varianza de baloncesto casi triplica la de fútbol. Hay más variabilidad en baloncesto: muchos jugadores con muy pocas lesiones y muchos con muchísimas. Se ve también en los gráficos: fútbol es una montaña y baloncesto una U.'),
    (7, 'En Excel, con relativas, la media es SUMAPRODUCTO de valores y frecuencias, sin dividir entre nada.'),
]))
# ---- Ej 5
S.append(Scene(*E(5, 'Histograma con amplitudes distintas'), 'mano', [
    Enun('Intervalos [7,8], (8,9], (9,10], (10,12], (12,15] con frecuencias 3, 6, 9, 9, 3.'),
    T(['Intervalo', 'nᵢ', 'aᵢ', 'dᵢ = nᵢ/aᵢ'], [['[7, 8]', 3, 1, 3], ['(8, 9]', 6, 1, 6], ['(9, 10]', 9, 1, 9], ['(10, 12]', 9, 2, '4,5'], ['(12, 15]', 3, 3, 1]], small=True),
    Img('b5_hist.svg', 820),
    Ojo('Con altura 9 en (10, 12], parecería tan lleno como (9, 10]. Pero sus 9 datos ocupan el doble: la altura es **4,5**.'),
], [
    (1, 'Ejercicio 5: dibujar el histograma de estos intervalos. Fíjate en que no miden lo mismo.'),
    (2, 'Las amplitudes son 1, 1, 1, 2 y 3. Así que la altura de cada barra tiene que ser la densidad: la frecuencia entre la amplitud. 3, 6, 9, 4,5 y 1.'),
    (3, 'Así queda el histograma. En papel, el eje horizontal va a escala, y el área de cada rectángulo es su frecuencia: en el de 10 a 12, base 2 por altura 4,5, 9.'),
    (4, 'El error sería dibujar el 9 como altura del intervalo de 10 a 12. Parecería igual de lleno que el de 9 a 10, pero sus 9 datos están repartidos en el doble de espacio.'),
]))
# ---- Ej 6
S.append(Scene(*E(6, 'Notas de un examen'), 'mano', [
    Enun('Notas 1 a 8 con frecuencias 4, 4, 8, 7, 5, 10, 7, 5.'),
    T(['xᵢ', 1, 2, 3, 4, 5, 6, 7, 8], [['nᵢ', 4, 4, 8, 7, 5, 10, 7, 5], ['Nᵢ', 4, 8, 16, 23, 28, 38, 45, 50], ['Fᵢ', '0,08', '0,16', '0,32', '0,46', '0,56', '0,76', '0,90', 1]], small=True),
    Step(1, 'Total: **50 alumnos**'),
    Step(2, 'Más de un 3: 50 − 16 = **34 alumnos**'),
    Step(3, 'Con un 6: 10/50 = **20 %** · Más de un 4: 1 − 0,46 = **54 %**'),
    Step(4, '≥ 2 y < 5 (2, 3 y 4): 4 + 8 + 7 = **19** (o 23 − 4)'),
    Truco('«**Más de** 3» no incluye el 3. «**Al menos** 3» sí. Subraya estas palabras.'),
], [
    (1, 'Ejercicio 6: las notas de un examen, del 1 al 8, con sus frecuencias.'),
    (2, 'Montamos la tabla con acumuladas absolutas y relativas.'),
    (3, 'El total de alumnos es la última acumulada: 50.'),
    (4, 'Alumnos con más de un 3: todos menos los que tienen 3 o menos. La acumulada hasta el 3 es 16, así que 50 menos 16, 34.'),
    (5, 'Porcentaje con un 6: 10 entre 50, el 20 por ciento. Con más de un 4: 1 menos la acumulada hasta el 4, 0,46: el 54 por ciento.'),
    (6, 'Nota mayor o igual que 2 y menor que 5: los que tienen 2, 3 o 4. 4 más 8 más 7, 19 alumnos. O con acumuladas: la del 4 menos la del 1, 23 menos 4.'),
    (7, 'El truco aquí son las palabras: más de 3 no incluye el 3; al menos 3, sí. Menos de 5 no incluye el 5. Subráyalas en el enunciado. En Excel, con datos sueltos, se haría con CONTAR.SI y CONTAR.SI.CONJUNTO.'),
]))
# ---- Ej 7
S.append(Scene(*E(7, 'Pólizas de seguros'), 'mano', [
    Enun('Pólizas al día en 26 días: [30,40] 2 · (40,50] 4 · (50,60] 6 · (60,70] 9 · (70,80] 5'),
    Step(1, 'a) Más de 50: 6 + 9 + 5 = **20 días**'),
    Step(2, 'b) Más de 62: el 62 está **dentro** de (60, 70]. Reparto uniforme: 9 · 8/10 = 7,2 → 7,2 + 5 = **12,2 ≈ 12 días**'),
    Step(3, 'c) Entre 52 y 67: 6 · 8/10 + 9 · 7/10 = 4,8 + 6,3 = 11,1 → 11,1/26 = **42,7 %**'),
    Ojo('Escribe la frase: «**suponiendo que los datos se reparten uniformemente dentro del intervalo**».'),
    XL('=C5*(B5-62)/(B5-A5)+C6', 'b) con celdas'),
], [
    (1, 'Ejercicio 7: pólizas vendidas al día durante 26 días, en intervalos.'),
    (2, 'a) Días con más de 50 pólizas: los tres últimos intervalos, 6 más 9 más 5: 20 días.'),
    (3, 'b) Más de 62: el 62 cae dentro del intervalo de 60 a 70. Como no tenemos los datos exactos, suponemos que los 9 días de ese intervalo están repartidos de forma uniforme. De 62 a 70 hay 8 de las 10 unidades, así que 9 por 8 décimos, 7,2 días. Más los 5 del último intervalo: 12,2, unos 12 días.'),
    (4, 'c) Entre 52 y 67, por trozos: de 52 a 60, 6 por 8 décimos, 4,8. De 60 a 67, 9 por 7 décimos, 6,3. En total 11,1 días, que sobre 26 es el 42,7 por ciento.'),
    (5, 'Es la misma idea que hay detrás de la fórmula de la mediana. Escribe siempre la frase de que suponemos un reparto uniforme dentro del intervalo.'),
    (6, 'En Excel se hace igual, con referencias a las celdas de la tabla.'),
]))
# ---- Ej 8
S.append(Scene(*E(8, 'Exportaciones'), 'mano', [
    Enun('Exportaciones (miles €): [0,10] 4 · (10,20] 20 · (20,40] 10 · (40,50] 10 empresas. a) Media, varianza y CV. b) Francia CV = 0,64. c) España +1 %, Francia +10⁶ €.'),
    T(['xᵢ', 'nᵢ', 'xᵢ·nᵢ', 'xᵢ²·nᵢ'], [[5, 4, 20, 100], [15, 20, 300, 4500], [30, 10, 300, 9000], [45, 10, 450, 20250], ['**Σ**', '**44**', '**1070**', '**33 850**']], small=True),
    Step(1, 'x̄ = 1070/44 = **24,32** · S² = 33 850/44 − 24,32² = **177,94** · S = 13,34 · CV = **0,549**'),
    Step(2, 'b) Francia 0,64 > 0,549 → **más dispersión relativa en Francia**'),
    Step(3, 'c) España ×1,01: media 24,56; varianza ×1,01² = 181,52; **CV igual**. Francia +1000 (miles): media +1000; **varianza igual**; **CV baja**.'),
], [
    (1, 'Ejercicio 8: exportaciones de empresas, en miles de euros, en intervalos.'),
    (2, 'Marcas de clase 5, 15, 30 y 45. Montamos la tabla con marca por frecuencia y marca al cuadrado por frecuencia.'),
    (3, 'Media: 1070 entre 44, 24,32 miles de euros. Varianza: 33 850 entre 44, menos la media al cuadrado: 177,94. Desviación típica, 13,34. CV: 0,549.'),
    (4, 'b) Francia tiene un CV de 0,64, mayor: más dispersión relativa en Francia. Comparamos el CV porque son países distintos, con medias distintas.'),
    (5, 'c) En España suben un 1 por ciento: se multiplica por 1,01. La media pasa a 24,56, la varianza se multiplica por 1,01 al cuadrado, y el CV no cambia. En Francia se suma un millón de euros, que son 1000 miles: la media sube 1000, la varianza no cambia, y como la media sube y la desviación no, el CV baja.'),
]))
# ---- Ej 9
S.append(Scene(*E(9, 'Óxido de azufre'), 'mano', [
    Enun('Toneladas diarias: intervalos [5,9) … [29,33) con % de días 3,75 · 12,5 · 17,5 · 31,25 · 21,25 · 11,25 · 2,5. Media, varianza y gráfico.'),
    T(['xᵢ', 'fᵢ', 'xᵢ·fᵢ', 'xᵢ²·fᵢ'], [[7, '0,0375', '0,2625', '1,8375'], [11, '0,125', '1,375', '15,125'], [15, '0,175', '2,625', '39,375'], [19, '0,3125', '5,9375', '112,8125'], [23, '0,2125', '4,8875', '112,4125'], [27, '0,1125', '3,0375', '82,0125'], [31, '0,025', '0,775', '24,025'], ['**Σ**', '**1**', '**18,9**', '**387,6**']], small=True),
    Res('Media = **18,9 t**. Varianza = 387,6 − 18,9² = **30,39 t²**. S = **5,51 t**.'),
    Li('**Histograma**: todos los intervalos miden 4 → la altura puede ser el %.'),
], [
    (1, 'Ejercicio 9: toneladas de óxido de azufre emitidas al día. Nos dan porcentajes de días.'),
    (2, 'Pasamos los porcentajes a frecuencias relativas, dividiendo entre 100, y usamos la media con relativas: marca por frecuencia relativa, sumado. Las marcas son 7, 11, 15, y así de 4 en 4.'),
    (3, 'La media es 18,9 toneladas al día. La varianza, 387,6 menos 18,9 al cuadrado: 30,39. Y la desviación típica, 5,51 toneladas.'),
    (4, 'El gráfico es un histograma, porque es continua en intervalos. Como todos miden 4, la altura puede ser directamente el porcentaje.'),
]))
# ---- Ej 10
S.append(Scene(*E(10, 'Sueldos de 15 trabajadores'), 'mano', [
    Enun('Sueldo (miles €): 10, 12, 15, 20, 30 con 3, 5, 3, 3, 1 trabajadores. a) Media, mediana y moda. b) Dispersión absoluta y relativa. c) Si suben un 5 %.'),
    Step(1, 'Media = (30 + 60 + 45 + 60 + 30)/15 = 225/15 = **15**'),
    Step(2, 'Mediana: n/2 = 7,5 → acumuladas 3, **8** → **12** · Moda: **12** (frecuencia 5)'),
    Step(3, 'Σxᵢ²nᵢ = 3795 → S² = 253 − 225 = 28 → S = **5,29** · CV = **0,353**'),
    T(['Medida', 'Antes', '+5 % (× 1,05)'], [['Media · Me · Mo', '15 · 12 · 12', '15,75 · 12,6 · 12,6'], ['S', '5,29', '5,56'], ['S²', 28, '30,87 (× 1,05²)'], ['CV', '0,353', '**no cambia**']], small=True),
], [
    (1, 'Ejercicio 10: los sueldos de 15 trabajadores, en miles de euros.'),
    (2, 'La media: cada sueldo por su frecuencia, 225, entre 15: 15 mil euros.'),
    (3, 'La mediana: n entre 2 es 7,5; las acumuladas son 3, 8… la primera que llega es 8, en el 12. La mediana es 12. Y la moda también es 12, el que más se repite. La media es mayor porque el sueldo de 30 tira hacia arriba.'),
    (4, 'b) Dispersión absoluta: la desviación típica. La suma de los cuadrados por frecuencia es 3795; entre 15, 253; menos 15 al cuadrado, 28. La raíz: 5,29. La relativa, el CV: 5,29 entre 15, 0,353.'),
    (5, 'c) Subir un 5 por ciento es multiplicar por 1,05. Media, mediana, moda y desviación típica se multiplican por 1,05; la varianza por 1,05 al cuadrado; y el CV no cambia.'),
]))
# ---- Ej 11
S.append(Scene(*E(11, 'Superficie de 200 apartamentos'), 'mano', [
    Enun('Superficie (m²): 40–50, 50–60, 60–80, 80–100, 100–120 con 50, 40, 60, 40, 10 pisos. a) Alquiler medio a 10 €/m². b) Tipo más frecuente.'),
    Step(1, 'a) Media = (45·50 + 55·40 + 70·60 + 90·40 + 110·10)/200 = 13 350/200 = **66,75 m²** → alquiler = 10 · 66,75 = **667,5 €**'),
    T(['Intervalo', 'nᵢ', 'aᵢ', 'dᵢ'], [['40–50', 50, 10, '**5**'], ['50–60', 40, 10, 4], ['60–80', 60, 20, 3], ['80–100', 40, 20, 2], ['100–120', 10, 20, '0,5']], small=True),
    Step(2, 'b) Mayor densidad: el **primero** (no hay anterior → 0): Mo = 40 + (5 − 0)/((5 − 0) + (5 − 4)) · 10 = **48,33 m²**'),
    Ojo('Mirando frecuencias ganaría 60–80 (60 pisos), pero es el doble de ancho. **Siempre densidades.**'),
], [
    (1, 'Ejercicio 11: la superficie de 200 apartamentos.'),
    (2, 'a) La superficie media con las marcas de clase: 13 350 entre 200, 66,75 metros cuadrados. Y como el alquiler es 10 euros por metro, es una transformación lineal: el alquiler medio es 10 por 66,75, 667,5 euros.'),
    (3, 'b) Para la moda, las amplitudes son distintas, así que necesitamos densidades: 5, 4, 3, 2 y 0,5.'),
    (4, 'La mayor densidad es la del primer intervalo. Como no tiene anterior, se pone 0. La moda: 40 más 5 entre 6, por 10: 48,33 metros cuadrados.'),
    (5, 'Ojo: mirando solo las frecuencias ganaría el de 60 a 80, con 60 pisos. Pero es el doble de ancho. Con amplitudes distintas, siempre densidades.'),
]))
# ---- Ej 12
S.append(Scene(*E(12, 'Puntuación para cada puesto'), 'mano', [
    Enun('Puntuaciones 0–30, 30–50, 50–70, 70–90, 90–100 con 94, 140, 160, 98, 8 empleados (n = 500). El 65 % con menos puntos: administrativos; el 20 % siguiente: jefes de sección; el 10 %: jefes de departamento; el 5 % con más: inspectores.'),
    P('Jefe de sección → superar al 65 % → **P₆₅**. Inspector → estar en el 5 % de arriba → **P₉₅**. Acumuladas: 94, 234, 394, 492, 500.', 's'),
    Step(1, 'P₆₅: 0,65 · 500 = 325 → 50–70: 50 + (325 − 234)/160 · 20 = **61,4 puntos**'),
    Step(2, 'P₉₅: 0,95 · 500 = 475 → 70–90: 70 + (475 − 394)/98 · 20 = **86,5 puntos**'),
    XL('=A4+(0,65*500-D3)/C4*(B4-A4)', 'P₆₅ con celdas'),
], [
    (1, 'Ejercicio 12: puntuaciones de 500 empleados para repartir puestos. El 65 por ciento con menos puntos serán administrativos, el siguiente 20 por ciento jefes de sección, el siguiente 10 por ciento jefes de departamento y el 5 por ciento con más puntos, inspectores.'),
    (2, 'El planteamiento: para ser jefe de sección hay que superar al 65 por ciento de abajo, así que necesitamos el percentil 65. Para ser inspector, estar en el 5 por ciento de arriba: el percentil 95.'),
    (3, 'Percentil 65: 0,65 por 500 es 325. La primera acumulada que llega es 394, el intervalo de 50 a 70. 50 más, 325 menos 234, entre 160, por 20: 61,4 puntos.'),
    (4, 'Percentil 95: 475, en el intervalo de 70 a 90. 70 más, 475 menos 394, entre 98, por 20: 86,5 puntos. Para jefe de departamento, el percentil 85: 76,3.'),
    (5, 'En Excel, la fórmula de los apuntes con referencias a las celdas de la tabla.'),
]))
# ---- Ej 13
S.append(Scene(*E(13, 'Viviendas en Pontevedra y Galicia'), 'mano', [
    Enun('Pontevedra: 20–40, 40–60, 60–90, 90–120, 120–150, 150–300 m² con 4, 12, 51, 19, 10, 14 viviendas (n = 110). a) Media, moda, dispersión y 30 % central. b) Media y varianza de Galicia.'),
    Step(1, 'Media = 11 040/110 = **100,36 m²** · Modal (mayor densidad 1,70): 60–90 → Mo = 60 + (1,7 − 0,6)/((1,7 − 0,6) + (1,7 − 0,633)) · 30 = **75,23**'),
    Step(2, 'S² = 1 420 950/110 − 100,36² = **2844,87** · S = **53,34** · CV = 0,53'),
    Step(3, '30 % central = entre **P₃₅ y P₆₅**: P₃₅ = 60 + (38,5 − 16)/51 · 30 = **73,24** · P₆₅ = 90 + (71,5 − 67)/19 · 30 = **97,11**'),
], [
    (1, 'Ejercicio 13: superficie de viviendas en Pontevedra, y después Galicia entera.'),
    (2, 'Con la tabla de trabajo de siempre: la media es 11 040 entre 110, 100,36 metros cuadrados. Para la moda, densidades: la mayor es 1,70, en el intervalo de 60 a 90. Aplicando la fórmula, 75,23.'),
    (3, 'La dispersión: la varianza, 1 420 950 entre 110 menos la media al cuadrado, 2844,87. La desviación típica, 53,34. Un CV de 0,53: dispersión relativa alta, sobre todo por las viviendas grandes.'),
    (4, 'El 30 por ciento central deja un 35 por ciento por debajo y otro 35 por encima: está entre el percentil 35 y el 65. Con la fórmula: entre 73,24 y 97,11 metros cuadrados.'),
]))
S.append(Scene(*E(13, 'Viviendas en Pontevedra y Galicia'), 'mano', [
    T(['Provincia', 'T', 'Media', 'Varianza'], [['Pontevedra', 110, '100,36', '2844,87'], ['A Coruña', 203, '102,2', '3058,09 (55,3²)'], ['Lugo', 46, '101,1', '2323,24 (48,2²)'], ['Ourense', 41, '105,7', '2601,00 (51²)']], small=True),
    Step(1, 'Media global = 40 770,9/400 = **101,93 m²**'),
    Step(2, 'Dentro = 1 147 237,8/400 = **2868,09**'),
    Step(3, 'Entre = 899,10/400 = **2,25**'),
    Step(4, 'Total = 2868,09 + 2,25 = **2870,34** → S = **53,58 m²**'),
    Res('Casi toda la variabilidad es **dentro** de cada provincia: sus medias son muy parecidas.'),
], [
    (1, 'b) Para Galicia, varianza en subpoblaciones. Nos dan desviaciones típicas, así que primero las elevamos al cuadrado.'),
    (2, 'La media global, ponderando por el tamaño: 101,93 metros cuadrados.'),
    (3, 'La varianza dentro: cada varianza por su tamaño, entre 400: 2868,09.'),
    (4, 'La varianza entre: cada media menos 101,93, al cuadrado, por su tamaño, entre 400: 2,25.'),
    (5, 'La total, 2870,34, y la desviación típica, 53,58.'),
    (6, 'Interpretación: casi toda la variabilidad es dentro de cada provincia; las cuatro tienen medias muy parecidas.'),
]))
# ---- Ej 14
S.append(Scene(*E(14, 'Salarios por categoría'), 'mano', [
    Enun('Técnicos: 30 empleados, media 30 mil €, desv. 7. Administrativos: 50, media 15, desv. 2,25. Operarios: 120, media 20, desv. 4,24. a) ¿Dónde hay más homogeneidad? b) Media y desviación de la empresa.'),
    Step(1, 'a) Medias distintas → **CV**: técnicos 0,233 · administrativos **0,150** · operarios 0,212 → **administrativos**, los más homogéneos'),
    Step(2, 'b) Media = (30·30 + 15·50 + 20·120)/200 = **20,25**'),
    Step(3, 'Dentro = (49·30 + 5,0625·50 + 17,98·120)/200 = **19,40**'),
    Step(4, 'Entre = (9,75²·30 + 5,25²·50 + 0,25²·120)/200 = **21,19**'),
    Step(5, 'Total = 40,59 → S = **6,37 mil €** · el **52 %** se debe a las diferencias entre categorías'),
], [
    (1, 'Ejercicio 14: salarios de tres categorías, con tamaño, media y desviación típica.'),
    (2, 'a) Como las medias son distintas, comparamos el coeficiente de variación: 7 entre 30, 2,25 entre 15 y 4,24 entre 20. El menor es el de administrativos: es la categoría más homogénea.'),
    (3, 'b) La media de la empresa, ponderada: 4050 entre 200, 20,25 mil euros.'),
    (4, 'La varianza dentro, con las desviaciones al cuadrado: 19,40.'),
    (5, 'La varianza entre: cada media menos 20,25, al cuadrado, por su tamaño: 21,19.'),
    (6, 'La total, 40,59, y la desviación típica de la empresa, 6,37 mil euros. Más de la mitad de la variabilidad, el 52 por ciento, se debe a las diferencias entre categorías.'),
]))
# ---- Ej 15
S.append(Scene(*E(15, 'Hogares: personas y superficie'), 'mano', [
    T(['X \\ Y', '0–60', '60–90', '90–120', '120–200', 'Total'], [[1, 43, 60, 23, 11, 137], [2, 39, 114, 46, 23, 222], [3, 36, 106, 45, 20, 207], [4, 30, 118, 58, 28, 234], ['5 o más', 23, 92, 53, 32, 200], ['Total', 171, 490, 225, 114, 1000]], hl_row=4, small=True),
    Step(1, 'a) Moda de Y (fila Total). Densidades: 2,85 · **16,33** · 7,5 · 1,43 → 60 + (16,33 − 2,85)/((16,33 − 2,85) + (16,33 − 7,5)) · 30 = **78,13 m²**'),
    Step(2, 'b) Mediana de X (columna Total): 500 → acumuladas 137, 359, **566** → **3 personas**'),
    Step(3, 'c) Y | X ≥ 5 (la fila «5 o más», n = 200): media = 18 275/200 = **91,38 m²**'),
    Step(4, 'Σxᵢ²nᵢ = 1 941 725 → S² = 9708,63 − 8349,39 = **1359,23** → S = 36,87'),
], [
    (1, 'Ejercicio 15: 1000 hogares según el número de personas y la superficie de la vivienda. a) La superficie más frecuente, b) el número mediano de integrantes, y c) la varianza de la superficie de los hogares con más de 4 personas.'),
    (2, 'a) La superficie es Y, así que usamos su marginal, la fila de totales. Las amplitudes son distintas: densidades. La mayor, 16,33, en el intervalo de 60 a 90. La moda: 78,13 metros cuadrados.'),
    (3, 'b) El número de personas es X: su marginal es la columna de totales. n entre 2 es 500; las acumuladas son 137, 359, 566. La mediana es 3 personas.'),
    (4, 'c) Más de 4 personas es la fila de 5 o más: una distribución condicionada, con 200 hogares. Con las marcas 30, 75, 105 y 160, la media es 91,38 metros cuadrados.'),
    (5, 'Y la varianza: 1 941 725 entre 200, menos la media al cuadrado: 1359,23. La desviación típica, 36,87.'),
]))
# ---- Ej 16
S.append(Scene(*E(16, 'Ingresos y gasto en streaming'), 'mano', [
    T(['X \\ Y', '0–12', '12–48', '48–120', '120–480', 'Total'], [['6–10', 4, 1, 1, 0, 6], ['10–15', 9, 8, 3, 0, 20], ['15–20', 9, 12, 20, 3, 44], ['20–30', 5, 8, 12, 3, 28], ['30–50', 1, 1, 0, 0, 2], ['Total', 28, 30, 36, 6, 100]], small=True),
    Step(1, 'a) x̄ = 1848/100 = **18,48 cientos € = 1848 €**'),
    Step(2, 'b) S²ₓ = 376,84 − 18,48² = **35,33** · ȳ = 58,92 € · S²ᵧ = 8220,24 − 58,92² = **4748,67**'),
    Step(3, 'c) f₁₁ = 0,04 ≠ (6/100)·(28/100) = 0,0168 → **no independientes**'),
    Step(4, 'd) X ≤ 20 → suma de las 3 primeras filas: 22, 21, 24, 3 (n = 70). C₁ = 0 + 17,5/22 · 12 = **9,55 €** · C₃ = 48 + (52,5 − 43)/24 · 72 = **76,50 €**'),
], [
    (1, 'Ejercicio 16: 100 familias según sus ingresos, en cientos de euros, y su gasto en plataformas de streaming.'),
    (2, 'a) El ingreso medio con la marginal de X y las marcas 8, 12,5, 17,5, 25 y 40: 1848 entre 100, 18,48 cientos de euros, es decir, 1848 euros.'),
    (3, 'b) La varianza de X: 35,33. Para Y, con marcas 6, 30, 84 y 300: media 58,92 euros y varianza 4748,67.'),
    (4, 'c) ¿Son independientes? Basta una casilla: la primera tiene una frecuencia relativa de 0,04, y el producto de sus marginales es 0,0168. No coinciden: no son independientes. El gasto depende de los ingresos.'),
    (5, 'd) Las familias que no superan los 2000 euros son las tres primeras filas; las sumamos: 22, 21, 24 y 3, con 70 familias. El 50 por ciento central está entre C1 y C3. C1: 17,5 cae en el primer intervalo, 9,55 euros. C3: 52,5 cae en el de 48 a 120, 76,50 euros.'),
]))
# ---- Ej 17
S.append(Scene(*E(17, 'Gasto de turistas en Galicia'), 'mano', [
    Enun('150 turistas. Gasto diario (€): 0–60, 60–90, 90–120, 120–180, 180–300 (marcas 30, 75, 105, 150, 240).\nA Coruña 5, 8, 10, 30, 10 · Lugo 1, 2, 6, 5, 2 · Ourense 1, 1, 4, 2, 1 · Pontevedra 8, 10, 28, 12, 4'),
    Step(1, 'a) A Coruña: 8700/63 = **138,10 €** · Pontevedra: 6690/62 = **107,90 €**'),
    Step(2, 'b) Galicia (15, 21, 48, 49, 17): Me = 90 + (75 − 36)/48 · 30 = **114,38 €** · Mo (densidades) = **106,04 €**'),
    Step(3, 'c) P₇₅ de Pontevedra: 46,5 → 120 + (46,5 − 46)/12 · 60 = **122,5 €**'),
    Step(4, 'd) Norte: media 135,95, S 57,00, **CV 0,419** · Sur: 109,23, 50,17, **CV 0,459**'),
    Res('En **absoluto** hay más dispersión en el norte, pero en **relativo (CV)** el sur es más disperso.'),
], [
    (1, 'Ejercicio 17: el gasto diario de 150 turistas en las cuatro provincias gallegas.'),
    (2, 'a) Media de A Coruña: 8700 entre 63, 138,10 euros al día. Pontevedra: 6690 entre 62, 107,90. En A Coruña gastan unos 30 euros más.'),
    (3, 'b) Galicia entera es la marginal: sumamos las cuatro provincias. La mediana: 75 cae en el intervalo de 90 a 120: 114,38 euros. Y la moda, con densidades, 106,04. Ojo: el intervalo de 120 a 180 tiene más turistas, pero es el doble de ancho.'),
    (4, 'c) Para estar en el 25 por ciento que más gasta en Pontevedra, el percentil 75: 46,5 cae en el intervalo de 120 a 180. 122,5 euros.'),
    (5, 'd) El norte, A Coruña más Lugo, y el sur, Ourense más Pontevedra. Sumando filas: el norte tiene media 135,95, desviación 57 y CV 0,419. El sur, 109,23, 50,17 y CV 0,459.'),
    (6, 'En términos absolutos hay más dispersión en el norte. Pero como las medias son distintas, lo correcto es el CV: el sur es relativamente más disperso.'),
]))
# ---- Ej 18
S.append(Scene(*E(18, 'Cinturón de seguridad'), 'mano', [
    T(['', 'Con cinturón', 'Sin cinturón', 'Total'], [['Grave', 5244, 2730, 7974], ['Leve', 24351, 6412, 30763], ['Total', 29595, 9142, 38737]], small=True),
    Step(1, 'a) Relativas: cada casilla ÷ 38 737. Grave–con: 0,1354'),
    Step(2, 'b) Marginales: grave 20,6 %, leve 79,4 % · con cinturón 76,4 %, sin 23,6 %'),
    Step(3, 'c) X | con cinturón: grave 5244/29 595 = **17,7 %** · Y | leve: con 79,2 %, sin 20,8 %'),
    Step(4, 'd) 0,1354 ≠ 0,2059 · 0,7640 = 0,1573 → **no independientes**'),
    Res('Sin cinturón, el **29,9 %** tuvo heridas graves; con cinturón, el **17,7 %**. La gravedad **depende** del cinturón.'),
], [
    (1, 'Ejercicio 18: 38 737 heridos en accidentes, según la gravedad y si llevaban cinturón.'),
    (2, 'a) Las frecuencias relativas: cada casilla entre el total. Grave con cinturón, 0,1354.'),
    (3, 'b) Las marginales: el 20,6 por ciento fueron graves y el 79,4 leves. El 76,4 llevaba cinturón y el 23,6 no.'),
    (4, 'c) Gravedad sabiendo que llevaban cinturón: la columna de con cinturón, dividida entre su total: el 17,7 por ciento graves. Y cinturón sabiendo que fue leve: la fila de leve: 79,2 con cinturón y 20,8 sin.'),
    (5, 'd) ¿Independientes? 0,1354 frente a 0,2059 por 0,7640, 0,1573. No coinciden: no son independientes.'),
    (6, 'La interpretación: entre los que no llevaban cinturón, el 29,9 por ciento tuvo heridas graves; entre los que sí, el 17,7. La gravedad depende del uso del cinturón.'),
]))
# ---- Ej 19
S.append(Scene(*E(19, 'Diagrama de caja: satisfacción laboral'), 'int', [
    Enun('Comenta el diagrama de caja de la satisfacción (0 a 10) en Educación, Sanidad y Servicios Sociales.'),
    Li('**Nivel:** Educación ≈ 7,2 > Sanidad ≈ 5,9 > Servicios Sociales ≈ 4,9'),
    Li('**Dispersión:** Educación, caja estrecha (opiniones parecidas). Servicios Sociales, la más ancha y bigotes de 1,3 a 9,7.'),
    Li('**Atípicos:** solo en Educación (≈ 9,2 y ≈ 4,7).'),
    Li('**Forma:** en Sanidad, mediana baja en la caja y bigote superior largo → ligera asimetría positiva.'),
    Res('Satisfacción **más alta y homogénea** en Educación; **más baja y heterogénea** en Servicios Sociales.'),
], [
    (1, 'Ejercicio 19: comentar un diagrama de caja de la satisfacción laboral en tres sectores. Se comenta siempre en cuatro puntos.'),
    (2, 'El nivel, con las medianas: Educación es el sector más satisfecho, con unos 7,2; después Sanidad, 5,9; y por último Servicios Sociales, 4,9.'),
    (3, 'La dispersión: Educación tiene la caja más estrecha, opiniones muy parecidas. Servicios Sociales, la más ancha y los bigotes más largos: opiniones muy variadas.'),
    (4, 'Los atípicos: solo en Educación, un trabajador muy satisfecho y otro muy poco.'),
    (5, 'La forma: en Sanidad la mediana está más cerca de la parte baja de la caja y el bigote de arriba es más largo: ligera asimetría positiva.'),
    (6, 'Conclusión: la satisfacción es más alta y homogénea en Educación, y más baja y heterogénea en Servicios Sociales.'),
]))
# ---- Ej 20
S.append(Scene(*E(20, 'Encuesta de Presupuestos Familiares'), 'int', [
    T(['', 'Alimentación', 'Vivienda', 'Sanidad'], [['Media · Mediana', '9532 · 9499', '7933 · 7737', '874 · 868'], ['CV', '0,11', '0,21', '0,30'], ['Asimetría · Curtosis', '−0,05 · −0,33', '0,98 · 1,49', '0,58 · 0,05']], small=True),
    Li('**Alimentación:** el gasto mayor; **simétrica**, algo platicúrtica; la **menos dispersa**.'),
    Li('**Vivienda:** media > mediana y asimetría **positiva** (Madrid, 13 718 €, atípico); leptocúrtica.'),
    Li('**Sanidad:** el gasto menor; la **más dispersa** en relativo (CV 30 %).'),
    Li('**Radial:** cada valor ÷ 12 000 = parte del radio. La línea que llega más lejos en alimentación y vivienda es **Barcelona**.'),
], [
    (1, 'Ejercicio 20: un resumen de estadísticos de la Encuesta de Presupuestos Familiares, por provincias.'),
    (2, 'Alimentación es el gasto mayor. La media y la mediana son casi iguales y la asimetría casi 0: es simétrica. La curtosis algo negativa. Y es la de menor dispersión relativa.'),
    (3, 'Vivienda: la media supera a la mediana y la asimetría es claramente positiva. Hay provincias con un gasto muy alto, como Madrid, que es un valor atípico, y estiran la cola a la derecha.'),
    (4, 'Sanidad es el gasto menor, pero la de mayor dispersión relativa, con un CV del 30 por ciento.'),
    (5, 'Y en el gráfico radial, con un máximo de 12 000, cada valor entre 12 000 da qué parte del radio ocupa. La línea que llega más lejos en alimentación y vivienda es Barcelona; la otra, Almería. Para dibujar Pontevedra, marcas cada valor sobre su radio y unes los puntos.'),
]))
# ---- Ej 21
S.append(Scene(*E(21, 'Desigualdad salarial por sexo'), 'mano', [
    Enun('Mujeres: n = 5, media 2240 €, varianza 34 400. Hombres: n = 5, media 2860 €, varianza 46 400.'),
    Step(1, 'a) Variabilidad absoluta: más en **hombres** (46 400 > 34 400)'),
    Step(2, 'b) CV: mujeres 185,47/2240 = **0,0828** · hombres 215,41/2860 = **0,0753** → más relativa en **mujeres**'),
    Step(3, 'c) Media global = **2550 €** · d) Dentro = **40 400** · e) Entre = **96 100**'),
    Step(4, 'f) Total = **136 500** · g) % entre = 96 100/136 500 = **70,4 %**'),
    Res('El **70 %** de la variabilidad de los salarios se explica por ser hombre o mujer: **desigualdad muy alta**.'),
], [
    (1, 'Ejercicio 21: salarios de mujeres y hombres.'),
    (2, 'a) La variabilidad absoluta, con las varianzas: mayor en los hombres.'),
    (3, 'b) La relativa, con el CV: mujeres, la raíz de 34 400 entre 2240, 0,0828; hombres, 0,0753. Más variabilidad relativa en las mujeres.'),
    (4, 'c) La media global, 2550 euros. d) La varianza dentro de los grupos, 40 400. e) La varianza entre: 2240 menos 2550, al cuadrado, por 5, más lo mismo con los hombres, entre 10: 96 100.'),
    (5, 'f) La total, 136 500. Y g) el porcentaje debido a las diferencias entre grupos: el 70,4 por ciento.'),
    (6, 'Interpretación: el 70 por ciento de la variabilidad de los salarios se explica por ser hombre o mujer. Es una desigualdad salarial muy alta.'),
]))
# ---- Ej 22
S.append(Scene(*E(22, 'Cuatro propuestas de subida salarial'), 'mano', [
    Enun('Media 2550 €, varianza 136 500. I: +50 € · II: +2 % · III: −1 % · IV: +1 % y +25 €.'),
    T(['', 'Y', 'Media', 'Varianza', 'S'], [['Actual', 'X', 2550, '136 500', '369,46'], ['I', 'X + 50', 2600, '136 500', '369,46'], ['II', '1,02·X', 2601, '142 014,6', '376,85'], ['III', '0,99·X', '2524,5', '133 783,65', '365,77'], ['IV', '1,01·X + 25', '2600,5', '139 243,65', '373,15']], small=True),
    Res('Para **no aumentar las diferencias**, la mejor es la **I** (suma fija): la dispersión no cambia.'),
    Ojo('En la IV no se dice el orden. Con 1,01·(X + 25) la media sería 2600,75. La varianza, igual. Escribe cuál usas.'),
], [
    (1, 'Último ejercicio, el 22: cuatro propuestas de subida salarial sobre una media de 2550 euros y una varianza de 136 500.'),
    (2, 'Aplicamos las reglas de los cambios de origen y escala: la media nueva es a por la media más b, y la varianza nueva, a al cuadrado por la varianza. Sumar 50 sube la media 50 y no cambia la varianza. Subir un 2 por ciento multiplica la media por 1,02 y la varianza por 1,02 al cuadrado. Y así con las otras.'),
    (3, 'Si lo que se quiere es no aumentar las diferencias salariales, la mejor es la primera, la suma fija: todos ganan lo mismo y la dispersión no cambia.'),
    (4, 'Un detalle: en la cuarta propuesta no se dice el orden. Aquí se aplica primero el 1 por ciento y luego los 25 euros, como en el Excel de clase. Si es al revés, la media sería 2600,75. Escribe en el examen cuál has usado.'),
]))
S.append(Scene('', '', 'title', card('Boletín', 'Fin del boletín de los Temas 1 y 2', 'Ahora: las **Prácticas 1 a 4** de la guía.'), [
    (3, 'Y hasta aquí el boletín de los Temas 1 y 2. Ahora, en la guía, las prácticas 1 a 4, primero con ayuda y después como en el examen.'),
]))
