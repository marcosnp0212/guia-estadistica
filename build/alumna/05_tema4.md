# Tema 4. Números índices

::: {.video data-v="t4"}
:::

::: {custom-style="Idea"}
**🧠 La idea del tema.** Un número índice dice **cuánto ha cambiado algo** respecto a un momento de referencia (el **año base**), al que se le da el valor **100**. Si el salario de 2025 tiene índice 120 respecto a 2020, ha subido un 20 %. Todo el tema es jugar con **divisiones y multiplicaciones por porcentajes**, nada más.
:::

## 4.1. Índice simple

$$I_0^t=\frac{x_t}{x_0}\cdot 100$$

- xₜ = valor en el año que estudiamos (t).
- x₀ = valor en el año base (0).
- I₀ᵗ se lee "índice del año t con base en el año 0".

**Cómo se interpreta:** índice − 100 = % de cambio.

- Índice 120 → ha subido un 20 %.
- Índice 97,44 → ha bajado un 100 − 97,44 = 2,56 %.
- Índice 100 → no ha cambiado (el año base siempre vale 100).

**Ejemplo de los apuntes.** Salario 1500 € en 2015 y 1600 € en 2018. I₂₀₁₅²⁰¹⁸ = 1600/1500 × 100 = **106,67** → el salario subió un 6,67 %.

Si en 2026 fuese 1900 € y en 2025 1950 €: I₂₀₂₅²⁰²⁶ = 1900/1950 × 100 = **97,44** → bajó un 2,56 %.

Los índices **no tienen unidades** (son un cociente: euros entre euros).

::: {custom-style="Truco"}
**💡 Trabajar sin el "× 100".** Muchas veces es más cómodo usar el índice en "tanto por uno": 1,20 en lugar de 120. Así subir un 20 % es "× 1,20" y encadenar es multiplicar. Al final, multiplica por 100 si te lo piden en la forma habitual.
:::

::: {custom-style="Excel"}
**🖥️ En Excel: serie de índices con base fija.** Años en A2:A12 y salarios en B2:B12; el año base (2015) está en la fila 2. En C2: `=B2/$B$2*100` y arrastra. El `$B$2` fija el año base. Para cambiar de base, solo cambia esa celda (por ejemplo, `$B$6` para 2019).
:::

::: {custom-style="Otra"}
Un índice dice "comparado con el año base, esto vale tanto", poniendo el año base en 100.

Si el pan costaba 1 € y ahora 1,20 €, el índice es 120: por cada 100 céntimos de antes, ahora pagas 120. Lo que pasa de 100 es lo que ha subido.
:::

## 4.2. Tasa de variación

$$\text{Tasa}=\frac{V_1-V_0}{V_0}\cdot 100=\left(\frac{V_1}{V_0}-1\right)\cdot 100$$

Es lo mismo que el índice menos 100. Positiva = crecimiento, negativa = disminución, 0 = sin cambio.

- Cuentas de un banco: 1000 en 2020 y 1100 en 2021 → 1100/1000 = 1,1 → **+10 %**.
- Precio: 11,42 € en 2024 y 8,41 € en 2025 → 8,41/11,42 = 0,736 → **−26,35 %**.

::: {custom-style="Excel"}
**🖥️ En Excel.** Valor anterior en B2 y nuevo en B3: `=(B3-B2)/B2` y dale formato de porcentaje (botón **%** de la pestaña Inicio). O `=B3/B2-1`.
:::

## 4.3. Propiedades de los índices

**Inversión:** el índice "al revés" es el inverso.

$$I_t^0=\frac{1}{I_0^t}$$

Ejemplo: I₂₀₁₅²⁰¹⁹ = 1,10 (subió un 10 %). Entonces I₂₀₁₉²⁰¹⁵ = 1/1,10 = 0,909. Comprobación: 1500/1650 = 0,909 ✔.

::: {custom-style="Ojo"}
**⚠️ Tanto por uno o base 100.** La profesora escribe las propiedades con los índices **en tanto por uno** (1,10 en vez de 110). En el examen la fórmula correcta de la inversión es **I = 1 / I**. Si trabajas con base 100, la misma idea se escribe I = 100 · 100 / I: con 110 sale 10000/110 = 90,9. Es lo mismo; solo cambia dónde va el 100.
:::

**Encadenamiento:** para ir del año 0 al año t' pasando por t, se **multiplican** los índices.

$$I_0^{t'}=I_0^t\cdot I_t^{t'}$$

Ejemplo: una empresa crece un 5 %, luego un 8 % y luego un 10 %. Crecimiento total: 1,05 × 1,08 × 1,10 = **1,2474** → ha crecido un **24,74 %** en los tres años.

::: {custom-style="Ojo"}
**⚠️ Ojo: los porcentajes NO se suman.** Subir un 5 %, un 8 % y un 10 % no es subir un 23 %, sino un 24,74 %. Y subir un 10 % y luego bajar un 10 % **no** te deja igual: 1,10 × 0,90 = 0,99, has perdido un 1 %. Siempre se **multiplica**.
:::

