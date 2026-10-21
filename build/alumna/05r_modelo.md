# Examen modelo de la profesora

## Cómo es el examen

La profesora enseñó en clase este modelo de parcial. Es la mejor pista que tenemos de cómo será el examen de verdad.

- **30 preguntas tipo test** con 4 opciones (A, B, C, D). Solo una es correcta. La letra se escribe **en mayúscula** en el recuadro.
- **10 preguntas de respuesta corta.** Se responde "de forma concisa": una definición, una fórmula o una cuenta corta.
- **En papel.** Las preguntas de Excel son de **elegir o escribir la fórmula**, no de usar el ordenador.
- Entra todo: Temas 1, 2, 3 y 4.

::: {custom-style="Idea"}
**🧠 Qué se ve en el modelo.** Pocas cuentas largas y mucha **teoría**: definiciones, fórmulas y saber interpretar. Las cuentas que hay son cortas: un CV, un R², un IQR, una predicción. Las trampas típicas son las de siempre: sumar porcentajes en vez de multiplicarlos, confundir intervalo modal con el de más frecuencia o creer que r = 0 significa "ninguna relación".
:::

**Cómo usar este apartado.** Lee cada pregunta, **decide tu respuesta antes** de abrir la solución y después pulsa «Ver la solución». Cada solución explica por qué es esa y por qué no son las otras, y te dice dónde está en la guía. Cuando lo tengas, haz el **Simulacro tipo test**, que es igual pero con preguntas nuevas y se corrige solo.

## Tipo test: Tema 1 (preguntas 1 a 10)

### Pregunta 1

En Excel se desea tipificar una serie de datos de la variable X colocados en A2:A50, restando la media (x̄), que está en la celda $B$1, y dividiendo entre la desviación típica (S), que está en $B$2. ¿Cuál es la fórmula correcta para escribir en B2 y copiar hacia abajo?

A) `=(A2-B1)/B2`
B) `=($A$2-B1)/B2`
C) `=(A$2-$B1)/$B2`
D) `=(A2-$B$1)/$B$2`

<details><summary>Ver la solución</summary>

**Correcta: D.** Al copiar hacia abajo, el dato tiene que ir cambiando (A2, A3, A4...), así que **A2 va sin dólares**. La media y la desviación son siempre las mismas celdas, así que van **fijas con dólares**: $B$1 y $B$2.

- A) Sin dólares, al bajar una fila la media pasaría a B2, B3... y el resultado sería basura.
- B) Fija el dato ($A$2): todas las filas usarían el primer dato.
- C) Fija a medias: A$2 no deja que el dato baje.

*En la guía:* apartado 1.9 (tipificar) y Parte 0 bis (referencias con $).

</details>

### Pregunta 2

Para calcular la media ponderada de unos datos que están en A2:A10, con sus pesos o frecuencias en B2:B10, ¿cuál es la sintaxis correcta con SUMAPRODUCTO?

A) `=SUMAPRODUCTO(A2:A10;B2:B10)`
B) `=SUMAPRODUCTO(A2:A10;B2:B10)/SUMA(B2:B10)`
C) `=SUMAPRODUCTO(A2:A10/B2:B10)`
D) `=SUMA(A2:A10)*SUMAPRODUCTO(B2:B10)/CONTAR(A2:A10)`

<details><summary>Ver la solución</summary>

**Correcta: B.** La media de una tabla es Σxᵢ·nᵢ / n. SUMAPRODUCTO hace el Σxᵢ·nᵢ y SUMA(B2:B10) es n (la suma de las frecuencias o de los pesos).

- A) Le falta dividir: eso es solo el numerador.
- C) Divide datos entre pesos, que no tiene sentido.
- D) Mezcla cosas sin sentido.

*En la guía:* media de una tabla y media ponderada (apartado 1.5) y la chuleta.

</details>

### Pregunta 3

En un estudio se registra el nivel de *satisfacción laboral* (Bajo, Medio, Alto) y el *salario bruto anual* (en euros). ¿Cómo se clasifican?

