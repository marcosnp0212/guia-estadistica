# Tema 3. Regresión y correlación

::: {.video data-v="t3"}
:::

::: {custom-style="Idea"}
**🧠 La idea del tema.** Tenemos **dos variables numéricas** de cada persona (antigüedad y salario, por ejemplo). Queremos saber: ¿cuando una sube, la otra también sube? ¿Cuánto? ¿Puedo **predecir** el salario de alguien sabiendo su antigüedad? La herramienta es una **recta** que se ajusta lo mejor posible a los puntos.
:::

Ejemplo que usaremos todo el tema (hoja de clase *Antig_Salario*): 10 trabajadores.

| Antigüedad (X, años) | 1 | 2 | 3 | 5 | 6 | 7 | 9 | 10 | 12 | 15 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Salario (Y, €)** | 1400 | 1600 | 1700 | 1700 | 1800 | 1850 | 2200 | 2400 | 2250 | 2500 |

## 3.1. La nube de puntos (diagrama de dispersión)

Cada trabajador es un punto: su antigüedad en el eje horizontal y su salario en el vertical. La forma de la nube dice qué relación hay.

![Tipos de relación](img/t3_tipos.png){width=100%}

- **Relación directa (positiva):** la nube sube hacia la derecha. Cuando X aumenta, Y tiende a aumentar. (Más antigüedad, más salario.)
- **Relación inversa (negativa):** la nube baja. Cuando X aumenta, Y tiende a bajar. (Más absentismo, menos productividad.)
- **Sin relación lineal:** nube sin dirección. (Talla de zapato y satisfacción laboral.)
- **Relación no lineal:** los puntos siguen una curva. Puede haber relación fuerte aunque no sea una recta.

Cuanto más **estrecha y alargada** es la nube, más fuerte es la relación.

::: {custom-style="Excel"}
**🖥️ En Excel: nube de puntos con recta.**

1. Selecciona las dos columnas (X a la izquierda, Y a la derecha).
2. **Insertar** → **Dispersión** (el icono de puntos sueltos).
3. Clic derecho sobre un punto → **Agregar línea de tendencia** → **Lineal**.
4. En el panel de la derecha marca **Presentar ecuación en el gráfico** y **Presentar el valor R cuadrado en el gráfico**.

Excel te escribe la recta (y = 78,533x + 1390,3) y el R² (0,9159) encima del gráfico. Es una forma estupenda de **comprobar** tus cálculos.
:::

::: {custom-style="Mano"}
**✍️ A mano: la nube de puntos en papel.**

1. Eje horizontal para X y vertical para Y, cada uno con su escala. No hace falta que empiecen en 0: para los salarios, el eje vertical puede ir de 1300 a 2600 (marca el corte con una pequeña rayita en zigzag).
2. Pon un punto por cada pareja (x, y). Por ejemplo (1, 1400), (2, 1600)…
3. Mira la forma: si sube hacia la derecha, relación directa; si baja, inversa.
4. Si te piden la recta, calcula dos puntos con la ecuación (por ejemplo, X = 0 y X = 15) y únelos con la regla. Comprueba que pasa por (x̄, ȳ).
:::


## 3.2. La covarianza

**Qué es.** Un número que dice si las dos variables se mueven **en el mismo sentido** o en sentido contrario.

$$S_{XY}=\frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{n}=\frac{\sum x_i y_i}{n}-\bar{x}\cdot\bar{y}$$

| Signo | Significa |
|:---:|:---|
| S_XY > 0 | Relación **directa** |
| S_XY < 0 | Relación **inversa** |
| S_XY = 0 | Sin relación **lineal** |

::: {custom-style="Truco"}
**💡 Por qué funciona.** Si un trabajador tiene antigüedad **por encima** de la media y salario **por encima** de la media, el producto (x − x̄)(y − ȳ) es (+)·(+) = +. Si los dos están por debajo, (−)·(−) = +. Si uno está arriba y otro abajo, sale −. Cuando la mayoría de productos son positivos, la covarianza es positiva: van juntas.
:::

::: {custom-style="Ojo"}
**⚠️ Ojo.** El **valor** de la covarianza no dice si la relación es fuerte o débil, porque depende de las unidades (no es lo mismo medir en euros que en céntimos). Solo mira el **signo**. Para la fuerza está el coeficiente de correlación.
:::

Curiosidad útil: la covarianza de una variable consigo misma es su varianza: Cov(X, X) = Var(X).

