P='/home/claude/build/alumna/04_tema3.md'
s=open(P).read()
def after(anchor,text):
    global s
    i=s.index(anchor);j=i+len(anchor);s=s[:j]+'\n\n'+text.strip()+'\n'+s[j:]
after("""Excel te escribe la recta (y = 78,533x + 1390,3) y el R² (0,9159) encima del gráfico. Es una forma estupenda de **comprobar** tus cálculos.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: la nube de puntos en papel.**

1. Eje horizontal para X y vertical para Y, cada uno con su escala. No hace falta que empiecen en 0: para los salarios, el eje vertical puede ir de 1300 a 2600 (marca el corte con una pequeña rayita en zigzag).
2. Pon un punto por cada pareja (x, y). Por ejemplo (1, 1400), (2, 1600)…
3. Mira la forma: si sube hacia la derecha, relación directa; si baja, inversa.
4. Si te piden la recta, calcula dos puntos con la ecuación (por ejemplo, X = 0 y X = 15) y únelos con la regla. Comprueba que pasa por (x̄, ȳ).
:::
""")
after("""A mano en Excel: columna C con `=A2*B2` arrastrada, y luego `=SUMA(C2:C11)/10-PROMEDIO(A2:A11)*PROMEDIO(B2:B11)`.
:::""","""
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
""")
s=s.replace("- Hacer la nube de puntos en Excel con la recta, la ecuación y el R².","- Hacer la nube de puntos en papel y en Excel con la recta, la ecuación y el R².\n- Montar a mano la tabla xᵢ, yᵢ, xᵢ², yᵢ², xᵢyᵢ y sacar de sus sumas todo lo demás.")
open(P,'w').write(s);print(s.count('"Mano"'))
