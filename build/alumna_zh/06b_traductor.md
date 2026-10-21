# ¿Qué me están pidiendo? Traductor de enunciados

::: {custom-style="Idea"}
**🧠 有什么用。** 很多时候难的不是计算，而是知道**该算什么**。在题目里找一句和左边差不多的话。中间一列告诉你算什么；右边一列告诉你用哪个函数，以及在哪里讲过。左边保留西班牙语，因为考试题就是这样写的。
:::

::: {custom-style="Truco"}
**💡 小技巧。** 用指南的搜索（按 / 键）可以输入题目里的一个词，比如 «homogéneo» 或 «términos reales»，它会找到这张表和讲解它的小节。
:::

## Tema 1：一个变量（una variable）

| 题目里写…… | 要你求…… | 怎么做 / 在哪里 |
|:---|:---|:---|
| "valor medio", "promedio", "por término medio"（平均值） | **均值** | `=PROMEDIO(datos)` · 有表时用 `SUMAPRODUCTO`。[看 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "el más frecuente", "el más habitual", "el que más se repite"（最常见的） | **众数**。区间宽度不同时，按**密度** | `=MODA.UNO(datos)` · 众数公式。[看 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "valor central", "la mitad tiene menos de…"（中间值，一半少于……） | **中位数** | `=MEDIANA(datos)` · 第一个 Nᵢ ≥ n/2。[看 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "el 25 % que menos…"（最少的 25%） | **第一四分位数**（P₂₅） | `=CUARTIL.INC(datos;1)`。[看 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "estar entre el 25 % que más…"（进入最多的 25%） | **第三四分位数**（P₇₅） | `=CUARTIL.INC(datos;3)`。[看 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "el X % que más…", "a partir de cuánto se está en el X % superior"（最高的 X%） | **第 100 − X 百分位数** | 最高的 10%：`=PERCENTIL.INC(datos;0,9)`。[看 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "como mucho, para estar en el X % que menos…"（最多……才在最低的 X%） | **第 X 百分位数** | `=PERCENTIL.INC(datos;X/100)`。[看 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "entre qué valores está el 50 % central"（中间 50%） | **C₁ 和 C₃** | [看 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "entre qué valores está el 30 % central"（中间 30%） | **P₃₅ 和 P₆₅**（两边各留 35%） | 练习题第 13 题 |
| "cuántos tienen más de k" · "al menos k" · "menos de k"（多于 / 至少 / 少于 k） | 数个数。**"Más de" 不包括 k**；"al menos" 包括 | `=CONTAR.SI(datos;">k")` · `">=k"` · `"<k"` |
| "dispersión", "variabilidad", "cuánto se separan"（离散、变异） | **方差**或**标准差** | `=VAR.P` · `=DESVEST.P`。[看 1.7](#medidas-de-dispersión) |
| "más homogéneo", "media más representativa", "variabilidad relativa"，均值不同的组 | **变异系数**。最小的最均匀 | `=DESVEST.P(r)/PROMEDIO(r)`。[看 1.7](#medidas-de-dispersión) |
| "cuasivarianza", "varianza muestral corregida"（修正方差） | 除以 **n − 1** | `=VAR.S` · `=DESVEST.S` |
| "forma", "simétrica", "cola"（形状、对称、尾巴） | **偏度**（看符号） | `=COEFICIENTE.ASIMETRIA.P`。[看 1.8](#medidas-de-forma-asimetría-y-curtosis) |
| "picuda", "aplanada", "apuntamiento"（尖、平） | **峰度**（看符号） | `=CURTOSIS`。[看 1.8](#medidas-de-forma-asimetría-y-curtosis) |
| "valores atípicos", "diagrama de caja"（异常值、箱线图） | 界限 C₁ − 1,5·IQR 和 C₃ + 1,5·IQR | [看 1.10](#valores-atípicos-y-diagrama-de-caja-boxplot) |
| "comparar la nota (o el salario) de alguien en dos grupos distintos"（比较不同组里的两个人） | **标准化**：z = (x − 均值)/S | `=NORMALIZACION(x;media;S)`。[看 1.9](#tipificar-estandarizar-una-variable) |
| "media de toda la empresa"，各组人数不同 | **加权均值** | `=SUMAPRODUCTO(medias;tamaños)/SUMA(tamaños)` |
| "varianza de todos"，由各组算出 | **组内方差 + 组间方差** | [看 1.7](#medidas-de-dispersión) |
| "% de la variabilidad debido a las diferencias entre grupos", "desigualdad"（不平等） | **组间**方差 ÷ **总**方差 | 练习题第 21 题 |
| "todos suben X €" / "suben un X %"：均值和方差会怎样？ | 加：均值加 X，方差**不变**。乘以 a：均值 × a，方差 × **a²** | 练习题第 22 题 |

## Tema 2：两个变量（dos variables）

| 题目里写…… | 要你求…… | 怎么做 / 在哪里 |
|:---|:---|:---|
| "distribución marginal de X"（边缘分布） | 各行的**合计**（Y 的话是各列） | [看 2.2](#distribuciones-marginales) |
| "distribución de Y condicionada a X = …", "de los que…, ¿qué %…?"（条件分布，在……中占百分之几） | 那一**行**（或列）除以**它自己**的合计 | [看 2.3](#distribuciones-condicionadas) |
| "¿son independientes?", "¿influye X en Y?", "¿depende…?"（独立吗？有影响吗？） | 在**所有**格子里比较 fᵢⱼ 和 fᵢ.·f.ⱼ | [看 2.4](#independencia) |
| 双向表的 "frecuencias relativas"（相对频数） | 每个格子 ÷ n | `=B3/$E$6` |

## Tema 3：回归（regresión）

| 题目里写…… | 要你求…… | 怎么做 / 在哪里 |
|:---|:---|:---|
| "recta que explica Y a partir de X", "Y en función de X"（用 X 解释 Y 的直线） | **Y 对 X 的直线**：Ŷ = a + b·X | `=PENDIENTE(Y;X)` · `=INTERSECCION.EJE(Y;X)`。[看 3.3](#la-recta-de-regresión) |
| "cuánto cambia Y por cada unidad de X"（X 每增加一个单位 Y 变多少） | **斜率** b | [看 3.3](#la-recta-de-regresión) |
| "grado o intensidad de la relación lineal", "sentido"（线性关系的强度、方向） | **相关系数** r | `=COEF.DE.CORREL(X;Y)`。[看 3.4](#coeficiente-de-correlación-r-y-de-determinación-r²) |
| "bondad del ajuste", "% explicado", "¿es fiable la recta?"（拟合优度、解释的百分比） | **R²**（用 %） | `=COEFICIENTE.R2(Y;X)`。[看 3.4](#coeficiente-de-correlación-r-y-de-determinación-r²) |
| "% que NO explica"（不能解释的百分比） | **1 − R²** | Tema 3 练习题第 3 题 |
| "¿cuánto se espera de Y si X vale…?", "estima", "predice"（预测） | 把 **X 代入**直线 | `=PRONOSTICO.LINEAL(x;Y;X)`。[看 3.5](#predicciones) |
| "¿relación directa o inversa?", "variación conjunta"（正相关还是负相关） | **协方差**（看符号） | `=COVARIANZA.P(X;Y)`。[看 3.2](#la-covarianza) |
| 给你均值、S 和 Sxy（或 r），但没有数据 | b = Sxy/Sx² · a = ȳ − b·x̄ · r = Sxy/(Sx·Sy) | [看 3.6](#fórmulas-útiles-para-ejercicios-sin-datos) |

## Tema 4：指数（números índices）

| 题目里写…… | 要你求…… | 怎么做 / 在哪里 |
|:---|:---|:---|
| "índice con base 20XX", "evolución respecto a 20XX"（以 20XX 为基期） | **简单指数**：值 ÷ 基期的值 × 100 | `=B3/$B$2*100`。[看 4.1](#índice-simple) |
| "tasa de variación", "cuánto ha subido o bajado"（变化率，涨了 / 降了多少） | 值 ÷ 前一个 − 1 | `=B3/B2-1`。[看 4.2](#tasa-de-variación) |
| "cambia la base a 20XX"（换基期） | 把整个序列除以 20XX 年的指数 | [看 4.4](#cambio-de-base) |
| "subió un X % y luego bajó un Y %"（总共） | **相乘**：(1 + X)·(1 − Y) | [看 4.3](#propiedades-de-los-índices) |
| "tasa media anual", "crecimiento medio por año"（年平均变化率） | **几何平均**：(1 + T)^(1/年数) − 1 | `=MEDIA.GEOM` · `=(1+T)^(1/k)-1`。[看 4.5](#media-geométrica-y-tasas-medias) |
| 和年变化率等价的 "tasa mensual equivalente"（月变化率） | (1 + 年变化率)^(1/12) − 1 | [看 4.5](#media-geométrica-y-tasas-medias) |
| "A superó en un X % a B"（A 比 B 多 X%） | A = (1 + X/100)·B → **B = A ÷ (1 + X/100)** | Tema 4 练习 1 和 2 |
| "índice de precios con las cantidades del año base"（用基期数量） | **拉氏指数（Laspeyres）** | [看 4.6](#índices-complejos-de-varios-productos) |
| "con las cantidades actuales"（用当期数量） | **帕氏指数（Paasche）** | [看 4.6](#índices-complejos-de-varios-productos) |
| "índice de Fisher" | √(Laspeyres · Paasche) | [看 4.6](#índices-complejos-de-varios-productos) |
| "en términos reales", "euros constantes", "poder adquisitivo", "deflactar"（实际值、不变价欧元、购买力、平减） | 名义值 ÷ IPC × 100 | `=B2/C2*100`。[看 4.7](#deflactar-de-euros-nominales-a-euros-reales) |
| "¿está bien actualizado el salario (o el alquiler)?"（工资或房租调整得对吗？） | 和这个比较：值 × 新 IPC ÷ 旧 IPC | Tema 4 练习 4 和 11 |