::: {custom-style="Otra"}
Dibuja una cruz en la nube de puntos justo en las medias (x̄, ȳ). La nube queda dividida en cuatro zonas.

Los puntos de **arriba a la derecha** y **abajo a la izquierda** suman a favor de una relación directa; los de arriba a la izquierda y abajo a la derecha, en contra. Si ganan los primeros, la covarianza es positiva: las dos variables suben juntas.
:::

**Receta (datos sueltos):**

1. Calcula x̄ e ȳ.
2. Añade una columna con xᵢ · yᵢ.
3. Suma esa columna y divide entre n.
4. Resta x̄ · ȳ.

**Ejemplo: antigüedad y salario.** x̄ = 70/10 = 7. ȳ = 19400/10 = 1940. Σxᵢyᵢ = 1·1400 + 2·1600 + ... + 15·2500 = 150250.

S_XY = 150250/10 − 7 × 1940 = 15025 − 13580 = **1445** → positiva → relación directa.

**Con tabla de frecuencias** (cada pareja aparece nᵢⱼ veces) se multiplica también por nᵢⱼ:

$$S_{XY}=\frac{\sum x_i y_j n_{ij}}{n}-\bar{x}\cdot\bar{y}$$

Ejemplo de los apuntes (la tabla de ausencias y asuntos propios del Tema 2): x̄ = 82/32 = 2,5625, ȳ = 111/32 = 3,46875, Σxᵢyⱼnᵢⱼ = 284. S_XY = 284/32 − 2,5625 × 3,46875 = 8,875 − 8,889 = **−0,014**. Negativa pero casi 0: prácticamente no hay relación lineal.

::: {custom-style="Excel"}
**🖥️ En Excel.** X en A2:A11, Y en B2:B11: `=COVARIANZA.P(A2:A11;B2:B11)` → 1445. (**COVARIANZA.P** divide entre n, como en clase. COVARIANZA.M divide entre n − 1; no la uses salvo que te lo pidan.)

A mano en Excel: columna C con `=A2*B2` arrastrada, y luego `=SUMA(C2:C11)/10-PROMEDIO(A2:A11)*PROMEDIO(B2:B11)`.
:::

::: {custom-style="Mano"}
**✍️ A mano: la tabla que lo resuelve todo.** En papel, haz **una sola tabla** con cinco columnas. Con sus sumas sacas la covarianza, las dos rectas, r y R² sin volver a tocar los datos.

| xᵢ | yᵢ | xᵢ² | yᵢ² | xᵢ·yᵢ |
|---:|---:|---:|---:|---:|
| 1 | 1400 | 1 | 1 960 000 | 1 400 |
| 2 | 1600 | 4 | 2 560 000 | 3 200 |
| 3 | 1700 | 9 | 2 890 000 | 5 100 |
| 5 | 1700 | 25 | 2 890 000 | 8 500 |
| 6 | 1800 | 36 | 3 240 000 | 10 800 |
| 7 | 1850 | 49 | 3 422 500 | 12 950 |
| 9 | 2200 | 81 | 4 840 000 | 19 800 |
| 10 | 2400 | 100 | 5 760 000 | 24 000 |
| 12 | 2250 | 144 | 5 062 500 | 27 000 |
| 15 | 2500 | 225 | 6 250 000 | 37 500 |
| **Σ = 70** | **19 400** | **674** | **38 875 000** | **150 250** |

Con las sumas (n = 10):

1. x̄ = 70/10 = **7** · ȳ = 19 400/10 = **1940**.
2. S²ₓ = 674/10 − 7² = 67,4 − 49 = **18,4**.
3. S²ᵧ = 38 875 000/10 − 1940² = 3 887 500 − 3 763 600 = **123 900**.
4. S_XY = 150 250/10 − 7·1940 = 15 025 − 13 580 = **1445**.
5. b = 1445/18,4 = **78,53** · a = 1940 − 78,53·7 = **1390,27**.
6. r = 1445/(√18,4 · √123 900) = 1445/(4,290 · 352,0) = **0,957** · R² = **0,916**.

**Para no equivocarte:** escribe las fórmulas en la hoja antes de poner números, y apunta cada resultado intermedio. Si un paso sale mal, solo repites ese.

**Comprobación con la calculadora:** en el modo estadístico de **2 variables** (A+BX, o "lineal"), metes las parejas y te da A (= a), B (= b) y r. Ojo: en la calculadora la pendiente es **B** y el término independiente **A**, igual que en la guía.
:::


## 3.3. La recta de regresión