::: {custom-style="Otra"}
Cada subida se aplica sobre **lo que ya tienes**, no sobre lo del principio.

Con 100 €: sube un 10 % y tienes 110 €. Ahora baja un 10 %, pero un 10 % de 110 son 11 €: te quedan 99 €. Por eso los porcentajes se multiplican (1,10 × 0,90 = 0,99) y no se suman.
:::

## 4.4. Cambio de base

**Qué es.** Pasar una serie de índices de un año base a otro. Se divide toda la serie entre el índice del nuevo año base (y se multiplica por 100).

$$I_{\text{nueva}}^t=\frac{I_{\text{vieja}}^t}{I_{\text{vieja}}^{\text{nuevo año base}}}\cdot 100$$

**Ejercicio de los apuntes: pasar los salarios a base 2019.** El índice de 2019 en base 2015 es 110. Dividimos todos entre 110:

| Año | Salario | Base 2015 | Base 2019 |
|:---:|---:|---:|---:|
| 2015 | 1500 | 100 | 100/110 × 100 = 90,91 |
| 2016 | 1530 | 102 | 92,73 |
| 2017 | 1570 | 104,67 | 95,15 |
| 2018 | 1600 | 106,67 | 96,97 |
| 2019 | 1650 | 110 | **100** |
| 2020 | 1700 | 113,33 | 103,03 |
| 2021 | 1750 | 116,67 | 106,06 |
| 2022 | 1800 | 120 | 109,09 |
| 2023 | 1850 | 123,33 | 112,12 |
| 2024 | 1900 | 126,67 | 115,15 |
| 2025 | 1950 | 130 | 118,18 |

::: {custom-style="Excel"}
**🖥️ En Excel.** Índices base 2015 en C2:C12; 2019 está en la fila 6. En D2: `=C2/$C$6*100` y arrastra.
:::

## 4.5. Media geométrica y tasas medias

**Qué es.** Cuando los datos son **crecimientos que se multiplican**, la media correcta no es la normal (aritmética) sino la geométrica: se multiplican los n valores y se hace la raíz n-ésima.

$$M_g=\sqrt[n]{x_1\cdot x_2\cdots x_n}=(x_1\cdot x_2\cdots x_n)^{1/n}$$

**Ejemplo 1.** Una inversión sube un 10 % y luego baja un 10 %. Mg = √(1,10 × 0,90) = √0,99 = **0,995**: de media, cada año se multiplica por 0,995 → pierde un **0,5 % anual**. (La media aritmética diría 0 %, y es falso: al final tienes un 1 % menos.)

**Ejemplo 2.** Crecimientos del 5 %, 8 % y 10 %. Mg = ∛(1,05 × 1,08 × 1,10) = ∛1,2474 = **1,0765** → crecimiento medio del **7,65 % anual**. Comprobación: 1,0765³ = 1,2475 ≈ 1,2474 ✔.

::: {custom-style="Excel"}
**🖥️ En Excel.** Valores 1,05; 1,08; 1,10 en A1:A3: `=MEDIA.GEOM(A1:A3)` → 1,0765. O `=PRODUCTO(A1:A3)^(1/3)`. La tasa media es ese resultado menos 1.
:::

::: {custom-style="Otra"}
La tasa media es la que, **repetida igual cada año**, te deja en el mismo sitio.

Si en dos años has crecido un 26 % en total (×1,26), la tasa media es el número que multiplicado por sí mismo da 1,26: √1,26 = 1,1225, es decir, un 12,25 % al año. Compruébalo: 1,1225 × 1,1225 = 1,26.
:::

### Tasa anual equivalente (pasar de un periodo largo a "por año" o "por mes")

Si en un periodo de **k** años (o meses) la tasa total ha sido T, la tasa media por año es:

$$t=(1+T)^{1/k}-1$$

**De anual a mensual:** tasa anual del 6 % → tₘ = 1,06^(1/12) − 1 = **0,00487** = 0,487 % mensual.

**Ejemplo de los apuntes.** Cantidad 3864 (2015), 5442 (2022), 5809 (2025).

- 2015-2022 (7 años): T = 5442/3864 − 1 = 0,408 (40,8 %). Anual: 1,408^(1/7) − 1 = **0,050** (5 % anual).
- 2022-2025 (3 años): T = 5809/5442 − 1 = 0,067 (6,7 %). Anual: 1,067^(1/3) − 1 = **0,022** (2,2 % anual).
- 2015-2025 (10 años): T = 5809/3864 − 1 = 0,503. Anual: 1,503^(1/10) − 1 = **0,0416** (4,16 % anual).

**Al revés: de tasas mensuales a trimestral.** Enero 0,5 %, febrero 0,4 %, marzo 0,3 %. Trimestre: 1,005 × 1,004 × 1,003 = 1,012047 → **1,2047 %**. Media mensual: 1,012047^(1/3) − 1 = **0,4 %**.