A) Satisfacción cualitativa nominal y salario cuantitativo discreto
B) Satisfacción cualitativa **ordinal** y salario cuantitativo **continuo**
C) Ambas cuantitativas continuas
D) Satisfacción cualitativa ordinal y salario cualitativo nominal

<details><summary>Ver la solución</summary>

**Correcta: B.** Bajo, Medio y Alto son palabras (cualitativa) **con orden** (ordinal). El salario es un número que puede tomar cualquier valor con céntimos: cuantitativa **continua**.

- A) Nominal sería sin orden (por ejemplo, el departamento).
- C) La satisfacción no es un número.
- D) El salario no es cualitativo.

*En la guía:* apartado 1.2 (tipos de variables).

</details>

### Pregunta 4

Sea X una variable con media x̄. Si aplicamos Y = aX + b, ¿qué propiedad es correcta?

A) La suma de las desviaciones a la media es siempre positiva
B) ȳ = x̄ + b y la varianza no se altera
C) El CV no cambia aunque haya cambio de origen b ≠ 0
D) **ȳ = a·x̄ + b y S²ᵧ = a²·S²ₓ**

<details><summary>Ver la solución</summary>

**Correcta: D.** La media sufre todo el cambio (se multiplica por a y se suma b). La varianza solo nota la multiplicación, y al cuadrado: sumar b mueve todos los datos lo mismo y no cambia su dispersión.

- A) La suma de las desviaciones a la media es **siempre 0**, no positiva.
- B) Olvida la a.
- C) Si sumas b, la media cambia pero S no, así que el CV **sí cambia**.

*En la guía:* apartado 1.5 (la media y los cambios de origen y escala) y 1.7 (cómo afectan a la dispersión).

</details>

### Pregunta 5

¿En qué caso es especialmente preferible la mediana o la media truncada en lugar de la media aritmética?

A) Distribución perfectamente simétrica y sin atípicos
B) **Datos con valores extremos (outliers) que distorsionan la tendencia central**
C) Solo cuando la variable es cualitativa nominal
D) Cuando hay más de un millón de datos agrupados

<details><summary>Ver la solución</summary>

**Correcta: B.** La media se deja arrastrar por los extremos. La mediana y la media truncada (que quita un porcentaje de datos de cada punta) son **robustas**: no les afectan.

- A) Si es simétrica y sin atípicos, la media es perfecta.
- C) Con una variable nominal no hay ni media ni mediana: solo moda.
- D) El tamaño no tiene nada que ver.

*En la guía:* apartado 1.5 (media truncada y «Media, mediana o moda: ¿cuál uso?»).

</details>

### Pregunta 6

En datos agrupados en intervalos de **distinta amplitud**, ¿cómo se determina el intervalo modal?

A) El de mayor frecuencia absoluta nᵢ
B) **El de mayor densidad dᵢ = nᵢ / aᵢ**
C) El que contiene la mediana
D) El de mayor marca de clase

<details><summary>Ver la solución</summary>

**Correcta: B.** Si los intervalos tienen distinto ancho, uno ancho tiene más datos solo por ser ancho. Para comparar hay que mirar cuántos datos hay **por unidad de ancho**: la densidad.

- A) Solo vale si todos los intervalos miden lo mismo. Es la trampa típica.
- C) y D) No tienen nada que ver con la moda.

*En la guía:* apartado 1.5 (moda con intervalos) y el Ejercicio 15 del boletín.

</details>

### Pregunta 7

Respecto al coeficiente de variación (CV = S / x̄), señala la afirmación correcta.

A) Expresa la dispersión en las mismas unidades que la variable
B) Es negativo cuando la dispersión es muy alta
C) **Permite comparar la variabilidad relativa de poblaciones con unidades o escalas distintas**
D) Mide la asimetría respecto a la moda

<details><summary>Ver la solución</summary>

