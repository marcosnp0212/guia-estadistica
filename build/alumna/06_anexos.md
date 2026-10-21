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

# El examen en papel: lista de comprobación

**Antes de empezar**

- Lee todo el examen una vez, sin calcular. Marca qué tema es cada pregunta.
- Empieza por la que te dé más seguridad.
- Comprueba que tu calculadora está en modo normal de cálculo, no en el estadístico (si lo usaste para comprobar algo, sal de él).

**Para cada ejercicio**

1. Escribe qué te piden y la **fórmula** antes de poner números. Si te equivocas en una cuenta, la fórmula bien escrita ya suma.
2. Haz **la tabla**: xᵢ, nᵢ, Nᵢ, xᵢ·nᵢ, xᵢ²·nᵢ (Temas 1 y 2) o xᵢ, yᵢ, xᵢ², yᵢ², xᵢyᵢ (Tema 3). Suma cada columna.
3. Escribe cada resultado intermedio con 3 o 4 decimales. **Redondea solo al final.**
4. Recuadra el resultado y escribe la **frase de interpretación**.

**Comprobaciones rápidas**

- ¿Σnᵢ = n? ¿La última Nᵢ es n? ¿Las fᵢ suman 1?
- ¿La media está entre el mínimo y el máximo? ¿La mediana también?
- ¿La varianza es positiva? (Si sale negativa, has olvidado el cuadrado o has redondeado la media antes de tiempo.)
- ¿r entre −1 y 1, con el mismo signo que b? ¿R² entre 0 y 1?
- ¿El año base vale 100? ¿Has multiplicado (no sumado) los porcentajes?

**Preguntas sobre Excel en papel**

- Escribe la función con su nombre exacto en español y con `;`: `=PROMEDIO(A2:A31)`.
- Si preguntan por qué se pone `$`: para que la referencia no cambie al arrastrar la fórmula.
- Repasa las 30 preguntas del apartado «Preguntas de Excel sin ordenador».

# El examen con Excel: lista de comprobación

**Antes de empezar**

- Abre tus prácticas de clase y tu solucionario antes de empezar. Ten el traductor a mano.
- Lee todo el examen una vez, sin calcular. Marca qué tema es cada pregunta. Si dudas qué te piden, mira el traductor de enunciados.
- Empieza por la que te dé más seguridad. Sumar puntos pronto quita nervios.

**Para cada ejercicio**

1. Escribe en una celda el **título** del ejercicio y del apartado (así no te pierdes y quien corrige lo encuentra).
2. Copia o escribe los datos en **columnas con título**.
3. Haz una columna por cada paso (marca de clase, xᵢ·nᵢ, xᵢ²·nᵢ, Nᵢ...). Ver los pasos te tranquiliza y, si hay un error, se localiza.
4. Pon al lado de cada resultado una **etiqueta** ("Media =", "Varianza =").
5. Escribe la **frase de interpretación** en una celda de texto. Muchas veces vale tanto como el número.

**Comprobaciones rápidas antes de entregar**

- ¿Las frecuencias relativas suman 1? ¿La última acumulada es n?
- ¿La media está entre el mínimo y el máximo?
- ¿La varianza es positiva? (Si sale negativa, hay un error seguro: probablemente olvidaste el cuadrado o el orden de la resta.)
- ¿r está entre −1 y 1? ¿R² entre 0 y 1? ¿r tiene el mismo signo que la pendiente?
- ¿El año base vale 100?
- ¿Has usado **VAR.P** (no VAR.S) salvo que pidan cuasivarianza?
- ¿En PENDIENTE e INTERSECCION.EJE pusiste **primero la Y**?
- Guarda el archivo cada poco (**Ctrl + G**).

**Atajos que ayudan**

| Atajo | Para qué |
|:---|:---|
| Ctrl + Z | Deshacer |
| Ctrl + G | Guardar |
| F4 | Poner los $ en una referencia mientras la escribes |
| F2 | Editar la celda (ver la fórmula) |
| Pestaña Fórmulas → Mostrar fórmulas | Ver todas las fórmulas de la hoja en vez de los resultados (pulsa otra vez para volver) |
| Doble clic en la esquina de una celda | Arrastrar la fórmula hasta el final de los datos |

**Errores que te puede mostrar Excel y qué significan**

| Error | Qué ha pasado |
|:---|:---|
| `#¡DIV/0!` | Estás dividiendo entre una celda vacía o 0. Suele ser un $ olvidado. |
| `#¿NOMBRE?` | Has escrito mal el nombre de una función (por ejemplo, PROMEDIO sin tilde está bien; MEDIA no existe). |
| `#¡VALOR!` | Hay texto donde debería haber un número (por ejemplo, un número escrito con punto en vez de coma). |
| `#N/A` | Falta un dato o un rango no tiene el tamaño correcto. |
| `####` | La columna es estrecha. Ensánchala con doble clic en el borde. |

# Plan de estudio

Tu plan se hace solo con tus fechas. Dime cuándo es el examen, qué días estudias y qué temas entran, y la guía reparte lo que te queda entre los días que tienes. Cada día mezcla teoría y ejercicios del mismo tema, y los últimos días son para los simulacros.

El plan se **recalcula cada día con lo que ya has hecho**: lo que marcas como hecho (con las comprobaciones, «Ya lo sé hacer» o «Lo he resuelto») desaparece de los días que vienen. Si un día no puedes, no pasa nada: mañana el plan se reparte otra vez.

::: {.plan-app}
:::

::: {custom-style="Truco"}
**💡 Para los días de poca energía.** Si un día no te ves con fuerzas, haz solo una cosa pequeña: rehaz **un** ejercicio que ya te salió bien, en papel. Mantener el contacto diario cuenta más que la cantidad.
:::

::: {custom-style="Truco"}
**💡 Cuando haya más temario.** Si se añaden temas nuevos o hay otro parcial, aparecerán solos en «Qué entra»: marca los que entran en ese examen y cambia la fecha.
:::