::: {custom-style="Ojo"}
**⚠️ Ojo.** En las fórmulas los porcentajes van en decimal: 0,5 % es 0,005, no 0,5. Y en Excel la raíz se escribe como potencia: `=1,06^(1/12)-1`. **El paréntesis en (1/12) es obligatorio.** Sin él, Excel haría 1,06¹ ÷ 12.
:::

::: {custom-style="Mano"}
**✍️ A mano: tasas medias con la calculadora.** Todo el Tema 4 se hace bien en papel. Lo único delicado es la raíz n-ésima.

1. Pasa cada porcentaje a "multiplicador": +5 % → 1,05; −3 % → 0,97; +0,5 % → 1,005.
2. Multiplícalos todos: es el crecimiento total.
3. Para la media por año, eleva a **(1 ÷ número de periodos)**. En la calculadora: `1,2474 ^ ( 1 ÷ 3 )` con el paréntesis, o con la tecla de raíz n-ésima (ˣ√): `3 ˣ√ 1,2474`.
4. Resta 1 y pasa a %: 1,0765 − 1 = 0,0765 → **7,65 %**.
5. **Comprueba** elevando: 1,0765³ tiene que dar 1,2474 (o casi, por el redondeo).

**Sin la tecla de raíz n-ésima:** con la de potencia (^ o xʸ) y el exponente entre paréntesis. Con 7 años: `1,408 ^ ( 1 ÷ 7 )` = 1,050.
:::


## 4.6. Índices complejos (de varios productos)

Cuando hay varios productos (una cesta de la compra), hay que combinar sus índices.

### Índice de Sauerbeck

La media aritmética de los índices simples de cada producto, sin ponderar. Supone que todos los productos son igual de importantes.

### Índice de Laspeyres de precios

Pondera con las **cantidades del año base** (q₀). Es el que se usa para el IPC.

$$L_p=\frac{\sum p_t\cdot q_0}{\sum p_0\cdot q_0}\cdot 100$$

Se lee: "lo que costaría **hoy** la cesta **de entonces**, dividido entre lo que costaba **entonces** esa misma cesta".

### Índice de Paasche de precios

Pondera con las **cantidades del año actual** (qₜ).

$$P_p=\frac{\sum p_t\cdot q_t}{\sum p_0\cdot q_t}\cdot 100$$

Se lee: "lo que cuesta **hoy** la cesta **de hoy**, dividido entre lo que habría costado **entonces** la cesta de hoy".

::: {custom-style="Truco"}
**💡 Para no confundirlos.** En los dos, **arriba van los precios de hoy (pₜ)** y **abajo los de antes (p₀)**. Lo único que cambia es la cantidad, que es **la misma arriba y abajo**: **L**aspeyres usa la cantidad de **antes** (q₀), **P**aasche la de ahora (qₜ). Un truco: "La**s**peyres = la cesta de **s**iempre (la del inicio)".
:::

**Ejemplo de los apuntes (2015 → 2025):**

| Producto | p₀ | pₜ | q₀ | qₜ |
|:---|---:|---:|---:|---:|
| Pan | 1,00 | 1,20 | 100 | 110 |
| Leche | 0,90 | 1,10 | 200 | 190 |

- Laspeyres: (1,20·100 + 1,10·200)/(1·100 + 0,9·200) × 100 = 340/280 × 100 = **121,43** → los precios subieron un 21,43 %.
- Paasche: (1,20·110 + 1,10·190)/(1·110 + 0,9·190) × 100 = 341/281 × 100 = **121,35** → subieron un 21,35 %.

::: {custom-style="Otra"}
**Laspeyres:** llenas el carro de la compra como en el año base y lo pagas hoy. ¿Cuánto más te cuesta?

**Paasche:** coges el carro de hoy y miras cuánto te habría costado en el año base.

Los dos comparan precios con **la misma cesta arriba y abajo**. Solo cambia qué cesta usan.
:::

### Índices de cantidades

Igual, pero intercambiando los papeles: ahora lo que cambia arriba y abajo son las **cantidades**, y el **precio** se queda fijo.

$$L_q=\frac{\sum q_t\cdot p_0}{\sum q_0\cdot p_0}\cdot 100 \qquad P_q=\frac{\sum q_t\cdot p_t}{\sum q_0\cdot p_t}\cdot 100$$

### Índice de Fisher

La media geométrica de Laspeyres y Paasche. Busca un equilibrio entre los dos.

$$F=\sqrt{L\cdot P}$$

**¿Por qué tres índices?** Laspeyres **sobreestima** la inflación: si algo sube mucho, la gente compra menos o lo cambia por otra cosa, pero Laspeyres sigue usando las cantidades antiguas. Paasche la **subestima**, porque da menos peso a lo que se ha dejado de comprar. Fisher queda en medio.