**Correcta: C.** Al dividir S entre la media, las unidades se van: el CV es un número puro (o un %). Por eso sirve para comparar kilos con gramos, o salarios con alturas.

- A) Eso es la desviación típica, no el CV.
- B) S nunca es negativa; con media positiva, el CV tampoco.
- D) La asimetría se mide con el coeficiente de Fisher.

*En la guía:* apartado 1.7 (coeficiente de variación).

</details>

### Pregunta 8

Al descomponer la varianza total de una población dividida en k grupos se cumple:

A) Total = dentro × entre
B) La varianza dentro mide la diferencia de las medias de los grupos
C) **Varianza total = varianza dentro (intrapoblacional) + varianza entre (interpoblacional)**
D) Si el 95 % es interpoblacional, los grupos son idénticos

<details><summary>Ver la solución</summary>

**Correcta: C.** La varianza total se reparte en dos partes que se **suman**: la que hay dentro de cada grupo y la que hay entre las medias de los grupos.

- A) Se suman, no se multiplican.
- B) Eso es la varianza **entre**, no la de dentro.
- D) Es al revés: si casi todo es "entre", los grupos son **muy distintos** entre sí.

*En la guía:* apartado 1.7 (varianza en subpoblaciones) y Ejercicios 13, 14 y 21 del boletín.

</details>

### Pregunta 9

Si el coeficiente de asimetría de Fisher es CA > 0, esto indica que:

A) Es simétrica y mesocúrtica
B) **Asimetría positiva o a la derecha: hay una cola de valores altos hacia la derecha**
C) Asimetría negativa, con los datos concentrados a la derecha
D) La moda coincide con el máximo

<details><summary>Ver la solución</summary>

**Correcta: B.** CA > 0 → cola larga a la derecha (unos pocos valores muy altos), y la media queda por encima de la mediana. Ejemplo típico: los salarios.

- A) Simétrica sería CA = 0.
- C) Eso es CA < 0.
- D) No tiene sentido.

*En la guía:* apartado 1.8 (asimetría y curtosis).

</details>

### Pregunta 10

En un diagrama de caja, ¿qué datos se consideran atípicos?

A) **x < C₁ − 1,5·IQR o x > C₃ + 1,5·IQR, con IQR = C₃ − C₁**
B) x < x̄ − S o x > x̄ + S
C) Cualquier valor por debajo de P₁₀ o por encima de P₉₀
D) x < C₂ − IQR o x > C₂ + IQR

<details><summary>Ver la solución</summary>

**Correcta: A.** Es la regla de los apuntes: los límites se ponen a 1,5 veces el IQR por fuera de la caja.

- B) Con esa regla, casi un tercio de los datos serían "atípicos".
- C) Siempre habría un 20 % de atípicos, por definición.
- D) Usa la mediana y no lleva el 1,5.

*En la guía:* apartado 1.10 (valores atípicos y diagrama de caja).

</details>

## Tipo test: Tema 2 (preguntas 11 a 15)

### Pregunta 11

En una tabla de doble entrada, la celda (i, j) tiene nᵢⱼ. ¿Cómo se obtiene la frecuencia marginal nᵢ. de la categoría xᵢ?

A) **Sumando las frecuencias de la fila i a lo largo de todas las columnas: nᵢ. = Σⱼ nᵢⱼ**
B) Dividiendo nᵢⱼ entre n
C) Multiplicando las marginales de xᵢ y yⱼ
D) Restando la suma de la columna j al total n

<details><summary>Ver la solución</summary>

**Correcta: A.** La marginal de una fila es el total de esa fila: lo que aparece en el margen derecho.

- B) Eso es la frecuencia relativa conjunta fᵢⱼ.
- C) Eso es lo que se usa para comprobar la independencia (casilla esperada).
- D) No tiene sentido.

*En la guía:* apartado 2.2 (distribuciones marginales).

</details>

### Pregunta 12

X e Y son estadísticamente independientes si y solo si, para todas las casillas:

