# Repaso exprés: el examen en 3 días

::: {custom-style="Idea"}
**🧠 Si te quedan pocos días, empieza aquí.** El examen es como el modelo de la profesora: 30 preguntas tipo test y 10 cortas, casi todo de **saber qué es cada cosa, qué fórmula va y qué trampa evitar**. No hace falta leer la guía entera. Esto es lo mínimo que tienes que saber, tema a tema. Si algo no lo entiendes, pincha en el enlace del tema y lee solo ese trozo.
:::

## El plan de 3 días

| Día | Qué hacer | Tiempo |
|:---|:---|---:|
| **Día 1** | Lee el **Repaso exprés de los Temas 1 y 2** (aquí abajo). Después, el **examen modelo, preguntas 1 a 15**: intenta cada una antes de abrir la solución. | 2 h |
| **Día 2** | **Repaso exprés de los Temas 3 y 4**. Después, el **examen modelo, preguntas 16 a 30 y P1 a P10**. Si te sobra tiempo, el vídeo del Tema 3 o del 4 a 1,25×. | 2 h 30 |
| **Día 3** | **Simulacro tipo test** con reloj (90 min). Al entregar, lee la explicación de cada fallo y vuelve a leer en este repaso el tema que peor te haya salido. Antes de dormir, la **chuleta**. | 2 h 30 |
| **Mañana del examen** | Solo la lista **"Las 15 trampas"** de abajo. Nada nuevo. | 15 min |

El plan de estudio largo (más abajo, en «Plan de estudio») es para cuando hay semanas. Para estos 3 días, sigue esta tabla.

## Tema 1 en 10 minutos

**Variables.** Cualitativa (palabras): **nominal** sin orden (departamento) u **ordinal** con orden (satisfacción baja/media/alta). Cuantitativa (números): **discreta** si se cuenta (hijos) o **continua** si se mide (salario, altura).

**Parámetro** = medida de la población. **Estadístico** = la misma medida en una muestra.

**Centro.**

- Media: x̄ = Σxᵢnᵢ / n. En Excel con tabla: `=SUMAPRODUCTO(x;n)/SUMA(n)`.
- Mediana: el dato del medio. **Robusta**: no le afectan los atípicos. Con atípicos o asimetría fuerte, mejor mediana o **media truncada** (`=MEDIA.ACOTADA`).
- Moda: el más repetido. **Con intervalos de distinto ancho, el intervalo modal es el de mayor densidad dᵢ = nᵢ / aᵢ**, no el de más datos. En el histograma, en el eje vertical va la densidad.

**Dispersión.**

- Varianza S² = Σxᵢ²nᵢ / n − x̄² (`=VAR.P`). Cuasivarianza: entre n − 1 (`=VAR.S`). Desviación típica S = √S².
- **CV = S / x̄.** Sin unidades. Sirve para comparar grupos con medias o unidades distintas: **menor CV, más homogéneo**.
- IQR = C₃ − C₁. **Atípicos:** por debajo de C₁ − 1,5·IQR o por encima de C₃ + 1,5·IQR.
- **Varianza total = dentro + entre.** Dentro = Σ S²ᵢ nᵢ / n. Entre = Σ (x̄ᵢ − x̄)² nᵢ / n. Si "entre" es grande, los grupos son muy distintos.

**Cambio Y = aX + b:** ȳ = a·x̄ + b · S²ᵧ = a²·S²ₓ · Sᵧ = |a|·Sₓ. Sumar b no cambia la dispersión.

**Forma.** CA > 0: cola a la derecha (media > mediana). CA < 0: cola a la izquierda. CA = 0: simétrica. Curtosis > 0 leptocúrtica (apuntada), < 0 platicúrtica.

**Diagrama de caja.** Mediana cerca del borde de abajo de la caja y bigote de arriba largo → asimetría positiva.

**Tipificar:** z = (x − x̄) / S. En Excel, `=(A2-$B$1)/$B$2`: el dato sin dólares, la media y S con dólares.