::: {custom-style="Excel"}
**🖥️ En Excel: Laspeyres y Paasche.** Columnas: B = p₀, C = q₀, D = pₜ, E = qₜ (filas 2 a 6).

- Laspeyres: `=SUMAPRODUCTO(D2:D6;C2:C6)/SUMAPRODUCTO(B2:B6;C2:C6)*100`
- Paasche: `=SUMAPRODUCTO(D2:D6;E2:E6)/SUMAPRODUCTO(B2:B6;E2:E6)*100`
- Fisher: `=RAIZ(celda_Laspeyres*celda_Paasche)`

Si prefieres verlo paso a paso, crea columnas auxiliares con `=D2*C2` (pₜ·q₀), `=B2*C2` (p₀·q₀), etc., súmalas y divide.
:::

::: {custom-style="Mano"}
**✍️ A mano: Laspeyres, Paasche y Fisher con una tabla.** Añade cuatro columnas de productos y súmalas. Con el ejemplo de los apuntes:

| Producto | pₜ·q₀ | p₀·q₀ | pₜ·qₜ | p₀·qₜ |
|:---|---:|---:|---:|---:|
| Pan | 1,20·100 = 120 | 1,00·100 = 100 | 1,20·110 = 132 | 1,00·110 = 110 |
| Leche | 1,10·200 = 220 | 0,90·200 = 180 | 1,10·190 = 209 | 0,90·190 = 171 |
| **Suma** | **340** | **280** | **341** | **281** |

- Laspeyres = 340 ÷ 280 × 100 = **121,43**.
- Paasche = 341 ÷ 281 × 100 = **121,35**.
- Fisher = √(121,43 × 121,35) = **121,39**.

Con la tabla delante, Laspeyres es "columna 1 entre columna 2" y Paasche "columna 3 entre columna 4". Así no se confunden.
:::


## 4.7. Deflactar: de euros "nominales" a euros "reales"

**Qué es.** Quitar el efecto de la inflación para saber si de verdad se puede comprar más o menos.

- **Valor nominal:** los euros tal cual (precios corrientes).
- **Valor real:** los euros expresados con el poder de compra del año base (precios constantes).

$$\text{Valor real}=\frac{\text{Valor nominal}}{\text{IPC}}\cdot 100$$

(Con el IPC en la forma "base = 100". Si el IPC está en tanto por uno, 1,10, se divide sin el × 100.)

**Definición para el examen:** deflactar es **dividir el valor nominal de cada periodo entre el índice de precios (IPC) de ese periodo, en tanto por uno**, para obtener el valor real, a poder adquisitivo constante.

**Ejemplo.** En 2020 una persona gana 20000 €. En 2025 gana 25000 €. El IPC de 2025 (base 2020) es 110. Valor real de 2025 = 25000/110 × 100 = **22727,27 €** de 2020. Su poder adquisitivo ha subido, pero no un 25 %, sino un 22727/20000 − 1 = 13,6 %.

::: {custom-style="Otra"}
Deflactar es traducir euros de hoy a "euros de entonces".

Si los precios han subido un 10 % (IPC 110), 25000 € de hoy compran lo mismo que 22727 € del año base. Así puedes comparar sueldos de años distintos como si los precios no hubieran cambiado.
:::

**Ejemplo de los apuntes (salarios 2015-2025 con IPC).** Salario real = salario / IPC × 100. Índice nominal = salario / 1500 × 100. Índice real = salario real / 1500 × 100.

| Año | Salario | IPC | Salario real | Índice nominal | Índice real |
|:---:|---:|---:|---:|---:|---:|
| 2015 | 1500 | 100,0 | 1500,00 | 100,00 | 100,00 |
| 2016 | 1530 | 101,2 | 1511,86 | 102,00 | 100,79 |
| 2017 | 1570 | 102,5 | 1531,71 | 104,67 | 102,11 |
| 2018 | 1600 | 104,0 | 1538,46 | 106,67 | 102,56 |
| 2019 | 1650 | 106,0 | 1556,60 | 110,00 | 103,77 |
| 2020 | 1700 | 108,5 | 1566,82 | 113,33 | 104,45 |
| 2021 | 1750 | 110,2 | 1588,02 | 116,67 | 105,87 |
| 2022 | 1800 | 112,0 | 1607,14 | 120,00 | 107,14 |
| 2023 | 1850 | 114,5 | 1615,72 | 123,33 | 107,71 |
| 2024 | 1900 | 117,0 | 1623,93 | 126,67 | 108,26 |
| 2025 | 1950 | 119,0 | 1638,66 | 130,00 | 109,24 |

![Índice nominal y real](img/t4_nominal_real.png){width=80%}

*Interpretación:* en euros corrientes el salario ha subido un 30 % entre 2015 y 2025. Pero los precios también han subido (un 19 %). En términos **reales**, el poder adquisitivo solo ha aumentado un **9,24 %**. La distancia entre las dos líneas es lo que "se ha comido" la inflación.