A) **fᵢⱼ = fᵢ. · f.ⱼ**
B) Todas las nᵢⱼ son iguales
C) S_XY > 0
D) Las condicionadas de Y varían mucho según X

<details><summary>Ver la solución</summary>

**Correcta: A.** Es la definición: en **todas** las casillas, la relativa conjunta es el producto de las marginales.

- B) No hace falta que sean iguales.
- C) Si son independientes, la covarianza es 0, no positiva.
- D) Es justo lo contrario: si las condicionadas cambian, **hay** relación.

*En la guía:* apartado 2.4 (independencia).

</details>

### Pregunta 13

Si X e Y son independientes, ¿qué relación hay entre las condicionadas Y | X = xᵢ y la marginal de Y?

A) Son inversamente proporcionales
B) No se pueden calcular
C) **Todas las condicionadas son iguales entre sí e iguales a la marginal de Y**
D) Suman 0

<details><summary>Ver la solución</summary>

**Correcta: C.** Independencia significa que saber X no cambia nada de Y. Así que la distribución de Y es la misma en cada fila, y coincide con la del total.

*En la guía:* apartados 2.3 y 2.4.

</details>

### Pregunta 14

En un gráfico de mosaico de dos variables cualitativas, ¿qué refleja la frecuencia marginal de la variable principal?

A) **El ancho de las columnas**
B) La intensidad del color
C) La inclinación de las diagonales
D) El número de sectores

<details><summary>Ver la solución</summary>

**Correcta: A.** En el mosaico, cada columna es una categoría y **su ancho es su frecuencia marginal**. El alto de cada trozo dentro de la columna es la condicionada.

*En la guía:* apartado 2.1 (gráficos para dos variables).

</details>

### Pregunta 15

Género (Hombre, Mujer) y jornada (Completa, Parcial) en 200 empleados. La proporción marginal de jornada completa es 0,70 y las variables son **independientes**. ¿Qué proporción de hombres tiene jornada completa en la condicionada Y | Hombre?

A) 0,30
B) **0,70**
C) 0,35
D) Depende del número de hombres

<details><summary>Ver la solución</summary>

**Correcta: B.** Si son independientes, la condicionada es igual a la marginal (pregunta 13). Si el 70 % del total tiene jornada completa, el 70 % de los hombres también.

- A) 0,30 es la proporción de jornada parcial.
- C) 0,35 sería suponer que la mitad son hombres y multiplicar: es la conjunta, no la condicionada.
- D) Con independencia no depende de eso.

*En la guía:* apartados 2.3 y 2.4.

</details>

## Tipo test: Tema 3 (preguntas 16 a 23)

### Pregunta 16

En una nube de puntos de antigüedad (X) y salario (Y), los puntos forman una nube alargada que sube de izquierda a derecha. ¿Qué relación hay?

A) **Lineal directa o positiva (S_XY > 0)**
B) Lineal inversa (S_XY < 0)
C) Ninguna relación
D) No lineal cuadrática con correlación nula

<details><summary>Ver la solución</summary>

**Correcta: A.** Si la nube sube, cuando X crece Y también crece: relación directa, y la covarianza es positiva.

*En la guía:* apartado 3.1 (nube de puntos) y 3.2 (covarianza).

</details>

### Pregunta 17

¿Qué expresión es la covarianza entre X e Y?

A) **S_XY = (1/n) · Σᵢ Σⱼ xᵢ · yⱼ · nᵢⱼ − x̄ · ȳ** · (las otras opciones son fórmulas incorrectas)

<details><summary>Ver la solución</summary>

**Correcta: A.** Es la fórmula práctica para una tabla de doble entrada: la media de los productos menos el producto de las medias. Con datos sueltos es lo mismo sin las nᵢⱼ: Σxᵢyᵢ / n − x̄·ȳ.

Recuerda las otras fórmulas para distinguirlas: r = S_XY / (Sₓ·Sᵧ) y b = S_XY / S²ₓ.

