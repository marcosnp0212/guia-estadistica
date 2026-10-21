# Boletín de ejercicios de los Temas 1 y 2, resuelto

::: {.video data-v="b12"}
:::

::: {custom-style="Idea"}
**🧠 Cómo usar este boletín.** Las soluciones están hechas **a mano, con calculadora**, con todas las cuentas a la vista: así es como lo harías en un examen en papel. El recuadro verde de cada ejercicio te dice cómo hacerlo en Excel. Intenta cada ejercicio primero tú, en papel, sin mirar. Luego abre la solución, mejor paso a paso. Los números finales están redondeados; en tu solucionario (apartado Descargas) tienes todos los decimales. Si tu resultado coincide en las dos o tres primeras cifras, está bien.
:::

::: {custom-style="Truco"}
**💡 Las 3 preguntas antes de empezar cualquier ejercicio.** (1) ¿Qué variable es y de qué tipo? (2) ¿Los datos vienen sueltos, en tabla de valores o en intervalos? (3) ¿Qué me piden exactamente: centro, dispersión, posición, forma, relación?
:::

## Ejercicio 1. Medias, varianzas y datos tipificados

::: {custom-style="Enunciado"}
Primer conjunto: 1, 2, 3, 4, 5, 6. Segundo: 1, 1, 1, 6, 6, 6. Tercero: −13, 2, 3, 4, 5, 20. a) Medias y varianzas. b) Datos tipificados del primer conjunto.
:::

**a) Medias.** Sumamos y dividimos entre 6.

- Primero: (1+2+3+4+5+6)/6 = 21/6 = **3,5**.
- Segundo: (1+1+1+6+6+6)/6 = 21/6 = **3,5**.
- Tercero: (−13+2+3+4+5+20)/6 = 21/6 = **3,5**.

Los tres tienen la misma media. Veremos que su dispersión es muy distinta.

**a) Varianzas.** Usamos S² = (Σxᵢ²)/n − x̄².

- Primero: Σxᵢ² = 1+4+9+16+25+36 = 91. S² = 91/6 − 3,5² = 15,1667 − 12,25 = **2,917**.
- Segundo: Σxᵢ² = 1+1+1+36+36+36 = 111. S² = 111/6 − 12,25 = 18,5 − 12,25 = **6,25**.
- Tercero: Σxᵢ² = 169+4+9+16+25+400 = 623. S² = 623/6 − 12,25 = 103,833 − 12,25 = **91,583**.

::: {custom-style="Resultado"}
**✅** Misma media (3,5) pero varianzas 2,92 · 6,25 · 91,58. El tercer conjunto es el más disperso por los valores extremos −13 y 20. El segundo es más disperso que el primero porque todos sus datos están lejos de la media (en 1 o en 6). Moraleja: **la media sola no basta para describir unos datos**.
:::

**b) Tipificar el primer conjunto.** S = √2,917 = 1,708. Para cada dato, z = (x − 3,5)/1,708:

| x | 1 | 2 | 3 | 4 | 5 | 6 |
|:---|---:|---:|---:|---:|---:|---:|
| z | −1,464 | −0,878 | −0,293 | 0,293 | 0,878 | 1,464 |

Comprobación: los z suman 0 (media 0) y su varianza es 1.

::: {custom-style="Excel"}
**🖥️ En Excel.** Datos del primer conjunto en A2:A7. Media: `=PROMEDIO(A2:A7)`. Varianza: `=VAR.P(A2:A7)`. Tipificado de A2: `=NORMALIZACION(A2;PROMEDIO($A$2:$A$7);DESVEST.P($A$2:$A$7))` y arrastrar. Repite con los otros conjuntos en las columnas B y C.
:::

## Ejercicio 2. Preguntas de teoría

::: {custom-style="Enunciado"}
a) ¿Qué significa que la renta de un trabajador esté en el percentil 98? b) Explica las diferencias entre las medidas de posición, de dispersión y de forma. c) ¿Qué diferencias hay entre la asimetría y la curtosis?
:::

**a) ¿Qué significa que la renta de un trabajador esté en el percentil 98?** Que el 98 % de los trabajadores tiene una renta menor o igual que la suya, y solo un 2 % gana más que él. Está entre los que más ganan.

**b) Diferencias entre medidas de posición, dispersión y forma.**

- Las de **posición** dicen **dónde** están los datos: el centro (media, mediana, moda) o puntos de corte (cuartiles, percentiles).
- Las de **dispersión** dicen **cuánto se separan** los datos entre sí o de la media (rango, IQR, varianza, desviación típica, CV).
- Las de **forma** describen **el dibujo** de la distribución: si es simétrica o tiene cola a un lado (asimetría) y si es picuda o plana (curtosis).

**c) Asimetría vs curtosis.** La asimetría mide si la distribución está equilibrada a izquierda y derecha de la media o si tiene una cola más larga hacia un lado. La curtosis mide cómo de concentrados están los datos alrededor de la media: si la distribución es más picuda o más plana que la normal.

## Ejercicio 3. Número de hijos

::: {custom-style="Enunciado"}
Hijos por familia: 0, 2, 2, 2, 4, 3, 3, 0, 0, 0, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1. a) Tamaño muestral. b) Tabla de frecuencias. c) Comenta los gráficos. d) Interpreta las medidas dadas (Min 0 · 1st Qu. 1 · Median 1 · Mean 1,6 · 3rd Qu. 2,5 · Max 4). ¿Son de posición, dispersión o forma?
:::

**a)** Contamos los datos: **n = 20** familias.

**b)** Variable cuantitativa discreta. Ordenamos y contamos:

| Hijos xᵢ | nᵢ | fᵢ | % | Nᵢ | Fᵢ |
|---:|---:|---:|---:|---:|---:|
| 0 | 4 | 0,20 | 20 | 4 | 0,20 |
| 1 | 7 | 0,35 | 35 | 11 | 0,55 |
| 2 | 4 | 0,20 | 20 | 15 | 0,75 |
| 3 | 3 | 0,15 | 15 | 18 | 0,90 |
| 4 | 2 | 0,10 | 10 | 20 | 1 |
| **Total** | **20** | **1** | **100** | | |

**c) Los gráficos.** Son tres diagramas de barras con **la misma forma**: el azul con frecuencias absolutas (eje hasta 7), el verde con relativas (hasta 0,35) y el rojo con porcentajes (hasta 35). Solo cambia la escala del eje vertical, porque las tres frecuencias son proporcionales. Se ve que lo más frecuente es tener 1 hijo y que a partir de ahí las barras bajan: hay pocas familias con 3 o 4 hijos. La distribución tiene una ligera cola a la derecha.

![](img/b3_hijos.png){width=70%}

**d) Las medidas.**

- Min = 0 y Max = 4: ninguna familia tiene más de 4 hijos ni menos de 0. (Su diferencia, el rango = 4, sería una medida de dispersión.)
- 1st Qu. = C₁ = 1: al menos el 25 % de las familias tiene 1 hijo o ninguno.
- Median = 1: la mitad de las familias tiene como mucho 1 hijo.
- Mean = 1,6: de media, 1,6 hijos por familia. Es mayor que la mediana porque las familias con 3 y 4 hijos tiran de la media hacia arriba (asimetría positiva).
- 3rd Qu. = C₃ = 2,5: el 75 % de las familias tiene 2,5 hijos o menos (en la práctica, 2 o menos).

Todas son **medidas de posición**. No hay medidas de forma, y de dispersión solo podríamos sacar el rango (4) y el IQR (2,5 − 1 = 1,5).

