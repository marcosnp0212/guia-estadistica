import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 'b4', 'tab': 'Boletín T4', 'color': 't4'}
S = []
def E(n, t): return (f'Ej. {n}.', t)
S.append(Scene('', '', 'title', card('Boletín', 'Ejercicios del Tema 4', 'Los 12 ejercicios de números índice, a mano y en Excel'), [
    (3, 'En este vídeo resolvemos los 12 ejercicios del boletín del Tema 4, números índice. Para cada uno: enunciado, resolución a mano, Excel e interpretación. Para el vídeo antes de cada solución e inténtalo tú.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:72px">La herramienta de todo el tema</h1>',
    F('sube un 15 % → × **1,15**    baja un 20 % → × **0,80**'), Step(1, 'Escribe la frase como **ecuación**: «A supera en un 15 % a B» → **A = 1,15 · B**'), Step(2, 'Tasa entre dos valores: **nuevo ÷ viejo − 1**')], [
    (2, 'En casi todo el tema usamos una sola idea: subir un porcentaje es multiplicar por 1 más la tasa, y bajar es multiplicar por 1 menos la tasa.'),
    (3, 'Cuando la frase es liosa, escríbela como ecuación antes de calcular. A supera en un 15 por ciento a B: A es 1,15 por B.'),
    (4, 'Y la tasa de variación entre dos valores: el nuevo entre el viejo, menos 1.'),
]))
# Ej1
S.append(Scene(*E(1, 'Índices de producción'), 'mano', [
    Enun('En 2020 la producción aumentó un 40 % respecto a 2019. En 2021 bajó un 20 % respecto a 2020 y superó en un 15 % la de 2022. Índices con base 2019.'),
    Step(1, '2019 = **100** · 2020: 100 · 1,40 = **140** · 2021: 140 · 0,80 = **112**'),
    Step(2, '«2021 superó en un 15 % a 2022» → 2021 = 1,15 · 2022 → 2022 = 112/1,15 = **97,39**'),
    Ojo('No es 112 · 0,85 (daría 95,2): la referencia es **2022**.'),
    XL('=B4/1,15', '2022'),
], [
    (1, 'Ejercicio 1: índices de producción con base 2019.'),
    (2, 'Ponemos 2019 igual a 100. 2020 sube un 40 por ciento: por 1,40, 140. 2021 baja un 20 por ciento respecto a 2020: por 0,80, 112.'),
    (3, 'Y la frase difícil: 2021 superó en un 15 por ciento a 2022. Como ecuación: 2021 es 1,15 por 2022. Despejamos: 112 entre 1,15, 97,39.'),
    (4, 'El error típico es multiplicar 112 por 0,85, que da 95,2. Está mal, porque la referencia del 15 por ciento es 2022, no 2021.'),
    (5, 'En Excel, la misma idea: multiplicar o dividir la celda anterior.'),
]))
# Ej2
S.append(Scene(*E(2, 'Precio de un bien'), 'mano', [
    Enun('En 2020 el precio fue un 20 % mayor que en 2019, un 20 % menor que en 2018 y un 50 % menor que en 2021. Base 2019.'),
    Step(1, '2019 = **100** · 2020 = **120**'),
    Step(2, '2020 = 0,80 · 2018 → 2018 = 120/0,80 = **150**'),
    Step(3, '2020 = 0,50 · 2021 → 2021 = 120/0,50 = **240**'),
    T(['Año', 2018, 2019, 2020, 2021], [['Índice', 150, 100, 120, 240]], small=True),
], [
    (1, 'Ejercicio 2: el precio de un bien, con base 2019. Todas las frases se refieren a 2020.'),
    (2, '2019 es 100, y 2020, un 20 por ciento más: 120.'),
    (3, '2020 es un 20 por ciento menor que 2018: 2020 es 0,80 por 2018. Despejando, 120 entre 0,80, 150.'),
    (4, 'Y 2020 es un 50 por ciento menor que 2021: 120 entre 0,50, 240.'),
    (5, 'La serie queda: 150, 100, 120 y 240.'),
]))
# Ej3
S.append(Scene(*E(3, 'Cuentas corrientes de un banco'), 'mano', [
    Enun('Variación anual: 2021 +9 %, 2022 +10 %, 2023 −2 %, 2024 +8 %, 2025 +10 %. Índices con base 2020.'),
    T(['Año', 'Cálculo', 'Índice'], [[2020, 'base', 100], [2021, '100 × 1,09', 109], [2022, '109 × 1,10', '119,90'], [2023, '119,9 × 0,98', '117,50'], [2024, '117,502 × 1,08', '126,90'], [2025, '126,902 × 1,10', '139,59']], small=True),
    XL('=C2*(1+B3)', 'y arrastrar'),
    Res('En 2025 hay un **39,6 %** más de cuentas que en 2020.'),
], [
    (1, 'Ejercicio 3: tasas anuales de cuentas corrientes. Índices con base 2020.'),
    (2, 'Se encadenan: cada año, el índice anterior por 1 más la tasa. 109, 119,90, 117,50, 126,90 y 139,59. Usa todos los decimales en la calculadora para no arrastrar errores.'),
    (3, 'En Excel, la celda anterior por 1 más la tasa, y arrastrar.'),
    (4, 'Interpretación: en 2025 hay un 39,6 por ciento más de cuentas que en 2020.'),
]))
# Ej4
S.append(Scene(*E(4, '¿Está bien ajustado el salario?'), 'mano', [
    Enun('IPC 2024 (base 2023) = 103,5. En 2023 nos pagan 433,45 € por un trabajo y en 2024, 442,20 € por el mismo trabajo.'),
    Step(1, 'Debería cobrar: 433,45 · 1,035 = **448,62 €** → cobra menos: **no está bien ajustado**'),
    Step(2, 'Valor real (€ de 2023): 442,20/103,5 · 100 = **427,25 €**'),
    Step(3, 'Variación real: 427,25/433,45 − 1 = **−1,43 %**'),
    Res('En nominal cobra un 2,02 % más, pero los precios subieron un 3,5 %: ha **perdido un 1,43 %** de poder adquisitivo.'),
], [
    (1, 'Ejercicio 4: ¿está bien ajustado el salario? El IPC de 2024 con base 2023 es 103,5: los precios subieron un 3,5 por ciento.'),
    (2, 'Para no perder poder adquisitivo debería cobrar 433,45 por 1,035: 448,62 euros. Cobra 442,20, menos: no está bien ajustado.'),
    (3, 'Otra forma: pasar el salario de 2024 a euros de 2023. Dividir entre el IPC y multiplicar por 100: 427,25 euros.'),
    (4, 'Y la variación real: 427,25 entre 433,45 menos 1: menos 1,43 por ciento.'),
    (5, 'La interpretación: aunque en euros cobra un 2 por ciento más, los precios subieron un 3,5. En términos reales ha perdido un 1,43 por ciento de poder adquisitivo.'),
]))
# Ej5
S.append(Scene(*E(5, 'Tasas de variación de inversiones'), 'mano', [
    Enun('Inversión: 45 000 (2020), 50 400 (2021), 48 300 (2022), 53 130 (2023), 55 786 (2024). Tasa de cada año respecto al anterior.'),
    T(['Año', 'Inversión', 'Tasa'], [[2020, '45 000', '—'], [2021, '50 400', '50 400/45 000 − 1 = **+12 %**'], [2022, '48 300', '48 300/50 400 − 1 = **−4,17 %**'], [2023, '53 130', '**+10 %**'], [2024, '55 786', '**+5 %**']], small=True),
    XL('=B3/B2-1', 'formato %, y arrastrar'),
], [
    (1, 'Ejercicio 5: las tasas de variación de una inversión, cada año respecto al anterior.'),
    (2, 'Nuevo entre viejo menos 1: 2021, más 12 por ciento; 2022, menos 4,17; 2023, más 10; y 2024, más 5.'),
    (3, 'En Excel, la celda entre la de arriba menos 1, con formato de porcentaje.'),
]))
# Ej6
S.append(Scene(*E(6, 'Justificar dos series de índices'), 'mano', [
    Enun('Producción 120, 135, 150, 165, 180 (2020-2024). Base 2020: 100; 112,5; 125; 137,5; 150. Base 2022: 80; 90; 100; 110; 120.'),
    Step(1, 'Base 2020: cada valor ÷ 120 · 100 → 2021: 135/120 · 100 = **112,5**'),
    Step(2, 'Cambio de base: cada índice ÷ el de 2022 (125) · 100 → 2020: 100/125 · 100 = **80** · 2024: 150/125 · 100 = **120**'),
    P('Es lo mismo que dividir cada producción entre la de 2022 (150).', 's'),
    XL('=C2/$C$4*100'),
], [
    (1, 'Ejercicio 6: justificar dos series de índices de producción.'),
    (2, 'La primera, base 2020: cada producción entre la de 2020, 120, por 100. Por ejemplo, 135 entre 120 por 100: 112,5.'),
    (3, 'La segunda es un cambio de base: cada índice de la serie anterior entre el de 2022, que es 125, por 100. 100 entre 125, 80. 150 entre 125, 120.'),
    (4, 'Y sale lo mismo que dividir directamente cada producción entre la de 2022.'),
    (5, 'En Excel, con el dólar para fijar la celda del año base.'),
]))
# Ej7
S.append(Scene(*E(7, 'Cantidad, precio y valor'), 'mano', [
    Enun('2015: cantidad 8820, precio 14. 2022: 9030 y 18. 2025: 9073 y 20.'),
    T(['', '2015 → 2022', '2022 → 2025'], [['a) Cantidad', '**2,38 %**', '**0,48 %**'], ['a) Precio', '**28,57 %**', '**11,11 %**'], ['b) Cantidad anual', '1,0238^(1/7) − 1 = **0,34 %**', '1,0048^(1/3) − 1 = **0,16 %**'], ['b) Precio anual', '**3,66 %**', '**3,57 %**']], small=True),
    Step(1, 'c) Valor = p · q: 123 480 · 162 540 · 181 460'),
    Step(2, 'd) Índice del valor (2015 = 100): 100 · **131,63** · **146,95** → +31,63 %, +11,64 %, total +46,95 %'),
    Truco('Índice de valor = índice de precio × índice de cantidad: 1,2857 · 1,0238 = 1,3163 ✔'),
], [
    (1, 'Ejercicio 7: cantidad, precio y valor de un producto en 2015, 2022 y 2025.'),
    (2, 'a) Las tasas de cada periodo, nuevo entre viejo menos 1. La cantidad sube un 2,38 y un 0,48 por ciento; el precio, un 28,57 y un 11,11. b) Las tasas anuales equivalentes: de 2015 a 2022 hay 7 años, así que elevamos 1 más la tasa a 1 séptimo y restamos 1. De 2022 a 2025, 3 años: a 1 tercio.'),
    (3, 'c) El valor es precio por cantidad: 123 480, 162 540 y 181 460.'),
    (4, 'd) Los índices del valor con base 2015: 131,63 y 146,95. En todo el periodo, el valor sube un 46,95 por ciento.'),
    (5, 'Una curiosidad útil: el índice de valor es el producto del de precios por el de cantidad. Sirve para comprobar.'),
]))
# Ej8
S.append(Scene(*E(8, 'Tasas mensuales'), 'mano', [
    Enun('Enero +5 %, febrero +4 %, marzo +3 %.'),
    Step(1, 'a) Trimestre: 1,05 · 1,04 · 1,03 = 1,12476 → **+12,48 %**'),
    Step(2, 'b) Con 100 €: 105 → 109,20 → **112,48** ✔'),
    Step(3, 'c) Media mensual: 1,12476^(1/3) − 1 = **4 %**'),
    Ojo('Las tasas **no se suman** (5 + 4 + 3 = 12 ≠ 12,48): se **multiplican**.'),
    XL('=((1+B2)*(1+B3)*(1+B4))^(1/3)-1'),
], [
    (1, 'Ejercicio 8: tasas mensuales del 5, 4 y 3 por ciento.'),
    (2, 'a) La tasa del trimestre: se multiplican los factores, 1,05 por 1,04 por 1,03, 1,12476. Un 12,48 por ciento.'),
    (3, 'b) Comprobación con 100 euros: 105, 109,20 y 112,48. Coincide.'),
    (4, 'c) La tasa media mensual: la raíz cúbica de 1,12476, menos 1. Un 4 por ciento.'),
    (5, 'Ojo: las tasas no se suman. 5 más 4 más 3 es 12, pero la tasa real es 12,48. Se multiplican.'),
    (6, 'En Excel, el producto elevado a 1 tercio, menos 1.'),
]))
# Ej9
S.append(Scene(*E(9, 'Laspeyres y Paasche de una cesta'), 'mano', [
    T(['', 'p₂₀', 'q₂₀', 'p₂₅', 'q₂₅', 'p₂₅q₂₀', 'p₂₀q₂₀', 'p₂₅q₂₅', 'p₂₀q₂₅'], [['Pan', '1,20', 300, '1,50', 280, 450, 360, 420, 336], ['Leche', '0,90', 200, '1,10', 210, 220, 180, 231, 189], ['Huevos', '2,50', 100, '3,00', 95, 300, 250, 285, '237,5'], ['Carne', '8,00', 50, '9,50', 48, 475, 400, 456, 384], ['Pescado', '10,00', 40, '12,00', 38, 480, 400, 456, 380], ['**Σ**', '', '', '', '', '**1925**', '**1590**', '**1848**', '**1526,5**']], small=True),
    Step(1, 'Laspeyres: 1925/1590 · 100 = **121,07**'),
    Step(2, 'Paasche: 1848/1526,5 · 100 = **121,06**'),
    XL('=SUMAPRODUCTO(D2:D6;C2:C6)/SUMAPRODUCTO(B2:B6;C2:C6)*100', 'Laspeyres'),
], [
    (1, 'Ejercicio 9: Laspeyres y Paasche de una cesta de cinco productos. La tabla de trabajo: cuatro columnas de productos de precio por cantidad.'),
    (2, 'Laspeyres pondera con las cantidades del año base: precios nuevos por cantidades de 2020, entre precios de 2020 por cantidades de 2020. 1925 entre 1590 por 100: 121,07. Los precios subieron un 21,07 por ciento.'),
    (3, 'Paasche pondera con las cantidades del año actual: 1848 entre 1526,5 por 100: 121,06. Salen casi iguales porque las cantidades apenas cambiaron.'),
    (4, 'En Excel, SUMAPRODUCTO arriba y abajo, por 100.'),
]))
# Ej10
S.append(Scene(*E(10, 'Sueldos e IPC'), 'mano', [
    T(['Año', 1992, 1993, 1994, 1995, 1996], [['Sueldo', '150 000', '162 000', '170 000', '183 000', '190 000'], ['IPC (1990)', 120, '130,5', '137,4', 144, '153,8'], ['a) IPC (1992)', 100, '108,75', '114,50', '120,00', '128,17'], ['b) Sueldo real', '150 000', '148 965,52', '148 471,62', '152 500', '148 244,47']], small=True),
    Step(1, 'a) Cambio de base: cada IPC ÷ 120 · 100'),
    Step(2, 'b) Sueldo real = sueldo ÷ IPC₁₉₉₂ · 100'),
    Step(3, 'c) Nominal: 190 000/150 000 − 1 = **+26,67 %** · Real: 148 244,47/150 000 − 1 = **−1,17 %**'),
    Res('El sueldo nominal sube mucho, pero los precios suben más: el poder adquisitivo **baja**.'),
], [
    (1, 'Ejercicio 10: sueldos e IPC de 1992 a 1996, con el IPC en base 1990.'),
    (2, 'a) Cambio de base a 1992: cada IPC entre el de 1992, 120, por 100.'),
    (3, 'b) El sueldo en dinero de 1992, el sueldo real: cada sueldo entre su IPC con base 1992, por 100.'),
    (4, 'c) La variación de 1992 a 1996. En términos corrientes, más 26,67 por ciento. En términos reales, menos 1,17.'),
    (5, 'Interpretación: aunque el sueldo nominal sube mucho, los precios suben más, y el poder adquisitivo baja ligeramente.'),
]))
# Ej11
S.append(Scene(*E(11, 'Actualizar un alquiler con el IPC'), 'mano', [
    Enun('Alquiler en 2020: 1200 €/mes. IPC: 2020 = 112, 2021 = 114, 2022 = 120.'),
    Step(1, 'a) 2021: 1200 · 114/112 = **1221,43 €** · 2022: 1200 · 120/112 = **1285,71 €**'),
    Step(2, 'b) 1300 € en 2022 equivalen en 2020 a 1300 · 112/120 = **1213,33 €**'),
    XL('=$B$1*B3/$B$2'),
], [
    (1, 'Ejercicio 11: actualizar un alquiler de 1200 euros con el IPC.'),
    (2, 'a) Se actualiza en la misma proporción que el IPC: por el IPC nuevo entre el de 2020. 2021, 1221,43 euros; 2022, 1285,71.'),
    (3, 'b) Si en 2022 quiere cobrar 1300, lo equivalente en dinero de 2020 es 1300 por 112 entre 120: 1213,33 euros. Más que los 1200 de 2020: sube por encima del IPC.'),
    (4, 'En Excel, el alquiler fijo con dólares por el cociente de IPC.'),
]))
# Ej12
S.append(Scene(*E(12, 'SMI real con base 2010'), 'mano', [
    T(['Año', 'SMI', 'IPC', 'SMI real (€ 2010)', 'Índice real'], [[2010, '633,3', '105,63', '633,30', '100,00'], [2011, '641,4', '109,01', '621,51', '98,14'], [2012, '641,4', '111,67', '606,71', '95,80'], [2013, '645,3', '113,25', '601,88', '95,04'], [2014, '645,3', '113,08', '602,79', '95,18'], [2015, '648,6', '112,52', '608,88', '96,14'], [2016, '655,2', '112,29', '616,34', '97,32']], small=True),
    Step(1, 'SMI real = SMI · 105,63/IPC → 2011: 641,4 · 105,63/109,01 = **621,51 €**'),
    XL('=B2*$C$2/C2'),
    Res('El SMI nominal sube un 3,46 %, pero en **real baja un 2,68 %**. Peor año: 2013 (−4,96 %).'),
], [
    (1, 'Último ejercicio, el 12: el salario mínimo en términos reales con base 2010.'),
    (2, 'El IPC no está en base 2010, así que lo pasamos dividiendo entre 105,63. Todo junto: SMI real igual a SMI por 105,63 entre el IPC de ese año. En 2011, 621,51 euros. El índice real, el SMI real entre 633,3 por 100.'),
    (3, 'En Excel, con el IPC de 2010 fijado con dólares, y arrastrar.'),
    (4, 'La interpretación: aunque el SMI nominal sube un 3,46 por ciento entre 2010 y 2016, en términos reales baja un 2,68. El peor año, 2013.'),
]))
S.append(Scene('', '', 'title', card('Boletín', 'Fin del boletín del Tema 4', 'Ahora: las **Prácticas 7 y 8** y los **simulacros** de la guía.'), [
    (3, 'Hasta aquí el boletín del Tema 4. Ahora, en la guía, las prácticas 7 y 8 y los simulacros. Mucho ánimo.'),
]))