*En la guía:* apartado 3.2 (covarianza, también con tabla de frecuencias).

</details>

### Pregunta 18

Para la recta de Y sobre X, Ŷ = a + bX, ¿cómo se calculan b y a?

A) b = S_XY/S²ᵧ y a = x̄ − bȳ
B) b = r·Sₓ y a = ȳ + bx̄
C) b = S²ₓ/S_XY y a = ȳ·x̄
D) **b = S_XY/S²ₓ y a = ȳ − b·x̄**

<details><summary>Ver la solución</summary>

**Correcta: D.** La pendiente es la covarianza entre la varianza de la **X** (la que explica). Y como la recta pasa por (x̄, ȳ), a = ȳ − b·x̄.

- A) Esas son las de la recta de **X sobre Y**, mal escritas.
- B) La relación correcta es b = r · Sᵧ / Sₓ, y a lleva un menos.
- C) Está dada la vuelta.

*En la guía:* apartado 3.3 (recta de regresión).

</details>

### Pregunta 19

¿Qué propiedad comparten la recta de Y sobre X y la de X sobre Y?

A) Tienen la misma pendiente
B) **Se cortan siempre en el punto de medias (x̄, ȳ)**
C) Son perpendiculares
D) Sus términos independientes suman 0

<details><summary>Ver la solución</summary>

**Correcta: B.** Las dos rectas pasan por (x̄, ȳ), así que ahí se cortan.

- A) Las pendientes son distintas: una divide entre S²ₓ y otra entre S²ᵧ.
- C) Solo son perpendiculares en el caso de covarianza 0 (pregunta 22).

*En la guía:* apartado 3.3 (recta de X sobre Y).

</details>

### Pregunta 20

El coeficiente de correlación de Pearson r = S_XY / (Sₓ·Sᵧ) cumple:

A) **Está entre −1 y 1 y no tiene unidades (es adimensional)**
B) Cambia según las unidades de X e Y
C) r = 0 garantiza que no hay ninguna relación, ni lineal ni curva
D) Si r = −1, la pendiente es positiva

<details><summary>Ver la solución</summary>

**Correcta: A.**

- B) Al revés: r **no cambia** con las unidades.
- C) r = 0 solo dice que no hay relación **lineal**. Puede haber una curva.
- D) r y la pendiente tienen siempre el mismo signo: con r = −1 la pendiente es negativa.

*En la guía:* apartado 3.4.

</details>

### Pregunta 21

Si en un ajuste por regresión R² = 0,81, ¿cómo se interpreta?

A) La pendiente es 0,81
B) La covarianza es 0,81
C) **El 81 % de la variabilidad de Y queda explicada por la recta**
D) Hay un error del 81 %

<details><summary>Ver la solución</summary>

**Correcta: C.** Es la frase de interpretación de R². El 19 % restante no lo explica la recta.

*En la guía:* apartado 3.4 (coeficiente de determinación).

</details>

### Pregunta 22

Si S_XY = 0, ¿qué forma tienen las rectas de Y sobre X y de X sobre Y?

A) **La de Y sobre X es horizontal (Ŷ = ȳ) y la de X sobre Y es vertical (X̂ = x̄)**
B) Las dos coinciden con la diagonal de 45°
C) Sus pendientes tienden a infinito
D) R² vale 1

<details><summary>Ver la solución</summary>

**Correcta: A.** Si la covarianza es 0, las dos pendientes valen 0. Y sobre X queda Ŷ = ȳ (siempre predice la media: horizontal) y X sobre Y queda X̂ = x̄ (vertical en los mismos ejes).

- D) Es lo contrario: R² = 0, la recta no explica nada.

*En la guía:* apartado 3.3 (caso especial: covarianza 0).

</details>

### Pregunta 23

Con el modelo Salario = 1390 + 78,5 · Antigüedad (R² = 0,92), ¿qué salario medio se estima para 10 años de antigüedad?

