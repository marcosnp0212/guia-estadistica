# Chuleta de fórmulas

## Tema 1. Una variable

| Qué | Fórmula | Excel |
|:---|:---|:---|
| Frecuencia relativa | fᵢ = nᵢ / n | `=B2/$B$9` |
| Acumulada | Nᵢ = n₁ + ... + nᵢ | `=C1+B2` |
| Media (datos sueltos) | x̄ = Σxᵢ / n | `=PROMEDIO(r)` |
| Media (tabla) | x̄ = Σxᵢnᵢ / n = Σxᵢfᵢ | `=SUMAPRODUCTO(x;n)/SUMA(n)` |
| Media ponderada | (x̄₁T₁ + x̄₂T₂ + ...) / (T₁ + T₂ + ...) | `=SUMAPRODUCTO(medias;T)/SUMA(T)` |
| Cambio Y = aX + b | ȳ = a·x̄ + b · S²ᵧ = a²·S²ₓ · Sᵧ = a·Sₓ | |
| Moda (intervalos) | Lᵢ₋₁ + (dᵢ − dᵢ₋₁)/((dᵢ − dᵢ₋₁) + (dᵢ − dᵢ₊₁)) · aᵢ | `=MODA.UNO(r)` (sueltos) |
| Densidad | dᵢ = nᵢ / aᵢ | `=C2/(B2-A2)` |
| Mediana (intervalos) | Lᵢ₋₁ + (n/2 − Nᵢ₋₁)/nᵢ · aᵢ | `=MEDIANA(r)` (sueltos) |
| Percentil r (intervalos) | Lᵢ₋₁ + (r·n/100 − Nᵢ₋₁)/nᵢ · aᵢ | `=PERCENTIL.INC(r;0,7)` |
| Cuartiles | C₁ → n/4 · C₃ → 3n/4 | `=CUARTIL.INC(r;1)` |
| Mediana o cuantil a mano (datos sueltos o tabla de valores) | posición k = r·n/100: si no es entera, el dato que ocupa el puesto siguiente; si es entera, media de ese dato y el siguiente | |
| Rango | máx − mín | `=MAX(r)-MIN(r)` |
| IQR | C₃ − C₁ | |
| Varianza | S² = Σxᵢ²nᵢ / n − x̄² | `=VAR.P(r)` |
| Cuasivarianza | s² = n/(n−1) · S² | `=VAR.S(r)` |
| Desviación típica | S = √S² | `=DESVEST.P(r)` |
| Cuasidesviación | s = √s² | `=DESVEST.S(r)` |
| Coef. de variación | CV = S / x̄ | `=DESVEST.P(r)/PROMEDIO(r)` |
| Var. dentro | (S²₁T₁ + S²₂T₂ + ...) / ΣT | |
| Var. entre | ((x̄₁ − x̄)²T₁ + (x̄₂ − x̄)²T₂ + ...) / ΣT | |
| Var. total | dentro + entre | |
| % entre grupos | entre / total × 100 | |
| Asimetría | CA > 0 cola derecha · < 0 cola izquierda | `=COEFICIENTE.ASIMETRIA.P(r)` |
| Curtosis | CC > 0 lepto · = 0 meso · < 0 plati | `=CURTOSIS(r)` |
| Tipificar | z = (x − x̄) / S | `=NORMALIZACION(x;media;S)` o `=(A2-$B$1)/$B$2` |
| Límites atípicos | C₁ − 1,5·IQR y C₃ + 1,5·IQR | |
| Media truncada | quitar un % de datos por cada extremo y hacer la media | `=MEDIA.ACOTADA(r;0,2)` |

## Tema 2. Dos variables