Comprobación a mano: n/2 = 10 → primera Nᵢ ≥ 10 es 11 (valor 1) → Me = 1. n/4 = 5 → Nᵢ = 11 → C₁ = 1. 3n/4 = 15 → Nᵢ = 15, **igual** → C₃ = (2 + 3)/2 = 2,5. Media = (0·4 + 1·7 + 2·4 + 3·3 + 4·2)/20 = 32/20 = 1,6.

::: {custom-style="Ojo"}
**⚠️ Ojo.** En Excel, `=CUARTIL.INC(datos;3)` da **2,25** y no 2,5, por la diferencia de método que vimos en el Tema 1. La mediana y C₁ sí coinciden.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Datos en A2:A21. n: `=CONTAR(A2:A21)`. Tabla: valores 0 a 4 en C2:C6 y en D2 `=CONTAR.SI($A$2:$A$21;C2)`, arrastrando. Media `=PROMEDIO(A2:A21)` → 1,6; mediana `=MEDIANA(A2:A21)` → 1; C₁ `=CUARTIL.INC(A2:A21;1)` → 1. Gráfico: selecciona C1:D6 → Insertar → Columna agrupada.
:::

## Ejercicio 4. Lesiones en fútbol y baloncesto

::: {custom-style="Enunciado"}
Fútbol (X): valores 1 a 7 con frecuencias absolutas 1, 3, 5, 7, 5, 3, 1. Baloncesto (Y): valores 1 a 7 con frecuencias **relativas** 0,24 · 0,16 · 0,08 · 0,04 · 0,08 · 0,16 · 0,24.
:::

**a) Promedio de lesiones.**

Fútbol (con absolutas, n = 25): Σxᵢnᵢ = 1·1 + 2·3 + 3·5 + 4·7 + 5·5 + 6·3 + 7·1 = 1 + 6 + 15 + 28 + 25 + 18 + 7 = 100. x̄ = 100/25 = **4 lesiones**.

Baloncesto (con relativas, se multiplica por fᵢ y no se divide): ȳ = 1·0,24 + 2·0,16 + 3·0,08 + 4·0,04 + 5·0,08 + 6·0,16 + 7·0,24 = 0,24 + 0,32 + 0,24 + 0,16 + 0,40 + 0,96 + 1,68 = **4 lesiones**.

**b) Número de lesiones más frecuente (moda).** Fútbol: la mayor frecuencia es 7, en el valor 4 → **Mo = 4**. Baloncesto: la mayor frecuencia (0,24) se da en 1 y en 7 → **dos modas, 1 y 7** (bimodal).

**c) Gráficos.** Diagramas de barras (variables discretas).

![](img/b4_lesiones.png){width=90%}

Fútbol tiene forma de "montaña" centrada en 4. Baloncesto tiene forma de "U": muchos jugadores con muy pocas lesiones y muchos con muchísimas, y pocos en el medio.

**d) Mínimo de lesiones para estar en el 50 % de futbolistas que más se lesionan.** Es la **mediana** de X. n/2 = 12,5. Acumuladas: 1, 4, 9, 16... La primera ≥ 12,5 es 16, en el valor 4. **Me = 4**: con 4 lesiones o más ya estás en la mitad que más se lesiona.

**e) Máximo de lesiones para estar en el 50 % de jugadores de baloncesto que menos se lesionan.** La mediana de Y. Acumuladas relativas: 0,24 · 0,40 · 0,48 · 0,52... La primera ≥ 0,5 es 0,52, en el valor 4. **Me = 4**.

**f) ¿Dónde hay más variabilidad?** Mirando los gráficos: en **baloncesto**, porque los datos se van a los extremos (1 y 7), lejos de la media 4. En fútbol se concentran cerca de 4.

Comprobamos con la varianza:

- Fútbol: Σxᵢ²nᵢ = 1 + 12 + 45 + 112 + 125 + 108 + 49 = 452. S²ₓ = 452/25 − 4² = 18,08 − 16 = **2,08**.
- Baloncesto: Σyᵢ²fᵢ = 0,24 + 0,64 + 0,72 + 0,64 + 2 + 5,76 + 11,76 = 21,76. S²ᵧ = 21,76 − 16 = **5,76**.

::: {custom-style="Resultado"}
**✅** Las dos tienen media 4, pero la varianza de baloncesto (5,76) casi triplica la de fútbol (2,08). Como las medias son iguales, podemos comparar directamente las varianzas: **hay más variabilidad en baloncesto**.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Valores en A2:A8, frecuencias de fútbol en B2:B8, frecuencias relativas de baloncesto en C2:C8.

- Media fútbol: `=SUMAPRODUCTO(A2:A8;B2:B8)/SUMA(B2:B8)`.
- Media baloncesto: `=SUMAPRODUCTO(A2:A8;C2:C8)` (con relativas no se divide, porque ya suman 1).
- Varianza fútbol (media en F2): `=SUMAPRODUCTO(A2:A8^2;B2:B8)/SUMA(B2:B8)-F2^2`.
- Varianza baloncesto (media en F3): `=SUMAPRODUCTO(A2:A8^2;C2:C8)-F3^2`.
- Acumuladas de fútbol en D: `=B2` y luego `=D2+B3` arrastrando.
:::

::: {custom-style="Mano"}
**✍️ A mano: el diagrama de barras doble.** Pon los dos gráficos uno al lado del otro con el mismo eje horizontal (1 a 7). Fútbol con frecuencias absolutas (eje vertical de 0 a 8). Baloncesto con relativas (de 0 a 0,25). Una barra por valor, sin tocarse. Se ve de un vistazo la «montaña» de fútbol y la «U» de baloncesto.
:::

## Ejercicio 5. Histograma con intervalos de distinta amplitud

::: {custom-style="Enunciado"}
Intervalos [7,8], (8,9], (9,10], (10,12], (12,15] con frecuencias 3, 6, 9, 9, 3.
:::

Las amplitudes no son iguales (1, 1, 1, 2 y 3), así que la altura de cada barra tiene que ser la **densidad** dᵢ = nᵢ / aᵢ.

| Intervalo | nᵢ | aᵢ | dᵢ = nᵢ/aᵢ |
|:---:|---:|---:|---:|
| [7, 8] | 3 | 1 | 3 |
| (8, 9] | 6 | 1 | 6 |
| (9, 10] | 9 | 1 | 9 |
| (10, 12] | 9 | 2 | 4,5 |
| (12, 15] | 3 | 3 | 1 |

![](img/b5_hist.png){width=75%}

::: {custom-style="Ojo"}
**⚠️ Ojo.** Si dibujaras la frecuencia (9) como altura del intervalo (10, 12], parecería tan "lleno" como (9, 10], pero sus 9 datos están repartidos en el doble de espacio. Por eso su barra mide la mitad (4,5).
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Calcula la columna de densidades (`=B2/C2`). Excel no dibuja automáticamente barras de distinta anchura. Opción práctica: gráfico de columnas con las densidades, ancho de intervalo 0 %, y explicar en el texto que las bases tienen amplitudes distintas. En el examen lo importante es **calcular bien las densidades** y saber que son las alturas.
:::

::: {custom-style="Mano"}
**✍️ A mano: el histograma con amplitudes distintas.** 1. Eje horizontal de 7 a 15, **a escala**: cada unidad ocupa lo mismo (si 1 unidad = 1 cm, (12, 15] mide 3 cm).
2. Eje vertical para la densidad, de 0 a 10.
3. Rectángulos pegados con altura = densidad: 3, 6, 9, 4,5 y 1.
4. Comprueba: el **área** de cada rectángulo (base × altura) es su nᵢ. (10, 12]: 2 × 4,5 = 9 ✔.
:::