**Qué es.** La recta que mejor se ajusta a la nube de puntos. Sirve para **explicar** y **predecir** una variable a partir de la otra.

### Recta de Y sobre X (la que casi siempre te pedirán)

Se usa para **predecir Y sabiendo X**. Y es la variable que queremos explicar (**respuesta** o dependiente). X es la que usamos para explicarla (**explicativa** o independiente).

$$\hat{Y}=a+b\cdot X$$

$$b=\frac{S_{XY}}{S_X^2} \qquad a=\bar{y}-b\cdot\bar{x}$$

- **b es la pendiente:** cuánto cambia Y, de media, cuando X aumenta **1 unidad**. Tiene el mismo signo que la covarianza.
- **a es el término independiente** (u ordenada en el origen): el valor de Y cuando X = 0. A veces no tiene sentido práctico (por ejemplo, si nadie tiene X = 0).
- El "sombrero" de Ŷ indica que es una **predicción** (un valor medio estimado), no un dato real.

**Receta:**

1. Calcula x̄, ȳ, S²ₓ y S_XY.
2. b = S_XY / S²ₓ.
3. a = ȳ − b · x̄.
4. Escribe la recta Ŷ = a + b·X.
5. Interpreta b con una frase.

**Ejemplo: antigüedad y salario.** S²ₓ = Σxᵢ²/n − x̄² = 674/10 − 49 = 18,4.

- b = 1445 / 18,4 = **78,53**.
- a = 1940 − 78,53 × 7 = **1390,27**.

::: {custom-style="Resultado"}
**✅** Salario estimado = 1390,27 + 78,53 · Antigüedad. **Interpretación de b:** por cada año más de antigüedad, el salario aumenta de media 78,53 €. **Interpretación de a:** un trabajador recién llegado (0 años) cobraría unos 1390 €.
:::

![Nube de puntos, recta y predicción](img/t3_antig.png){width=85%}

::: {custom-style="Otra"}
La recta es una **regla para adivinar Y cuando sabes X**.

- **b** es lo que sube Y por cada paso de X: 78,53 € por cada año de antigüedad.
- **a** es el punto de partida: lo que tendría alguien con 0 años.

Para predecir: punto de partida + paso × número de pasos. Con 11 años: 1390,27 + 78,53 × 11.
:::

### Recta de X sobre Y

Si lo que queremos es predecir **X** a partir de **Y**, la recta es otra:

$$\hat{X}=a'+b'\cdot Y \qquad b'=\frac{S_{XY}}{S_Y^2} \qquad a'=\bar{x}-b'\cdot\bar{y}$$

Fíjate que ahora se divide entre la varianza de **Y**. Las dos rectas son distintas (salvo que la relación sea perfecta), pero **las dos pasan por el punto de medias (x̄, ȳ)**: ahí se cortan siempre.

### Caso especial: covarianza 0

Si S_XY = 0, las dos pendientes valen 0:

- **Y sobre X:** b = 0, así que **Ŷ = ȳ**. Es una recta **horizontal**: sepas lo que sepas de X, predices siempre la media de Y.
- **X sobre Y:** b' = 0, así que **X̂ = x̄**. Dibujada en los mismos ejes, es una recta **vertical**.

Las dos se cortan en ángulo recto en (x̄, ȳ). Es la señal de que **no hay relación lineal**: r = 0 y R² = 0.

**Ejemplo de los apuntes:** puntos (−2, 0), (−1, 0), (0, 1), (1, 1), (2, 3). x̄ = 0, ȳ = 1, S²ₓ = 2, S²ᵧ = 6/5 = 1,2, S_XY = 7/5 = 1,4.

- Y sobre X: b = 1,4/2 = 0,7; a = 1 − 0,7·0 = 1 → **Ŷ = 1 + 0,7X**.
- X sobre Y: b' = 1,4/1,2 = 7/6 = 1,167; a' = 0 − 1,167·1 = −1,167 → **X̂ = −1,167 + 1,167Y**.

::: {custom-style="Excel"}
**🖥️ En Excel.**

- Pendiente de Y sobre X: `=PENDIENTE(B2:B11;A2:A11)` → 78,53.
- Término independiente: `=INTERSECCION.EJE(B2:B11;A2:A11)` → 1390,27.

**Muy importante: primero va la Y y después la X.** Si las pones al revés, obtienes la recta de X sobre Y. Para la recta de X sobre Y, precisamente, invierte el orden: `=PENDIENTE(A2:A11;B2:B11)`.