| Qué | Fórmula |
|:---|:---|
| Frec. relativa conjunta | fᵢⱼ = nᵢⱼ / n |
| Marginal de X | nᵢ. = suma de la fila i |
| Marginal de Y | n.ⱼ = suma de la columna j |
| Condicionada X \| Y = yⱼ | la columna j (dividida entre n.ⱼ) |
| Condicionada Y \| X = xᵢ | la fila i (dividida entre nᵢ.) |
| Independencia | fᵢⱼ = fᵢ. · f.ⱼ en **todas** las casillas |
| Frecuencia esperada (a mano) | nᵢ. · n.ⱼ / n; si coincide con nᵢⱼ en todas, independientes |
| Si son independientes | todas las condicionadas son iguales entre sí e iguales a la marginal |
| Mosaico | ancho de columna = marginal · alto de cada trozo = condicionada |

Excel: tabla dinámica (Filas, Columnas, Valores = Cuenta); "Mostrar valores como" → % del total general / de fila / de columna.

## Tema 3. Regresión

| Qué | Fórmula | Excel (Y en B, X en A) |
|:---|:---|:---|
| Covarianza | S_XY = Σxᵢyᵢ/n − x̄·ȳ | `=COVARIANZA.P(A;B)` |
| Pendiente (Y sobre X) | b = S_XY / S²ₓ | `=PENDIENTE(B;A)` |
| Término independiente | a = ȳ − b·x̄ | `=INTERSECCION.EJE(B;A)` |
| Recta | Ŷ = a + b·X | |
| Recta X sobre Y | b' = S_XY / S²ᵧ · a' = x̄ − b'·ȳ | `=PENDIENTE(A;B)` |
| Correlación | r = S_XY / (Sₓ·Sᵧ) | `=COEF.DE.CORREL(A;B)` |
| Determinación | R² = r² | `=COEFICIENTE.R2(B;A)` |
| Predicción | Ŷ = a + b·x₀ | `=PRONOSTICO.LINEAL(x0;B;A)` |
| Relaciones útiles | r = b·Sₓ/Sᵧ · S_XY = r·Sₓ·Sᵧ · ȳ = a + b·x̄ | |
| Si S_XY = 0 | Ŷ = ȳ (horizontal) · X̂ = x̄ (vertical) | |

Recuerda: las dos rectas se cortan en (x̄, ȳ). r está entre −1 y 1, no tiene unidades y no cambia si cambias de unidades. No predigas fuera del rango de los datos (extrapolar).

## Tema 4. Números índices

| Qué | Fórmula | Excel |
|:---|:---|:---|
| Índice simple | I = xₜ / x₀ · 100 | `=B3/$B$2*100` |
| Tasa de variación | (V₁ − V₀)/V₀ = V₁/V₀ − 1 | `=B3/B2-1` |
| Subir p % | × (1 + p/100) | |
| Encadenar | multiplicar los índices | `=PRODUCTO(r)` |
| Inversión | I₍ₜ→₀₎ = 1 / I₍₀→ₜ₎ | |
| Cambio de base | índice viejo / índice viejo del nuevo año base · 100 | `=C2/$C$6*100` |
| Media geométrica | (x₁·x₂···xₙ)^(1/n) | `=MEDIA.GEOM(r)` |
| Tasa media por periodo | (1 + T)^(1/k) − 1 | `=(1+T)^(1/k)-1` |
| Laspeyres precios | Σpₜq₀ / Σp₀q₀ · 100 | `=SUMAPRODUCTO(pt;q0)/SUMAPRODUCTO(p0;q0)*100` |
| Paasche precios | Σpₜqₜ / Σp₀qₜ · 100 | `=SUMAPRODUCTO(pt;qt)/SUMAPRODUCTO(p0;qt)*100` |
| Laspeyres cantidades | Σqₜp₀ / Σq₀p₀ · 100 | |
| Paasche cantidades | Σqₜpₜ / Σq₀pₜ · 100 | |
| Fisher | √(L · P) | `=RAIZ(L*P)` |
| Valor real (deflactar) | nominal / IPC · 100 | `=B2/C2*100` |
