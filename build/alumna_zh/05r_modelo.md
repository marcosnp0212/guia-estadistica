# Examen modelo de la profesora

## 考试是什么样的（Cómo es el examen）

老师在课上给大家看了这份期中样卷。这是我们了解真实考试最好的线索。

- **30 道选择题（tipo test）**，每题 4 个选项（A、B、C、D）。只有一个是对的。字母要**大写**写在方框里。
- **10 道简答题（respuesta corta）。** 要“简洁地”回答（de forma concisa）：一个定义、一个公式或者一个简短的计算。
- **纸笔考试。** 关于 Excel 的题是**选择或写出公式**，不用电脑。
- 范围是全部内容：Tema 1、2、3 和 4。

::: {custom-style="Idea"}
**🧠 样卷里能看出什么。** 长计算很少，**理论**很多：定义、公式和会解释结果。有的计算都很短：一个 CV、一个 R²、一个 IQR、一个预测。常见的陷阱还是那些：把百分比相加而不是相乘，把众数区间和频数最大的区间搞混，或者以为 r = 0 就是“没有任何关系”。
:::

**怎么用这一部分。** 考试是用西班牙语的，所以题目和选项保留西班牙语原文，下面附上中文翻译。先读题，**自己决定答案**，再点“看答案”。每个答案都会解释为什么是这个、为什么不是别的，还告诉你在指南的哪里。做完以后，再做**选择题模拟考试（Simulacro tipo test）**：形式一样，但题目是新的，而且会自动批改。

## 选择题：Tema 1（第 1 到 10 题）

### Pregunta 1（第 1 题）

En Excel se desea tipificar una serie de datos de la variable X colocados en A2:A50, restando la media (x̄), que está en la celda $B$1, y dividiendo entre la desviación típica (S), que está en $B$2. ¿Cuál es la fórmula correcta para escribir en B2 y copiar hacia abajo?

A) `=(A2-B1)/B2`
B) `=($A$2-B1)/B2`
C) `=(A$2-$B1)/$B2`
D) `=(A2-$B$1)/$B$2`

*中文：* 在 Excel 里要把变量 X 的一列数据（在 A2:A50）标准化：减去均值 x̄（在单元格 $B$1），再除以标准差 S（在 $B$2）。在 B2 里写什么公式、再往下复制，才是对的？

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 往下复制时，数据要跟着变（A2、A3、A4……），所以 **A2 不加 $**。均值和标准差一直是同样的格子，所以要**用 $ 固定**：$B$1 和 $B$2。

- A）没有 $，往下一行时均值会变成 B2、B3……，结果就乱了。
- B）把数据固定了（$A$2）：每一行都会用第一个数据。
- C）只固定了一半：A$2 让数据没法往下走。

*在指南里：* 1.9 小节（标准化）和“Excel 入门”（带 $ 的引用）。

</details>

### Pregunta 2（第 2 题）

Para calcular la media ponderada de unos datos que están en A2:A10, con sus pesos o frecuencias en B2:B10, ¿cuál es la sintaxis correcta con SUMAPRODUCTO?

A) `=SUMAPRODUCTO(A2:A10;B2:B10)`
B) `=SUMAPRODUCTO(A2:A10;B2:B10)/SUMA(B2:B10)`
C) `=SUMAPRODUCTO(A2:A10/B2:B10)`
D) `=SUMA(A2:A10)*SUMAPRODUCTO(B2:B10)/CONTAR(A2:A10)`

*中文：* 数据在 A2:A10，权重或频数在 B2:B10，要算加权平均数。用 SUMAPRODUCTO 的正确写法是哪个？

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 表格的均值是 Σxᵢ·nᵢ / n。SUMAPRODUCTO 算出 Σxᵢ·nᵢ，SUMA(B2:B10) 就是 n（频数或权重之和）。

- A）少了除法：这只是分子。
- C）用数据除以权重，没有意义。
- D）乱七八糟地混在一起，没有意义。

*在指南里：* 表格的均值和加权平均数（1.5 小节），以及公式表。

</details>

### Pregunta 3（第 3 题）

En un estudio se registra el nivel de *satisfacción laboral* (Bajo, Medio, Alto) y el *salario bruto anual* (en euros). ¿Cómo se clasifican?

A) Satisfacción cualitativa nominal y salario cuantitativo discreto
B) Satisfacción cualitativa **ordinal** y salario cuantitativo **continuo**
C) Ambas cuantitativas continuas
D) Satisfacción cualitativa ordinal y salario cualitativo nominal

*中文：* 一项研究记录了*工作满意度*（低、中、高）和*年税前工资*（欧元）。它们属于什么类型？A）满意度是名义型分类变量，工资是离散型数量变量；B）满意度是**有序型**分类变量，工资是**连续型**数量变量；C）两个都是连续型数量变量；D）满意度是有序型分类变量，工资是名义型分类变量。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 低、中、高是词（分类变量），而且**有顺序**（有序型）。工资是一个数，可以有分（小数）：**连续型**数量变量。

- A）名义型是没有顺序的（比如部门）。
- C）满意度不是数。
- D）工资不是分类变量。