Con fórmulas: `=COVARIANZA.P(A2:A11;B2:B11)/VAR.P(A2:A11)` da la misma pendiente.
:::

## 3.4. Coeficiente de correlación (r) y de determinación (R²)

### Correlación lineal de Pearson (r)

**Qué es.** Mide la **fuerza** y el **sentido** de la relación lineal. No tiene unidades y siempre está entre −1 y 1.

$$r=\frac{S_{XY}}{S_X\cdot S_Y}$$

| Valor de r | Significa |
|:---|:---|
| r = 1 | Relación lineal **perfecta y directa** (todos los puntos sobre una recta que sube) |
| r cerca de 1 (0,8; 0,9...) | Relación directa **fuerte** |
| r cerca de 0 | Relación lineal **débil o nula** |
| r cerca de −1 | Relación inversa **fuerte** |
| r = −1 | Relación lineal **perfecta e inversa** |

r tiene siempre **el mismo signo** que la covarianza y que la pendiente b.

**r no depende de las unidades.** Si pasas X de euros a miles de euros (o de kilos a gramos), la covarianza y la pendiente cambian, pero **r se queda igual**. Es una medida **adimensional**. Por eso sirve para comparar la fuerza de la relación en cualquier problema.

**Ojo: r = 0 no quiere decir "ninguna relación".** Quiere decir que no hay relación **lineal**. Puede haber una relación curva (por ejemplo, en forma de U) con r = 0.

### Coeficiente de determinación (R²)

**Qué es.** r al cuadrado. Dice **qué proporción de la variabilidad de Y queda explicada por la recta** (por X). Está entre 0 y 1; se suele dar en %.

$$R^2=r^2$$

- R² cerca de 1 → buen ajuste, la recta predice bien.
- R² cerca de 0 → mal ajuste, la recta casi no sirve para predecir.
- 1 − R² es la parte **no explicada** (lo que depende de otras cosas).

::: {custom-style="Ojo"}
**⚠️ No predigas fuera de tus datos (extrapolar).** La recta solo vale para valores de X **dentro del rango observado**. Si los datos van de 1 a 15 años de antigüedad, no la uses para 40 años: no sabemos si la relación sigue siendo una recta tan lejos (el salario podría estancarse). Predecir fuera del rango se llama **extrapolar** y puede dar disparates. Esto lo preguntan en el examen.
:::

**Ejemplo: antigüedad y salario.** S²ᵧ = 38875000/10 − 1940² = 123900, así que Sᵧ = 352,0 y Sₓ = √18,4 = 4,29.

- r = 1445 / (4,29 × 352,0) = **0,957** → relación directa muy fuerte.
- R² = 0,957² = **0,916** → el **91,6 %** de la variabilidad del salario se explica por la antigüedad. El 8,4 % restante depende de otros factores.

::: {custom-style="Excel"}
**🖥️ En Excel.** `=COEF.DE.CORREL(A2:A11;B2:B11)` → 0,957 (aquí el orden da igual). `=COEFICIENTE.R2(B2:B11;A2:A11)` → 0,916 (primero Y, luego X).
:::

::: {custom-style="Ojo"}
**⚠️ Ojo: correlación no es causalidad.** Que dos variables estén muy correlacionadas no demuestra que una provoque la otra. Puede haber una tercera variable detrás. En esta asignatura basta con decir "están relacionadas", no "una causa la otra".
:::

::: {custom-style="Otra"}
**r** dice cómo de bien se alinean los puntos con una recta: 1 o −1, perfectamente alineados; 0, una nube sin forma.

**R²** lo traduce a porcentaje: de todo lo que varía Y, cuánto se debe a X. Con R² = 0,92, si conoces la antigüedad de alguien ya explicas el 92 % de lo que cobra; el 8 % restante depende de otras cosas.
:::

## 3.5. Predicciones

Si el ajuste es bueno (R² alto), se puede usar la recta para predecir: se sustituye X por el valor que nos den.

**Ejemplo:** salario de una trabajadora con **11 años** de antigüedad.

Ŷ = 1390,27 + 78,53 × 11 = 1390,27 + 863,86 = **2254,13 €**.

Como R² = 0,916, es una predicción fiable.

::: {custom-style="Excel"}
**🖥️ En Excel.** `=PRONOSTICO.LINEAL(11;B2:B11;A2:A11)` → 2254,13. Orden: el valor de X, luego los Y, luego los X. O bien, con a en E2 y b en E3: `=E2+E3*11`. (En el Excel de clase se predijo para X = 8: 2018,53 €.)
:::