## Ejercicio 6. Notas de un examen

::: {custom-style="Enunciado"}
Notas 1 a 8 con frecuencias 4, 4, 8, 7, 5, 10, 7, 5.
:::

**a) Tabla completa.** n = 50.

| xᵢ | nᵢ | fᵢ | Nᵢ | Fᵢ |
|---:|---:|---:|---:|---:|
| 1 | 4 | 0,08 | 4 | 0,08 |
| 2 | 4 | 0,08 | 8 | 0,16 |
| 3 | 8 | 0,16 | 16 | 0,32 |
| 4 | 7 | 0,14 | 23 | 0,46 |
| 5 | 5 | 0,10 | 28 | 0,56 |
| 6 | 10 | 0,20 | 38 | 0,76 |
| 7 | 7 | 0,14 | 45 | 0,90 |
| 8 | 5 | 0,10 | 50 | 1 |

**b) Alumnos totales:** **50**.

**c) Alumnos con más de un 3:** todos menos los que tienen 3 o menos. La acumulada hasta el 3 es 16. 50 − 16 = **34 alumnos**.

**d) Porcentaje con un 6:** f = 10/50 = 0,20 → **20 %**.

**e) Porcentaje con más de un 4:** acumulada hasta el 4 = 0,46. 1 − 0,46 = 0,54 → **54 %**.

**f) Nota ≥ 2 y < 5:** son los que tienen 2, 3 o 4: 4 + 8 + 7 = **19 alumnos**. (Con acumuladas: N hasta 4 menos N hasta 1 = 23 − 4 = 19.)

::: {custom-style="Truco"}
**💡 Truco con las palabras.** "Más de 3" **no** incluye el 3. "Al menos 3" o "3 o más" **sí** lo incluye. "Menos de 5" no incluye el 5. Subraya estas palabras en el enunciado.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Con la tabla montada (nᵢ en B2:B9): "más de 3" = `=SUMA(B5:B9)` o `=50-D4` (D = acumuladas). Si tuvieras los 50 datos sueltos en una columna: `=CONTAR.SI(datos;">3")` y `=CONTAR.SI.CONJUNTO(datos;">=2";datos;"<5")`.
:::

## Ejercicio 7. Pólizas de seguros (26 días)

::: {custom-style="Enunciado"}
Intervalos [30,40], (40,50], (50,60], (60,70], (70,80] con 2, 4, 6, 9, 5 días.
:::

**a) Días con más de 50 pólizas:** 6 + 9 + 5 = **20 días**.

**b) Días con más de 62 pólizas.** El 62 está **dentro** del intervalo (60, 70]. Como no tenemos los datos exactos, suponemos que los 9 días de ese intervalo están repartidos de forma uniforme. De 62 a 70 hay 8 de las 10 unidades del intervalo → 9 × 8/10 = 7,2 días. Más los 5 días de (70, 80]: 7,2 + 5 = **12,2 ≈ 12 días**.

**c) Porcentaje de días entre 52 y 67 pólizas.** Mismo razonamiento, por trozos:

- De 52 a 60 (dentro de (50,60], que tiene 6 días): 6 × 8/10 = 4,8 días.
- De 60 a 67 (dentro de (60,70], que tiene 9 días): 9 × 7/10 = 6,3 días.
- Total: 4,8 + 6,3 = 11,1 días. Porcentaje: 11,1/26 × 100 = **42,7 %**.

::: {custom-style="Ojo"}
**⚠️ Ojo.** Esta "regla de tres dentro del intervalo" es la misma idea que hay detrás de la fórmula de la mediana. Escribe siempre la frase "suponiendo que los datos se reparten uniformemente dentro del intervalo".
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Linf en A2:A6, Lsup en B2:B6, días en C2:C6. a) `=SUMA(C4:C6)` → 20. b) Parte de (60, 70] por encima de 62 más el último intervalo: `=C5*(B5-62)/(B5-A5)+C6` → 12,2. c) `=(C4*(B4-52)/(B4-A4)+C5*(67-A5)/(B5-A5))/SUMA(C2:C6)` → 0,427 (con formato %).
:::

## Ejercicio 8. Exportaciones (miles de euros)

::: {custom-style="Enunciado"}
Intervalos [0,10], (10,20], (20,40], (40,50] con 4, 20, 10, 10 empresas. a) Media, varianza y CV. b) Francia tiene CV = 0,64: ¿dónde hay más dispersión? c) En España las exportaciones suben un 1 % y en Francia aumentan 10⁶ euros. ¿Cómo afecta a la media y la varianza?
:::

**a)** Marcas de clase: 5, 15, 30, 45. n = 44.

| Intervalo | xᵢ | nᵢ | xᵢ·nᵢ | xᵢ²·nᵢ |
|:---:|---:|---:|---:|---:|
| [0, 10] | 5 | 4 | 20 | 100 |
| (10, 20] | 15 | 20 | 300 | 4500 |
| (20, 40] | 30 | 10 | 300 | 9000 |
| (40, 50] | 45 | 10 | 450 | 20250 |
| **Total** | | **44** | **1070** | **33850** |

- Media: 1070/44 = **24,32 miles de €**.
- Varianza: 33850/44 − 24,32² = 769,32 − 591,37 = **177,94** (miles de €)².
- Desviación típica: √177,94 = 13,34. CV = 13,34/24,32 = **0,549** (54,9 %).

**b)** Francia 0,64 > España 0,549 → **más dispersión relativa en Francia**. Comparamos CV porque son países distintos (medias distintas).

**c)**

- **España, +1 %** (multiplicar por 1,01): la media se multiplica por 1,01 → 24,32 × 1,01 = **24,56**. La varianza se multiplica por 1,01² = 1,0201 → 177,94 × 1,0201 = **181,52**. El CV **no cambia**.
- **Francia, +10⁶ €** (sumar a todas): como los datos están en miles de euros, 10⁶ € = 1000 miles de €. La media **aumenta en 1000** (miles de €). La varianza **no cambia** (sumar no cambia la dispersión). Como la media sube y la desviación no, el CV de Francia **baja**.

::: {custom-style="Excel"}
**🖥️ En Excel.** Columnas: A = Linf, B = Lsup, C = nᵢ. Marca en D2: `=(A2+B2)/2`. Media: `=SUMAPRODUCTO(D2:D5;C2:C5)/SUMA(C2:C5)` (en F2). Varianza: `=SUMAPRODUCTO(D2:D5^2;C2:C5)/SUMA(C2:C5)-F2^2` (en F3). CV: `=RAIZ(F3)/F2`.
:::

## Ejercicio 9. Óxido de azufre

::: {custom-style="Enunciado"}
Intervalos [5,9), [9,13), ..., [29,33) con % de días 3,75 · 12,5 · 17,5 · 31,25 · 21,25 · 11,25 · 2,5. Media, varianza y gráfico.
:::

Nos dan **porcentajes**: los pasamos a frecuencias relativas (÷ 100) y usamos x̄ = Σxᵢfᵢ. Marcas: 7, 11, 15, 19, 23, 27, 31.

| xᵢ | fᵢ | xᵢ·fᵢ | xᵢ²·fᵢ |
|---:|---:|---:|---:|
| 7 | 0,0375 | 0,2625 | 1,8375 |
| 11 | 0,125 | 1,375 | 15,125 |
| 15 | 0,175 | 2,625 | 39,375 |
| 19 | 0,3125 | 5,9375 | 112,8125 |
| 23 | 0,2125 | 4,8875 | 112,4125 |
| 27 | 0,1125 | 3,0375 | 82,0125 |
| 31 | 0,025 | 0,775 | 24,025 |
| **Total** | **1** | **18,9** | **387,6** |

