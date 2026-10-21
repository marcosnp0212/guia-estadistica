P='/home/claude/build/alumna/02_tema2.md'
s=open(P).read()
def after(anchor,text):
    global s
    i=s.index(anchor);j=i+len(anchor);s=s[:j]+'\n\n'+text.strip()+'\n'+s[j:]
after("""Las casillas con más gente se colorean más fuerte y se ve la diagonal de un vistazo.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: construir la tabla de doble entrada.**

1. Dibuja una cuadrícula: una **fila** por cada valor de X y una **columna** por cada valor de Y. Deja una fila y una columna más para los totales.
2. Recorre los datos **persona a persona**. Para cada una, mira su X y su Y y pon un palote en la casilla donde se cruzan.
3. Cuenta los palotes de cada casilla: esas son las nᵢⱼ.
4. Suma cada fila (columna Total) y cada columna (fila Total).
5. **Comprobación:** la suma de los totales de fila y la de los totales de columna tienen que dar lo mismo: n.
6. Si te piden frecuencias relativas, divide cada casilla entre n.
:::
""")
after("""Una distribución marginal es una tabla de frecuencias normal y corriente, así que **se le aplica todo el Tema 1**: media, mediana, moda, varianza...""","""
::: {custom-style="Mano"}
**✍️ A mano: la media de una marginal.** Con el ejercicio de los apuntes de más abajo (X = días de ausencia):

| xᵢ | nᵢ. | xᵢ·nᵢ. | xᵢ²·nᵢ. |
|---:|---:|---:|---:|
| 1 | 6 | 6 | 6 |
| 2 | 10 | 20 | 40 |
| 3 | 8 | 24 | 72 |
| 4 | 8 | 32 | 128 |
| **Total** | **32** | **82** | **246** |

- Media: x̄ = 82 ÷ 32 = **2,5625 días**.
- Varianza: S² = 246 ÷ 32 − 2,5625² = 7,6875 − 6,5664 = **1,121**.

Es exactamente lo mismo que en el Tema 1: la columna de totales hace de nᵢ.
:::
""")
after("""| **Total** | **18** | **1** |""","""
::: {custom-style="Mano"}
**✍️ A mano: la media de una condicionada.** Con la tabla de Y | X ∈ {2, 3} que acabas de hacer:

ȳ = (2·7 + 3·4 + 5·7) ÷ 18 = (14 + 12 + 35) ÷ 18 = 61 ÷ 18 = **3,39 días** de asuntos propios, de media, entre los que faltan 2 o 3 días.

La receta es la del Tema 1, usando solo las frecuencias de esa fila (o de la suma de filas) y dividiendo entre **su** total (18), no entre n = 32.
:::
""")
after("""Mirando las condicionadas por fila: RRHH tiene 61,5 % presencial, Finanzas 50 %, Producción 58,8 %. Son distintas, así que la modalidad depende algo del departamento.""","""
::: {custom-style="Mano"}
**✍️ A mano: comprobar la independencia sin tantos decimales.** Hay una forma equivalente que da números más cómodos: comparar cada casilla con la **frecuencia esperada** si fueran independientes.

$$\\text{esperada}_{ij}=\\frac{n_{i\\cdot}\\cdot n_{\\cdot j}}{n}$$

1. Para cada casilla: (total de su fila × total de su columna) ÷ n.
2. Compárala con la que hay en la tabla (nᵢⱼ).
3. Si coinciden **todas** → independientes. Si **alguna** no coincide → dependientes.

**Ejemplo 1**, casilla RRHH-Presencial: 13 × 23 ÷ 40 = **7,475**. En la tabla hay **8**. No coinciden → **no son independientes**. Con una casilla basta para decir que no.

**Ejemplo 7**, casilla Hombre-Indefinido: 180 × 120 ÷ 240 = 90, y en la tabla hay 90 ✔. Hay que repetirlo en las seis casillas para decir que sí son independientes (salen todas iguales).

Es la misma comprobación que fᵢⱼ = fᵢ. · f.ⱼ, multiplicada por n en los dos lados.
:::
""")
s=s.replace("- Construir una tabla de doble entrada con tabla dinámica.","- Construir una tabla de doble entrada **a mano** (con palotes) y en Excel con tabla dinámica.")
s=s.replace("- Comprobar si dos variables son independientes comparando fᵢⱼ con fᵢ. × f.ⱼ, o comparando los porcentajes por filas.","- Comprobar si dos variables son independientes comparando fᵢⱼ con fᵢ. × f.ⱼ, con las frecuencias esperadas (a mano) o comparando los porcentajes por filas.\n- Calcular la media de una marginal y de una condicionada con calculadora.")
open(P,'w').write(s);print(s.count('"Mano"'))