::: {custom-style="Excel"}
**🖥️ En Excel.** Salario en B, IPC en C (filas 2 a 12). Salario real en D2: `=B2/C2*100`. Índice nominal en E2: `=B2/$B$2*100`. Índice real en F2: `=D2/$D$2*100`. Arrastra las tres. Para el gráfico: selecciona años, E y F → Insertar → Líneas.
:::

::: {custom-style="Mano"}
**✍️ A mano: deflactar una serie.** Para cada año, tres cuentas con la calculadora (una fila cada vez):

1. **Salario real** = salario ÷ IPC × 100. 2025: 1950 ÷ 119 × 100 = **1638,66**.
2. **Índice nominal** = salario ÷ salario del año base × 100. 2025: 1950 ÷ 1500 × 100 = **130**.
3. **Índice real** = salario real ÷ salario real del año base × 100. 2025: 1638,66 ÷ 1500 × 100 = **109,24**.

**Atajo:** índice real = índice nominal ÷ IPC × 100. 2025: 130 ÷ 119 × 100 = 109,24. Da lo mismo y es una sola cuenta.

**Gráfico en papel:** años en el eje horizontal, índices en el vertical (de 95 a 135, por ejemplo); una línea para el nominal y otra para el real. La separación entre las dos es lo que se ha comido la inflación.
:::


## 4.8. Aplicaciones: el IPC y el IBEX 35

**El IPC** (Índice de Precios de Consumo) lo elabora el INE y mide la evolución de los precios de lo que compran los hogares. Es un índice tipo **Laspeyres encadenado**: las ponderaciones (el peso de cada grupo de gasto) salen del consumo de las familias y se actualizan. Se usa para actualizar alquileres, salarios, pensiones... Desde enero de 2022 se publica en base 2021. Los grupos con más peso son Alimentos y bebidas no alcohólicas (18,54 %), Hoteles, cafés y restaurantes (14,75 %), Transporte (14,39 %) y Vivienda (12,16 %).

Práctica rápida: con IPC del 6,5 % (2021), 5,7 % (2022), 3,5 % (2023) y 2,8 % (2024), la subida acumulada de precios es 1,065 × 1,057 × 1,035 × 1,028 = 1,1977 → **19,8 %** en cuatro años (no 18,5 %, que sería sumar).

**El IBEX 35** es el índice de referencia de la Bolsa española: las 35 empresas más negociadas. Está ponderado por capitalización (las empresas que valen más pesan más). Su fórmula es tipo Laspeyres, con base 1000:

$$IBEX_t=\frac{\sum p_{t}\cdot q_{0}}{\sum p_{0}\cdot q_{0}}\cdot 1000$$

Ejemplo de los apuntes con 3 empresas: base = 10·1000000 + 20·500000 + 40·200000 = 28000000. Actual = 12·1000000 + 18·500000 + 44·200000 = 29800000. IBEX = 29800000/28000000 × 1000 = **1064,3 puntos** → las acciones han subido de media un 6,43 %.

## ✔ Comprueba que sabes hacer (Tema 4)

- Calcular un índice simple e interpretarlo como % de subida o bajada.
- Calcular tasas de variación y encadenarlas multiplicando.
- Hacer un cambio de base.
- Calcular una tasa media con la media geométrica o con la raíz (1/k).
- Calcular Laspeyres, Paasche y Fisher.
- Deflactar con el IPC y comparar evolución nominal y real.
- Hacer todo lo anterior **a mano con calculadora**, sabiendo usar la potencia (1/n) para las tasas medias.

# Boletín del Tema 4, resuelto

::: {.video data-v="b4"}
:::

## Ejercicio 1. Índices de producción

::: {custom-style="Enunciado"}
En 2020 la producción aumentó un 40 % respecto a 2019. En 2021 bajó un 20 % respecto a 2020 y superó en un 15 % la de 2022. Índices con base 2019.
:::

Ponemos 2019 = 100 y vamos paso a paso:

- **2019:** 100.
- **2020:** +40 % → 100 × 1,40 = **140**.
- **2021:** −20 % respecto a 2020 → 140 × 0,80 = **112**.
- **2022:** "2021 superó en un 15 % a 2022" significa 2021 = 1,15 × 2022. Despejamos: 2022 = 112/1,15 = **97,39**.

::: {custom-style="Ojo"}
**⚠️ Ojo con la última frase.** La referencia es 2022, no 2021. No es "2022 = 112 × 0,85" (eso daría 95,2). Escribe la frase como ecuación antes de calcular: "A supera en un 15 % a B" → A = 1,15·B.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** En B2 escribe 100 (2019). 2020: `=B2*1,4`. 2021: `=B3*0,8`. 2022: `=B4/1,15`. Es la misma idea que a mano: multiplicar o dividir por (1 + tasa).
:::

## Ejercicio 2. Precio de un bien