::: {custom-style="Ojo"}
**⚠️ Ojo con predecir lejos.** Solo es fiable predecir para valores de X **dentro** del rango de los datos (aquí, de 1 a 15 años). Predecir el salario con 40 años de antigüedad sería arriesgado: no sabemos si la relación sigue siendo una recta.
:::

## 3.6. Fórmulas útiles para ejercicios "sin datos"

Muchos ejercicios no dan los datos, sino algunos resultados (medias, desviaciones, covarianza...). Estas relaciones permiten despejar lo que falta:

- b = S_XY / S²ₓ → S_XY = b · S²ₓ.
- r = S_XY / (Sₓ · Sᵧ) → S_XY = r · Sₓ · Sᵧ.
- r = b · Sₓ / Sᵧ (combinando las dos anteriores).
- R² = r² → r = ±√R² (con el signo de b).
- La recta pasa por (x̄, ȳ) → ȳ = a + b · x̄.

::: {custom-style="Ojo"}
**⚠️ Ojo: ¿me dan S o S²?** Lee con cuidado si el enunciado da la **desviación típica** (S) o la **varianza** (S²). Si te dan Sₓ = 40, entonces S²ₓ = 1600. Es el error más común en estos ejercicios.
:::

## ✔ Comprueba que sabes hacer (Tema 3)

- Hacer la nube de puntos en papel y en Excel con la recta, la ecuación y el R².
- Montar a mano la tabla xᵢ, yᵢ, xᵢ², yᵢ², xᵢyᵢ y sacar de sus sumas todo lo demás.
- Calcular la covarianza e interpretar su signo.
- Calcular la recta de Y sobre X (y la de X sobre Y) e interpretar la pendiente.
- Calcular r y R² e interpretarlos con una frase.
- Hacer una predicción y decir si es fiable.
- Despejar datos que faltan con las relaciones entre b, r, S y S_XY.

# Boletín del Tema 3, resuelto

::: {.video data-v="b3"}
:::

## Ejercicio 1. Publicidad y ventas

::: {custom-style="Enunciado"}
X = gasto en publicidad (miles €), Y = ventas (millones de cajas). x̄ = 60, ȳ = 850, Sₓ = 40, Sᵧ = 500, S_XY = 19200. a) Recta de las ventas según la publicidad. b) Coeficiente de determinación. c) Ventas esperadas con 100000 € de publicidad.
:::

Nos dan **desviaciones típicas**: S²ₓ = 40² = 1600.

**a)** b = 19200/1600 = **12**. a = 850 − 12 × 60 = 850 − 720 = **130**.

Ŷ = 130 + 12X. Por cada **mil euros** más de publicidad, las ventas aumentan de media **12 millones de cajas**. Sin publicidad (X = 0) se venderían unos 130 millones de cajas.

**b)** r = 19200/(40 × 500) = 19200/20000 = 0,96. R² = 0,96² = **0,9216**. El 92,16 % de la variabilidad de las ventas se explica por el gasto en publicidad: muy buen ajuste.

**c)** 100000 € = **100 miles de €** (cuidado con las unidades). Ŷ = 130 + 12 × 100 = **1330 millones de cajas**.

::: {custom-style="Excel"}
**🖥️ En Excel** (sin datos sueltos, se usan fórmulas con celdas). Pon x̄ en B1, ȳ en B2, Sₓ en B3, Sᵧ en B4, S_XY en B5. b: `=B5/B3^2`. a: `=B2-B7*B1` (si b está en B7). R²: `=(B5/(B3*B4))^2`. Predicción: `=B8+B7*100` (a en B8).
:::

## Ejercicio 2. Rendimiento de acciones e índice bursátil

::: {custom-style="Enunciado"}
n = 25. ΣY = 22,6; ΣX = 25,4; ΣY² = 172; ΣX² = 145,7; ΣXY = 150,5. a) Recta de Y sobre X. b) R². c) Rendimiento esperado si X = 1,5.
:::

1. Medias: x̄ = 25,4/25 = 1,016; ȳ = 22,6/25 = 0,904.
2. Varianzas: S²ₓ = 145,7/25 − 1,016² = 5,828 − 1,0323 = 4,7957. S²ᵧ = 172/25 − 0,904² = 6,88 − 0,8172 = 6,0628.
3. Covarianza: S_XY = 150,5/25 − 1,016 × 0,904 = 6,02 − 0,9185 = 5,1015.