::: {custom-style="Resultado"}
**✅** Media = **18,9 toneladas** al día. Varianza = 387,6 − 18,9² = 387,6 − 357,21 = **30,39 t²**. Desviación típica = 5,51 t.
:::

Gráfico: **histograma** (variable continua en intervalos). Todos los intervalos miden 4, así que la altura puede ser directamente el %.

![](img/b9_hist.png){width=75%}

::: {custom-style="Excel"}
**🖥️ En Excel.** Marcas en A2:A8 y % en B2:B8. Media: `=SUMAPRODUCTO(A2:A8;B2:B8)/100` → 18,9 (en D2). Varianza: `=SUMAPRODUCTO(A2:A8^2;B2:B8)/100-D2^2` → 30,39. Histograma: columnas con los % y ancho de intervalo 0 %.
:::

::: {custom-style="Mano"}
**✍️ A mano: el histograma.** Todos los intervalos miden 4, así que la altura de cada rectángulo puede ser directamente el %. Eje horizontal de 5 a 33 marcando 5, 9, 13… y vertical de 0 a 35 %. Rectángulos pegados.
:::

## Ejercicio 10. Sueldos de 15 trabajadores

::: {custom-style="Enunciado"}
Sueldo (miles €): 10, 12, 15, 20, 30 con 3, 5, 3, 3, 1 trabajadores. a) Media, mediana y moda. b) Una medida de dispersión absoluta y otra relativa. c) ¿Qué pasa si todos los sueldos suben un 5 %?
:::

**a)**

- Media: (10·3 + 12·5 + 15·3 + 20·3 + 30·1)/15 = (30 + 60 + 45 + 60 + 30)/15 = 225/15 = **15 mil €**.
- Mediana: n/2 = 7,5. Acumuladas: 3, 8, 11, 14, 15. Primera ≥ 7,5 es 8 (valor 12) → **Me = 12 mil €**.
- Moda: la mayor frecuencia (5) está en 12 → **Mo = 12 mil €**.

La media (15) es mayor que la mediana (12) porque el sueldo de 30 tira hacia arriba.

**b)** Absoluta: la **desviación típica**. Σxᵢ²nᵢ = 100·3 + 144·5 + 225·3 + 400·3 + 900·1 = 3795. S² = 3795/15 − 15² = 253 − 225 = 28 → S = **5,29 mil €**. Relativa: **CV** = 5,29/15 = **0,353** (35,3 %).

**c)** Subir un 5 % es multiplicar por 1,05:

| Medida | Antes | Después |
|:---|---:|---:|
| Media, mediana, moda | 15 · 12 · 12 | × 1,05 → 15,75 · 12,6 · 12,6 |
| Desviación típica | 5,29 | × 1,05 → 5,56 |
| Varianza | 28 | × 1,05² → 30,87 |
| CV | 0,353 | **No cambia** |

::: {custom-style="Excel"}
**🖥️ En Excel.** Valores en A2:A6 y nᵢ en B2:B6. Media (en E2): `=SUMAPRODUCTO(A2:A6;B2:B6)/SUMA(B2:B6)` → 15. Acumuladas en C: `=B2` y `=C2+B3` arrastrando, para buscar la mediana. Moda: `=INDICE(A2:A6;COINCIDIR(MAX(B2:B6);B2:B6;0))` → 12. Desviación típica: `=RAIZ(SUMAPRODUCTO(A2:A6^2;B2:B6)/SUMA(B2:B6)-E2^2)` → 5,29. CV: `=E3/E2` (con S en E3). Con la subida: `=1,05*E2`.
:::

## Ejercicio 11. Superficie de 200 apartamentos

::: {custom-style="Enunciado"}
Superficie (m²): 40–50, 50–60, 60–80, 80–100, 100–120 con 50, 40, 60, 40, 10 apartamentos. a) Si se alquilan a 10 €/m² de media, ¿alquiler medio? b) Tipo de apartamento más frecuente.
:::

**a)** Marcas: 45, 55, 70, 90, 110. Superficie media = (45·50 + 55·40 + 70·60 + 90·40 + 110·10)/200 = (2250 + 2200 + 4200 + 3600 + 1100)/200 = 13350/200 = **66,75 m²**.

El alquiler es 10 × superficie, así que (transformación lineal) el alquiler medio es 10 × 66,75 = **667,5 €**.

**b)** Las amplitudes son distintas (10, 10, 20, 20, 20) → hay que usar **densidades**.

| Intervalo | nᵢ | aᵢ | dᵢ |
|:---:|---:|---:|---:|
| 40–50 | 50 | 10 | **5** |
| 50–60 | 40 | 10 | 4 |
| 60–80 | 60 | 20 | 3 |
| 80–100 | 40 | 20 | 2 |
| 100–120 | 10 | 20 | 0,5 |

La mayor densidad es la del **primer intervalo** (40–50). No hay anterior → dᵢ₋₁ = 0.

$$Mo=40+\frac{5-0}{(5-0)+(5-4)}\cdot 10=40+\frac{5}{6}\cdot 10=48{,}33\ m^2$$

::: {custom-style="Resultado"}
**✅** El tipo más frecuente es el apartamento de **40 a 50 m²** (moda ≈ 48,3 m²).
:::

::: {custom-style="Ojo"}
**⚠️ Ojo.** Si miras solo las frecuencias, 60–80 tiene más pisos (60). Pero ese intervalo es el doble de ancho. Por cada m² de tramo, hay más pisos en 40–50. Por eso, con amplitudes distintas, **siempre densidades**.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Linf en A2:A6, Lsup en B2:B6, nᵢ en C2:C6. Marca en D2: `=(A2+B2)/2`. Media: `=SUMAPRODUCTO(D2:D6;C2:C6)/SUMA(C2:C6)` → 66,75; alquiler `=10*` esa celda. Densidad en E2: `=C2/(B2-A2)`. Moda (el modal es el primero, anterior = 0): `=A2+(E2-0)/((E2-0)+(E2-E3))*(B2-A2)` → 48,33.
:::

## Ejercicio 12. Puntuación para cada puesto

::: {custom-style="Enunciado"}
Puntuaciones 0–30, 30–50, 50–70, 70–90, 90–100 con 94, 140, 160, 98, 8 empleados. El 65 % con menos puntos serán administrativos, el siguiente 20 % jefes de sección, el siguiente 10 % jefes de departamento y el 5 % con más puntos, inspectores. ¿Puntos para ser jefe de sección? ¿Y para inspector?
:::

**Planteamiento.** Ordenamos de menos a más puntos. Para ser jefe de sección hay que superar al 65 % de abajo → necesitamos el **percentil 65**. Para ser inspector hay que estar en el 5 % de arriba → **percentil 95**.

n = 500. Acumuladas: 94, 234, 394, 492, 500.

**P₆₅:** 0,65 × 500 = 325. Primera Nᵢ ≥ 325 es 394 → intervalo 50–70 (nᵢ = 160, anterior 234, amplitud 20).

$$P_{65}=50+\frac{325-234}{160}\cdot 20=50+11{,}375=61{,}375$$

**P₉₅:** 0,95 × 500 = 475. Primera Nᵢ ≥ 475 es 492 → intervalo 70–90 (nᵢ = 98, anterior 394, amplitud 20).

$$P_{95}=70+\frac{475-394}{98}\cdot 20=70+16{,}53=86{,}53$$