::: {custom-style="Enunciado"}
En 2020 el precio fue un 20 % mayor que en 2019, un 20 % menor que en 2018 y un 50 % menor que en 2021. Base 2019.
:::

- **2019:** 100.
- **2020:** un 20 % más que 2019 → **120**.
- **2018:** "2020 es un 20 % menor que 2018" → 2020 = 0,80 × 2018 → 2018 = 120/0,80 = **150**.
- **2021:** "2020 es un 50 % menor que 2021" → 2020 = 0,50 × 2021 → 2021 = 120/0,50 = **240**.

| Año | 2018 | 2019 | 2020 | 2021 |
|:---|---:|---:|---:|---:|
| Índice (2019 = 100) | 150 | 100 | 120 | 240 |

::: {custom-style="Excel"}
**🖥️ En Excel.** 2019 en C2 = 100. 2020: `=C2*1,2`. 2018: `=C3/0,8`. 2021: `=C3/0,5`.
:::

## Ejercicio 3. Cuentas corrientes de un banco

::: {custom-style="Enunciado"}
Variación anual: 2021 +9 %, 2022 +10 %, 2023 −2 %, 2024 +8 %, 2025 +10 %. Índices con base 2020.
:::

Se encadenan multiplicando cada año por (1 + tasa):

| Año | Cálculo | Índice |
|:---:|:---|---:|
| 2020 | base | 100 |
| 2021 | 100 × 1,09 | 109 |
| 2022 | 109 × 1,10 | 119,90 |
| 2023 | 119,9 × 0,98 | 117,50 |
| 2024 | 117,502 × 1,08 | 126,90 |
| 2025 | 126,902 × 1,10 | 139,59 |

En 2025 hay un 39,6 % más de cuentas que en 2020.

::: {custom-style="Excel"}
**🖥️ En Excel.** Tasas en B3:B7 (como 9 %, 10 %... con formato %). En C2 escribe 100. En C3: `=C2*(1+B3)` y arrastra.
:::

## Ejercicio 4. ¿Está bien ajustado el salario?

::: {custom-style="Enunciado"}
IPC 2024 (base 2023) = 103,5. En 2023 nos pagan 433,45 € por un trabajo y en 2024, 442,20 € por el mismo trabajo.
:::

**Lo que debería cobrar para no perder poder adquisitivo:** 433,45 × 1,035 = **448,62 €**. Cobra 442,20 €, menos de eso → **no está bien ajustado**.

**En euros de 2023 (valor real):** 442,20/103,5 × 100 = **427,25 €**. Variación real: 427,25/433,45 − 1 = **−1,43 %**.

::: {custom-style="Resultado"}
**✅** Aunque en euros nominales cobra un 2,02 % más, los precios han subido un 3,5 %. En términos reales ha **perdido un 1,43 %** de poder adquisitivo.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Salarios en B2 (2023) y B3 (2024), IPC 2024 en C3. Lo que debería cobrar: `=B2*C3/100` → 448,62. Valor real: `=B3/C3*100` → 427,25. Variación real: `=B4/B2-1` (con el valor real en B4) → −1,43 %.
:::

## Ejercicio 5. Tasas de variación de inversiones

::: {custom-style="Enunciado"}
Inversión de una empresa extranjera en España: 45000 (2020), 50400 (2021), 48300 (2022), 53130 (2023) y 55786 (2024). Calcula la tasa de variación de cada año respecto al anterior.
:::

| Año | Inversión | Tasa respecto al año anterior |
|:---:|---:|---:|
| 2020 | 45000 | — |
| 2021 | 50400 | 50400/45000 − 1 = **+12 %** |
| 2022 | 48300 | 48300/50400 − 1 = **−4,17 %** |
| 2023 | 53130 | 53130/48300 − 1 = **+10 %** |
| 2024 | 55786 | 55786/53130 − 1 = **+5 %** |

::: {custom-style="Excel"}
**🖥️ En Excel.** En C3 `=B3/B2-1` con formato %, y arrastrar.
:::

## Ejercicio 6. Justificar dos series de índices

::: {custom-style="Enunciado"}
Producción 120, 135, 150, 165, 180 (2020-2024). Índice base 2020: 100; 112,5; 125; 137,5; 150. Índice base 2022: 80; 90; 100; 110; 120.
:::

**Base 2020:** cada producción dividida entre la de 2020 (120), por 100. Por ejemplo, 2021: 135/120 × 100 = 112,5.

**Base 2022 a partir de la anterior (cambio de base):** se divide cada índice base 2020 entre el de 2022 (125), por 100. Por ejemplo, 2020: 100/125 × 100 = 80; 2024: 150/125 × 100 = 120. Se obtiene lo mismo que dividiendo directamente cada producción entre 150 (la de 2022).

::: {custom-style="Excel"}
**🖥️ En Excel.** Producción en B2:B6. Base 2020 en C2: `=B2/$B$2*100`. Base 2022 en D2: `=C2/$C$4*100` (o `=B2/$B$4*100`). Arrastra.
:::

