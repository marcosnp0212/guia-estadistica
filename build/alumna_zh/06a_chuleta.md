# Chuleta de fórmulas

Excel 一列是西班牙语版的写法（考试时用这个）。`r` = 数据范围。

## Tema 1. 一个变量（Una variable）

| 什么 | 公式 | Excel |
|:---|:---|:---|
| 相对频数（frecuencia relativa） | fᵢ = nᵢ / n | `=B2/$B$9` |
| 累积频数（acumulada） | Nᵢ = n₁ + ... + nᵢ | `=C1+B2` |
| 均值（零散数据） | x̄ = Σxᵢ / n | `=PROMEDIO(r)`（AVERAGE） |
| 均值（表） | x̄ = Σxᵢnᵢ / n = Σxᵢfᵢ | `=SUMAPRODUCTO(x;n)/SUMA(n)`（SUMPRODUCT、SUM） |
| 加权均值（media ponderada） | (x̄₁T₁ + x̄₂T₂ + ...) / (T₁ + T₂ + ...) | `=SUMAPRODUCTO(medias;T)/SUMA(T)` |
| 变换 Y = aX + b | ȳ = a·x̄ + b · S²ᵧ = a²·S²ₓ · Sᵧ = a·Sₓ | |
| 众数（区间） | Lᵢ₋₁ + (dᵢ − dᵢ₋₁)/((dᵢ − dᵢ₋₁) + (dᵢ − dᵢ₊₁)) · aᵢ | `=MODA.UNO(r)`（MODE.SNGL，零散数据） |
| 密度（densidad） | dᵢ = nᵢ / aᵢ | `=C2/(B2-A2)` |
| 中位数（区间） | Lᵢ₋₁ + (n/2 − Nᵢ₋₁)/nᵢ · aᵢ | `=MEDIANA(r)`（MEDIAN，零散数据） |
| 第 r 百分位数（区间） | Lᵢ₋₁ + (r·n/100 − Nᵢ₋₁)/nᵢ · aᵢ | `=PERCENTIL.INC(r;0,7)`（PERCENTILE.INC） |
| 四分位数（cuartiles） | C₁ → n/4 · C₃ → 3n/4 | `=CUARTIL.INC(r;1)`（QUARTILE.INC） |
| 手算中位数或分位数（零散数据或取值表） | 位置 k = r·n/100：不是整数，取下一个位置的数据；是整数，取这个数据和下一个的平均 | |
| 极差（rango） | 最大 − 最小 | `=MAX(r)-MIN(r)` |
| IQR | C₃ − C₁ | |
| 方差（varianza） | S² = Σxᵢ²nᵢ / n − x̄² | `=VAR.P(r)` |
| 修正方差（cuasivarianza） | s² = n/(n−1) · S² | `=VAR.S(r)` |
| 标准差（desviación típica） | S = √S² | `=DESVEST.P(r)`（STDEV.P） |
| 修正标准差（cuasidesviación） | s = √s² | `=DESVEST.S(r)`（STDEV.S） |
| 变异系数（coef. de variación） | CV = S / x̄ | `=DESVEST.P(r)/PROMEDIO(r)` |
| 组内方差（var. dentro） | (S²₁T₁ + S²₂T₂ + ...) / ΣT | |
| 组间方差（var. entre） | ((x̄₁ − x̄)²T₁ + (x̄₂ − x̄)²T₂ + ...) / ΣT | |
| 总方差（var. total） | 组内 + 组间 | |
| 组间百分比 | 组间 / 总方差 × 100 | |
| 偏度（asimetría） | CA > 0 右边有尾巴 · < 0 左边有尾巴 | `=COEFICIENTE.ASIMETRIA.P(r)`（SKEW.P） |
| 峰度（curtosis） | CC > 0 尖峰（lepto）· = 0 常峰（meso）· < 0 低峰（plati） | `=CURTOSIS(r)`（KURT） |
| 标准化（tipificar） | z = (x − x̄) / S | `=NORMALIZACION(x;media;S)`（STANDARDIZE）或 `=(A2-$B$1)/$B$2` |
| 异常值的界限（atípicos） | C₁ − 1,5·IQR 和 C₃ + 1,5·IQR | |
| 截尾均值（media truncada） | 两头各去掉一定百分比的数据，再求均值 | `=MEDIA.ACOTADA(r;0,2)`（TRIMMEAN） |

## Tema 2. 两个变量（Dos variables）