**a)** b = 5,1015/4,7957 = **1,0638**. a = 0,904 − 1,0638 × 1,016 = **−0,1768**. Ŷ = −0,1768 + 1,0638X. Cuando el índice sube un punto porcentual, la acción sube de media 1,06 puntos.

**b)** R² = S²_XY/(S²ₓ · S²ᵧ) = 5,1015²/(4,7957 × 6,0628) = **0,895**. El 89,5 % de la variabilidad del rendimiento de la acción se explica por el del índice.

**c)** Ŷ = −0,1768 + 1,0638 × 1,5 = **1,419 %**.

::: {custom-style="Excel"}
**🖥️ En Excel.** Pon n y las sumas en celdas: n en B1, ΣX en B2, ΣY en B3, ΣX² en B4, ΣY² en B5, ΣXY en B6. x̄ `=B2/B1`, ȳ `=B3/B1` (en B8 y B9). S²ₓ `=B4/B1-B8^2`. S_XY `=B6/B1-B8*B9`. b `=S_XY/S²ₓ`; a `=B9-b*B8`. Mismo método que a mano, con celdas.
:::

## Ejercicio 3. Precio por hora y clientes de talleres

::: {custom-style="Enunciado"}
Euros/hora: 20,40 · 21,80 · 22,00 · 23,00 · 23,60. Clientes: 80 · 64 · 46 · 50 · 51. a) Recta de clientes según precio. b) Gráfico. c) % de la variabilidad de clientes **no** explicado por el precio. d) ¿Cuánto varían los clientes por cada euro más?
:::

X = precio, Y = clientes. n = 5.

| X | Y | X·Y | X² | Y² |
|---:|---:|---:|---:|---:|
| 20,4 | 80 | 1632 | 416,16 | 6400 |
| 21,8 | 64 | 1395,2 | 475,24 | 4096 |
| 22,0 | 46 | 1012 | 484 | 2116 |
| 23,0 | 50 | 1150 | 529 | 2500 |
| 23,6 | 51 | 1203,6 | 556,96 | 2601 |
| **110,8** | **291** | **6392,8** | **2461,36** | **17713** |

x̄ = 22,16; ȳ = 58,2. S²ₓ = 2461,36/5 − 22,16² = 1,2064. S²ᵧ = 17713/5 − 58,2² = 155,36. S_XY = 6392,8/5 − 22,16 × 58,2 = −11,152.

**a)** b = −11,152/1,2064 = **−9,244**. a = 58,2 − (−9,244) × 22,16 = **263,05**. Ŷ = 263,05 − 9,244X.

**b)**

![](img/r3_talleres.png){width=80%}

**c)** r = −11,152/√(1,2064 × 155,36) = −0,815. R² = 0,664. No explicado: 1 − 0,664 = 0,336 → **33,6 %**.

**d)** La pendiente: por cada euro más por hora, el taller tiene de media **9,24 clientes menos**.

::: {custom-style="Excel"}
**🖥️ En Excel.** X en A2:A6, Y en B2:B6. `=PENDIENTE(B2:B6;A2:A6)` → −9,244. `=INTERSECCION.EJE(B2:B6;A2:A6)` → 263,05. `=COEFICIENTE.R2(B2:B6;A2:A6)` → 0,664; no explicado: `=1-` esa celda. Gráfico: Insertar → Dispersión y línea de tendencia con ecuación y R².
:::

::: {custom-style="Mano"}
**✍️ A mano: la nube de puntos.** Eje X de 20 a 24 (euros/hora) y eje Y de 40 a 85 (clientes). Cinco puntos. Para la recta, calcula Ŷ en X = 20 (78,2) y en X = 24 (41,2) y únelos: baja, relación inversa.
:::

## Ejercicio 4. Tasación y precio de venta de viviendas

::: {custom-style="Enunciado"}
12 viviendas. X = tasación, Y = precio (miles €). x̄ = 115, ȳ = 130, Sₓ = 20, Sᵧ = 25, S_XY = 480.
:::

**a)** b = 480/20² = 480/400 = **1,2**. a = 130 − 1,2 × 115 = **−8**. Ŷ = −8 + 1,2X. Por cada 1000 € más de tasación, el precio de venta sube de media 1200 €. El término a = −8 no tiene sentido práctico (no hay viviendas tasadas en 0 €).

**b)** R² = (480/(20 × 25))² = 0,96² = **0,9216**: el 92,2 % de la variabilidad del precio se explica por la tasación.