::: {custom-style="Resultado"}
**✅** Para ser jefe de sección hacen falta unos **61,4 puntos**. Para ser inspector, unos **86,5 puntos**. (Para jefe de departamento, el P₈₅ = 76,3 puntos.)
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Tabla con Linf (A), Lsup (B), nᵢ (C), Nᵢ (D). Para P₆₅, con el intervalo en la fila 4: `=A4+(0,65*500-D3)/C4*(B4-A4)`. Una forma de encontrar la fila sin pensar: añade una columna `=D2>=0,65*500` y busca el primer VERDADERO.
:::

## Ejercicio 13. Viviendas en Pontevedra y Galicia

::: {custom-style="Enunciado"}
Pontevedra: 20–40, 40–60, 60–90, 90–120, 120–150, 150–300 m² con 4, 12, 51, 19, 10, 14 viviendas. a.1) Superficie media y más frecuente. a.2) Una medida de dispersión. a.3) ¿Entre qué valores está el 30 % central? b) Con A Coruña (203 viviendas, media 102,2, desv. 55,3), Lugo (46; 101,1; 48,2) y Ourense (41; 105,7; 51,0): media y varianza de toda Galicia.
:::

Tabla de trabajo (n = 110):

| Intervalo | xᵢ | nᵢ | aᵢ | dᵢ | Nᵢ | xᵢ·nᵢ | xᵢ²·nᵢ |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| 20–40 | 30 | 4 | 20 | 0,20 | 4 | 120 | 3600 |
| 40–60 | 50 | 12 | 20 | 0,60 | 16 | 600 | 30000 |
| 60–90 | 75 | 51 | 30 | **1,70** | 67 | 3825 | 286875 |
| 90–120 | 105 | 19 | 30 | 0,63 | 86 | 1995 | 209475 |
| 120–150 | 135 | 10 | 30 | 0,33 | 96 | 1350 | 182250 |
| 150–300 | 225 | 14 | 150 | 0,09 | 110 | 3150 | 708750 |
| **Total** | | **110** | | | | **11040** | **1420950** |

**a.1)** Media = 11040/110 = **100,36 m²**. Moda: intervalo modal 60–90 (mayor densidad, 1,70).

$$Mo=60+\frac{1{,}7-0{,}6}{(1{,}7-0{,}6)+(1{,}7-0{,}633)}\cdot 30=60+15{,}23=75{,}23\ m^2$$

**a.2)** Varianza = 1420950/110 − 100,36² = 12917,73 − 10072,86 = **2844,87** (en unidades al cuadrado). Desviación típica = √2844,87 = **53,34 m²**. CV = 53,34/100,36 = 0,53: dispersión relativa alta, sobre todo por las viviendas de 150 a 300 m².

**a.3)** El 30 % central deja un 35 % por debajo y un 35 % por encima: entre **P₃₅ y P₆₅**.

- P₃₅: 0,35 × 110 = 38,5 → intervalo 60–90 (anterior 16): 60 + (38,5 − 16)/51 × 30 = **73,24 m²**.
- P₆₅: 0,65 × 110 = 71,5 → intervalo 90–120 (anterior 67): 90 + (71,5 − 67)/19 × 30 = **97,11 m²**.

El 30 % central de las viviendas mide entre 73,2 y 97,1 m².

**b) Galicia entera** (varianza en subpoblaciones). Pasamos las desviaciones a varianzas (elevando al cuadrado).

| Provincia | T | Media | Varianza |
|:---|---:|---:|---:|
| Pontevedra | 110 | 100,36 | 2844,87 |
| A Coruña | 203 | 102,2 | 3058,09 |
| Lugo | 46 | 101,1 | 2323,24 |
| Ourense | 41 | 105,7 | 2601,00 |

1. Media global = (11040 + 20746,6 + 4650,6 + 4333,7)/400 = 40770,9/400 = **101,93 m²**.
2. Varianza dentro = (110·2844,87 + 203·3058,09 + 46·2323,24 + 41·2601)/400 = 1147237,8/400 = **2868,09**.
3. Varianza entre = (110·(100,36 − 101,93)² + 203·(102,2 − 101,93)² + 46·(101,1 − 101,93)² + 41·(105,7 − 101,93)²)/400 = 899,10/400 = **2,25**.
4. Varianza total = 2868,09 + 2,25 = **2870,34** → desviación típica = **53,58 m²**.

::: {custom-style="Resultado"}
**✅** En Galicia, superficie media 101,9 m² y varianza 2870,3. Casi toda la variabilidad es **dentro** de cada provincia: las cuatro provincias tienen medias muy parecidas.
:::

::: {custom-style="Ojo"}
**⚠️ Ojo.** El enunciado pone "desviación típica (s)". La tratamos como S (la de dividir entre n), igual que en los apuntes. Si fuera la cuasidesviación, el resultado cambiaría muy poco.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Tabla de Pontevedra con Linf (A), Lsup (B), nᵢ (C), marca (D), Nᵢ (E). Media (en H2): `=SUMAPRODUCTO(D2:D7;C2:C7)/SUMA(C2:C7)`. Varianza: `=SUMAPRODUCTO(D2:D7^2;C2:C7)/SUMA(C2:C7)-H2^2`. P₃₅ (intervalo en la fila 4): `=A4+(0,35*110-E3)/C4*(B4-A4)`.

Galicia: tamaños en K2:K5, medias en L2:L5, desviaciones en M2:M5. Varianzas en N2: `=M2^2`. Media global (en P2): `=SUMAPRODUCTO(K2:K5;L2:L5)/SUMA(K2:K5)`. Dentro: `=SUMAPRODUCTO(K2:K5;N2:N5)/SUMA(K2:K5)`. Entre: `=SUMAPRODUCTO(K2:K5;(L2:L5-P2)^2)/SUMA(K2:K5)`.
:::

## Ejercicio 14. Salarios por categoría

::: {custom-style="Enunciado"}
Técnicos: 30 empleados, media 30 mil €, desv. 7. Administrativos: 50, media 15, desv. 2,25. Operarios: 120, media 20, desv. 4,24. a) ¿Dónde hay más homogeneidad? b) Media y desviación típica de toda la empresa.
:::

**a)** Medias distintas → comparamos **CV**:

- Técnicos: 7/30 = 0,233 (23,3 %).
- Administrativos: 2,25/15 = **0,150** (15 %).
- Operarios: 4,24/20 = 0,212 (21,2 %).

El menor CV es el de **administrativos**: es la categoría con salarios más homogéneos.

**b)**

1. Media global = (30·30 + 15·50 + 20·120)/200 = (900 + 750 + 2400)/200 = 4050/200 = **20,25 mil €**.
2. Varianzas: 7² = 49; 2,25² = 5,0625; 4,24² = 17,98.
3. Dentro = (49·30 + 5,0625·50 + 17,98·120)/200 = 3880,44/200 = **19,40**.
4. Entre = ((30 − 20,25)²·30 + (15 − 20,25)²·50 + (20 − 20,25)²·120)/200 = (2851,88 + 1378,13 + 7,5)/200 = **21,19**.
5. Total = 19,40 + 21,19 = 40,59 → desviación típica = √40,59 = **6,37 mil €**.

Más de la mitad de la variabilidad (21,19/40,59 = 52 %) se debe a las diferencias **entre** categorías.