A) 1390 €
B) 785 €
C) 2310,5 €
D) **2175 €**

<details><summary>Ver la solución</summary>

**Correcta: D.** Se sustituye X = 10: 1390 + 78,5 · 10 = 1390 + 785 = **2175 €**.

- A) Es solo el punto de partida (0 años).
- B) Es solo lo que suman los 10 años.
- C) No sale de ninguna cuenta correcta.

El R² no se usa para la cuenta: solo dice que la predicción es fiable.

*En la guía:* apartado 3.5 (predicciones).

</details>

## Tipo test: Tema 4 (preguntas 24 a 30)

### Pregunta 24

Un índice simple de salarios vale I₂₀₁₅²⁰²⁵ = 125,4 con base 2015 = 100. ¿Qué significa?

A) El salario bajó un 25,4 %
B) El salario en 2025 es 125,4 €
C) El poder adquisitivo subió un 125,4 %
D) **El salario subió un 25,4 % en 2025 respecto a 2015**

<details><summary>Ver la solución</summary>

**Correcta: D.** Índice − 100 = variación en %: 125,4 − 100 = +25,4 %.

- B) El índice no son euros.
- C) Es un índice nominal: no descuenta la inflación, y además la subida es 25,4 %, no 125,4 %.

*En la guía:* apartado 4.1 (índice simple).

</details>

### Pregunta 25

Según la propiedad de **inversión** de los índices simples:

A) **I_t^0 = 1 / I_0^t**
B) I_t^0 = I_t^k + I_k^0
C) I_t^0 = 100 − I_0^t
D) I_t^0 = (I_0^t)²

<details><summary>Ver la solución</summary>

**Correcta: A.** El índice "al revés" es el inverso. En tanto por uno: si de 2015 a 2019 se multiplica por 1,10, de 2019 a 2015 se multiplica por 1/1,10 = 0,909.

- B) Mezcla con el encadenamiento, que se hace **multiplicando**, no sumando.

*En la guía:* apartado 4.3 (propiedades de los índices).

</details>

### Pregunta 26

Para calcular la tasa media anual de algo que crece con porcentajes encadenados durante n periodos, la media adecuada es:

A) La media aritmética de las tasas
B) La mediana de los incrementos en euros
C) **La media geométrica: ⁿ√((1+t₁)(1+t₂)···(1+tₙ)) − 1**
D) La moda de las tasas

<details><summary>Ver la solución</summary>

**Correcta: C.** Los porcentajes se encadenan **multiplicando**, así que la media correcta es la geométrica: se multiplican los factores, se hace la raíz n-ésima y se resta 1.

- A) La media aritmética da un resultado falso: subir un 10 % y bajar un 10 % daría 0 %, y en realidad pierdes un 1 %.

*En la guía:* apartado 4.5 (media geométrica y tasas medias).

</details>

### Pregunta 27

Si la tasa anual es del 6 %, ¿cómo se obtiene la tasa mensual equivalente?

A) 0,06/12 = 0,5 %
B) (1 + 0,06)¹² − 1
C) **(1 + 0,06)^(1/12) − 1 ≈ 0,486 %**
D) √0,06 ≈ 24,49 %

<details><summary>Ver la solución</summary>

**Correcta: C.** Para pasar de un año a un mes se hace la raíz 12 (elevar a 1/12) del factor 1,06 y se resta 1. Sale 0,487 % (la profesora lo redondea a 0,486 %).

- A) Repartir entre 12 es la trampa: los porcentajes no se dividen, porque se encadenan.
- B) Eso es pasar de mensual a anual (al revés).

*En la guía:* apartado 4.5 (tasa anual equivalente). En Excel: `=1,06^(1/12)-1`.

</details>

### Pregunta 28

En el índice de precios de **Laspeyres**, ¿qué ponderación tienen los precios?

A) **Las cantidades del periodo base (q₀)**
B) Las cantidades del periodo actual (qₜ)
C) El promedio de los precios
D) La tasa de variación de las ventas