*在指南里：* 1.2 小节（变量的类型）。

</details>

### Pregunta 4（第 4 题）

Sea X una variable con media x̄. Si aplicamos Y = aX + b, ¿qué propiedad es correcta?

A) La suma de las desviaciones a la media es siempre positiva
B) ȳ = x̄ + b y la varianza no se altera
C) El CV no cambia aunque haya cambio de origen b ≠ 0
D) **ȳ = a·x̄ + b y S²ᵧ = a²·S²ₓ**

*中文：* X 是一个变量，均值是 x̄。如果做 Y = aX + b，哪个性质是对的？A）离差之和永远是正的；B）ȳ = x̄ + b，方差不变；C）即使有平移 b ≠ 0，CV 也不变；D）ȳ = a·x̄ + b，S²ᵧ = a²·S²ₓ。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 均值受到全部变化（乘以 a，再加 b）。方差只受乘法影响，而且是平方：加 b 让所有数据移动得一样多，不改变离散程度。

- A）离差之和**永远是 0**，不是正的。
- B）忘了 a。
- C）加上 b，均值变了而 S 没变，所以 CV **会变**。

*在指南里：* 1.5 小节（均值以及平移和缩放）和 1.7 小节（对离散程度的影响）。

</details>

### Pregunta 5（第 5 题）

¿En qué caso es especialmente preferible la mediana o la media truncada en lugar de la media aritmética?

A) Distribución perfectamente simétrica y sin atípicos
B) **Datos con valores extremos (outliers) que distorsionan la tendencia central**
C) Solo cuando la variable es cualitativa nominal
D) Cuando hay más de un millón de datos agrupados

*中文：* 在什么情况下，用中位数或截尾均值比用算术平均数特别好？A）完全对称、没有异常值的分布；B）有极端值（异常值）扭曲了集中趋势；C）只有变量是名义型分类变量的时候；D）分组数据超过一百万个的时候。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 均值会被极端值拉走。中位数和截尾均值（两头各去掉一定比例的数据）是**稳健的**：不受影响。

- A）如果对称又没有异常值，均值就很好。
- C）名义型变量既没有均值也没有中位数：只有众数。
- D）数据多少和这个没关系。

*在指南里：* 1.5 小节（截尾均值和“均值、中位数还是众数：用哪个？”）。

</details>

### Pregunta 6（第 6 题）

En datos agrupados en intervalos de **distinta amplitud**, ¿cómo se determina el intervalo modal?

A) El de mayor frecuencia absoluta nᵢ
B) **El de mayor densidad dᵢ = nᵢ / aᵢ**
C) El que contiene la mediana
D) El de mayor marca de clase

*中文：* 数据分组成**宽度不同**的区间时，怎么确定众数区间？A）绝对频数 nᵢ 最大的；B）密度 dᵢ = nᵢ / aᵢ 最大的；C）包含中位数的那个；D）组中值最大的。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 如果区间宽度不同，宽的区间数据多只是因为它宽。要比较，就得看**每单位宽度**有多少数据：也就是密度。

- A）只有所有区间一样宽时才对。这是典型陷阱。
- C）和 D）跟众数没关系。

*在指南里：* 1.5 小节（区间数据的众数）和练习题第 15 题。

</details>

### Pregunta 7（第 7 题）

Respecto al coeficiente de variación (CV = S / x̄), señala la afirmación correcta.

A) Expresa la dispersión en las mismas unidades que la variable
B) Es negativo cuando la dispersión es muy alta
C) **Permite comparar la variabilidad relativa de poblaciones con unidades o escalas distintas**
D) Mide la asimetría respecto a la moda

*中文：* 关于变异系数（CV = S / x̄），哪个说法是对的？A）它用和变量相同的单位表示离散程度；B）离散程度很大时它是负的；C）它可以比较单位或尺度不同的总体的相对变异；D）它衡量相对于众数的偏度。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** S 除以均值，单位就约掉了：CV 是一个纯数（或者 %）。所以可以用来比较公斤和克，或者工资和身高。

- A）那是标准差，不是 CV。
- B）S 永远不是负的；均值是正的时，CV 也不是负的。
- D）偏度用费希尔系数衡量。

*在指南里：* 1.7 小节（变异系数）。

</details>

### Pregunta 8（第 8 题）

Al descomponer la varianza total de una población dividida en k grupos se cumple:

A) Total = dentro × entre
B) La varianza dentro mide la diferencia de las medias de los grupos
C) **Varianza total = varianza dentro (intrapoblacional) + varianza entre (interpoblacional)**
D) Si el 95 % es interpoblacional, los grupos son idénticos

*中文：* 把分成 k 个组的总体的总方差分解时，下面哪个成立？A）总方差 = 组内 × 组间；B）组内方差衡量各组均值的差别；C）总方差 = 组内方差 + 组间方差；D）如果 95% 是组间方差，这些组完全一样。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** 总方差分成两部分，两部分**相加**：每个组内部的方差，和各组均值之间的方差。