::: {custom-style="Excel"}
**🖥️ En Excel.** Tamaños en B2:B4, medias en C2:C4, desviaciones en D2:D4. CV en E2: `=D2/C2` y arrastra. Media global (en G2): `=SUMAPRODUCTO(B2:B4;C2:C4)/SUMA(B2:B4)` → 20,25. Dentro: `=SUMAPRODUCTO(B2:B4;D2:D4^2)/SUMA(B2:B4)` → 19,40. Entre: `=SUMAPRODUCTO(B2:B4;(C2:C4-G2)^2)/SUMA(B2:B4)` → 21,19. Desviación total: `=RAIZ(dentro+entre)`.
:::

## Ejercicio 15. Hogares: personas y superficie

::: {custom-style="Enunciado"}
Tabla de 1000 hogares: X = nº de personas (1, 2, 3, 4, 5 o más), Y = superficie (0–60, 60–90, 90–120, 120–200). a) Superficie más frecuente. b) Número mediano de integrantes. c) Varianza de la superficie de las viviendas con más de 4 personas.
:::

| X \\ Y | 0–60 | 60–90 | 90–120 | 120–200 | Total |
|:---|---:|---:|---:|---:|---:|
| 1 | 43 | 60 | 23 | 11 | 137 |
| 2 | 39 | 114 | 46 | 23 | 222 |
| 3 | 36 | 106 | 45 | 20 | 207 |
| 4 | 30 | 118 | 58 | 28 | 234 |
| 5 o más | 23 | 92 | 53 | 32 | 200 |
| **Total** | **171** | **490** | **225** | **114** | **1000** |

**a)** Marginal de Y (fila de totales). Amplitudes 60, 30, 30, 80 → densidades: 171/60 = 2,85 · 490/30 = **16,33** · 225/30 = 7,5 · 114/80 = 1,43. Intervalo modal: 60–90.

$$Mo=60+\frac{16{,}33-2{,}85}{(16{,}33-2{,}85)+(16{,}33-7{,}5)}\cdot 30=78{,}13\ m^2$$

**b)** Marginal de X (columna de totales). n/2 = 500. Acumuladas: 137, 359, 566... Primera ≥ 500: 566 → **Me = 3 personas**.

**c)** "Más de 4 personas" = la fila "5 o más" (distribución condicionada Y | X ≥ 5). n = 200. Marcas: 30, 75, 105, 160.

- Media = (30·23 + 75·92 + 105·53 + 160·32)/200 = (690 + 6900 + 5565 + 5120)/200 = 18275/200 = **91,38 m²**.
- Σxᵢ²nᵢ = 900·23 + 5625·92 + 11025·53 + 25600·32 = 20700 + 517500 + 584325 + 819200 = 1941725.
- Varianza = 1941725/200 − 91,375² = 9708,63 − 8349,39 = **1359,23**. Desviación típica = 36,87 m².

::: {custom-style="Excel"}
**🖥️ En Excel.** Tabla en B2:E6 (filas = personas, columnas = superficie), totales de columna en B7:E7 y de fila en F2:F6. Densidades de Y: `=B7/60`, `=C7/30`… Mediana de X: acumuladas de F2:F6. Condicionada «5 o más» (fila 6) con marcas en B9:E9: media `=SUMAPRODUCTO(B9:E9;B6:E6)/F6` → 91,38; varianza `=SUMAPRODUCTO(B9:E9^2;B6:E6)/F6-` media al cuadrado → 1359,23.
:::

## Ejercicio 16. Ingresos y gasto en streaming

::: {custom-style="Enunciado"}
100 familias. X = ingresos (cientos €): 6–10, 10–15, 15–20, 20–30, 30–50. Y = gasto en streaming (€): 0–12, 12–48, 48–120, 120–480. a) Ingreso medio. b) Varianzas de X e Y. c) ¿Son independientes? d) Valores que delimitan el gasto del 50 % central de las familias con ingresos que no superan 2000 €.
:::

| X \\ Y | 0–12 | 12–48 | 48–120 | 120–480 | Total |
|:---|---:|---:|---:|---:|---:|
| 6–10 | 4 | 1 | 1 | 0 | 6 |
| 10–15 | 9 | 8 | 3 | 0 | 20 |
| 15–20 | 9 | 12 | 20 | 3 | 44 |
| 20–30 | 5 | 8 | 12 | 3 | 28 |
| 30–50 | 1 | 1 | 0 | 0 | 2 |
| **Total** | **28** | **30** | **36** | **6** | **100** |

**a)** Marcas de X: 8; 12,5; 17,5; 25; 40. x̄ = (8·6 + 12,5·20 + 17,5·44 + 25·28 + 40·2)/100 = 1848/100 = **18,48 cientos de € = 1848 €**.

**b)**

- S²ₓ = (64·6 + 156,25·20 + 306,25·44 + 625·28 + 1600·2)/100 − 18,48² = 376,84 − 341,51 = **35,33** (cientos de €)².
- Marcas de Y: 6, 30, 84, 300. ȳ = (6·28 + 30·30 + 84·36 + 300·6)/100 = 5892/100 = 58,92 €. S²ᵧ = (36·28 + 900·30 + 7056·36 + 90000·6)/100 − 58,92² = 8220,24 − 3471,57 = **4748,67** €².

**c)** Basta una casilla. Fila 6–10, columna 0–12: f₁₁ = 4/100 = 0,04. Producto de marginales: (6/100)·(28/100) = 0,0168. Como 0,04 ≠ 0,0168 → **no son independientes**. Además hay casillas con 0 (por ejemplo, 30–50 y 48–120) cuyos totales no son 0. El gasto en streaming depende de los ingresos.

**d)** "No superan 2000 €" = X ≤ 20 cientos → las tres primeras filas. Sumamos esas filas (distribución condicionada):

| Y \| X ≤ 20 | nⱼ | Nⱼ |
|:---:|---:|---:|
| 0–12 | 4+9+9 = 22 | 22 |
| 12–48 | 1+8+12 = 21 | 43 |
| 48–120 | 1+3+20 = 24 | 67 |
| 120–480 | 0+0+3 = 3 | 70 |

El 50 % central está entre **C₁ y C₃**. n = 70.

- C₁: 70/4 = 17,5 → intervalo 0–12: 0 + 17,5/22 × 12 = **9,55 €**.
- C₃: 3·70/4 = 52,5 → intervalo 48–120 (anterior 43): 48 + (52,5 − 43)/24 × 72 = 48 + 28,5 = **76,50 €**.

::: {custom-style="Resultado"}
**✅** El 50 % central de las familias con ingresos de hasta 2000 € gasta entre 9,55 y 76,50 € al mes en plataformas.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Tabla en B2:E6, totales de fila en F2:F6, de columna en B7:E7, n en F7. Marcas de X en A2:A6 y de Y en B9:E9. x̄: `=SUMAPRODUCTO(A2:A6;F2:F6)/F7`. ȳ: `=SUMAPRODUCTO(B9:E9;B7:E7)/F7`. Varianzas igual con `^2` y restando la media al cuadrado. Independencia, casilla 1: `=B2/F7` frente a `=(F2/F7)*(B7/F7)`. d) Suma las tres primeras filas con `=SUMA(B2:B4)` en cada columna y aplica la fórmula de los cuartiles con celdas.
:::

## Ejercicio 17. Gasto de turistas en Galicia

::: {custom-style="Enunciado"}
150 turistas. X = provincia; Y = gasto diario (€): 0–60, 60–90, 90–120, 120–180, 180–300. A Coruña: 5, 8, 10, 30, 10. Lugo: 1, 2, 6, 5, 2. Ourense: 1, 1, 4, 2, 1. Pontevedra: 8, 10, 28, 12, 4.
:::

Marcas de Y: 30, 75, 105, 150, 240.

**a) A Coruña vs Pontevedra.**

