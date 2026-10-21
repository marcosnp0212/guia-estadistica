import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 't3', 'tab': 'Tema 3', 'color': 't3'}
S = []
DAT = T(['Antigüedad X', 1, 2, 3, 5, 6, 7, 9, 10, 12, 15], [['Salario Y', 1400, 1600, 1700, 1700, 1800, 1850, 2200, 2400, 2250, 2500]], small=True)
S.append(Scene('', '', 'title', card('Tema 3', 'Regresión y correlación', 'Cuando una variable sube, ¿la otra también? ¿Cuánto? ¿Puedo predecirla?'), [
    (3, 'Tema 3: regresión y correlación. Tenemos dos variables numéricas de cada persona, por ejemplo la antigüedad y el salario. Queremos saber si cuando una sube la otra también, cuánto, y si podemos predecir el salario de alguien sabiendo su antigüedad. La herramienta es una recta.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:80px">Qué vamos a ver</h1>', toc([('3.1', 'La nube de puntos'), ('3.2', 'La covarianza'), ('3.3', 'La recta de regresión'), ('3.4', 'r y R²'), ('3.5', 'Predicciones'), ('3.6', 'Ejercicios sin datos')]), DAT], [
    (2, 'Estos son los seis apartados del tema.'),
    (3, 'Y este es el ejemplo de clase que usaremos todo el tema: diez trabajadores, con su antigüedad en años y su salario en euros.'),
]))
# 3.1
S.append(Scene('3.1.', 'La nube de puntos', 'teo', [
    Img('t3_tipos.svg', 1500),
    Li('**Directa:** sube hacia la derecha · **Inversa:** baja · **Sin relación lineal:** sin dirección · **No lineal:** curva'),
    Li('Cuanto más **estrecha y alargada**, más **fuerte** la relación.'),
], [
    (1, 'Apartado 3.1: la nube de puntos. Cada trabajador es un punto: su antigüedad en el eje horizontal y su salario en el vertical. La forma de la nube dice qué relación hay.'),
    (2, 'Si la nube sube hacia la derecha, la relación es directa: cuando una aumenta, la otra tiende a aumentar. Si baja, inversa. Si no tiene dirección, no hay relación lineal. Y si los puntos siguen una curva, la relación no es lineal.'),
    (3, 'Cuanto más estrecha y alargada es la nube, más fuerte es la relación.'),
]))
S.append(Scene('3.1.', 'La nube de puntos', 'mano', [
    Step(1, 'Eje X con escala (0 a 16) y eje Y (de 1300 a 2600: no hace falta empezar en 0).'),
    Step(2, 'Un **punto** por pareja: (1, 1400), (2, 1600)…'),
    Step(3, 'Mira la forma: sube → **directa**.'),
    Step(4, 'Para dibujar la recta: calcula **dos puntos** con la ecuación y únelos. Pasa por **(x̄, ȳ)**.'),
    XL('Insertar → Dispersión → Agregar línea de tendencia → Lineal', ''),
    Res('Excel escribe **y = 78,533x + 1390,3** y **R² = 0,9159**: la mejor forma de **comprobar** tus cálculos.'),
], [
    (1, 'En papel: dibuja los ejes con su escala. El vertical no tiene que empezar en 0: para los salarios, de 1300 a 2600 está bien.'),
    (2, 'Pon un punto por cada pareja: antigüedad 1 y salario 1400, antigüedad 2 y salario 1600, y así.'),
    (3, 'Mira la forma: aquí sube hacia la derecha, relación directa.'),
    (4, 'Si te piden dibujar la recta, calcula dos puntos con su ecuación, por ejemplo en X igual a 0 y en X igual a 15, y únelos con la regla. Tiene que pasar por el punto de las medias.'),
    (5, 'En Excel: selecciona las dos columnas, Insertar, Dispersión. Después, clic derecho sobre un punto, Agregar línea de tendencia, Lineal, y marca presentar la ecuación y el R cuadrado.'),
    (6, 'Excel te escribe la recta y el R cuadrado encima del gráfico. Es la mejor forma de comprobar tus cálculos a mano.'),
]))
# 3.2
S.append(Scene('3.2.', 'La covarianza', 'teo', [
    F('S_XY = ' + frac('Σxᵢyᵢ', 'n') + ' − x̄ · ȳ'),
    T(['Signo', 'Relación'], [['S_XY > 0', '**Directa**'], ['S_XY < 0', '**Inversa**'], ['S_XY = 0', 'Sin relación **lineal**']], small=True),
    Ojo('El **valor** de la covarianza no dice si la relación es fuerte: depende de las unidades. **Solo se mira el signo.**'),
    Truco('Cruz en las medias: los puntos de **arriba a la derecha** y **abajo a la izquierda** suman a favor de una relación directa.'),
], [
    (1, 'Apartado 3.2: la covarianza. Es un número que dice si las dos variables se mueven en el mismo sentido o en sentido contrario. La fórmula práctica: la suma de los productos equis por y, entre n, menos el producto de las medias.'),
    (2, 'Si es positiva, la relación es directa. Si es negativa, inversa. Si es 0, no hay relación lineal.'),
    (3, 'Ojo: el valor de la covarianza no dice si la relación es fuerte o débil, porque depende de las unidades. No es lo mismo medir en euros que en céntimos. Solo se mira el signo. Para la fuerza está el coeficiente de correlación.'),
    (4, 'Para entender por qué funciona: dibuja una cruz en la nube justo en las medias. Los puntos de arriba a la derecha y de abajo a la izquierda suman a favor de una relación directa. Los otros dos cuadrantes, en contra.'),
]))
S.append(Scene('3.2.', 'La tabla que lo resuelve todo', 'mano', [
    T(['xᵢ', 'yᵢ', 'xᵢ²', 'yᵢ²', 'xᵢ·yᵢ'], [[1, 1400, 1, '1 960 000', '1 400'], [2, 1600, 4, '2 560 000', '3 200'], [3, 1700, 9, '2 890 000', '5 100'], ['…', '…', '…', '…', '…'], [15, 2500, 225, '6 250 000', '37 500'], ['**70**', '**19 400**', '**674**', '**38 875 000**', '**150 250**']], small=True),
    Step(1, 'x̄ = 70 ÷ 10 = **7** · ȳ = 19 400 ÷ 10 = **1940**'),
    Step(2, 'S²ₓ = 674 ÷ 10 − 7² = **18,4**'),
    Step(3, 'S²ᵧ = 38 875 000 ÷ 10 − 1940² = **123 900**'),
    Step(4, 'S_XY = 150 250 ÷ 10 − 7 · 1940 = 15 025 − 13 580 = **1445** → directa'),
], [
    (1, 'A mano, en papel, haz una sola tabla con cinco columnas: equis, y, equis al cuadrado, y al cuadrado, y equis por y. Súmalas. Con esas cinco sumas sacas todo el tema sin volver a tocar los datos.'),
    (2, 'Las medias: 70 entre 10, 7 años; 19400 entre 10, 1940 euros.'),
    (3, 'La varianza de X: 674 entre 10, menos 7 al cuadrado: 18,4.'),
    (4, 'La varianza de Y: 38 875 000 entre 10, menos 1940 al cuadrado: 123 900.'),
    (5, 'Y la covarianza: 150 250 entre 10, menos 7 por 1940. 15 025 menos 13 580: 1445. Positiva: relación directa.'),
]))
S.append(Scene('3.2.', 'La covarianza', 'xl', [
    XL('=COVARIANZA.P(A2:A11;B2:B11)', '→ 1445'),
    Ojo('**COVARIANZA.P** divide entre n, como en clase. COVARIANZA.M divide entre n − 1.'),
], [
    (1, 'En Excel: COVARIANZA.P con las dos columnas. Da 1445.'),
    (2, 'Usa la punto P, que divide entre n, como en clase. La punto M divide entre n menos 1; no la uses salvo que te lo pidan.'),
]))
# 3.3
S.append(Scene('3.3.', 'La recta de regresión', 'teo', [
    F('Ŷ = a + b·X'),
    F('b = ' + frac('S_XY', 'S²ₓ') + '&nbsp;&nbsp;&nbsp;&nbsp;a = ȳ − b·x̄'),
    Li('**b, la pendiente:** cuánto cambia Y, de media, cuando X sube **1 unidad**. Mismo signo que la covarianza.'),
    Li('**a:** el valor de Y cuando X = 0. A veces no tiene sentido práctico.'),
    Li('**Ŷ** con sombrero: es una **predicción**, no un dato real.'),
], [
    (1, 'Apartado 3.3: la recta de regresión. Es la recta que mejor se ajusta a la nube. La de Y sobre X sirve para predecir Y sabiendo X: Y estimada es igual a a más b por X.'),
    (2, 'La pendiente b es la covarianza entre la varianza de X. Y a es la media de Y menos b por la media de X.'),
    (3, 'La pendiente es lo más importante: dice cuánto cambia Y, de media, cuando X aumenta una unidad. Tiene el mismo signo que la covarianza.'),
    (4, 'El término a es el valor de Y cuando X vale 0. A veces no tiene sentido práctico, por ejemplo si nadie tiene X igual a 0.'),
    (5, 'Y el sombrero sobre la Y indica que es una predicción, un valor medio estimado, no un dato real.'),
]))
S.append(Scene('3.3.', 'La recta de regresión', 'mano', [
    Step(1, 'b = 1445 ÷ 18,4 = **78,53**'),
    Step(2, 'a = 1940 − 78,53 · 7 = **1390,27**'),
    Res('Salario estimado = **1390,27 + 78,53 · Antigüedad**'),
    Res('**b:** por cada año más de antigüedad, el salario aumenta de media **78,53 €**. **a:** alguien recién llegado cobraría unos 1390 €.'),
    P('**Recta de X sobre Y** (para predecir X): b′ = S_XY ÷ **S²ᵧ** · a′ = x̄ − b′·ȳ. Las dos rectas pasan por **(x̄, ȳ)**.', 's'),
], [
    (1, 'Con nuestras sumas: b es 1445 entre 18,4, 78,53.'),
    (2, 'Y a es 1940 menos 78,53 por 7: 1390,27.'),
    (3, 'La recta: salario estimado igual a 1390,27 más 78,53 por la antigüedad.'),
    (4, 'Y la interpretación, que es lo que más puntúa: por cada año más de antigüedad, el salario aumenta de media 78,53 euros. Y un trabajador recién llegado, con 0 años, cobraría unos 1390.'),
    (5, 'Si te piden la recta de X sobre Y, para predecir X a partir de Y, se divide entre la varianza de Y en vez de la de X, y a prima es la media de X menos b prima por la media de Y. Las dos rectas son distintas, pero las dos pasan por el punto de las medias.'),
]))
S.append(Scene('3.3.', 'La recta de regresión', 'xl', [
    XL('=PENDIENTE(B2:B11;A2:A11)', '→ 78,53'),
    XL('=INTERSECCION.EJE(B2:B11;A2:A11)', '→ 1390,27'),
    Ojo('**Primero la Y, después la X.** Al revés obtienes la recta de X sobre Y.'),
], [
    (1, 'En Excel, la pendiente con PENDIENTE.'),
    (2, 'Y el término independiente con INTERSECCION.EJE.'),
    (3, 'Muy importante: primero va la Y y después la X. Si las pones al revés, te da la recta de X sobre Y.'),
]))
# 3.4
S.append(Scene('3.4.', 'r y R²', 'teo', [
    F('r = ' + frac('S_XY', 'Sₓ · Sᵧ') + '&nbsp;&nbsp;&nbsp;&nbsp;R² = r²'),
    T(['r', 'Significa'], [['1', 'Relación lineal perfecta y directa'], ['cerca de 1', 'Directa fuerte'], ['cerca de 0', 'Débil o nula'], ['cerca de −1', 'Inversa fuerte']], small=True),
    Li('**r** entre −1 y 1, mismo signo que b. **R²** entre 0 y 1: **qué % de Y explica la recta**.'),
    Step(1, 'r = 1445 ÷ (√18,4 · √123 900) = 1445 ÷ (4,290 · 352,0) = **0,957**'),
    Res('**R² = 0,916** → el **91,6 %** de la variabilidad del salario se explica por la antigüedad. El 8,4 % depende de otras cosas.'),
    Ojo('**Correlación no es causalidad.** Di «están relacionadas», no «una causa la otra».'),
], [
    (1, 'Apartado 3.4. El coeficiente de correlación r mide la fuerza y el sentido de la relación lineal: la covarianza entre el producto de las dos desviaciones típicas. Y el coeficiente de determinación, R cuadrado, es r al cuadrado.'),
    (2, 'r está siempre entre menos 1 y 1. Cerca de 1, relación directa fuerte. Cerca de 0, débil o nula. Cerca de menos 1, inversa fuerte.'),
    (3, 'r tiene el mismo signo que la pendiente. Y R cuadrado, entre 0 y 1, dice qué parte de la variabilidad de Y queda explicada por la recta.'),
    (4, 'Con nuestros datos: 1445 entre la raíz de 18,4 por la raíz de 123 900. 1445 entre 4,29 por 352: 0,957. Relación directa muy fuerte.'),
    (5, 'R cuadrado es 0,916: el 91,6 por ciento de la variabilidad del salario se explica por la antigüedad. El 8,4 por ciento restante depende de otros factores.'),
    (6, 'Y un aviso: que dos variables estén muy correlacionadas no demuestra que una provoque la otra. Puede haber una tercera detrás. Basta con decir que están relacionadas. En Excel: COEF.DE.CORREL y COEFICIENTE.R2.'),
]))
# 3.5
S.append(Scene('3.5.', 'Predicciones', 'teo', [
    P('Se **sustituye X** en la recta. Salario con **11 años**:', 's'),
    F('Ŷ = 1390,27 + 78,53 · 11 = **2254,13 €**'),
    Li('Es **fiable** porque R² = 0,916 es alto.'),
    Ojo('Solo es fiable **dentro del rango** de los datos (de 1 a 15 años). Con 40 años, arriesgado.'),
    XL('=PRONOSTICO.LINEAL(11;B2:B11;A2:A11)', 'el valor de X, los Y, los X'),
], [
    (1, 'Apartado 3.5: las predicciones. Si el ajuste es bueno, se usa la recta para predecir: se sustituye X por el valor que te den. Por ejemplo, el salario de una trabajadora con 11 años.'),
    (2, '1390,27 más 78,53 por 11: 2254,13 euros.'),
    (3, 'Es una predicción fiable porque R cuadrado es alto.'),
    (4, 'Pero cuidado: solo es fiable predecir dentro del rango de los datos, aquí de 1 a 15 años. Predecir para 40 años de antigüedad sería arriesgado: no sabemos si la relación sigue siendo una recta.'),
    (5, 'En Excel: PRONOSTICO.LINEAL, con el valor de X, luego las Y y luego las X.'),
]))
# 3.6
S.append(Scene('3.6.', 'Ejercicios sin datos', 'teo', [
    Li('b = S_XY ÷ S²ₓ → **S_XY = b · S²ₓ**'),
    Li('r = S_XY ÷ (Sₓ·Sᵧ) → **S_XY = r · Sₓ · Sᵧ**'),
    Li('**r = b · Sₓ ÷ Sᵧ**'),
    Li('R² = r² → **r = ±√R²** con el signo de b'),
    Li('La recta pasa por las medias → **ȳ = a + b·x̄**'),
    Ojo('¿Te dan **S** (desviación) o **S²** (varianza)? Si Sₓ = 40, entonces S²ₓ = **1600**.'),
], [
    (1, 'Apartado 3.6: los ejercicios sin datos. Muchos ejercicios no dan los datos, sino algunos resultados, y hay que despejar lo que falta. Estas relaciones lo permiten. De la pendiente: la covarianza es b por la varianza de X.'),
    (2, 'De r: la covarianza es r por las dos desviaciones típicas.'),
    (3, 'Combinando las dos: r es b por la desviación de X entre la de Y.'),
    (4, 'Si te dan R cuadrado, r es su raíz, con el signo de la pendiente.'),
    (5, 'Y como la recta pasa por las medias, la media de Y es a más b por la media de X.'),
    (6, 'El error más común: confundir la desviación típica con la varianza. Lee con cuidado qué te dan. Si la desviación de X es 40, la varianza es 1600.'),
]))
S.append(Scene('3.6.', 'Ejercicios sin datos', 'mano', [
    P('**Ejemplo:** Ŷ = 2 − 3X, R² = 0,81, x̄ = 2, Sᵧ = 10. Calcula ȳ, Sₓ y S_XY.', 's'),
    Step(1, 'ȳ = 2 − 3 · 2 = **−4** (la recta pasa por las medias)'),
    Step(2, 'r = −√0,81 = **−0,9** (negativa, como b)'),
    Step(3, 'Sₓ: −0,9 = −3 · Sₓ ÷ 10 → Sₓ = **3**'),
    Step(4, 'S_XY = b · S²ₓ = −3 · 9 = **−27**. Comprobación: −27 ÷ (3 · 10) = −0,9 ✔'),
], [
    (1, 'Un ejemplo del boletín: la recta es Y igual a 2 menos 3X, R cuadrado 0,81, la media de X es 2 y la desviación de Y es 10.'),
    (2, 'La media de Y: sustituyes la media de X en la recta. 2 menos 3 por 2: menos 4.'),
    (3, 'r es la raíz de 0,81, 0,9, pero negativa, porque la pendiente es negativa.'),
    (4, 'La desviación de X: r es b por Sx entre Sy. Menos 0,9 igual a menos 3 por Sx entre 10. Despejando, Sx es 3.'),
    (5, 'Y la covarianza: b por la varianza de X, menos 3 por 9, menos 27. Y compruebas: menos 27 entre 3 por 10 da menos 0,9. Correcto.'),
]))
S.append(Scene('', '', 'title', card('Tema 3', 'Fin del Tema 3', 'Ahora: el boletín del Tema 3 y las **Prácticas 5 y 6**.'), [
    (3, 'Y hasta aquí el Tema 3. En la guía tienes el boletín del tema y las prácticas 5 y 6. Haz la tabla de cinco columnas en papel, y comprueba con Excel.'),
]))

def _find(title, kind):
    for i, s in enumerate(S):
        if s.title == title and s.kind == kind: return i
    raise KeyError(title)
S.insert(_find('La covarianza', 'xl') + 1, Scene('3.2.', 'Covarianza con tabla de frecuencias', 'mano', [
    F('S_XY = ' + frac('Σxᵢ·yⱼ·nᵢⱼ', 'n') + ' − x̄ · ȳ'),
    T(['X \\ Y', '2', '3', '5', 'Total'], [[1, 1, 3, 2, 6], [2, 4, 1, 5, 10], [3, 3, 3, 2, 8], [4, 1, 4, 3, 8], ['Total', 9, 11, 12, 32]], small=True),
    Step(1, 'Cada casilla: **x · y · nᵢⱼ**. Fila X = 1: 1·(2·1 + 3·3 + 5·2) = **21**. Luego 72, 75 y 116.'),
    Step(2, 'Σxᵢyⱼnᵢⱼ = 21 + 72 + 75 + 116 = **284**'),
    Step(3, 'x̄ = 82 ÷ 32 = 2,5625 · ȳ = (2·9 + 3·11 + 5·12) ÷ 32 = 111 ÷ 32 = 3,46875'),
    Step(4, 'S_XY = 284 ÷ 32 − 2,5625 · 3,46875 = 8,875 − 8,889 = **−0,014**'),
    Res('Negativa pero **casi 0**: prácticamente **no hay relación lineal**.'),
], [
    (1, 'Si los datos vienen en una tabla de doble entrada, cada pareja aparece n sub i j veces, así que en la suma también se multiplica por la frecuencia de la casilla.'),
    (2, 'El ejemplo de los apuntes, la tabla de días de ausencia y asuntos propios del Tema 2.'),
    (3, 'Para cada casilla, multiplica el valor de X, el de Y y la frecuencia. Por filas es más cómodo: en la fila de X igual a 1, 1 por, 2 por 1, más 3 por 3, más 5 por 2: 21. Las otras filas dan 72, 75 y 116.'),
    (4, 'La suma total es 284.'),
    (5, 'Las medias, con las marginales: la de X es 82 entre 32, 2,5625; la de Y, 111 entre 32, 3,46875.'),
    (6, 'Y la covarianza: 284 entre 32, 8,875, menos el producto de las medias, 8,889. Da menos 0,014.'),
    (7, 'Es negativa pero casi 0: prácticamente no hay relación lineal entre faltar más días y coger más días de asuntos propios.'),
]))