<details><summary>Ver la solución</summary>

**Correcta: A.** Laspeyres mantiene la cesta del año base: L = Σpₜq₀ / Σp₀q₀.

- B) Eso es **Paasche**: Σpₜqₜ / Σp₀qₜ.

*En la guía:* apartado 4.6 (Laspeyres y Paasche). Truco: **L**aspeyres = cantidades del año base, las "de **L**a base".

</details>

### Pregunta 29

¿Qué diferencia fundamental hay entre Laspeyres y Paasche?

A) **Laspeyres tiende a sobreestimar la subida de precios porque mantiene fijas las cantidades de la cesta base; Paasche usa las del periodo actual**
B) Laspeyres mide cantidades y Paasche tipos de interés
C) Paasche no se puede calcular con más de tres bienes
D) Laspeyres es una media geométrica y Paasche una armónica

<details><summary>Ver la solución</summary>

**Correcta: A.** Cuando algo sube mucho, la gente compra menos. Laspeyres no se entera (usa la cesta antigua) y exagera la inflación. Paasche usa la cesta nueva y tiende a quedarse corto.

*En la guía:* apartado 4.6 (¿por qué tres índices?).

</details>

### Pregunta 30

Deflactar una serie de salarios nominales consiste en:

A) Multiplicar por la tasa de desempleo
B) Sumar la inflación al salario
C) Restar la cuasivarianza de los precios
D) **Dividir el salario nominal de cada periodo entre el índice de precios (IPC) en base 1, para obtener el salario real a poder adquisitivo constante**

<details><summary>Ver la solución</summary>

**Correcta: D.** Valor real = nominal / IPC (en tanto por uno). Con el IPC en base 100 es lo mismo, multiplicando por 100: nominal / IPC × 100.

*En la guía:* apartado 4.7 (deflactar).

</details>

## Respuesta corta (P1 a P10)

### P1. Parámetro y estadístico

Define brevemente ambos conceptos.

<details><summary>Ver la solución</summary>

**Respuesta modelo:** Un **parámetro** es una medida que describe a toda la **población** (por ejemplo, la media de todos los trabajadores de España). Un **estadístico** es la misma medida calculada en una **muestra** (la media de los 200 encuestados). El estadístico sirve para estimar el parámetro.

*En la guía:* apartado 1.1 (vocabulario básico).

</details>

### P2. Densidad de frecuencia e intervalo modal

Al construir un histograma con intervalos de distinta amplitud aᵢ, ¿qué magnitud se debe representar en el eje de alturas?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** La **densidad de frecuencia**, dᵢ = nᵢ / aᵢ (o fᵢ / aᵢ). Así el **área** de cada barra es proporcional a su frecuencia y los intervalos anchos no parecen más frecuentes solo por ser anchos. El intervalo modal es el de **mayor densidad**.

*En la guía:* apartado 1.4 (histograma) y 1.5 (moda).

</details>

### P3. Robustez y diagrama de caja

¿Por qué el diagrama de caja es preferible a la media y la desviación típica cuando hay un fuerte sesgo y valores atípicos?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** Porque se construye con la **mediana y los cuartiles**, que son medidas **robustas**: no se dejan arrastrar por los valores extremos. La media y la desviación típica sí se distorsionan con los atípicos. Además, el diagrama de caja **muestra** directamente los atípicos y la asimetría (posición de la mediana y longitud de los bigotes).

*En la guía:* apartados 1.5 y 1.10.

</details>

### P4. Descomposición de la varianza

En una población dividida en k subgrupos, escribe la descomposición de la varianza total.

<details><summary>Ver la solución</summary>

**Respuesta modelo:**

S² = varianza dentro + varianza entre

- Dentro (intrapoblacional) = Σ Sᵢ² · nᵢ / n: la media de las varianzas de cada grupo.
- Entre (interpoblacional) = Σ (x̄ᵢ − x̄)² · nᵢ / n: lo que se separan las medias de los grupos de la media global.