- A）是相加，不是相乘。
- B）那是**组间**方差，不是组内。
- D）正好相反：如果几乎都是“组间”，说明各组**差别很大**。

*在指南里：* 1.7 小节（分组的方差）和练习题第 13、14、21 题。

</details>

### Pregunta 9（第 9 题）

Si el coeficiente de asimetría de Fisher es CA > 0, esto indica que:

A) Es simétrica y mesocúrtica
B) **Asimetría positiva o a la derecha: hay una cola de valores altos hacia la derecha**
C) Asimetría negativa, con los datos concentrados a la derecha
D) La moda coincide con el máximo

*中文：* 如果费希尔偏度系数 CA > 0，说明：A）对称且常峰；B）正偏或右偏：右边有一条由大值组成的尾巴；C）负偏，数据集中在右边；D）众数等于最大值。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** CA > 0 → 右边有长尾巴（少数几个很大的值），均值在中位数上面。典型例子：工资。

- A）对称是 CA = 0。
- C）那是 CA < 0。
- D）没有意义。

*在指南里：* 1.8 小节（偏度和峰度）。

</details>

### Pregunta 10（第 10 题）

En un diagrama de caja, ¿qué datos se consideran atípicos?

A) **x < C₁ − 1,5·IQR o x > C₃ + 1,5·IQR, con IQR = C₃ − C₁**
B) x < x̄ − S o x > x̄ + S
C) Cualquier valor por debajo de P₁₀ o por encima de P₉₀
D) x < C₂ − IQR o x > C₂ + IQR

*中文：* 在箱线图里，哪些数据算异常值？A）x < C₁ − 1,5·IQR 或 x > C₃ + 1,5·IQR，其中 IQR = C₃ − C₁；B）x < x̄ − S 或 x > x̄ + S；C）任何低于 P₁₀ 或高于 P₉₀ 的值；D）x < C₂ − IQR 或 x > C₂ + IQR。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 这是讲义里的规则：界限在箱子外面 1,5 倍 IQR 的地方。

- B）用这个规则，差不多三分之一的数据都会成为“异常值”。
- C）按定义永远会有 20% 的异常值。
- D）用的是中位数，而且没有 1,5。

*在指南里：* 1.10 小节（异常值和箱线图）。

</details>

## 选择题：Tema 2（第 11 到 15 题）

### Pregunta 11（第 11 题）

En una tabla de doble entrada, la celda (i, j) tiene nᵢⱼ. ¿Cómo se obtiene la frecuencia marginal nᵢ. de la categoría xᵢ?

A) **Sumando las frecuencias de la fila i a lo largo de todas las columnas: nᵢ. = Σⱼ nᵢⱼ**
B) Dividiendo nᵢⱼ entre n
C) Multiplicando las marginales de xᵢ y yⱼ
D) Restando la suma de la columna j al total n

*中文：* 在列联表里，格子 (i, j) 的频数是 nᵢⱼ。类别 xᵢ 的边缘频数 nᵢ. 怎么得到？A）把第 i 行所有列的频数加起来：nᵢ. = Σⱼ nᵢⱼ；B）nᵢⱼ 除以 n；C）xᵢ 和 yⱼ 的边缘频数相乘；D）总数 n 减去第 j 列的和。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 一行的边缘频数就是这一行的合计：写在右边边上的那个数。

- B）那是联合相对频数 fᵢⱼ。
- C）那是检验独立性时用的（期望频数）。
- D）没有意义。

*在指南里：* 2.2 小节（边缘分布）。

</details>

### Pregunta 12（第 12 题）

X e Y son estadísticamente independientes si y solo si, para todas las casillas:

A) **fᵢⱼ = fᵢ. · f.ⱼ**
B) Todas las nᵢⱼ son iguales
C) S_XY > 0
D) Las condicionadas de Y varían mucho según X

*中文：* X 和 Y 统计独立，当且仅当对所有格子：A）fᵢⱼ = fᵢ. · f.ⱼ；B）所有 nᵢⱼ 都相等；C）S_XY > 0；D）Y 的条件分布随 X 变化很大。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 这是定义：在**所有**格子里，联合相对频数等于边缘频数的乘积。

- B）不需要相等。
- C）如果独立，协方差是 0，不是正的。
- D）正好相反：如果条件分布变化，说明**有**关系。

*在指南里：* 2.4 小节（独立性）。

</details>

### Pregunta 13（第 13 题）

Si X e Y son independientes, ¿qué relación hay entre las condicionadas Y | X = xᵢ y la marginal de Y?

A) Son inversamente proporcionales
B) No se pueden calcular
C) **Todas las condicionadas son iguales entre sí e iguales a la marginal de Y**
D) Suman 0

*中文：* 如果 X 和 Y 独立，条件分布 Y | X = xᵢ 和 Y 的边缘分布有什么关系？A）成反比；B）算不出来；C）所有条件分布彼此相等，而且都等于 Y 的边缘分布；D）加起来等于 0。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** 独立的意思是知道 X 对 Y 没有任何影响。所以 Y 的分布在每一行都一样，并且和总体的分布一样。