## Ejercicio 7. Cantidad, precio y valor

::: {custom-style="Enunciado"}
2015: cantidad 8820, precio 14. 2022: 9030 y 18. 2025: 9073 y 20.
:::

**a) Tasas de variación de cada periodo.**

| | 2015 → 2022 | 2022 → 2025 |
|:---|---:|---:|
| Cantidad | 9030/8820 − 1 = **2,38 %** | 9073/9030 − 1 = **0,48 %** |
| Precio | 18/14 − 1 = **28,57 %** | 20/18 − 1 = **11,11 %** |

**b) Tasas anuales equivalentes** (2015-2022 son 7 años; 2022-2025 son 3 años).

| | Anual 2015-2022 | Anual 2022-2025 |
|:---|---:|---:|
| Cantidad | 1,0238^(1/7) − 1 = **0,34 %** | 1,0048^(1/3) − 1 = **0,16 %** |
| Precio | 1,2857^(1/7) − 1 = **3,66 %** | 1,1111^(1/3) − 1 = **3,57 %** |

**c) Valor = precio × cantidad:** 2015: 14 × 8820 = **123480**. 2022: 18 × 9030 = **162540**. 2025: 20 × 9073 = **181460**.

**d) Índices del valor (base 2015):** 100 · 162540/123480 × 100 = **131,63** · 181460/123480 × 100 = **146,95**.

Tasas: 2015-2022: **+31,63 %**. 2022-2025: 146,95/131,63 − 1 = **+11,64 %**. Todo el periodo: **+46,95 %**.

Curiosidad: el índice del valor es el producto del de precio por el de cantidad: 1,2857 × 1,0238 = 1,3163 ✔.

::: {custom-style="Excel"}
**🖥️ En Excel.** Cantidades en B2:B4 y precios en C2:C4 (2015, 2022, 2025). Tasa de cantidad 2015-2022: `=B3/B2-1`. Anual: `=(B3/B2)^(1/7)-1`. Valor en D2: `=B2*C2`. Índice del valor: `=D2/$D$2*100`.
:::

## Ejercicio 8. Tasas mensuales

::: {custom-style="Enunciado"}
Enero +5 %, febrero +4 %, marzo +3 %.
:::

**a) Tasa del trimestre:** 1,05 × 1,04 × 1,03 = 1,12476 → **+12,48 %**.

**b) Con 100 €:**

| Momento | Cálculo | Valor |
|:---|:---|---:|
| Inicio | | 100,00 |
| Fin de enero | 100 × 1,05 | 105,00 |
| Fin de febrero | 105 × 1,04 | 109,20 |
| Fin de marzo | 109,2 × 1,03 | 112,48 |

Tasa trimestral: 112,476/100 − 1 = 12,48 % ✔ (coincide con a).

**c) Tasa media mensual:** 1,12476^(1/3) − 1 = **0,0400 → 4 %**. (Casualidad bonita: es la media de 5, 4 y 3, pero en general no coincide exactamente; aquí da 3,997 %.)

::: {custom-style="Excel"}
**🖥️ En Excel.** Tasas en B2:B4 (5 %, 4 %, 3 %). Trimestre: `=(1+B2)*(1+B3)*(1+B4)-1` → 12,48 %. Media mensual: `=((1+B2)*(1+B3)*(1+B4))^(1/3)-1` → 4,00 %.
:::

## Ejercicio 9. Laspeyres y Paasche de una cesta

::: {custom-style="Enunciado"}
Precios y cantidades de pan, leche, huevos, carne y pescado en 2020 y 2025 (tabla del boletín). Calcula el índice de precios de Laspeyres y de Paasche con base 2020.
:::

| Producto | p₂₀₂₀ | q₂₀₂₀ | p₂₀₂₅ | q₂₀₂₅ | p₂₅·q₂₀ | p₂₀·q₂₀ | p₂₅·q₂₅ | p₂₀·q₂₅ |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| Pan | 1,20 | 300 | 1,50 | 280 | 450 | 360 | 420 | 336 |
| Leche | 0,90 | 200 | 1,10 | 210 | 220 | 180 | 231 | 189 |
| Huevos | 2,50 | 100 | 3,00 | 95 | 300 | 250 | 285 | 237,5 |
| Carne | 8,00 | 50 | 9,50 | 48 | 475 | 400 | 456 | 384 |
| Pescado | 10,00 | 40 | 12,00 | 38 | 480 | 400 | 456 | 380 |
| **Suma** | | | | | **1925** | **1590** | **1848** | **1526,5** |

- **Laspeyres:** 1925/1590 × 100 = **121,07** → precios +21,07 %.
- **Paasche:** 1848/1526,5 × 100 = **121,06** → precios +21,06 %.
- (Fisher: √(121,07 × 121,06) = 121,07.)

Salen casi iguales porque las cantidades apenas cambiaron entre 2020 y 2025.

