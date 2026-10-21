P='/home/claude/build/alumna/00_inicio.md'
s=open(P).read()
rep=[
("La estadística de esta asignatura no es \"matemáticas difíciles\". Es, sobre todo, **ordenar datos, contar, sumar, dividir y saber qué significa cada número**. Las cuentas largas las hace Excel. Tu trabajo es saber **qué pedirle a Excel** y **qué quiere decir el resultado**.",
 "La estadística de esta asignatura no es \"matemáticas difíciles\". Es, sobre todo, **ordenar datos, contar, sumar, dividir y saber qué significa cada número**. Aprenderás a hacerlo de dos formas: **a mano, con papel y calculadora**, y **en Excel**. En las dos, tu trabajo es el mismo: saber **qué cálculo toca** y **qué quiere decir el resultado**."),
("3. **Cómo se calcula a mano**, como una receta.\n4. **Cómo se hace en Excel**.","3. **Cómo se calcula a mano**, como una receta, con un recuadro azul de cuaderno.\n4. **Cómo se hace en Excel**, con un recuadro verde."),
("""::: {custom-style="Excel"}
**🖥️ En Excel.** Lo que tienes que escribir en las celdas.
:::""","""::: {custom-style="Mano"}
**✍️ A mano, con calculadora.** Los pasos para hacerlo en papel, como en un examen sin ordenador.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Lo que tienes que escribir en las celdas.
:::"""),
("1. **Lee** la explicación con el Excel abierto y haz el ejemplo tú.","1. **Lee** la explicación y haz el ejemplo tú: primero a mano, con papel y calculadora, y después en Excel."),
("El **plan de 3 semanas** te dice qué toca cada día. La portada te recuerda dónde lo dejaste.","El **plan de estudio** se adapta a tus fechas: eliges cuándo empiezas, cuándo es el examen y qué temas entran, y te dice qué toca cada día. La portada te recuerda dónde lo dejaste."),
("1. Vuelve a leer el apartado despacio, con el Excel abierto, y repite el ejemplo.","1. Vuelve a leer el apartado despacio y repite el ejemplo con papel y calculadora."),
("""::: {custom-style="Idea"}
**🧠 La idea.** El examen es con Excel, con tus prácticas de clase y tu solucionario. Eso es una buena noticia: no vas a tener que hacer divisiones largas a mano. Lo importante es saber qué te piden, qué fórmula usar y explicar el resultado con una frase.
:::""","""::: {custom-style="Idea"}
**🧠 La idea.** El examen puede ser en papel, con preguntas cortas, ejercicios a mano y preguntas sobre Excel. Por eso cada apartado tiene las dos versiones. Lo importante es lo mismo en las dos: saber qué te piden, qué cálculo hacer y explicar el resultado con una frase.
:::"""),
]
for a,b in rep:
    assert a in s,a[:60]; s=s.replace(a,b)
calc='''## 0.10. La calculadora

En un examen en papel, la calculadora hace las cuentas y tú haces la tabla. Con una calculadora científica normal basta.

**Lo que más vas a usar:**

| Para | Tecla |
|:---|:---|
| Elevar al cuadrado | x² |
| Raíz cuadrada | √ |
| Otra potencia (por ejemplo, ³ o ⁴) | ^ (o xʸ, o x■) |
| Raíz n-ésima (para tasas medias) | ˣ√ (normalmente con SHIFT) o elevar a (1/n) |
| Usar el último resultado | Ans |
| Guardar un número | STO (o SHIFT + RCL) y una letra |

::: {custom-style="Truco"}
**💡 Truco: no redondees a mitad de cuenta.** Si un resultado lo vas a volver a usar (la media para la varianza, por ejemplo), no lo copies redondeado: usa Ans o guárdalo en una memoria. Redondea solo el resultado final, a 2 o 3 decimales.
:::

### El modo estadístico: para comprobar

Casi todas las calculadoras científicas tienen un modo **estadístico** (se llama STAT, SD o Estadística, según el modelo). Metes los datos y te da la media y la desviación típica directamente. **No sustituye a la tabla** (en el examen hay que enseñar los pasos), pero sirve para **comprobar** que no te has equivocado.

Lo que suele aparecer en pantalla:

| Símbolo en la calculadora | Qué es en la guía |
|:---|:---|
| n | Número de datos |
| x̄ | Media |
| Σx | Suma de los datos |
| Σx² | Suma de los cuadrados |
| σx (o σn, xσn) | Desviación típica S (divide entre n) |
| sx (o σn−1, xσn−1) | Cuasidesviación típica s (divide entre n − 1) |
| a, b, r | Recta de regresión y correlación (Tema 3) |

**Pasos generales** (en las Casio de clase; en otras marcas es parecido):

1. Entra en el modo estadístico y elige **1 variable** (1-VAR).
2. Si tienes una tabla de frecuencias, activa la columna de **frecuencias** (FREQ) en la configuración. Así metes cada valor una vez con su nᵢ.
3. Escribe los datos (y sus frecuencias) en la tabla de la pantalla.
4. Sal de la tabla (AC) y busca en el menú de opciones el **cálculo de 1 variable**: ahí salen x̄, σx, sx, n…

::: {custom-style="Ojo"}
**⚠️ Ojo.** σx es la desviación típica **S** de los apuntes (la que divide entre n). sx es la cuasidesviación **s**. Y si la calculadora te da cuartiles (Q1, Q3), pueden no coincidir con la receta de los apuntes: en el examen, usa la receta.
:::

Cada modelo tiene las teclas en un sitio distinto. Practica con **tu** calculadora con el ejemplo de los hermanos: tiene que salirte x̄ = 0,977 y σx = 1,252. Si no te sale, pide ayuda a tu tutor la primera vez.

'''
s=s.replace("# Parte 0 bis. Excel desde cero",calc+"# Parte 0 bis. Excel desde cero")
import re
for old,new in [("0.10. Lo básico","0.11. Lo básico"),("0.11. Escribir","0.12. Escribir"),("0.12. Arrastrar","0.13. Arrastrar"),("0.13. Fijar","0.14. Fijar"),("0.14. Las funciones","0.15. Las funciones"),("0.15. Insertar","0.16. Insertar"),("0.16. Tabla din","0.17. Tabla din")]:
    s=s.replace("## "+old,"## "+new,1)
open(P,'w').write(s)