**c)** r = **0,96**: relación directa muy fuerte.

**d)** 100000 € = 100 miles. Ŷ = −8 + 1,2 × 100 = **112 miles de € (112000 €)**.

::: {custom-style="Excel"}
**🖥️ En Excel.** Igual que el ejercicio 1: x̄, ȳ, Sₓ, Sᵧ y S_XY en celdas (B1 a B5). b `=B5/B3^2` → 1,2. a `=B2-b*B1` → −8. r `=B5/(B3*B4)` → 0,96. Predicción `=a+b*100`.
:::

## Ejercicio 5. Vertidos y sanciones

::: {custom-style="Enunciado"}
X (miles de litros): 0,5 · 1 · 1,5 · 2 · 2,5 · 3 · 3,5. Y (miles €): 100 · 300 · 500 · 800 · 1100 · 1500 · 2400. La industria ha vertido unos 2200 litros.
:::

x̄ = 14/7 = 2; ȳ = 6700/7 = 957,14. S²ₓ = 35/7 − 4 = 1. ΣXY = 18350 → S_XY = 18350/7 − 2 × 957,14 = 2621,43 − 1914,29 = 707,14. S²ᵧ = 10210000/7 − 957,14² = 542449.

**a)** b = 707,14/1 = **707,14**; a = 957,14 − 707,14 × 2 = **−457,14**. Ŷ = −457,14 + 707,14X. Cada mil litros más se sanciona de media con 707140 € más.

**b)** r = 707,14/(1 × 736,51) = **0,960**: relación directa muy fuerte. R² = 0,922.

**c)** 2200 litros = **2,2 miles de litros**. Ŷ = −457,14 + 707,14 × 2,2 = **1098,57 miles de €** (unos 1,1 millones de euros).

**d)**

![](img/r5_vertidos.png){width=80%}

::: {custom-style="Ojo"}
**⚠️ Un detalle para lucirte.** En el gráfico se ve que los puntos forman una **curva** que se acelera (la sanción crece cada vez más deprisa). La recta funciona bien (r = 0,96), pero se queda corta en los extremos. Comentarlo demuestra que sabes leer una nube de puntos.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** X en A2:A8, Y en B2:B8. `=PENDIENTE(B2:B8;A2:A8)` → 707,14. `=INTERSECCION.EJE(B2:B8;A2:A8)` → −457,14. `=COEF.DE.CORREL(A2:A8;B2:B8)` → 0,960. `=PRONOSTICO.LINEAL(2,2;B2:B8;A2:A8)` → 1098,57.
:::

## Ejercicio 6. Recuperar datos a partir de la recta

::: {custom-style="Enunciado"}
n = 100. Ŷ = 2 − 3X, R² = 0,81, x̄ = 2, Sᵧ = 10. Calcula ȳ, Sₓ y S_XY.
:::

1. **ȳ:** la recta pasa por las medias → ȳ = 2 − 3 × 2 = **−4**.
2. **r:** √0,81 = 0,9. La pendiente es negativa (−3), así que **r = −0,9**.
3. **Sₓ:** r = b · Sₓ/Sᵧ → −0,9 = −3 · Sₓ/10 → Sₓ = 0,9 × 10/3 = **3**.
4. **S_XY:** b = S_XY/S²ₓ → S_XY = −3 × 3² = **−27**.

Comprobación: r = −27/(3 × 10) = −0,9 ✔.

::: {custom-style="Excel"}
**🖥️ En Excel.** Sin datos sueltos se usan celdas: b en B1, R² en B2, x̄ en B3, Sᵧ en B4. ȳ `=2+B1*B3` (con a = 2). r `=SIGNO(B1)*RAIZ(B2)` → −0,9. Sₓ `=r*B4/B1` → 3. S_XY `=B1*Sₓ^2` → −27.
:::

## Ejercicio 7. Las dos rectas a partir de r

::: {custom-style="Enunciado"}
r = 0,56; x̄ = 12; ȳ = 24; S²ₓ = 3,6; S²ᵧ = 2,5. Rectas de Y sobre X y de X sobre Y.
:::

Aquí nos dan **varianzas**. Sₓ = √3,6 = 1,897; Sᵧ = √2,5 = 1,581.

S_XY = r · Sₓ · Sᵧ = 0,56 × 1,897 × 1,581 = 0,56 × 3 = **1,68** (porque √(3,6 × 2,5) = √9 = 3).