*在指南里：* 2.3 和 2.4 小节。

</details>

### Pregunta 14（第 14 题）

En un gráfico de mosaico de dos variables cualitativas, ¿qué refleja la frecuencia marginal de la variable principal?

A) **El ancho de las columnas**
B) La intensidad del color
C) La inclinación de las diagonales
D) El número de sectores

*中文：* 在两个分类变量的马赛克图里，主变量的边缘频数用什么表示？A）列的宽度；B）颜色的深浅；C）对角线的倾斜；D）扇形的个数。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 在马赛克图里，每一列是一个类别，**列的宽度就是它的边缘频数**。列里每一块的高度是条件频数。

*在指南里：* 2.1 小节（双变量的图形）。

</details>

### Pregunta 15（第 15 题）

Género (Hombre, Mujer) y jornada (Completa, Parcial) en 200 empleados. La proporción marginal de jornada completa es 0,70 y las variables son **independientes**. ¿Qué proporción de hombres tiene jornada completa en la condicionada Y | Hombre?

A) 0,30
B) **0,70**
C) 0,35
D) Depende del número de hombres

*中文：* 200 名员工的性别（男、女）和工作时间（全职、兼职）。全职的边缘比例是 0,70，两个变量**独立**。在条件分布 Y | 男 里，全职男性的比例是多少？A）0,30；B）0,70；C）0,35；D）取决于男性的人数。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 如果独立，条件分布等于边缘分布（第 13 题）。如果总体有 70% 是全职，男性里也有 70% 是全职。

- A）0,30 是兼职的比例。
- C）0,35 是假设一半是男性再相乘：那是联合比例，不是条件比例。
- D）独立时和这个无关。

*在指南里：* 2.3 和 2.4 小节。

</details>

## 选择题：Tema 3（第 16 到 23 题）

### Pregunta 16（第 16 题）

En una nube de puntos de antigüedad (X) y salario (Y), los puntos forman una nube alargada que sube de izquierda a derecha. ¿Qué relación hay?

A) **Lineal directa o positiva (S_XY > 0)**
B) Lineal inversa (S_XY < 0)
C) Ninguna relación
D) No lineal cuadrática con correlación nula

*中文：* 在工龄（X）和工资（Y）的散点图里，点形成一团从左到右往上走的长条。是什么关系？A）正向线性关系（S_XY > 0）；B）反向线性关系（S_XY < 0）；C）没有关系；D）相关系数为零的二次非线性关系。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 点往上走，说明 X 变大时 Y 也变大：正向关系，协方差是正的。

*在指南里：* 3.1 小节（散点图）和 3.2 小节（协方差）。

</details>

### Pregunta 17（第 17 题）

¿Qué expresión es la covarianza entre X e Y?

A) **S_XY = (1/n) · Σᵢ Σⱼ xᵢ · yⱼ · nᵢⱼ − x̄ · ȳ** · (las otras opciones son fórmulas incorrectas)

*中文：* X 和 Y 的协方差是哪个式子？（其他选项都是错误的公式。）

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 这是列联表的实用公式：乘积的均值减去均值的乘积。零散数据也一样，只是没有 nᵢⱼ：Σxᵢyᵢ / n − x̄·ȳ。

记住其他公式，好区分它们：r = S_XY / (Sₓ·Sᵧ)，b = S_XY / S²ₓ。

*在指南里：* 3.2 小节（协方差，也有频数表的情况）。

</details>

### Pregunta 18（第 18 题）

Para la recta de Y sobre X, Ŷ = a + bX, ¿cómo se calculan b y a?

A) b = S_XY/S²ᵧ y a = x̄ − bȳ
B) b = r·Sₓ y a = ȳ + bx̄
C) b = S²ₓ/S_XY y a = ȳ·x̄
D) **b = S_XY/S²ₓ y a = ȳ − b·x̄**

*中文：* Y 对 X 的回归直线 Ŷ = a + bX，b 和 a 怎么算？

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 斜率是协方差除以 **X**（用来解释的那个变量）的方差。因为直线经过 (x̄, ȳ)，所以 a = ȳ − b·x̄。

- A）这是 **X 对 Y** 的直线的公式，而且写错了。
- B）正确的关系是 b = r · Sᵧ / Sₓ，而且 a 里是减号。
- C）分子分母颠倒了。

*在指南里：* 3.3 小节（回归直线）。

</details>

### Pregunta 19（第 19 题）

¿Qué propiedad comparten la recta de Y sobre X y la de X sobre Y?

A) Tienen la misma pendiente
B) **Se cortan siempre en el punto de medias (x̄, ȳ)**
C) Son perpendiculares
D) Sus términos independientes suman 0

*中文：* Y 对 X 的直线和 X 对 Y 的直线有什么共同点？A）斜率相同；B）永远在均值点 (x̄, ȳ) 相交；C）互相垂直；D）它们的截距加起来等于 0。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：B。** 两条直线都经过 (x̄, ȳ)，所以在这里相交。

- A）斜率不同：一个除以 S²ₓ，一个除以 S²ᵧ。
- C）只有协方差为 0 时才垂直（第 22 题）。