- A Coruña (n = 63): (30·5 + 75·8 + 105·10 + 150·30 + 240·10)/63 = 8700/63 = **138,10 €/día**.
- Pontevedra (n = 62): (30·8 + 75·10 + 105·28 + 150·12 + 240·4)/62 = 6690/62 = **107,90 €/día**.

En A Coruña los turistas gastan de media unos 30 € más al día que en Pontevedra.

**b) Galicia (marginal de Y):** 15, 21, 48, 49, 17; n = 150. Acumuladas: 15, 36, 84, 133, 150.

- Mediana: 75 → intervalo 90–120 (anterior 36): 90 + (75 − 36)/48 × 30 = **114,38 €**.
- Moda: densidades 15/60 = 0,25 · 21/30 = 0,70 · 48/30 = **1,60** · 49/60 = 0,82 · 17/120 = 0,14. Modal 90–120:

$$Mo=90+\frac{1{,}6-0{,}7}{(1{,}6-0{,}7)+(1{,}6-0{,}817)}\cdot 30=106{,}04\ \text{€}$$

::: {custom-style="Ojo"}
**⚠️ Ojo.** 120–180 tiene más turistas (49) que 90–120 (48), pero es el doble de ancho. Con densidades gana 90–120.
:::

**c) Para estar en el 25 % que más gasta en Pontevedra** → P₇₅ de Pontevedra. 0,75 × 62 = 46,5. Acumuladas: 8, 18, 46, 58, 62. Primera ≥ 46,5: 58 → intervalo 120–180 (anterior 46, nᵢ = 12): 120 + (46,5 − 46)/12 × 60 = **122,5 €**.

**d) Norte (A Coruña + Lugo) vs sur (Ourense + Pontevedra).** Sumamos filas.

| Grupo | Frecuencias | n | Media | S | CV |
|:---|:---|---:|---:|---:|---:|
| Norte | 6, 10, 16, 35, 12 | 79 | 135,95 | 57,00 | 0,419 |
| Sur | 9, 11, 32, 14, 5 | 71 | 109,23 | 50,17 | 0,459 |

::: {custom-style="Resultado"}
**✅** En términos **absolutos** (desviación típica) la dispersión es mayor en el norte (57,0 frente a 50,2). Pero las medias son distintas, así que lo correcto es comparar el **CV**: el sur tiene más dispersión **relativa** (0,459 frente a 0,419). Respuesta: **no**, relativamente el gasto es más disperso en el sur.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Frecuencias de cada provincia en B2:F5 (una fila por provincia) y marcas en B1:F1. Media de A Coruña: `=SUMAPRODUCTO($B$1:$F$1;B2:F2)/SUMA(B2:F2)` y arrastra hacia abajo para las demás. Galicia: fila de totales con `=SUMA(B2:B5)`. Norte: `=B2+B3` en cada columna; sur: `=B4+B5`. Desviación típica de una fila: `=RAIZ(SUMAPRODUCTO($B$1:$F$1^2;B7:F7)/SUMA(B7:F7)-H7^2)`, con su media en H7.
:::

## Ejercicio 18. Cinturón de seguridad y gravedad de las heridas

::: {custom-style="Enunciado"}
| X \\ Y | Con cinturón | Sin cinturón |
|:---|---:|---:|
| Grave | 5244 | 2730 |
| Leve | 24351 | 6412 |
:::

n = 5244 + 2730 + 24351 + 6412 = **38737**.

**a) Frecuencias relativas** (cada casilla ÷ 38737):

| X \\ Y | Con cinturón | Sin cinturón | Total |
|:---|---:|---:|---:|
| Grave | 0,1354 | 0,0705 | 0,2059 |
| Leve | 0,6286 | 0,1655 | 0,7941 |
| Total | 0,7640 | 0,2360 | 1 |

**b) Marginales.** X (gravedad): grave 7974 (20,6 %), leve 30763 (79,4 %). Y (cinturón): con 29595 (76,4 %), sin 9142 (23,6 %).

**c) Condicionadas.**

- X | Y = Con cinturón (columna "con", ÷ 29595): grave 5244/29595 = **17,7 %**, leve 24351/29595 = **82,3 %**.
- Y | X = Leve (fila "leve", ÷ 30763): con cinturón 24351/30763 = **79,2 %**, sin cinturón 6412/30763 = **20,8 %**.

**d) ¿Independientes?** f₁₁ = 0,1354. f₁. · f.₁ = 0,2059 × 0,7640 = 0,1573. Son distintos → **no son independientes**.

::: {custom-style="Resultado"}
**✅** Interpretación: entre los que **no** llevaban cinturón, el 29,9 % (2730/9142) tuvo heridas graves; entre los que **sí** lo llevaban, solo el 17,7 %. La gravedad depende del uso del cinturón.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Tabla en B2:C3, totales de fila en D2:D3, de columna en B4:C4 y n en D4. Relativas: `=B2/$D$4` y arrastra. Condicionada por columna (X | Y): `=B2/B$4`. Por fila (Y | X): `=B2/$D2`. Si fueran independientes: `=$D2*B$4/$D$4` y compara con B2.
:::

## Ejercicio 19. Diagrama de caja: satisfacción laboral por sector

::: {custom-style="Enunciado"}
Comenta e interpreta el diagrama de caja de la satisfacción laboral (0 a 10) en tres sectores: Educación, Sanidad y Servicios Sociales (está en el boletín de la profesora).
:::

El gráfico muestra la satisfacción (0 a 10) en Educación, Sanidad y Servicios Sociales.

- **Nivel (medianas).** Educación es el sector más satisfecho (mediana ≈ 7,2), después Sanidad (≈ 5,9) y por último Servicios Sociales (≈ 4,9).
- **Dispersión.** Educación tiene la caja más estrecha (≈ 6,6 a 7,6): opiniones muy parecidas entre sí. Servicios Sociales tiene la caja más ancha (≈ 3,6 a 6,1) y los bigotes más largos (de ≈ 1,3 a ≈ 9,7): opiniones muy variadas. Sanidad queda en medio.
- **Atípicos.** Solo en Educación: un trabajador con satisfacción muy alta (≈ 9,2) y otro muy baja (≈ 4,7), que se salen de lo habitual en su sector.
- **Forma.** En Sanidad la mediana está más cerca de la parte baja de la caja y el bigote superior es más largo: ligera asimetría positiva (algunos muy satisfechos).

*Conclusión:* la satisfacción es más alta y más homogénea en Educación, y más baja y más heterogénea en Servicios Sociales.

## Ejercicio 20. Encuesta de Presupuestos Familiares (EPF)

::: {custom-style="Enunciado"}
Resumen de estadísticos (51 provincias) de alimentación, vivienda y sanidad, con tres histogramas, un diagrama de caja y un gráfico radial de Almería y Barcelona. a) Interpreta los resultados. b) ¿Qué gráficos se han hecho y a qué variable corresponde cada uno? c) Con un máximo de 12000 en el radial, identifica Almería y Barcelona y dibuja aproximadamente el radial de Pontevedra.
:::

**a) Interpretación** (51 provincias, gasto en euros):

| | Alimentación | Vivienda | Sanidad |
|:---|---:|---:|---:|
| Media | 9532 | 7933 | 874 |
| Mediana | 9499 | 7737 | 868 |
| sd | 1047 | 1705 | 265 |
| CV (sd/media) | 0,11 | 0,21 | 0,30 |
| Asimetría | −0,05 | 0,98 | 0,58 |
| Curtosis | −0,33 | 1,49 | 0,05 |
| Mín – Máx | 6830 – 11685 | 5278 – 13718 | 388 – 1549 |
| C₁ – C₃ | 8681 – 10253 | 6627 – 8783 | 676 – 1001 |