| 什么 | 公式 |
|:---|:---|
| 联合相对频数 | fᵢⱼ = nᵢⱼ / n |
| X 的边缘分布（marginal） | nᵢ. = 第 i 行的和 |
| Y 的边缘分布 | n.ⱼ = 第 j 列的和 |
| 条件分布 X \| Y = yⱼ（condicionada） | 第 j 列（除以 n.ⱼ） |
| 条件分布 Y \| X = xᵢ | 第 i 行（除以 nᵢ.） |
| 独立（independencia） | **所有**格子里 fᵢⱼ = fᵢ. · f.ⱼ |
| 期望频数（手算） | nᵢ. · n.ⱼ / n；如果所有格子都和 nᵢⱼ 一样，就独立 |
| 如果独立 | 所有条件分布彼此相同，也和边缘分布相同 |
| 马赛克图（mosaico） | 列宽 = 边缘分布 · 每块的高 = 条件分布 |

Excel：数据透视表（tabla dinámica；行、列、值 = 计数）；“值显示方式”（Mostrar valores como）→ 占总计 / 行 / 列的百分比。

## Tema 3. 回归（Regresión）

| 什么 | 公式 | Excel（Y 在 B，X 在 A） |
|:---|:---|:---|
| 协方差（covarianza） | S_XY = Σxᵢyᵢ/n − x̄·ȳ | `=COVARIANZA.P(A;B)`（COVARIANCE.P） |
| 斜率（Y 对 X） | b = S_XY / S²ₓ | `=PENDIENTE(B;A)`（SLOPE） |
| 截距（término independiente） | a = ȳ − b·x̄ | `=INTERSECCION.EJE(B;A)`（INTERCEPT） |
| 直线 | Ŷ = a + b·X | |
| X 对 Y 的直线 | b' = S_XY / S²ᵧ · a' = x̄ − b'·ȳ | `=PENDIENTE(A;B)` |
| 相关系数（correlación） | r = S_XY / (Sₓ·Sᵧ) | `=COEF.DE.CORREL(A;B)`（CORREL） |
| 决定系数（determinación） | R² = r² | `=COEFICIENTE.R2(B;A)`（RSQ） |
| 预测（predicción） | Ŷ = a + b·x₀ | `=PRONOSTICO.LINEAL(x0;B;A)`（FORECAST.LINEAR） |
| 有用的关系 | r = b·Sₓ/Sᵧ · S_XY = r·Sₓ·Sᵧ · ȳ = a + b·x̄ | |
| 如果 S_XY = 0 | Ŷ = ȳ（水平）· X̂ = x̄（竖直） | |

记住：两条直线交于 (x̄, ȳ)。r 在 −1 和 1 之间，没有单位，换单位也不变。不要在数据范围之外做预测（外推，extrapolar）。

## Tema 4. 指数（Números índices）

| 什么 | 公式 | Excel |
|:---|:---|:---|
| 简单指数（índice simple） | I = xₜ / x₀ · 100 | `=B3/$B$2*100` |
| 变化率（tasa de variación） | (V₁ − V₀)/V₀ = V₁/V₀ − 1 | `=B3/B2-1` |
| 涨 p % | × (1 + p/100) | |
| 连锁（encadenar） | 把指数相乘 | `=PRODUCTO(r)`（PRODUCT） |
| 倒数（inversión） | I₍ₜ→₀₎ = 1 / I₍₀→ₜ₎ | |
| 换基期（cambio de base） | 旧指数 / 新基期那年的旧指数 · 100 | `=C2/$C$6*100` |
| 几何平均（media geométrica） | (x₁·x₂···xₙ)^(1/n) | `=MEDIA.GEOM(r)`（GEOMEAN） |
| 每期平均变化率 | (1 + T)^(1/k) − 1 | `=(1+T)^(1/k)-1` |
| 拉氏价格指数 | Σpₜq₀ / Σp₀q₀ · 100 | `=SUMAPRODUCTO(pt;q0)/SUMAPRODUCTO(p0;q0)*100` |
| 帕氏价格指数 | Σpₜqₜ / Σp₀qₜ · 100 | `=SUMAPRODUCTO(pt;qt)/SUMAPRODUCTO(p0;qt)*100` |
| 拉氏数量指数 | Σqₜp₀ / Σq₀p₀ · 100 | |
| 帕氏数量指数 | Σqₜpₜ / Σq₀pₜ · 100 | |
| 费雪指数（Fisher） | √(L · P) | `=RAIZ(L*P)`（SQRT） |
| 实际值（平减，deflactar） | 名义值 / IPC · 100 | `=B2/C2*100` |