*在指南里：* 3.3 小节（X 对 Y 的直线）。

</details>

### Pregunta 20（第 20 题）

El coeficiente de correlación de Pearson r = S_XY / (Sₓ·Sᵧ) cumple:

A) **Está entre −1 y 1 y no tiene unidades (es adimensional)**
B) Cambia según las unidades de X e Y
C) r = 0 garantiza que no hay ninguna relación, ni lineal ni curva
D) Si r = −1, la pendiente es positiva

*中文：* 皮尔逊相关系数 r = S_XY / (Sₓ·Sᵧ) 满足：A）在 −1 和 1 之间，没有单位（无量纲）；B）随 X 和 Y 的单位变化；C）r = 0 保证没有任何关系，线性和曲线都没有；D）如果 r = −1，斜率是正的。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。**

- B）正好相反：r **不随**单位变化。
- C）r = 0 只说明没有**线性**关系。可能有曲线关系。
- D）r 和斜率的正负号永远相同：r = −1 时斜率是负的。

*在指南里：* 3.4 小节。

</details>

### Pregunta 21（第 21 题）

Si en un ajuste por regresión R² = 0,81, ¿cómo se interpreta?

A) La pendiente es 0,81
B) La covarianza es 0,81
C) **El 81 % de la variabilidad de Y queda explicada por la recta**
D) Hay un error del 81 %

*中文：* 如果回归拟合的 R² = 0,81，怎么解释？A）斜率是 0,81；B）协方差是 0,81；C）Y 的变异有 81% 被直线解释了；D）有 81% 的误差。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** 这就是 R² 的解释句。剩下的 19% 直线解释不了。

*在指南里：* 3.4 小节（决定系数）。

</details>

### Pregunta 22（第 22 题）

Si S_XY = 0, ¿qué forma tienen las rectas de Y sobre X y de X sobre Y?

A) **La de Y sobre X es horizontal (Ŷ = ȳ) y la de X sobre Y es vertical (X̂ = x̄)**
B) Las dos coinciden con la diagonal de 45°
C) Sus pendientes tienden a infinito
D) R² vale 1

*中文：* 如果 S_XY = 0，Y 对 X 的直线和 X 对 Y 的直线是什么样子？A）Y 对 X 的是水平线（Ŷ = ȳ），X 对 Y 的是竖直线（X̂ = x̄）；B）两条都和 45° 对角线重合；C）斜率趋向无穷大；D）R² 等于 1。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 协方差为 0 时，两个斜率都是 0。Y 对 X 变成 Ŷ = ȳ（永远预测均值：水平线），X 对 Y 变成 X̂ = x̄（在同样的坐标轴上是竖直线）。

- D）正好相反：R² = 0，直线什么也解释不了。

*在指南里：* 3.3 小节（特殊情况：协方差为 0）。

</details>

### Pregunta 23（第 23 题）

Con el modelo Salario = 1390 + 78,5 · Antigüedad (R² = 0,92), ¿qué salario medio se estima para 10 años de antigüedad?

A) 1390 €
B) 785 €
C) 2310,5 €
D) **2175 €**

*中文：* 模型是 工资 = 1390 + 78,5 · 工龄（R² = 0,92）。工龄 10 年时，估计的平均工资是多少？

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 代入 X = 10：1390 + 78,5 · 10 = 1390 + 785 = **2175 €**。

- A）这只是起点（0 年）。
- B）这只是 10 年增加的部分。
- C）不是任何正确计算的结果。

计算时不用 R²：它只说明这个预测可靠。

*在指南里：* 3.5 小节（预测）。

</details>

## 选择题：Tema 4（第 24 到 30 题）

### Pregunta 24（第 24 题）

Un índice simple de salarios vale I₂₀₁₅²⁰²⁵ = 125,4 con base 2015 = 100. ¿Qué significa?

A) El salario bajó un 25,4 %
B) El salario en 2025 es 125,4 €
C) El poder adquisitivo subió un 125,4 %
D) **El salario subió un 25,4 % en 2025 respecto a 2015**

*中文：* 工资的简单指数 I₂₀₁₅²⁰²⁵ = 125,4，基期 2015 = 100。这是什么意思？A）工资下降了 25,4%；B）2025 年的工资是 125,4 €；C）购买力上升了 125,4%；D）2025 年的工资比 2015 年上涨了 25,4%。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 指数 − 100 = 变化的百分比：125,4 − 100 = +25,4%。

- B）指数不是欧元。
- C）这是名义指数：没有扣除通货膨胀，而且涨幅是 25,4%，不是 125,4%。

*在指南里：* 4.1 小节（简单指数）。

</details>

### Pregunta 25（第 25 题）

Según la propiedad de **inversión** de los índices simples:

A) **I_t^0 = 1 / I_0^t**
B) I_t^0 = I_t^k + I_k^0
C) I_t^0 = 100 − I_0^t
D) I_t^0 = (I_0^t)²