[Ir al Tema 1 completo](#tema-1.-análisis-descriptivo-de-una-variable)

## Tema 2 en 5 minutos

- **Conjunta** nᵢⱼ: la casilla. Relativa: fᵢⱼ = nᵢⱼ / n.
- **Marginal:** los totales. nᵢ. = suma de la fila i; n.ⱼ = suma de la columna j.
- **Condicionada** Y | X = xᵢ: coges la fila de xᵢ y la divides entre su total.
- **Independencia:** fᵢⱼ = fᵢ. · f.ⱼ **en todas** las casillas. Equivale a que **todas las condicionadas son iguales entre sí e iguales a la marginal**. Ejemplo: si el 70 % del total tiene jornada completa y son independientes, el 70 % de los hombres también.
- Frecuencia esperada si fueran independientes: nᵢ. · n.ⱼ / n.
- **Gráficos:** barras agrupadas o apiladas y mosaico (dos cualitativas). En el **mosaico**, el **ancho** de cada columna es la frecuencia marginal.

[Ir al Tema 2 completo](#tema-2.-análisis-descriptivo-de-dos-variables)

## Tema 3 en 10 minutos

- **Nube de puntos** que sube → relación directa (S_XY > 0). Que baja → inversa (S_XY < 0).
- **Covarianza:** S_XY = Σxᵢyᵢ / n − x̄·ȳ (con tabla, Σxᵢyⱼnᵢⱼ / n − x̄·ȳ). Solo mira su **signo**: su tamaño depende de las unidades.
- **Recta de Y sobre X:** Ŷ = a + bX, con **b = S_XY / S²ₓ** y **a = ȳ − b·x̄**. b = lo que sube Y de media por cada unidad más de X.
- **Recta de X sobre Y:** b′ = S_XY / S²ᵧ. Las dos rectas **se cortan en (x̄, ȳ)**.
- **Si S_XY = 0:** Ŷ = ȳ (horizontal) y X̂ = x̄ (vertical). No hay relación lineal.
- **r = S_XY / (Sₓ·Sᵧ):** entre −1 y 1, **sin unidades** (no cambia si pasas de euros a miles de euros), mismo signo que b. **r = 0 no es "ninguna relación"**: solo que no es lineal.
- **R² = r²:** el % de la variabilidad de Y que explica la recta. Si r = −0,85, R² = 0,7225 → 72,25 %.
- **Predecir:** sustituir X en la recta. Con Salario = 1390 + 78,5·Antigüedad y 10 años: 1390 + 785 = 2175 €. **No predigas fuera del rango de los datos** (extrapolar).
- **Pasa por las medias:** ȳ = a + b·x̄. Útil en los ejercicios "sin datos".
- Excel: `=PENDIENTE(Y;X)`, `=INTERSECCION.EJE(Y;X)`, `=COEF.DE.CORREL(X;Y)`, `=COEFICIENTE.R2(Y;X)`. Siempre primero la Y.

[Ir al Tema 3 completo](#tema-3.-regresión-y-correlación)

## Tema 4 en 10 minutos

- **Índice simple** = valor / valor del año base × 100. **Índice − 100 = variación en %**: 125,4 → +25,4 %; 92 → −8 %.
- **Tasa de variación** = nuevo / viejo − 1.
- **Los porcentajes se multiplican, nunca se suman:** +10 % y +20 % = 1,10·1,20 = +32 %.
- **Inversión:** I(al revés) = 1 / I (en tanto por uno). **Encadenamiento:** se multiplican.
- **Cambio de base:** cada índice entre el del nuevo año base, × 100.
- **Tasa media:** media **geométrica**: ⁿ√((1+t₁)(1+t₂)…) − 1. En Excel, `=MEDIA.GEOM(rango)-1` o `=PRODUCTO(rango)^(1/n)-1`.
- **De anual a mensual:** (1 + t)^(1/12) − 1. 6 % anual → 0,487 % mensual. **De mensual a anual:** (1 + t)¹² − 1.
- **Laspeyres:** pondera con las cantidades del **año base** (q₀); tiende a **sobreestimar** la subida de precios. **Paasche:** cantidades del **año actual** (qₜ). **Fisher:** √(L·P).
- **Deflactar:** valor real = nominal / IPC (en tanto por uno), o nominal / IPC × 100 si el IPC está en base 100. Real sube = 1,05 / 1,03 − 1, no 5 − 3.

[Ir al Tema 4 completo](#tema-4.-números-índices)

## Las 15 trampas del test

1. Intervalos de distinto ancho → moda por **densidad**, no por frecuencia.
2. Varianza = entre n (VAR.P). Cuasivarianza = entre n − 1 (VAR.S).
3. ¿Te dan S o S²? Para la pendiente necesitas la **varianza**.
4. El CV compara grupos con medias o unidades distintas; S sola no.
5. La suma de las desviaciones a la media es siempre **0**.
6. Sumar una constante no cambia la varianza ni S; multiplicar por a multiplica S² por a².
7. Total = dentro **+** entre (se suman).
8. CA > 0 = cola a la **derecha**.
9. Atípicos: **1,5 · IQR** por fuera de C₁ y C₃.
10. Independencia: condicionadas = marginal, en **todas** las casillas.
11. r = 0 → no hay relación **lineal** (puede haber curva). r no cambia con las unidades.
12. R² es r al cuadrado: el signo desaparece. r lleva el signo de la pendiente.
13. b = S_XY / S²ₓ (la X abajo); a = ȳ − b·x̄.
14. Los porcentajes se **multiplican**; la tasa media es la **geométrica**; 6 % anual no es 0,5 % al mes.
15. Laspeyres = cantidades del año **base**; deflactar = **dividir** entre el IPC.

::: {custom-style="Truco"}
**💡 En el test.** Lee las 4 opciones antes de elegir. Muchas veces dos se descartan solas: "es negativo cuando…", "siempre positiva", "suman cero", "tienden a infinito". Si dudas entre dos, busca cuál dice algo **imposible** (un CV negativo, un R² mayor que 1, una varianza negativa).
:::
