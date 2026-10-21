import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 't4', 'tab': 'Tema 4', 'color': 't4'}
S = []
S.append(Scene('', '', 'title', card('Tema 4', 'Números índices', 'Cuánto ha cambiado algo respecto a un año de referencia'), [
    (3, 'Tema 4: los números índices. Un índice dice cuánto ha cambiado algo respecto a un momento de referencia, el año base, al que se le da el valor 100. Todo el tema es jugar con divisiones y multiplicaciones por porcentajes. Nada más.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:80px">Qué vamos a ver</h1>', toc([('4.1', 'Índice simple'), ('4.2', 'Tasa de variación'), ('4.3', 'Propiedades'), ('4.4', 'Cambio de base'), ('4.5', 'Media geométrica y tasas medias'), ('4.6', 'Laspeyres, Paasche y Fisher'), ('4.7', 'Deflactar'), ('4.8', 'El IPC y el IBEX 35')])], [
    (2, 'Estos son los ocho apartados. Es el tema con menos fórmulas nuevas y el que mejor se hace a mano.'),
]))
S.append(Scene('4.1.', 'Índice simple', 'teo', [
    F('I = ' + frac('xₜ', 'x₀') + ' · 100'),
    Li('**Índice − 100 = % de cambio.** 120 → sube un 20 %. 97,44 → baja un 2,56 %. El año base vale **100**.'),
    Step(1, 'Salario 1500 € (2015) y 1600 € (2018): 1600 ÷ 1500 × 100 = **106,67** → subió un **6,67 %**.'),
    Truco('Sin el «× 100»: subir un 20 % es **× 1,20**. Así, encadenar es multiplicar.'),
    XL('=B2/$B$2*100', 'y arrastras; $B$2 es el año base'),
], [
    (1, 'Apartado 4.1: el índice simple. El valor del año que estudias, dividido entre el del año base, por 100.'),
    (2, 'Se interpreta así: el índice menos 100 es el porcentaje de cambio. Un índice de 120 significa que ha subido un 20 por ciento. Uno de 97,44, que ha bajado un 2,56 por ciento. Y el año base siempre vale 100.'),
    (3, 'Ejemplo de los apuntes: un salario de 1500 euros en 2015 y de 1600 en 2018. 1600 entre 1500, por 100: 106,67. El salario subió un 6,67 por ciento.'),
    (4, 'Un truco: muchas veces es más cómodo trabajar sin el por 100. Subir un 20 por ciento es multiplicar por 1,20. Así, encadenar subidas es multiplicar.'),
    (5, 'En Excel: cada valor entre el del año base, fijado con dólares, por 100, y arrastras.'),
]))
S.append(Scene('4.2.', 'Tasa de variación', 'teo', [
    F('Tasa = ' + frac('V₁ − V₀', 'V₀') + ' = ' + frac('V₁', 'V₀') + ' − 1'),
    Step(1, 'Cuentas: 1000 → 1100: 1100 ÷ 1000 − 1 = **+10 %**'),
    Step(2, 'Precio: 11,42 → 8,41: 8,41 ÷ 11,42 − 1 = **−26,35 %**'),
    XL('=B3/B2-1', 'con formato %'),
], [
    (1, 'Apartado 4.2: la tasa de variación. El valor nuevo menos el antiguo, entre el antiguo. O, más cómodo: el nuevo entre el antiguo, menos 1. Positiva es crecimiento; negativa, disminución.'),
    (2, 'Unas cuentas que pasan de 1000 a 1100: 1100 entre 1000 es 1,1; menos 1, 0,1: un 10 por ciento más.'),
    (3, 'Un precio que baja de 11,42 a 8,41: 8,41 entre 11,42, menos 1: menos 26,35 por ciento.'),
    (4, 'En Excel: el nuevo entre el anterior, menos 1, con formato de porcentaje.'),
]))
S.append(Scene('4.3.', 'Propiedades', 'teo', [
    F('Inversión: I(t→0) = ' + frac('1', 'I(0→t)')),
    F('Encadenar: I(0→t′) = I(0→t) · I(t→t′)'),
    Step(1, '+5 %, +8 % y +10 % → 1,05 × 1,08 × 1,10 = **1,2474** → **+24,74 %** en total'),
    Ojo('Los porcentajes **no se suman**: no es un 23 %. Y +10 % y luego −10 %: 1,10 × 0,90 = **0,99** → pierdes un 1 %.'),
], [
    (1, 'Apartado 4.3: dos propiedades. La inversión: el índice al revés es el inverso. Si de 2015 a 2019 sube a 1,10, de 2019 a 2015 es 1 entre 1,10, 0,909.'),
    (2, 'Y el encadenamiento: para ir de un año a otro pasando por uno intermedio, se multiplican los índices.'),
    (3, 'Ejemplo: una empresa crece un 5, luego un 8 y luego un 10 por ciento. 1,05 por 1,08 por 1,10: 1,2474. Ha crecido un 24,74 por ciento en los tres años.'),
    (4, 'Cuidado: los porcentajes no se suman. No es un 23 por ciento. Y si algo sube un 10 y luego baja un 10, no te quedas igual: 1,10 por 0,90 es 0,99, has perdido un 1 por ciento. Cada subida se aplica sobre lo que ya tienes.'),
]))
S.append(Scene('4.4.', 'Cambio de base', 'teo', [
    F('I nueva = ' + frac('I vieja', 'I vieja del nuevo año base') + ' · 100'),
    T(['Año', 'Base 2015', 'Base 2019'], [[2015, 100, '100 ÷ 110 × 100 = 90,91'], [2016, 102, '92,73'], [2019, 110, '**100**'], [2025, 130, '118,18']], small=True),
    XL('=C2/$C$6*100', '$C$6 = el índice del nuevo año base'),
], [
    (1, 'Apartado 4.4: el cambio de base. Para pasar una serie de índices a otro año base, se divide toda la serie entre el índice del nuevo año base, y se multiplica por 100.'),
    (2, 'Ejemplo de los apuntes: pasar unos salarios de base 2015 a base 2019. El índice de 2019 en base 2015 es 110, así que dividimos todos entre 110. 2015 queda en 90,91, 2019 pasa a valer 100, y 2025, 118,18.'),
    (3, 'En Excel: cada índice entre el del nuevo año base, fijado con dólares, por 100.'),
]))
S.append(Scene('4.5.', 'Media geométrica y tasas medias', 'teo', [
    F('M<sub>g</sub> = (x₁ · x₂ ··· xₙ)<sup>1/n</sup>'),
    Step(1, '+5 %, +8 %, +10 % → (1,2474)<sup>1/3</sup>'.replace('<sup>', '^(').replace('</sup>', ')') + ' = **1,0765** → **7,65 % anual**'),
    Step(2, '+10 % y −10 % → √(1,10 × 0,90) = √0,99 = **0,995** → pierde un **0,5 % anual**'),
    F('Tasa media = (1 + T)<sup>1/k</sup> − 1'),
    Step(3, '6 % anual → mensual: 1,06^(1/12) − 1 = **0,487 %**'),
], [
    (1, 'Apartado 4.5: la media geométrica. Cuando los datos son crecimientos que se multiplican, la media correcta no es la normal, sino la geométrica: se multiplican los n valores y se hace la raíz n-ésima, es decir, se eleva a 1 entre n.'),
    (2, 'Con los crecimientos del 5, 8 y 10 por ciento: 1,2474 elevado a un tercio, 1,0765. El crecimiento medio es del 7,65 por ciento anual. Si lo compruebas, 1,0765 al cubo da 1,2474.'),
    (3, 'Y si algo sube un 10 y baja un 10: la raíz de 0,99, 0,995. De media pierde un 0,5 por ciento al año. La media normal diría 0, y es falso.'),
    (4, 'En general, si en k periodos la tasa total ha sido T, la tasa media por periodo es 1 más T, elevado a 1 entre k, menos 1.'),
    (5, 'Por ejemplo, un 6 por ciento anual en mensual: 1,06 elevado a un doceavo, menos 1: 0,487 por ciento al mes.'),
]))
S.append(Scene('4.5.', 'Tasas medias con la calculadora', 'mano', [
    Step(1, 'Pasa cada % a multiplicador: +5 % → 1,05 · −3 % → 0,97'),
    Step(2, 'Multiplícalos: el crecimiento total.'),
    Step(3, 'Eleva a **(1 ÷ nº de periodos)**: `1,2474 ^ ( 1 ÷ 3 )` — con el **paréntesis**.'),
    Step(4, 'Resta 1 y pasa a %: 1,0765 − 1 = **7,65 %**.'),
    Step(5, '**Comprueba** elevando: 1,0765³ ≈ 1,2474 ✔'),
    XL('=1,06^(1/12)-1', 'o =MEDIA.GEOM(A1:A3)'),
    Ojo('Sin el paréntesis, 1,06^1/12 hace 1,06 ÷ 12. **El paréntesis es obligatorio**, en Excel y en la calculadora.'),
], [
    (1, 'Con la calculadora: primero pasa cada porcentaje a multiplicador. Más 5 por ciento es 1,05; menos 3 por ciento, 0,97.'),
    (2, 'Multiplícalos todos: ese es el crecimiento total.'),
    (3, 'Para la media, eleva a 1 entre el número de periodos. En la calculadora, la tecla de potencia y el exponente entre paréntesis. O la tecla de raíz n-ésima, si la tiene.'),
    (4, 'Resta 1 y pásalo a porcentaje.'),
    (5, 'Y comprueba elevando el resultado al número de periodos: tiene que darte el total.'),
    (6, 'En Excel es igual: 1,06 elevado a, entre paréntesis, 1 entre 12, menos 1. O MEDIA.GEOM, si tienes los multiplicadores en celdas.'),
    (7, 'Y el paréntesis es obligatorio. Sin él, Excel y la calculadora harían 1,06 entre 12.'),
]))
S.append(Scene('4.6.', 'Laspeyres, Paasche y Fisher', 'teo', [
    F('L = ' + frac('Σpₜ·q₀', 'Σp₀·q₀') + ' · 100&nbsp;&nbsp;&nbsp;&nbsp;P = ' + frac('Σpₜ·qₜ', 'Σp₀·qₜ') + ' · 100'),
    Li('**Laspeyres:** la cesta **de entonces** pagada hoy. Es el del **IPC**.'),
    Li('**Paasche:** la cesta **de hoy** pagada entonces.'),
    F('Fisher = √(L · P)'),
    Truco('Arriba precios de **hoy**, abajo de **antes**. La **cantidad es la misma** arriba y abajo: **L**aspeyres, la cesta del inicio; **P**aasche, la de ahora.'),
], [
    (1, 'Apartado 4.6: los índices de varios productos, una cesta de la compra. El de Laspeyres de precios: arriba, los precios de hoy por las cantidades del año base; abajo, los precios del año base por esas mismas cantidades. El de Paasche usa las cantidades de hoy.'),
    (2, 'Laspeyres responde a: lo que costaría hoy la cesta de entonces, comparado con lo que costaba entonces. Es el que se usa para el IPC.'),
    (3, 'Paasche: lo que cuesta hoy la cesta de hoy, comparado con lo que habría costado entonces.'),
    (4, 'Y el de Fisher es la media geométrica de los dos: la raíz de Laspeyres por Paasche.'),
    (5, 'Para no confundirlos: arriba siempre van los precios de hoy y abajo los de antes. Lo único que cambia es la cantidad, que es la misma arriba y abajo. Laspeyres usa la cesta del inicio; Paasche, la de ahora.'),
]))
S.append(Scene('4.6.', 'Laspeyres, Paasche y Fisher', 'mano', [
    T(['', 'pₜ·q₀', 'p₀·q₀', 'pₜ·qₜ', 'p₀·qₜ'], [['Pan', '1,20·100 = 120', '1·100 = 100', '1,20·110 = 132', '1·110 = 110'], ['Leche', '1,10·200 = 220', '0,90·200 = 180', '1,10·190 = 209', '0,90·190 = 171'], ['**Suma**', '**340**', '**280**', '**341**', '**281**']], small=True),
    Step(1, 'Laspeyres = 340 ÷ 280 × 100 = **121,43** → precios +21,43 %'),
    Step(2, 'Paasche = 341 ÷ 281 × 100 = **121,35**'),
    Step(3, 'Fisher = √(121,43 × 121,35) = **121,39**'),
    XL('=SUMAPRODUCTO(D2:D6;C2:C6)/SUMAPRODUCTO(B2:B6;C2:C6)*100', 'Laspeyres'),
], [
    (1, 'A mano: cuatro columnas de productos y sus sumas. Ejemplo de los apuntes con pan y leche. Precio de hoy por cantidad de antes, precio de antes por cantidad de antes, precio de hoy por cantidad de hoy, y precio de antes por cantidad de hoy.'),
    (2, 'Laspeyres es la columna 1 entre la 2: 340 entre 280, por 100, 121,43. Los precios subieron un 21,43 por ciento.'),
    (3, 'Paasche, la columna 3 entre la 4: 341 entre 281, 121,35.'),
    (4, 'Y Fisher, la raíz del producto: 121,39.'),
    (5, 'En Excel, con SUMAPRODUCTO arriba y abajo, multiplicado por 100.'),
]))
S.append(Scene('4.7.', 'Deflactar', 'teo', [
    F('Valor real = ' + frac('Valor nominal', 'IPC') + ' · 100'),
    Li('**Nominal:** los euros tal cual. **Real:** con el poder de compra del año base.'),
    Step(1, '25 000 € en 2025, IPC 110 (base 2020) → 25 000 ÷ 110 × 100 = **22 727,27 €** de 2020'),
    Step(2, 'Antes ganaba 20 000 € → poder adquisitivo: 22 727 ÷ 20 000 − 1 = **+13,6 %**, no +25 %'),
    Img('t4_nominal_real.svg', 900),
], [
    (1, 'Apartado 4.7: deflactar. Es quitar el efecto de la inflación. El valor real es el valor nominal entre el IPC, por 100.'),
    (2, 'El valor nominal son los euros tal cual. El real, los euros expresados con el poder de compra del año base.'),
    (3, 'Ejemplo: alguien gana 25 000 euros en 2025, y el IPC de 2025 con base 2020 es 110. 25 000 entre 110, por 100: 22 727 euros de 2020.'),
    (4, 'Si en 2020 ganaba 20 000, su poder adquisitivo ha subido, pero no un 25 por ciento, sino un 13,6.'),
    (5, 'En el gráfico de los apuntes: en euros corrientes el salario sube un 30 por ciento en diez años, pero en términos reales solo un 9,24. La distancia entre las dos líneas es lo que se ha comido la inflación.'),
]))
S.append(Scene('4.7.', 'Deflactar', 'mano', [
    Step(1, '**Salario real** = salario ÷ IPC × 100 → 2025: 1950 ÷ 119 × 100 = **1638,66**'),
    Step(2, '**Índice nominal** = salario ÷ salario base × 100 → 1950 ÷ 1500 × 100 = **130**'),
    Step(3, '**Índice real** = índice nominal ÷ IPC × 100 → 130 ÷ 119 × 100 = **109,24**'),
    XL('=B2/C2*100', 'salario real'),
    Res('En términos **reales**, el poder adquisitivo solo ha subido un **9,24 %**.'),
], [
    (1, 'A mano, para cada año, tres cuentas. El salario real: el salario entre el IPC, por 100. En 2025: 1950 entre 119, por 100, 1638,66 euros.'),
    (2, 'El índice nominal: el salario entre el del año base, por 100. 1950 entre 1500: 130.'),
    (3, 'Y el índice real, con un atajo: el índice nominal entre el IPC, por 100. 130 entre 119: 109,24.'),
    (4, 'En Excel, el salario entre el IPC por 100, y arrastras.'),
    (5, 'Interpretación: en términos reales, el poder adquisitivo solo ha aumentado un 9,24 por ciento.'),
]))
S.append(Scene('4.8.', 'El IPC y el IBEX 35', 'teo', [
    Li('**IPC:** lo elabora el **INE**. Mide los precios de lo que compran los hogares. Tipo **Laspeyres encadenado**. Base 2021.'),
    Li('Sirve para actualizar alquileres, salarios, pensiones…'),
    Step(1, 'IPC +6,5 %, +5,7 %, +3,5 %, +2,8 % → 1,065 × 1,057 × 1,035 × 1,028 = **1,1977** → **+19,8 %**, no 18,5 %'),
    Li('**IBEX 35:** las 35 empresas más negociadas de la Bolsa española. Tipo Laspeyres, **base 1000**.'),
    Step(2, '29 800 000 ÷ 28 000 000 × 1000 = **1064,3 puntos** → +6,43 %'),
], [
    (1, 'Último apartado, el 4.8: dos aplicaciones. El IPC, el índice de precios de consumo, lo elabora el INE y mide la evolución de los precios de lo que compran los hogares. Es un índice tipo Laspeyres encadenado, y desde 2022 se publica en base 2021.'),
    (2, 'Se usa para actualizar alquileres, salarios y pensiones.'),
    (3, 'Una práctica rápida: con un IPC del 6,5, el 5,7, el 3,5 y el 2,8 por ciento en cuatro años, la subida acumulada es el producto, 1,1977: un 19,8 por ciento, no el 18,5 que saldría sumando.'),
    (4, 'Y el IBEX 35 es el índice de la Bolsa española: las 35 empresas más negociadas, ponderadas por lo que valen. Es tipo Laspeyres, con base 1000.'),
    (5, 'En el ejemplo de los apuntes: el valor actual entre el de la base, por 1000. 1064,3 puntos: las acciones han subido de media un 6,43 por ciento.'),
]))
S.append(Scene('', '', 'title', card('Tema 4', 'Fin del Tema 4', 'Ahora: el boletín del Tema 4, las **Prácticas 7 y 8** y los **simulacros**.'), [
    (3, 'Y con esto termina el temario. En la guía tienes el boletín del Tema 4, las prácticas 7 y 8, las 30 preguntas de Excel sin ordenador y los simulacros: el tercero, en papel. Mucho ánimo.'),
]))

def _find(title, kind):
    for i, s in enumerate(S):
        if s.title == title and s.kind == kind: return i
    raise KeyError(title)
S.insert(_find('Laspeyres, Paasche y Fisher', 'mano') + 1, Scene('4.6.', 'Sauerbeck e índices de cantidades', 'teo', [
    Li('**Sauerbeck:** la **media aritmética** de los índices simples, sin ponderar. Pan 1,20/1,00 → 120 · Leche 1,10/0,90 → 122,22 → **121,11**'),
    F('L<sub>q</sub> = ' + frac('Σqₜ·p₀', 'Σq₀·p₀') + ' · 100&nbsp;&nbsp;&nbsp;&nbsp;P<sub>q</sub> = ' + frac('Σqₜ·pₜ', 'Σq₀·pₜ') + ' · 100'),
    Step(1, 'Lq = (110·1 + 190·0,90) ÷ (100·1 + 200·0,90) × 100 = 281 ÷ 280 × 100 = **100,36**'),
    Step(2, 'Pq = (110·1,20 + 190·1,10) ÷ (100·1,20 + 200·1,10) × 100 = 341 ÷ 340 × 100 = **100,29**'),
    Ojo('**Laspeyres sobreestima** la inflación (usa las cantidades antiguas aunque la gente compre menos de lo que sube). **Paasche la subestima.** Fisher queda en medio.'),
], [
    (1, 'Dos índices más del apartado. El de Sauerbeck es la media aritmética de los índices simples de cada producto, sin ponderar: supone que todos los productos son igual de importantes. Con el pan, 120, y la leche, 122,22, sale 121,11.'),
    (2, 'Y los índices de cantidades: igual que los de precios, pero intercambiando los papeles. Ahora lo que cambia arriba y abajo son las cantidades, y el precio se queda fijo: el del año base en Laspeyres y el de hoy en Paasche.'),
    (3, 'Con el pan y la leche, Laspeyres de cantidades: 110 por 1 más 190 por 0,90, entre 100 por 1 más 200 por 0,90. 281 entre 280: 100,36. Se ha comprado un 0,36 por ciento más.'),
    (4, 'Y Paasche de cantidades, con los precios de hoy: 341 entre 340, 100,29.'),
    (5, '¿Por qué tantos índices? Laspeyres sobreestima la inflación: si algo sube mucho, la gente compra menos, pero Laspeyres sigue usando las cantidades antiguas. Paasche la subestima. Fisher queda en medio.'),
]))