*中文：* 根据简单指数的**倒数性质（inversión）**：

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** “反过来”的指数是倒数。用小数表示：如果从 2015 到 2019 乘以 1,10，那么从 2019 到 2015 就是乘以 1/1,10 = 0,909。

- B）把它和连锁（encadenamiento）搞混了，而且连锁是**相乘**，不是相加。

*在指南里：* 4.3 小节（指数的性质）。

</details>

### Pregunta 26（第 26 题）

Para calcular la tasa media anual de algo que crece con porcentajes encadenados durante n periodos, la media adecuada es:

A) La media aritmética de las tasas
B) La mediana de los incrementos en euros
C) **La media geométrica: ⁿ√((1+t₁)(1+t₂)···(1+tₙ)) − 1**
D) La moda de las tasas

*中文：* 某个东西在 n 个时期里按连续的百分比增长，要算年平均变化率，合适的平均数是：A）各变化率的算术平均；B）以欧元计的增量的中位数；C）几何平均数；D）各变化率的众数。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** 百分比是通过**相乘**连起来的，所以正确的平均数是几何平均数：把各系数相乘，开 n 次方，再减 1。

- A）算术平均会得到错误的结果：涨 10% 再跌 10%，会得出 0%，实际上你少了 1%。

*在指南里：* 4.5 小节（几何平均数和平均变化率）。

</details>

### Pregunta 27（第 27 题）

Si la tasa anual es del 6 %, ¿cómo se obtiene la tasa mensual equivalente?

A) 0,06/12 = 0,5 %
B) (1 + 0,06)¹² − 1
C) **(1 + 0,06)^(1/12) − 1 ≈ 0,486 %**
D) √0,06 ≈ 24,49 %

*中文：* 如果年变化率是 6%，等价的月变化率怎么算？

<details><summary>看答案（Ver la solución）</summary>

**正确答案：C。** 从一年换成一个月，要对系数 1,06 开 12 次方（也就是 1/12 次幂），再减 1。结果是 0,487%（老师四舍五入成了 0,486%）。

- A）除以 12 就是陷阱：百分比不能直接除，因为它们是连乘的。
- B）这是从月换成年（反过来了）。

*在指南里：* 4.5 小节（等价年率）。在 Excel 里：`=1,06^(1/12)-1`。

</details>

### Pregunta 28（第 28 题）

En el índice de precios de **Laspeyres**, ¿qué ponderación tienen los precios?

A) **Las cantidades del periodo base (q₀)**
B) Las cantidades del periodo actual (qₜ)
C) El promedio de los precios
D) La tasa de variación de las ventas

*中文：* 在**拉氏**价格指数里，价格用什么加权？A）基期的数量（q₀）；B）当期的数量（qₜ）；C）价格的平均数；D）销售额的变化率。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 拉氏指数保持基期的篮子不变：L = Σpₜq₀ / Σp₀q₀。

- B）那是**帕氏指数**：Σpₜqₜ / Σp₀qₜ。

*在指南里：* 4.6 小节（拉氏和帕氏）。小技巧：**L**aspeyres = 基期的数量，西班牙语 "de **L**a base"。

</details>

### Pregunta 29（第 29 题）

¿Qué diferencia fundamental hay entre Laspeyres y Paasche?

A) **Laspeyres tiende a sobreestimar la subida de precios porque mantiene fijas las cantidades de la cesta base; Paasche usa las del periodo actual**
B) Laspeyres mide cantidades y Paasche tipos de interés
C) Paasche no se puede calcular con más de tres bienes
D) Laspeyres es una media geométrica y Paasche una armónica

*中文：* 拉氏和帕氏指数的根本区别是什么？A）拉氏指数因为固定了基期篮子的数量，往往会高估价格的上涨；帕氏指数用当期的数量；B）拉氏衡量数量，帕氏衡量利率；C）商品超过三种时帕氏指数算不出来；D）拉氏是几何平均，帕氏是调和平均。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：A。** 某样东西涨价很多时，人们就会少买。拉氏指数不知道这一点（它用旧的篮子），所以会夸大通货膨胀。帕氏指数用新的篮子，往往会偏低。

*在指南里：* 4.6 小节（为什么有三种指数？）。

</details>

### Pregunta 30（第 30 题）

Deflactar una serie de salarios nominales consiste en:

A) Multiplicar por la tasa de desempleo
B) Sumar la inflación al salario
C) Restar la cuasivarianza de los precios
D) **Dividir el salario nominal de cada periodo entre el índice de precios (IPC) en base 1, para obtener el salario real a poder adquisitivo constante**

*中文：* 对一列名义工资做平减，就是：A）乘以失业率；B）把通货膨胀加到工资上；C）减去价格的准方差；D）把每一期的名义工资除以以 1 为基数的价格指数（IPC），得到购买力不变的实际工资。

<details><summary>看答案（Ver la solución）</summary>

**正确答案：D。** 实际值 = 名义值 / IPC（用小数表示）。IPC 以 100 为基数时也一样，只是要乘以 100：名义值 / IPC × 100。

*在指南里：* 4.7 小节（平减）。

</details>

## 简答题（Respuesta corta，P1 到 P10）