::: {custom-style="Excel"}
**🖥️ En Excel.** p₂₀ en B, q₂₀ en C, p₂₅ en D, q₂₅ en E (filas 2 a 6). Laspeyres: `=SUMAPRODUCTO(D2:D6;C2:C6)/SUMAPRODUCTO(B2:B6;C2:C6)*100` → 121,07. Paasche: `=SUMAPRODUCTO(D2:D6;E2:E6)/SUMAPRODUCTO(B2:B6;E2:E6)*100` → 121,06.
:::

## Ejercicio 10. Sueldos e IPC (base 1990)

::: {custom-style="Enunciado"}
1992: sueldo 150000, IPC 120. 1993: 162000; 130,5. 1994: 170000; 137,4. 1995: 183000; 144. 1996: 190000; 153,8.
:::

**a) IPC con base 1992** (cambio de base: dividir entre 120):

| Año | 1992 | 1993 | 1994 | 1995 | 1996 |
|:---|---:|---:|---:|---:|---:|
| IPC (1992 = 100) | 100 | 108,75 | 114,50 | 120,00 | 128,17 |

**b) Sueldo en unidades monetarias de 1992 (sueldo real)** = sueldo / IPC₁₉₉₂ × 100:

| Año | 1992 | 1993 | 1994 | 1995 | 1996 |
|:---|---:|---:|---:|---:|---:|
| Sueldo real | 150000 | 148965,52 | 148471,62 | 152500 | 148244,47 |

**c) Variación 1992-1996:**

- En términos **corrientes** (nominales): 190000/150000 − 1 = **+26,67 %**.
- En términos **reales**: 148244,47/150000 − 1 = **−1,17 %**.

Aunque el sueldo nominal sube mucho, los precios suben más: el poder adquisitivo **baja** ligeramente.

::: {custom-style="Ojo"}
**⚠️ Ojo con el enunciado.** Los datos son de los años 90 (probablemente en pesetas). "Euros del año 1992" se entiende como "dinero con el poder de compra de 1992". Si te pidieran pasarlo a euros, habría que dividir además entre 166,386 pesetas por euro (150000 pts = 901,52 €).
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Sueldo en B2:B6 e IPC en C2:C6. IPC base 1992 en D2: `=C2/$C$2*100`. Sueldo real en E2: `=B2/D2*100`. Variación nominal `=B6/B2-1`; real `=E6/E2-1`.
:::

## Ejercicio 11. Actualizar un alquiler con el IPC

::: {custom-style="Enunciado"}
Alquiler en 2020: 1200 €/mes. IPC: 2020 = 112, 2021 = 114, 2022 = 120.
:::

**a)** Se actualiza en la misma proporción que el IPC:

- 2021: 1200 × 114/112 = **1221,43 €**.
- 2022: 1200 × 120/112 = **1285,71 €**.

**b)** Si en 2022 quiere cobrar 1300 €, lo equivalente en 2020 sería 1300 × 112/120 = **1213,33 €**.

::: {custom-style="Excel"}
**🖥️ En Excel.** Alquiler en B1, IPC 2020, 2021 y 2022 en B2:B4. 2021: `=$B$1*B3/$B$2`. 2022: `=$B$1*B4/$B$2`. b) `=1300*B2/B4`.
:::

## Ejercicio 12. SMI real con base 2010

::: {custom-style="Enunciado"}
SMI e IPC de 2010 a 2016 (Ministerio de Trabajo). Calcula el SMI con base en el año 2010 en términos reales.
:::

| Año | SMI | IPC | SMI real (€ de 2010) | Índice real (2010 = 100) |
|:---:|---:|---:|---:|---:|
| 2010 | 633,3 | 105,63 | 633,30 | 100,00 |
| 2011 | 641,4 | 109,01 | 621,51 | 98,14 |
| 2012 | 641,4 | 111,67 | 606,71 | 95,80 |
| 2013 | 645,3 | 113,25 | 601,88 | 95,04 |
| 2014 | 645,3 | 113,08 | 602,79 | 95,18 |
| 2015 | 648,6 | 112,52 | 608,88 | 96,14 |
| 2016 | 655,2 | 112,29 | 616,34 | 97,32 |

**Cómo se calcula.** Como el IPC no está en base 2010, primero lo pasamos a base 2010 dividiendo entre 105,63. Así, SMI real = SMI × 105,63 / IPC. Por ejemplo, 2011: 641,4 × 105,63/109,01 = 621,51 €. El índice real es el SMI real dividido entre 633,3, por 100.

::: {custom-style="Resultado"}
**✅** Aunque el SMI nominal subió un 3,46 % entre 2010 y 2016, en términos reales **bajó un 2,68 %**. El peor año fue 2013 (−4,96 % respecto a 2010).
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** SMI en B2:B8, IPC en C2:C8. SMI real en D2: `=B2*$C$2/C2`. Índice real en E2: `=D2/$D$2*100`. Arrastra las dos.
:::