*En la guía:* apartado 1.7 y la chuleta.

</details>

### P5. Coeficiente de variación

Producto A: media 40 kg, S = 8 kg. Producto B: media 200 g, S = 30 g. Calcula el CV de cada uno e indica cuál tiene más variabilidad relativa.

<details><summary>Ver la solución</summary>

**Respuesta modelo:**

- CV A = 8 / 40 = **0,20** (20 %).
- CV B = 30 / 200 = **0,15** (15 %).

El **producto A** tiene más variabilidad relativa. Las unidades son distintas (kg y g), y por eso hay que usar el CV y no S.

*En la guía:* apartado 1.7.

</details>

### P6. Coeficiente de determinación

Si r = −0,85, ¿cuánto vale R² y qué porcentaje de la varianza de Y explica la recta?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** R² = (−0,85)² = **0,7225**. La recta explica el **72,25 %** de la variabilidad de Y. El signo de r desaparece al elevar al cuadrado; solo dice que la relación es inversa.

*En la guía:* apartado 3.4.

</details>

### P7. Tasa media en Excel

Una inversión ha tenido tasas del +5 %, +10 % y −2 % en 3 años (1,05; 1,10; 0,98 en A1:A3). ¿Qué fórmula de Excel da la tasa media anual?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** `=MEDIA.GEOM(A1:A3)-1`, o también `=PRODUCTO(A1:A3)^(1/3)-1`.

Cuenta: 1,05 · 1,10 · 0,98 = 1,1319. Raíz cúbica: 1,0422. Tasa media: **4,22 % anual**. No vale `=PROMEDIO`, que daría un 4,33 % falso.

*En la guía:* apartado 4.5.

</details>

### P8. Predecir fuera del rango

¿Por qué no es recomendable usar la recta para predecir Y con un valor de X muy fuera del rango observado?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** Porque la recta solo está comprobada **dentro del rango de los datos**. Fuera de él no sabemos si la relación sigue siendo lineal (puede cambiar, estancarse o curvarse), así que la predicción puede ser muy errónea. Predecir fuera del rango se llama **extrapolar**.

*En la guía:* apartado 3.4 (no predigas fuera de tus datos).

</details>

### P9. Cambio de unidades y r

Si X pasa de euros a miles de euros, ¿cómo cambia r?

<details><summary>Ver la solución</summary>

**Respuesta modelo:** **No cambia.** r no tiene unidades (es adimensional): al dividir entre miles cambian la covarianza y Sₓ en la misma proporción y se compensan. Solo cambiaría de signo si se multiplicara por un número negativo.

*En la guía:* apartado 3.4.

</details>

### P10. Diagrama de caja de tiempos de espera

Diagrama de caja de tiempos de espera (minutos): mínimo 5, Q₁ = 8, Me = 11, Q₃ = 16, bigote superior hasta unos 23 y un atípico en 27. Calcula el IQR, el límite teórico superior para considerar un dato atípico y el tipo de asimetría.

<details><summary>Ver la solución</summary>

**Respuesta modelo:**

- IQR = Q₃ − Q₁ = 16 − 8 = **8 minutos**.
- Límite superior = Q₃ + 1,5 · IQR = 16 + 12 = **28 minutos**. Por encima de 28, un dato es atípico.
- **Asimetría positiva (a la derecha):** la mediana (11) está más cerca de Q₁ (8 → distancia 3) que de Q₃ (16 → distancia 5), y el bigote superior (16 a 23) es mucho más largo que el inferior (5 a 8).

::: {custom-style="Ojo"}
**⚠️ Una incoherencia del enunciado.** Con la fórmula, el límite es 28, así que un dato de 27 **no** sería atípico, aunque el dibujo lo marque así. En el examen, escribe el 28 que sale de la fórmula y, si quieres, añade una línea: "según el límite calculado, 27 no sería atípico".
:::

*En la guía:* apartado 1.10.

</details>