::: {custom-style="Ojo"}
**⚠️ 考试要用西班牙语回答。** 每道题先给中文解答，方便你理解；下面附上西班牙语的参考答案，考试时可以照着这个样子写。
:::

### P1. 参数和统计量（Parámetro y estadístico）

Define brevemente ambos conceptos.

*中文：* 简要定义这两个概念。

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** **参数**是描述整个**总体**的指标（比如西班牙所有劳动者的平均值）。**统计量**是在**样本**里算出的同一种指标（比如 200 个受访者的平均值）。统计量用来估计参数。

**西班牙语：** Un **parámetro** es una medida que describe a toda la **población** (por ejemplo, la media de todos los trabajadores de España). Un **estadístico** es la misma medida calculada en una **muestra** (la media de los 200 encuestados). El estadístico sirve para estimar el parámetro.

*在指南里：* 1.1 小节（基本词汇）。

</details>

### P2. 频数密度和众数区间（Densidad de frecuencia e intervalo modal）

Al construir un histograma con intervalos de distinta amplitud aᵢ, ¿qué magnitud se debe representar en el eje de alturas?

*中文：* 用宽度 aᵢ 不同的区间画直方图时，纵轴（高度）应该表示什么量？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** **频数密度**，dᵢ = nᵢ / aᵢ（或 fᵢ / aᵢ）。这样每个条形的**面积**和它的频数成比例，宽的区间不会只因为宽就显得频数多。众数区间是**密度最大**的那个。

**西班牙语：** La **densidad de frecuencia**, dᵢ = nᵢ / aᵢ (o fᵢ / aᵢ). Así el **área** de cada barra es proporcional a su frecuencia y los intervalos anchos no parecen más frecuentes solo por ser anchos. El intervalo modal es el de **mayor densidad**.

*在指南里：* 1.4 小节（直方图）和 1.5 小节（众数）。

</details>

### P3. 稳健性和箱线图（Robustez y diagrama de caja）

¿Por qué el diagrama de caja es preferible a la media y la desviación típica cuando hay un fuerte sesgo y valores atípicos?

*中文：* 当数据严重偏斜、有异常值时，为什么箱线图比均值和标准差更好？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** 因为它是用**中位数和四分位数**做的，这些指标是**稳健的**：不会被极端值拉走。均值和标准差会被异常值扭曲。而且，箱线图能直接**显示**异常值和偏度（中位数的位置和须的长度）。

**西班牙语：** Porque se construye con la **mediana y los cuartiles**, que son medidas **robustas**: no se dejan arrastrar por los valores extremos. La media y la desviación típica sí se distorsionan con los atípicos. Además, el diagrama de caja **muestra** directamente los atípicos y la asimetría (posición de la mediana y longitud de los bigotes).

*在指南里：* 1.5 和 1.10 小节。

</details>

### P4. 方差分解（Descomposición de la varianza）

En una población dividida en k subgrupos, escribe la descomposición de la varianza total.

*中文：* 一个总体分成 k 个子组，写出总方差的分解。

<details><summary>看答案（Ver la solución）</summary>

**参考答案：**

S² = 组内方差 + 组间方差（varianza dentro + varianza entre）

- 组内（intrapoblacional）= Σ Sᵢ² · nᵢ / n：各组方差的平均。
- 组间（interpoblacional）= Σ (x̄ᵢ − x̄)² · nᵢ / n：各组均值离总均值有多远。

**西班牙语：** S² = varianza dentro + varianza entre. Dentro (intrapoblacional) = Σ Sᵢ² · nᵢ / n: la media de las varianzas de cada grupo. Entre (interpoblacional) = Σ (x̄ᵢ − x̄)² · nᵢ / n: lo que se separan las medias de los grupos de la media global.

*在指南里：* 1.7 小节和公式表。

</details>

### P5. 变异系数（Coeficiente de variación）

Producto A: media 40 kg, S = 8 kg. Producto B: media 200 g, S = 30 g. Calcula el CV de cada uno e indica cuál tiene más variabilidad relativa.

*中文：* 产品 A：均值 40 公斤，S = 8 公斤。产品 B：均值 200 克，S = 30 克。算出各自的 CV，并说明哪个的相对变异更大。

<details><summary>看答案（Ver la solución）</summary>

**参考答案：**

- CV A = 8 / 40 = **0,20**（20%）。
- CV B = 30 / 200 = **0,15**（15%）。

**产品 A** 的相对变异更大。单位不同（公斤和克），所以要用 CV，不能用 S。

**西班牙语：** CV A = 8 / 40 = 0,20 (20 %). CV B = 30 / 200 = 0,15 (15 %). El **producto A** tiene más variabilidad relativa. Las unidades son distintas (kg y g), y por eso hay que usar el CV y no S.

*在指南里：* 1.7 小节。

</details>

### P6. 决定系数（Coeficiente de determinación）

Si r = −0,85, ¿cuánto vale R² y qué porcentaje de la varianza de Y explica la recta?