- **Alimentación** es el gasto mayor. Media y mediana casi iguales y asimetría ≈ 0: **simétrica**. Curtosis algo negativa: un poco **platicúrtica**. Es la de menor dispersión relativa (CV = 11 %).
- **Vivienda**: la media supera a la mediana y la asimetría es claramente **positiva** (0,98): hay provincias con gasto muy alto (Madrid, 13718 €) que estiran la cola a la derecha. Curtosis positiva: **leptocúrtica**.
- **Sanidad** es el gasto menor, con ligera asimetría positiva y curtosis ≈ 0 (mesocúrtica). Es la de **mayor dispersión relativa** (CV = 30 %).

**b) Gráficos.** Tres **histogramas** y un **diagrama de caja** con tres cajas, y un **gráfico radial**.

- Histograma azul (eje de 6000 a 14000, con una barra aislada a la derecha) → **Vivienda**.
- Histograma rojo (de 7000 a 11000, bastante simétrico) → **Alimentación**.
- Histograma verde (de 200 a 1600) → **Sanidad**.
- Cajas: la 1 (roja) es **Alimentación**, la 2 (verde, muy abajo) **Sanidad** y la 3 (azul, con un punto atípico arriba) **Vivienda**. El atípico es Madrid: el límite superior es 8782,64 + 1,5 × 2155,26 = 12015,5 y Madrid gasta 13717,62. En Sanidad también hay un atípico arriba (Barcelona, 1548,51 > 1488,3).

**c) Gráfico radial.** El borde exterior vale 12000. Almería gasta 9820,82 en alimentación → 9820,82/12000 = 82 % del radio. Barcelona gasta 11153,03 → 93 %. En el dibujo, la línea **continua** llega más lejos en Alimentación y en Vivienda (Barcelona: 11143 frente a 8284 de Almería) → la línea continua es **Barcelona** y la discontinua es **Almería**.

Pontevedra: cada valor ÷ 12000 da qué parte del radio ocupa: Alimentación 97 %, Vivienda 62 %, Transporte 46 %, Vestido 35 %, Mobiliario 18 %, Educación 17 %, Sanidad 7 %.

![](img/b20_radial_pontevedra.png){width=55%}

::: {custom-style="Excel"}
**🖥️ En Excel.** Con los datos de la EPF (hoja de clase): `=PROMEDIO(B2:B52)`, `=MEDIANA(B2:B52)`, `=DESVEST.S(B2:B52)` (la "sd" de R), `=CUARTIL.INC(B2:B52;1)`, `=COEFICIENTE.ASIMETRIA.P(B2:B52)` y `=CURTOSIS(B2:B52)`. Estas dos pueden diferir un poco en los decimales de las de los apuntes (cada programa usa una pequeña corrección distinta), pero el signo y la interpretación son los mismos. Radial: selecciona los nombres de las partidas y la fila de Pontevedra → Insertar → Radial. Para fijar el máximo en 12000: clic derecho en el eje → Dar formato al eje → Máximo = 12000.
:::

::: {custom-style="Mano"}
**✍️ A mano: el gráfico radial.** Dibuja un radio por partida, todos de la misma longitud (el borde = 12000). Sobre cada radio marca el punto a la fracción que toca (Alimentación al 97 %, Vivienda al 62 %…). Une los puntos en orden. Para Almería y Barcelona, compara solo qué línea llega más lejos en cada radio.
:::

## Ejercicio 21. Desigualdad salarial por sexo

::: {custom-style="Enunciado"}
Mujeres: n = 5, salario medio 2240 €, varianza 34400. Hombres: n = 5, media 2860, varianza 46400.
:::

**a) Variabilidad absoluta:** varianza mayor en **hombres** (46400 > 34400).

**b) Variabilidad relativa (CV):** mujeres √34400/2240 = 185,47/2240 = **0,0828**; hombres √46400/2860 = 215,41/2860 = **0,0753**. Hay más variabilidad relativa en **mujeres**.

**c) Media global:** (2240·5 + 2860·5)/10 = **2550 €**.

**d) Dentro de los grupos:** (34400·5 + 46400·5)/10 = **40400 €²**.

**e) Entre los grupos:** ((2240 − 2550)²·5 + (2860 − 2550)²·5)/10 = (96100·5 + 96100·5)/10 = **96100 €²**.

**f) Total:** 40400 + 96100 = **136500 €²**.

**g) % debido a las diferencias entre grupos:** 96100/136500 × 100 = **70,4 %**.

::: {custom-style="Resultado"}
**✅** El 70 % de la variabilidad de los salarios se explica por ser hombre o mujer. Es una medida de **desigualdad salarial** muy alta.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Tamaños en B2:B3, medias en C2:C3, varianzas en D2:D3. CV en E2: `=RAIZ(D2)/C2`. Media global (en G2): `=SUMAPRODUCTO(B2:B3;C2:C3)/SUMA(B2:B3)` → 2550. Dentro: `=SUMAPRODUCTO(B2:B3;D2:D3)/SUMA(B2:B3)` → 40400. Entre: `=SUMAPRODUCTO(B2:B3;(C2:C3-G2)^2)/SUMA(B2:B3)` → 96100. % entre: `=entre/(dentro+entre)`.
:::

## Ejercicio 22. Cuatro propuestas de subida salarial

::: {custom-style="Enunciado"}
Salario medio 2025: 2550 €, varianza 136500 €². I: +50 € a todos. II: +2 %. III: −1 %. IV: +25 € y +1 %.
:::

Aplicamos x̄ nueva = a·x̄ + b y S² nueva = a²·S².

| Propuesta | Transformación | Media | Varianza | Desv. típica |
|:---|:---|---:|---:|---:|
| Actual | — | 2550 | 136500 | 369,46 |
| I | X + 50 | 2600 | 136500 | 369,46 |
| II | 1,02·X | 2601 | 142014,6 | 376,85 |
| III | 0,99·X | 2524,5 | 133783,65 | 365,77 |
| IV | 1,01·X + 25 | 2600,5 | 139243,65 | 373,15 |

*Interpretación:*

- **I:** todos ganan 50 € más. La media sube 50 € y la dispersión no cambia: las diferencias entre trabajadores en euros siguen siendo las mismas.
- **II:** la media sube 51 € (casi igual que en I), pero ahora las diferencias aumentan: quien más cobra, más sube en euros.
- **III:** bajada. La media cae 25,5 € y la dispersión se reduce un poco.
- **IV:** la media sube 50,5 € y la dispersión aumenta algo (solo por la parte del 1 %).

Para no aumentar las diferencias salariales, la mejor es la **I** (suma fija).

::: {custom-style="Ojo"}
**⚠️ Ojo con la propuesta IV.** Se ha aplicado como en el Excel de clase: subida del 1 % sobre el salario y luego +25 € (Y = 1,01·X + 25). Si primero se suman 25 € y luego se sube el 1 % del total, Y = 1,01·(X + 25) y la media sería 2600,75 €. La varianza es la misma en los dos casos. Si en el examen el orden no está claro, escribe cuál has usado.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Pon a (el multiplicador) en B y b (lo que se suma) en C para cada propuesta: I → 1 y 50; II → 1,02 y 0; III → 0,99 y 0; IV → 1,01 y 25. Media en D2: `=B2*2550+C2`. Varianza en E2: `=B2^2*136500`. Desviación en F2: `=RAIZ(E2)`. Arrastra.
:::
