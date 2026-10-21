import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 'b3', 'tab': 'Boletín T3', 'color': 't3'}
S = []
def E(n, t): return (f'Ej. {n}.', t)
S.append(Scene('', '', 'title', card('Boletín', 'Ejercicios del Tema 3', 'Los 9 ejercicios de regresión, a mano y en Excel'), [
    (3, 'En este vídeo resolvemos los 9 ejercicios del boletín del Tema 3, regresión lineal. Para cada uno: enunciado, resolución a mano, Excel e interpretación. Para el vídeo antes de cada solución e inténtalo tú.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:72px">Qué te pueden dar</h1>',
    Step(1, '**Datos sueltos** → tabla X, Y, XY, X²'), Step(2, '**Sumas** (Σx, Σxy…) → medias, varianzas y covarianza'), Step(3, '**Estadísticos** (x̄, Sₓ, S_XY…) → directo a b y a'), Ojo('Mira si te dan **desviaciones típicas** o **varianzas**.')], [
    (2, 'En regresión te pueden dar la información de tres formas. Con datos sueltos, haces la tabla de trabajo con X, Y, X por Y y X al cuadrado.'),
    (3, 'Con las sumas ya hechas, calculas las medias, las varianzas y la covarianza.'),
    (4, 'O directamente los estadísticos, y entonces vas directo a la pendiente y la ordenada.'),
    (5, 'Y en todos los casos, fíjate bien en si te dan la desviación típica o la varianza. Para la pendiente necesitas la varianza: si te dan la desviación típica, elévala al cuadrado.'),
]))
# Ej1
S.append(Scene(*E(1, 'Publicidad y ventas'), 'mano', [
    Enun('X = publicidad (miles €), Y = ventas (millones de cajas). x̄ = 60, ȳ = 850, Sₓ = 40, Sᵧ = 500, S_XY = 19 200. a) Recta. b) R². c) Ventas con 100 000 € de publicidad.'),
    Step(1, 'S²ₓ = 40² = 1600 → b = 19 200/1600 = **12** · a = 850 − 12·60 = **130** → **Ŷ = 130 + 12X**'),
    Step(2, 'r = 19 200/(40·500) = 0,96 → **R² = 0,9216**'),
    Step(3, '100 000 € = **100** miles → Ŷ = 130 + 12·100 = **1330 millones de cajas**'),
    XL('=B5/B3^2', 'b, con S_XY en B5 y Sₓ en B3'),
    Res('Por cada mil euros más en publicidad, las ventas suben de media **12 millones de cajas**. El **92 %** de la variabilidad de las ventas se explica por la publicidad.'),
], [
    (1, 'Ejercicio 1: publicidad y ventas. Nos dan las medias, las desviaciones típicas y la covarianza.'),
    (2, 'Ojo, nos dan desviaciones típicas: la varianza de X es 40 al cuadrado, 1600. La pendiente, 19 200 entre 1600: 12. La ordenada, 850 menos 12 por 60: 130.'),
    (3, 'El coeficiente de correlación, la covarianza entre el producto de las desviaciones típicas: 0,96. Al cuadrado, R cuadrado igual a 0,9216.'),
    (4, 'Para la predicción, cuidado con las unidades: 100 000 euros son 100 miles. 130 más 12 por 100: 1330 millones de cajas.'),
    (5, 'En Excel, con los datos en celdas: la covarianza entre la desviación típica al cuadrado.'),
    (6, 'La interpretación: por cada mil euros más en publicidad, las ventas suben de media 12 millones de cajas, y el ajuste es muy bueno: el 92 por ciento.'),
]))
# Ej2
S.append(Scene(*E(2, 'Acciones e índice bursátil'), 'mano', [
    Enun('n = 25. ΣY = 22,6; ΣX = 25,4; ΣY² = 172; ΣX² = 145,7; ΣXY = 150,5. a) Recta de Y sobre X. b) R². c) Y si X = 1,5.'),
    Step(1, 'x̄ = 25,4/25 = 1,016 · ȳ = 22,6/25 = 0,904'),
    Step(2, 'S²ₓ = 145,7/25 − 1,016² = **4,7957** · S²ᵧ = 172/25 − 0,904² = **6,0628**'),
    Step(3, 'S_XY = 150,5/25 − 1,016·0,904 = **5,1015**'),
    Step(4, 'b = 5,1015/4,7957 = **1,0638** · a = 0,904 − 1,0638·1,016 = **−0,1768**'),
    Step(5, 'R² = 5,1015²/(4,7957·6,0628) = **0,895** · Ŷ(1,5) = **1,419 %**'),
], [
    (1, 'Ejercicio 2: rendimiento de una acción y de un índice bursátil. Nos dan n y las sumas.'),
    (2, 'Primero las medias: 25,4 entre 25, 1,016; y 22,6 entre 25, 0,904.'),
    (3, 'Las varianzas con la fórmula práctica: la de X, 4,7957; la de Y, 6,0628.'),
    (4, 'La covarianza: la suma de los productos entre n, menos el producto de las medias: 5,1015.'),
    (5, 'La pendiente, 1,0638: cuando el índice sube un punto, la acción sube de media 1,06. La ordenada, menos 0,1768.'),
    (6, 'R cuadrado, la covarianza al cuadrado entre el producto de las varianzas: 0,895, el 89,5 por ciento. Y si el índice rinde un 1,5, esperamos un 1,419 por ciento.'),
]))
# Ej3
S.append(Scene(*E(3, 'Precio por hora y clientes'), 'mano', [
    Enun('Euros/hora: 20,4 · 21,8 · 22 · 23 · 23,6. Clientes: 80 · 64 · 46 · 50 · 51. a) Recta. b) Gráfico. c) % no explicado. d) ¿Cuánto varían los clientes por cada euro más?'),
    T(['X', 'Y', 'X·Y', 'X²', 'Y²'], [['20,4', 80, 1632, '416,16', 6400], ['21,8', 64, '1395,2', '475,24', 4096], ['22,0', 46, 1012, 484, 2116], ['23,0', 50, 1150, 529, 2500], ['23,6', 51, '1203,6', '556,96', 2601], ['**110,8**', '**291**', '**6392,8**', '**2461,36**', '**17 713**']], small=True),
    Step(1, 'x̄ = 22,16 · ȳ = 58,2 · S²ₓ = 1,2064 · S²ᵧ = 155,36 · S_XY = **−11,152**'),
    Step(2, 'b = −11,152/1,2064 = **−9,244** · a = 58,2 + 9,244·22,16 = **263,05**'),
], [
    (1, 'Ejercicio 3: el precio por hora de cinco talleres y su número de clientes.'),
    (2, 'Con datos sueltos, la tabla de trabajo: X, Y, X por Y, X al cuadrado e Y al cuadrado, y las sumas abajo.'),
    (3, 'Medias: 22,16 euros y 58,2 clientes. Varianzas: 1,2064 y 155,36. La covarianza sale negativa: menos 11,152. Relación inversa.'),
    (4, 'La pendiente, menos 11,152 entre 1,2064: menos 9,244. La ordenada, 263,05.'),
]))
S.append(Scene(*E(3, 'Precio por hora y clientes'), 'mano', [
    Img('r3_talleres.svg', 900),
    Step(1, 'c) r = −11,152/√(1,2064·155,36) = −0,815 → R² = 0,664 → **no explicado: 33,6 %**'),
    Step(2, 'd) Por cada euro más por hora: **9,24 clientes menos** de media'),
    XL('=PENDIENTE(B2:B6;A2:A6)', '→ −9,244'),
], [
    (1, 'b) El gráfico: la nube de puntos con la recta. A mano, ejes de 20 a 24 y de 40 a 85. Para la recta, calcula Y gorro en 20, 78,2, y en 24, 41,2, y los unes: baja.'),
    (2, 'c) r es menos 0,815, y R cuadrado, 0,664. Lo que no explica el precio es 1 menos 0,664: el 33,6 por ciento.'),
    (3, 'd) La pendiente: por cada euro más por hora, el taller tiene de media 9,24 clientes menos.'),
    (4, 'En Excel: PENDIENTE, INTERSECCION.EJE y COEFICIENTE.R2, siempre primero las Y y luego las X. Y el gráfico, de dispersión con línea de tendencia.'),
]))
# Ej4
S.append(Scene(*E(4, 'Tasación y precio de viviendas'), 'mano', [
    Enun('12 viviendas. X = tasación, Y = precio (miles €). x̄ = 115, ȳ = 130, Sₓ = 20, Sᵧ = 25, S_XY = 480.'),
    Step(1, 'b = 480/20² = **1,2** · a = 130 − 1,2·115 = **−8** → **Ŷ = −8 + 1,2X**'),
    Step(2, 'r = 480/(20·25) = **0,96** · R² = **0,9216**'),
    Step(3, 'Tasada en 100 000 € → Ŷ = −8 + 1,2·100 = **112 miles de €**'),
    Ojo('a = −8 no tiene sentido práctico: no hay viviendas tasadas en 0 €.'),
], [
    (1, 'Ejercicio 4: tasación y precio de venta de 12 viviendas. Igual que el ejercicio 1.'),
    (2, 'La pendiente, 480 entre 20 al cuadrado: 1,2. Por cada 1000 euros más de tasación, el precio sube de media 1200. La ordenada, 130 menos 1,2 por 115: menos 8.'),
    (3, 'r es 0,96: relación directa muy fuerte. R cuadrado, 0,9216.'),
    (4, 'Una vivienda tasada en 100 000 euros: menos 8 más 1,2 por 100, 112 mil euros.'),
    (5, 'Y un detalle: la ordenada negativa no tiene sentido práctico, porque no hay viviendas tasadas en 0 euros. Solo sirve para dibujar la recta.'),
]))
# Ej5
S.append(Scene(*E(5, 'Vertidos y sanciones'), 'mano', [
    Enun('X (miles de litros): 0,5 · 1 · 1,5 · 2 · 2,5 · 3 · 3,5. Y (miles €): 100 · 300 · 500 · 800 · 1100 · 1500 · 2400. Una industria ha vertido 2200 litros.'),
    Step(1, 'x̄ = 2 · ȳ = 957,14 · S²ₓ = 35/7 − 4 = 1 · S_XY = 18 350/7 − 2·957,14 = **707,14**'),
    Step(2, 'b = **707,14** · a = 957,14 − 707,14·2 = **−457,14**'),
    Step(3, 'r = 707,14/(1·736,51) = **0,960** · R² = 0,922'),
    Step(4, '2200 litros = **2,2** miles → Ŷ = **1098,57 miles de €**'),
    XL('=PRONOSTICO.LINEAL(2,2;B2:B8;A2:A8)', '→ 1098,57'),
], [
    (1, 'Ejercicio 5: litros vertidos y la sanción. Una industria ha vertido unos 2200 litros.'),
    (2, 'Medias: 2 y 957,14. La varianza de X sale 1. La covarianza, 707,14.'),
    (3, 'Como la varianza de X es 1, la pendiente es igual a la covarianza: 707,14. Cada mil litros más se sancionan con unos 707 000 euros más. La ordenada, menos 457,14.'),
    (4, 'r es 0,96: relación directa muy fuerte.'),
    (5, 'Para la predicción, de nuevo las unidades: 2200 litros son 2,2 miles. La sanción esperada, 1098,57 miles de euros, unos 1,1 millones.'),
    (6, 'En Excel, PRONOSTICO.LINEAL con el valor de X, las Y y las X.'),
]))
S.append(Scene(*E(5, 'Vertidos y sanciones'), 'int', [
    Img('r5_vertidos.svg', 950),
    Ojo('Los puntos forman una **curva** que se acelera. La recta funciona (r = 0,96), pero se queda corta en los extremos.'),
], [
    (1, 'd) El gráfico.'),
    (2, 'Un detalle para lucirte: los puntos forman una curva que se acelera, la sanción crece cada vez más deprisa. La recta funciona bien, pero se queda corta en los extremos. Comentarlo demuestra que sabes leer una nube de puntos.'),
]))
# Ej6
S.append(Scene(*E(6, 'Recuperar datos a partir de la recta'), 'mano', [
    Enun('n = 100. Ŷ = 2 − 3X, R² = 0,81, x̄ = 2, Sᵧ = 10. Calcula ȳ, Sₓ y S_XY.'),
    Step(1, 'La recta pasa por las medias: ȳ = 2 − 3·2 = **−4**'),
    Step(2, 'r = √0,81 = 0,9, con el signo de b (−3) → **r = −0,9**'),
    Step(3, 'r = b · Sₓ/Sᵧ → −0,9 = −3 · Sₓ/10 → **Sₓ = 3**'),
    Step(4, 'b = S_XY/S²ₓ → S_XY = −3 · 9 = **−27** · comprobación: −27/(3·10) = −0,9 ✔'),
], [
    (1, 'Ejercicio 6: un ejercicio sin datos. Nos dan la recta, R cuadrado, la media de X y la desviación de Y, y hay que recuperar lo demás.'),
    (2, 'La clave: la recta siempre pasa por el punto de las medias. Sustituimos X por 2: la media de Y es menos 4.'),
    (3, 'r es la raíz de 0,81, 0,9. Pero ¿positivo o negativo? Lleva el signo de la pendiente, que es negativa: r es menos 0,9.'),
    (4, 'Con la fórmula que une r y b: r es b por Sx entre Sy. Despejando, Sx es 3.'),
    (5, 'Y la covarianza: b por la varianza de X, menos 3 por 9, menos 27. Comprobamos: menos 27 entre 3 por 10, menos 0,9. Correcto.'),
]))
# Ej7
S.append(Scene(*E(7, 'Las dos rectas a partir de r'), 'mano', [
    Enun('r = 0,56; x̄ = 12; ȳ = 24; S²ₓ = 3,6; S²ᵧ = 2,5. Rectas de Y sobre X y de X sobre Y.'),
    Step(1, 'Nos dan **varianzas**. S_XY = r · Sₓ · Sᵧ = 0,56 · √(3,6·2,5) = 0,56 · 3 = **1,68**'),
    Step(2, 'Y sobre X: b = 1,68/3,6 = 0,467 · a = 24 − 0,467·12 = 18,4 → **Ŷ = 18,4 + 0,467X**'),
    Step(3, 'X sobre Y: b′ = 1,68/2,5 = 0,672 · a′ = 12 − 0,672·24 = −4,128 → **X̂ = −4,128 + 0,672Y**'),
], [
    (1, 'Ejercicio 7: las dos rectas a partir de r. Aquí nos dan varianzas.'),
    (2, 'La covarianza, de la fórmula de r: r por Sx por Sy. La raíz de 3,6 por 2,5 es la raíz de 9, 3. Así que 0,56 por 3: 1,68.'),
    (3, 'La recta de Y sobre X divide entre la varianza de X: pendiente 0,467 y ordenada 18,4.'),
    (4, 'La de X sobre Y divide entre la varianza de Y, y se cambian los papeles: pendiente 0,672 y ordenada menos 4,128.'),
]))
# Ej8
S.append(Scene(*E(8, 'Emparejar gráficos y rectas'), 'int', [
    P('**a** (número suelto) = dónde corta al eje vertical. **b** (multiplica a X) = sube si es positivo, baja si es negativo; cuanto mayor, más empinada. Comprueba con X = 10.', 's'),
    T(['Gráfico', 'Qué se ve', 'Recta', 'X = 10'], [[1, 'De 0 sube a 20', 'III: Ŷ = 2X', '20 ✔'], [2, 'De 5 sube a 20', 'VI: Ŷ = 5 + 1,5X', '20 ✔'], [3, 'De 5 baja a −35', 'II: Ŷ = 5 − 4X', '−35 ✔'], [4, 'De 5 sube a 45', 'V: Ŷ = 5 + 4X', '45 ✔'], [5, 'Horizontal en 5', 'I: Ŷ = 5', 'sin relación'], [6, 'De 5 baja a −10', 'IV: Ŷ = 5 − 1,5X', '−10 ✔']], small=True),
], [
    (1, 'Ejercicio 8: emparejar seis gráficos con seis rectas. Para leer una recta: el número suelto es donde corta al eje vertical; el que multiplica a X dice si sube o baja y cuánto. Para comprobar, calcula Y gorro en X igual a 10.'),
    (2, 'El gráfico que empieza en 0 solo puede ser Y igual a 2X: en 10 vale 20. Los que empiezan en 5 y suben: el suave es 5 más 1,5X, y el empinado, 5 más 4X. Los que bajan: el suave, 5 menos 1,5X, que llega a menos 10; el empinado, 5 menos 4X, que llega a menos 35. Y la línea horizontal es Y igual a 5: pendiente cero, sin relación lineal.'),
]))
# Ej9
S.append(Scene(*E(9, 'Rectas con la EPF'), 'xl', [
    Enun('Rectas de regresión entre variables de la EPF (51 provincias): qué explicas con qué, ecuación y bondad del ajuste.'),
    T(['Explico (Y)', 'Con (X)', 'Recta', 'R²'], [['Turismo y ocio', 'Educación', 'Ŷ = 2138,84 + 1,275X', '0,714'], ['Turismo y ocio', 'Vivienda', 'Ŷ = 1047,74 + 0,457X', '0,656'], ['Vivienda', 'Alimentación', 'Ŷ = 555,20 + 0,774X', '0,226']], small=True),
    XL('=COEFICIENTE.R2(I2:I52;H2:H52)'),
    Res('Por cada euro más en educación, **1,27 €** más de media en ocio; explica el **71 %**. Vivienda según alimentación: solo el **23 %**, ajuste **débil**.'),
], [
    (1, 'Ejercicio 9: un ejercicio abierto con la Encuesta de Presupuestos Familiares. Tú eliges las variables.'),
    (2, 'Tres propuestas, de más a menos ajuste: turismo y ocio según educación, R cuadrado 0,71; ocio según vivienda, 0,66; y vivienda según alimentación, solo 0,23.'),
    (3, 'En Excel, PENDIENTE, INTERSECCION.EJE, COEF.DE.CORREL y COEFICIENTE.R2 sobre las 51 filas, y la nube de puntos con línea de tendencia.'),
    (4, 'La interpretación: por cada euro más que una provincia gasta en educación y cultura, gasta de media 1,27 euros más en ocio, y eso explica el 71 por ciento de las diferencias. En cambio, la recta de vivienda según alimentación tiene un ajuste débil: no serviría para predecir bien.'),
]))
S.append(Scene('', '', 'title', card('Boletín', 'Fin del boletín del Tema 3', 'Ahora: las **Prácticas 5 y 6** de la guía.'), [
    (3, 'Hasta aquí el boletín del Tema 3. Ahora, en la guía, las prácticas 5 y 6, de regresión.'),
]))