*中文：* 如果 r = −0,85，R² 是多少？直线解释了 Y 的方差的百分之几？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** R² = (−0,85)² = **0,7225**。直线解释了 Y 的变异的 **72,25%**。平方以后 r 的正负号没有了；负号只说明关系是反向的。

**西班牙语：** R² = (−0,85)² = 0,7225. La recta explica el **72,25 %** de la variabilidad de Y. El signo de r desaparece al elevar al cuadrado; solo dice que la relación es inversa.

*在指南里：* 3.4 小节。

</details>

### P7. 在 Excel 里算平均变化率（Tasa media en Excel）

Una inversión ha tenido tasas del +5 %, +10 % y −2 % en 3 años (1,05; 1,10; 0,98 en A1:A3). ¿Qué fórmula de Excel da la tasa media anual?

*中文：* 一项投资 3 年的变化率是 +5%、+10% 和 −2%（A1:A3 里是 1,05；1,10；0,98）。哪个 Excel 公式能算出年平均变化率？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** `=MEDIA.GEOM(A1:A3)-1`，或者 `=PRODUCTO(A1:A3)^(1/3)-1`。（英文版：GEOMEAN、PRODUCT。）

计算：1,05 · 1,10 · 0,98 = 1,1319。开三次方：1,0422。平均变化率：**每年 4,22%**。不能用 `=PROMEDIO`，它会得出一个错误的 4,33%。

**西班牙语：** `=MEDIA.GEOM(A1:A3)-1`, o también `=PRODUCTO(A1:A3)^(1/3)-1`. Tasa media: 4,22 % anual. No vale `=PROMEDIO`, que daría un 4,33 % falso.

*在指南里：* 4.5 小节。

</details>

### P8. 在范围以外预测（Predecir fuera del rango）

¿Por qué no es recomendable usar la recta para predecir Y con un valor de X muy fuera del rango observado?

*中文：* 为什么不建议用回归直线去预测 X 远远超出观测范围时的 Y？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** 因为这条直线只在**数据的范围内**得到过验证。在范围以外，我们不知道关系是否还是线性的（可能改变、停滞或变弯），所以预测可能错得很厉害。在范围以外预测叫**外推（extrapolar）**。

**西班牙语：** Porque la recta solo está comprobada **dentro del rango de los datos**. Fuera de él no sabemos si la relación sigue siendo lineal (puede cambiar, estancarse o curvarse), así que la predicción puede ser muy errónea. Predecir fuera del rango se llama **extrapolar**.

*在指南里：* 3.4 小节（不要在数据范围以外预测）。

</details>

### P9. 换单位和 r（Cambio de unidades y r）

Si X pasa de euros a miles de euros, ¿cómo cambia r?

*中文：* 如果 X 从欧元换成千欧元，r 怎么变？

<details><summary>看答案（Ver la solución）</summary>

**参考答案：** **不变。** r 没有单位（无量纲）：除以 1000 时，协方差和 Sₓ 按同样的比例变化，互相抵消。只有乘以一个负数时，r 才会改变正负号。

**西班牙语：** **No cambia.** r no tiene unidades (es adimensional): al dividir entre miles cambian la covarianza y Sₓ en la misma proporción y se compensan. Solo cambiaría de signo si se multiplicara por un número negativo.

*在指南里：* 3.4 小节。

</details>

### P10. 等待时间的箱线图（Diagrama de caja de tiempos de espera）

Diagrama de caja de tiempos de espera (minutos): mínimo 5, Q₁ = 8, Me = 11, Q₃ = 16, bigote superior hasta unos 23 y un atípico en 27. Calcula el IQR, el límite teórico superior para considerar un dato atípico y el tipo de asimetría.

*中文：* 等待时间（分钟）的箱线图：最小值 5，Q₁ = 8，Me = 11，Q₃ = 16，上面的须到大约 23，在 27 有一个异常值。算出 IQR、判断异常值的理论上界，以及偏度的类型。

<details><summary>看答案（Ver la solución）</summary>

**参考答案：**

- IQR = Q₃ − Q₁ = 16 − 8 = **8 分钟**。
- 上界 = Q₃ + 1,5 · IQR = 16 + 12 = **28 分钟**。高于 28 的数据是异常值。
- **正偏（向右偏）：** 中位数（11）离 Q₁（8 → 距离 3）比离 Q₃（16 → 距离 5）更近，而且上面的须（16 到 23）比下面的须（5 到 8）长得多。

**西班牙语：** IQR = 16 − 8 = 8 minutos. Límite superior = Q₃ + 1,5 · IQR = 16 + 12 = 28 minutos. Asimetría positiva (a la derecha): la mediana está más cerca de Q₁ que de Q₃ y el bigote superior es mucho más largo que el inferior.

::: {custom-style="Ojo"}
**⚠️ 题目本身有一个矛盾。** 按公式，上界是 28，所以 27 **不是**异常值，虽然图上把它标成了异常值。考试时，写公式算出的 28；如果愿意，再加一句："según el límite calculado, 27 no sería atípico"（按算出的界限，27 不算异常值）。
:::

*在指南里：* 1.10 小节。

</details>