- **Y sobre X:** b = 1,68/3,6 = 0,467; a = 24 − 0,467 × 12 = 18,4 → **Ŷ = 18,4 + 0,467X**.
- **X sobre Y:** b' = 1,68/2,5 = 0,672; a' = 12 − 0,672 × 24 = −4,128 → **X̂ = −4,128 + 0,672Y**.

::: {custom-style="Excel"}
**🖥️ En Excel.** r en B1, x̄ en B2, ȳ en B3, S²ₓ en B4, S²ᵧ en B5. S_XY `=B1*RAIZ(B4)*RAIZ(B5)` → 1,68 (en B7). Y sobre X: b `=B7/B4`, a `=B3-b*B2`. X sobre Y: b' `=B7/B5`, a' `=B2-b'*B3`.
:::

## Ejercicio 8. Emparejar gráficos y rectas

::: {custom-style="Enunciado"}
Relaciona cada uno de los seis gráficos del boletín con su recta: I: Ŷ = 5 · II: Ŷ = 5 − 4X · III: Ŷ = 2X · IV: Ŷ = 5 − 1,5X · V: Ŷ = 5 + 4X · VI: Ŷ = 5 + 1,5X. Justifica la respuesta.
:::

Pistas para leer una recta: el número **suelto** (a) es dónde corta al eje vertical (en X = 0). El número que **multiplica a X** (b) dice cuánto sube o baja: positivo sube, negativo baja, y cuanto mayor, más empinada. Para comprobarlo, calcula Ŷ en X = 10 y mira el gráfico.

| Gráfico | Qué se ve | Recta | Comprobación en X = 10 |
|:---:|:---|:---|:---|
| 1 | Empieza en 0 y sube hasta 20 | **III: Ŷ = 2X** | 2·10 = 20 ✔ |
| 2 | Empieza en 5 y sube hasta 20 | **VI: Ŷ = 5 + 1,5X** | 5 + 15 = 20 ✔ |
| 3 | Empieza en 5 y baja mucho, hasta −35 | **II: Ŷ = 5 − 4X** | 5 − 40 = −35 ✔ |
| 4 | Empieza en 5 y sube mucho, hasta 45 | **V: Ŷ = 5 + 4X** | 5 + 40 = 45 ✔ |
| 5 | Línea horizontal en 5, puntos sin tendencia | **I: Ŷ = 5** | Pendiente 0: sin relación lineal |
| 6 | Empieza en 5 y baja hasta −10 | **IV: Ŷ = 5 − 1,5X** | 5 − 15 = −10 ✔ |

## Ejercicio 9. Rectas con la EPF

::: {custom-style="Enunciado"}
Calcula rectas de regresión entre variables de la EPF (51 provincias). Indica qué variable explicas con cuál, las ecuaciones y la bondad del ajuste.
:::

Es un ejercicio abierto: puedes elegir las variables. Te propongo tres, de más a menos ajuste. Todas con Excel sobre la hoja *EncuestaPresupuestosFamiliares*.

| Explico (Y) | Con (X) | Recta | r | R² |
|:---|:---|:---|---:|---:|
| Turismo y ocio | Educación y cultura | Ŷ = 2138,84 + 1,275·X | 0,845 | 0,714 |
| Turismo y ocio | Vivienda | Ŷ = 1047,74 + 0,457·X | 0,810 | 0,656 |
| Vivienda | Alimentación | Ŷ = 555,20 + 0,774·X | 0,475 | 0,226 |

*Interpretación:*

- **Ocio según educación:** por cada euro más que una provincia gasta en educación y cultura, gasta de media 1,27 € más en turismo y ocio. El 71 % de las diferencias en ocio entre provincias se explica por el gasto en educación. Buen ajuste: provincias con más gasto "no básico" en una partida también lo tienen en la otra.
- **Ocio según vivienda:** relación directa fuerte (R² = 66 %).
- **Vivienda según alimentación:** relación directa pero **débil**: solo el 23 % se explica. La recta no serviría para predecir bien.

::: {custom-style="Excel"}
**🖥️ En Excel** (EducacionCultura en la columna H y TurismoOcio en la I, filas 2 a 52): `=PENDIENTE(I2:I52;H2:H52)`, `=INTERSECCION.EJE(I2:I52;H2:H52)`, `=COEF.DE.CORREL(H2:H52;I2:I52)`, `=COEFICIENTE.R2(I2:I52;H2:H52)`. Haz también la nube de puntos con línea de tendencia para ver el ajuste.
:::
