import re
P='/home/claude/build/alumna/01_tema1.md'
s=open(P).read()
def after(anchor,text,occ=1):
    global s
    i=-1
    for _ in range(occ):
        i=s.index(anchor,i+1)
    j=i+len(anchor)
    s=s[:j]+'\n\n'+text.strip()+'\n'+s[j:]
def before(anchor,text):
    global s
    i=s.index(anchor); s=s[:i]+text.strip()+'\n\n'+s[i:]

# A. tabla de frecuencias
after("""Si se te olvida, verás resultados raros o errores `#¡DIV/0!` en las filas de abajo.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: la tabla de frecuencias.**

1. **Ordena** los datos de menor a mayor (o apunta los valores distintos: 0, 1, 2…).
2. **Cuenta con palotes.** Recorre la lista una sola vez y pon un palote junto a cada valor cada vez que aparezca. Agrupa de 5 en 5 (𝍸) para no perderte.
3. Columna **nᵢ**: el número de palotes de cada valor. Súmala: tiene que darte n. Si no, has contado mal; repite antes de seguir.
4. Columna **fᵢ**: divide cada nᵢ entre n con la calculadora. Con 3 o 4 decimales basta.
5. Columna **%**: fᵢ × 100.
6. Columna **Nᵢ**: la primera es igual que la primera nᵢ; cada una de las siguientes es la de arriba más la nᵢ de su fila. La última tiene que ser n.
7. Columna **Fᵢ**: Nᵢ ÷ n. La última tiene que ser 1.

**Comprobación final:** Σnᵢ = n, Σfᵢ = 1 (puede salir 0,999 o 1,001 por los redondeos: está bien) y Σ% = 100.
:::
""")
# B. intervalos
after("""Alternativa sin FRECUENCIA: `=CONTAR.SI.CONJUNTO(A2:A17;">170";A2:A17;"<=180")` cuenta los datos de (170, 180].
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: agrupar en intervalos.**

1. Calcula el número de intervalos: √n redondeado. Con 16 datos, 4.
2. Calcula la amplitud: (máximo − mínimo) ÷ nº de intervalos, y redondea **hacia arriba** a un número cómodo: (198 − 163) ÷ 4 = 8,75 → 10.
3. Escribe los intervalos empezando en un número redondo por debajo del mínimo: [160, 170], (170, 180], (180, 190], (190, 200].
4. Cuenta con palotes cuántos datos caen en cada uno. **Cuidado con los extremos:** un dato que vale justo 170 va en [160, 170], no en (170, 180], porque el paréntesis dice que el 170 no entra.
5. Marca de clase de cada intervalo: (abajo + arriba) ÷ 2. Amplitud: arriba − abajo.
6. Termina la tabla igual que antes: fᵢ, %, Nᵢ y Fᵢ.
:::
""")
# C. gráficos
after("""- **Histograma desde una tabla ya agrupada:** haz un gráfico de columnas con las frecuencias (o densidades) y luego clic derecho en una barra → Dar formato a serie de datos → **Ancho del intervalo = 0 %**, para que las barras se toquen.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: dibujar los gráficos en papel.**

**Diagrama de barras.**

1. Dibuja dos ejes. En el horizontal, los valores (0, 1, 2…) separados por el mismo espacio. En el vertical, una escala que llegue un poco por encima de la nᵢ más alta. Con los hermanos, de 0 a 25, marcando de 5 en 5.
2. Sobre cada valor, una barra de la altura de su nᵢ. Todas igual de anchas y **sin tocarse**.
3. Pon nombre a los ejes ("Nº de hermanos", "Nº de personas") y un título.

**Diagrama de sectores.**

1. Calcula el ángulo de cada sector: 360 × fᵢ (o 360 × nᵢ ÷ n). Con los hermanos: 0 → 171,8°, 1 → 98,2°, 2 → 49,1°, 3 → 16,4°, 4 → 16,4°, 5 → 8,2°. Suman 360°.
2. Dibuja un círculo, traza un radio y mide cada ángulo con el transportador, uno detrás de otro.
3. Escribe en cada trozo la categoría y su %.

**Histograma.**

1. En el eje horizontal, los extremos de los intervalos, a escala (un intervalo el doble de ancho ocupa el doble).
2. Altura de cada rectángulo: si todos los intervalos miden lo mismo, nᵢ. Si no, la **densidad** dᵢ = nᵢ ÷ aᵢ.
3. Los rectángulos van **pegados**, sin hueco entre ellos.
4. **Polígono de frecuencias:** marca un punto en el centro del techo de cada rectángulo (encima de la marca de clase) y únelos con líneas rectas.
:::
""")
# D. media
after("""SUMAPRODUCTO hace en un paso la columna xᵢ·nᵢ y su suma. Si te da inseguridad, haz la columna auxiliar `=D2*E2`, arrástrala y luego divide su suma entre n. Da lo mismo.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: la media.**

**Datos sueltos.** Suma todos los datos con la calculadora y divide entre cuántos hay. Alturas: 163 + 167 + … + 198 = 2868; 2868 ÷ 16 = **179,25 cm**.

**Con tabla de frecuencias:**

1. Añade la columna **xᵢ·nᵢ**: cada valor por su frecuencia.
2. Suma esa columna: **Σxᵢnᵢ**. Hermanos: 0 + 12 + 12 + 6 + 8 + 5 = 43.
3. Divide entre n: 43 ÷ 44 = **0,977**.

**Con intervalos:** lo mismo, pero xᵢ es la **marca de clase**.

**Truco para no equivocarte con la calculadora:** escribe en la hoja el resultado de cada fila antes de sumar. Si te equivocas, solo repites una fila, no todo.
:::
""")
# E. mediana datos sueltos
after("""`=A3+(C7/2-E2)/C3*D3` → 178,33.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: la mediana con datos sueltos (sin tabla).** Es la misma receta de los apuntes: n/2 y buscar en qué dato caes.

1. **Ordena** los datos de menor a mayor y numéralos: 1.º, 2.º, 3.º…
2. Calcula n/2.
3. Si n/2 **no es un número entero**, redondéalo hacia arriba: la mediana es el dato que ocupa ese puesto. Con 15 datos, n/2 = 7,5 → el dato 8.º.
4. Si n/2 **es entero**, la mediana es la media del dato que ocupa ese puesto y el siguiente. Con 16 datos, n/2 = 8 → media del 8.º y del 9.º.

**Alturas** (ya ordenadas): 163, 167, 169, 172, 174, 176, 177, **178**, **179**, 181, 182, 184, 186, 189, 193, 198. n/2 = 8 → Me = (178 + 179) ÷ 2 = **178,5 cm**.

Con la tabla de intervalos salía 178,33: es una aproximación, porque ahí no conocemos los datos exactos.
:::
""")
# F. cuartiles sueltos
after("""Si dudas, pon los dos y di cuál es cuál.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: cuartiles y percentiles con datos sueltos.** Igual que la mediana, cambiando n/2 por r·n/4 (cuartiles) o r·n/100 (percentiles).

1. Ordena y numera los datos.
2. Calcula la posición: n/4 para C₁, 3n/4 para C₃, r·n/100 para Pᵣ.
3. ¿No es entero? Redondea hacia arriba y coge ese dato.
4. ¿Es entero? Haz la media de ese dato y el siguiente.

**Alturas (n = 16):**

- C₁: 16/4 = 4, entero → media del 4.º y el 5.º = (172 + 174) ÷ 2 = **173**.
- C₃: 3·16/4 = 12, entero → media del 12.º y el 13.º = (184 + 186) ÷ 2 = **185**.
- P₉₀: 90·16/100 = 14,4 → redondeo a 15 → el 15.º dato = **193**.

Con esta receta de los apuntes, el IQR de las alturas es 185 − 173 = **12**. Excel (y el programa R de los apuntes) da 173,5 y 184,5, porque usa otro método. **En papel, usa la receta**; si te dan una salida de ordenador, usa sus números.
:::
""")
# G. varianza
after("""Si solo tienes la tabla de frecuencias (valores en D2:D7, nᵢ en E2:E7) y la media en una celda, por ejemplo J2: `=SUMAPRODUCTO(D2:D7^2;E2:E7)/SUMA(E2:E7)-J2^2`.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: varianza, cuasivarianza y desviaciones.** Usa siempre la **fórmula práctica**: es la que menos cuentas tiene.

**Con tabla de frecuencias:**

1. Columnas que necesitas: xᵢ, nᵢ, xᵢ·nᵢ y **xᵢ²·nᵢ**. Truco: xᵢ²·nᵢ = xᵢ · (xᵢ·nᵢ). Multiplica cada valor por lo que ya tienes en la columna de al lado.
2. x̄ = Σxᵢnᵢ ÷ n.
3. S² = Σxᵢ²nᵢ ÷ n − x̄².
4. S = √S².
5. Si te piden las "cuasi": s² = S² · n ÷ (n − 1), y s = √s².

**Con datos sueltos** es igual, con nᵢ = 1 en todos: S² = Σxᵢ² ÷ n − x̄².

**Alturas:** Σxᵢ = 2868 y Σxᵢ² = 163² + 167² + … + 198² = 515 420.

- x̄ = 2868 ÷ 16 = 179,25.
- S² = 515 420 ÷ 16 − 179,25² = 32 213,75 − 32 130,5625 = **83,19**.
- S = √83,19 = **9,12 cm**.
- s² = 83,19 · 16/15 = **88,73**. s = √88,73 = **9,42 cm**.

**Ojo con la calculadora:** usa la media **sin redondear** al elevarla al cuadrado. Si redondeas x̄ a 179 antes, sale una varianza muy distinta. Guarda x̄ en la memoria o usa la tecla Ans.
:::
""")
# I. forma
after("""El signo, que es lo que se interpreta, coincide casi siempre.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: asimetría y curtosis.** Es largo, así que en papel suelen darte la tabla hecha o pedirte solo el signo y la interpretación. Si te lo piden entero:

1. Calcula x̄ y S.
2. Columna **dᵢ = xᵢ − x̄** (la distancia de cada valor a la media).
3. Columnas **dᵢ³·nᵢ** y **dᵢ⁴·nᵢ**. Súmalas.
4. CA = (Σdᵢ³nᵢ ÷ n) ÷ S³.
5. CC = (Σdᵢ⁴nᵢ ÷ n) ÷ S⁴ − 3.

**Hermanos** (x̄ = 0,9773, S = 1,2521):

| xᵢ | nᵢ | dᵢ | dᵢ³·nᵢ | dᵢ⁴·nᵢ |
|---:|---:|---:|---:|---:|
| 0 | 21 | −0,9773 | −19,60 | 19,16 |
| 1 | 12 | 0,0227 | 0,00 | 0,00 |
| 2 | 6 | 1,0227 | 6,42 | 6,56 |
| 3 | 2 | 2,0227 | 16,55 | 33,48 |
| 4 | 2 | 3,0227 | 55,24 | 166,97 |
| 5 | 1 | 4,0227 | 65,10 | 261,87 |
| **Suma** | **44** | | **123,70** | **488,03** |

- CA = (123,70 ÷ 44) ÷ 1,2521³ = 2,811 ÷ 1,963 = **1,43** → asimetría positiva.
- CC = (488,03 ÷ 44) ÷ 1,2521⁴ − 3 = 11,092 ÷ 2,458 − 3 = **1,51** → leptocúrtica.

(El programa de los apuntes da 1,48 y 1,85 porque usa una corrección para muestras; el signo y la interpretación son los mismos.)

**Atajo sin cuentas:** si la media es claramente mayor que la mediana, asimetría positiva; si es menor, negativa.
:::
""")
# J. boxplot
after("""Excel dibuja la media con una "x" además de la mediana con una línea.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: dibujar el diagrama de caja.**

1. Calcula C₁, la mediana y C₃ con la receta. Alturas: C₁ = 173, Me = 178,5, C₃ = 185.
2. IQR = C₃ − C₁ = 12.
3. Límites: Lᵢ = C₁ − 1,5·IQR = 173 − 18 = **155**. Lₛ = C₃ + 1,5·IQR = 185 + 18 = **203**.
4. Busca atípicos: ¿algún dato menor que 155 o mayor que 203? No → no hay atípicos.
5. Dibuja un eje con escala (de 150 a 210, por ejemplo).
6. Dibuja la **caja** de C₁ a C₃ y una raya gruesa dentro, en la mediana.
7. **Bigotes:** desde la caja hasta el dato más pequeño y el más grande que **no** sean atípicos (aquí 163 y 198).
8. Si hubiera atípicos, dibújalos como puntitos sueltos.
:::
""")
s=s.replace("""- Decir de qué tipo es una variable.
- Montar en Excel una tabla de frecuencias con nᵢ, fᵢ, %, Nᵢ y Fᵢ.
- Hacer un diagrama de barras y un histograma.""","""- Decir de qué tipo es una variable.
- Montar una tabla de frecuencias con nᵢ, fᵢ, %, Nᵢ y Fᵢ, **a mano y en Excel**.
- Hacer un diagrama de barras, de sectores y un histograma, **en papel y en Excel**.""")
s=s.replace("- Leer un diagrama de caja y decir si hay atípicos.","- Dibujar y leer un diagrama de caja y decir si hay atípicos.\n- Hacer todo lo anterior **solo con calculadora**, con la tabla en papel.")
open(P,'w').write(s)
print(s.count('custom-style="Mano"'))
