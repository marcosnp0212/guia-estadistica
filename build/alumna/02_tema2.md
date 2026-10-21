# Tema 2. Análisis descriptivo de dos variables

::: {.video data-v="t2"}
:::

::: {custom-style="Idea"}
**🧠 La idea del tema.** Ahora miramos **dos características a la vez** de cada persona (por ejemplo, su departamento y si teletrabaja). Queremos saber si están **relacionadas**: ¿en unos departamentos se teletrabaja más que en otros? ¿O da igual el departamento?
:::

## 2.1. La tabla de doble entrada

Es una tabla de frecuencias con **filas** para los valores de una variable (X) y **columnas** para los de la otra (Y). En cada casilla va el número de personas que tienen **a la vez** ese valor de X y ese de Y. Se llama **frecuencia conjunta** y se escribe nᵢⱼ (fila i, columna j).

- Si al menos una variable es cualitativa, se llama **tabla de contingencia**.
- Si las dos son cuantitativas, se llama **tabla de correlación**.

**Ejemplo 1 (tabla de contingencia).** 40 empleados según su departamento (X) y su modalidad de trabajo (Y).

| Departamento \\ Modalidad | Presencial | Híbrido | Remoto | **Total** |
|:---|---:|---:|---:|---:|
| RRHH | 8 | 3 | 2 | **13** |
| Finanzas | 5 | 4 | 1 | **10** |
| Producción | 10 | 6 | 1 | **17** |
| **Total** | **23** | **13** | **4** | **40** |

Cómo se lee una casilla: "8 empleados son de RRHH **y** trabajan en presencial".

**Ejemplo 2 (tabla de correlación).** 40 empleados según su edad y su antigüedad, agrupadas en intervalos.

| Edad \\ Antigüedad | 0-5 | 5-10 | 10-15 | 15-20 | **Total** |
|:---|---:|---:|---:|---:|---:|
| 18-30 | 7 | 2 | 0 | 0 | **9** |
| 30-40 | 2 | 8 | 3 | 0 | **13** |
| 40-50 | 0 | 3 | 7 | 1 | **11** |
| 50-67 | 0 | 1 | 2 | 4 | **7** |
| **Total** | **9** | **14** | **12** | **5** | **40** |

Fíjate que los números grandes van en diagonal: los jóvenes tienen poca antigüedad y los mayores, mucha. Eso ya sugiere relación.

### Frecuencias relativas conjuntas

Se divide cada casilla entre el total n: fᵢⱼ = nᵢⱼ / n. Por ejemplo, 8/40 = 0,20: el 20 % de los empleados son de RRHH y presenciales.

::: {custom-style="Excel"}
**🖥️ En Excel: construir la tabla de doble entrada con tabla dinámica** (lo que hizo la profesora en *DatosTema2*).

1. Ten los datos en dos columnas con título (por ejemplo, A = Departamento, B = Modalidad), una fila por persona.
2. Clic en una celda de los datos → **Insertar** → **Tabla dinámica** → Aceptar.
3. Arrastra **Departamento** a **Filas** y **Modalidad** a **Columnas**.
4. Arrastra **Departamento** (otra vez) a **Valores**. Saldrá "Cuenta de Departamento". Eso son las nᵢⱼ.
5. Para frecuencias relativas: clic derecho en un número → **Mostrar valores como** → **% del total general**.

Si las columnas salen en un orden raro (por ejemplo, Híbrido antes que Presencial, porque Excel ordena alfabéticamente), puedes arrastrar los títulos de columna a mano para reordenarlos.

**Para agrupar edades en intervalos** (tabla de correlación) la profesora añadió columnas "Grupo Edad" y "Grupo Antigüedad" con el intervalo de cada persona, y después hizo la tabla dinámica con esas columnas. También puedes hacer clic derecho en la edad dentro de la tabla dinámica → **Agrupar**.

**Truco visual de clase:** selecciona los números de la tabla → **Inicio** → **Formato condicional** → **Escalas de color**. Las casillas con más gente se colorean más fuerte y se ve la diagonal de un vistazo.
:::

::: {custom-style="Mano"}
**✍️ A mano: construir la tabla de doble entrada.**

1. Dibuja una cuadrícula: una **fila** por cada valor de X y una **columna** por cada valor de Y. Deja una fila y una columna más para los totales.
2. Recorre los datos **persona a persona**. Para cada una, mira su X y su Y y pon un palote en la casilla donde se cruzan.
3. Cuenta los palotes de cada casilla: esas son las nᵢⱼ.
4. Suma cada fila (columna Total) y cada columna (fila Total).
5. **Comprobación:** la suma de los totales de fila y la de los totales de columna tienen que dar lo mismo: n.
6. Si te piden frecuencias relativas, divide cada casilla entre n.
:::


### Gráficos para dos variables

- **Diagrama de barras agrupadas o apiladas:** el más usado.
- **Gráfico de mosaico:** rectángulos cuyo tamaño es proporcional a la frecuencia; se usa con dos variables cualitativas. Excel no lo tiene; se puede imitar con un gráfico de **barras apiladas al 100 %** (Insertar → Columnas → Columna 100 % apilada), que muestra justo las distribuciones condicionadas.

::: {custom-style="Ojo"}
**⚠️ Cómo se lee un mosaico (pregunta de examen).** Cada columna es una categoría de la variable principal. El **ancho** de la columna es su **frecuencia marginal**: cuantas más personas, más ancha. Dentro de cada columna, el **alto** de cada trozo es la **frecuencia condicionada** de la otra variable. Si todas las columnas están cortadas a la misma altura, las variables son independientes.
:::

## 2.2. Distribuciones marginales

**Qué son.** La distribución de **una sola** de las dos variables, olvidándote de la otra. Son los **totales** de la tabla: la columna de la derecha (para X) y la fila de abajo (para Y). Se llaman "marginales" porque están en los márgenes.

$$n_{i\cdot}=\sum_j n_{ij} \qquad n_{\cdot j}=\sum_i n_{ij}$$

El puntito indica la variable que hemos "sumado". nᵢ. es el total de la fila i; n.ⱼ el total de la columna j.

**Ejemplo 1:**

| Departamento | nᵢ. |
|:---|---:|
| RRHH | 13 |
| Finanzas | 10 |
| Producción | 17 |

| Modalidad | n.ⱼ |
|:---|---:|
| Presencial | 23 |
| Híbrido | 13 |
| Remoto | 4 |

Una distribución marginal es una tabla de frecuencias normal y corriente, así que **se le aplica todo el Tema 1**: media, mediana, moda, varianza...

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


## 2.3. Distribuciones condicionadas

**Qué son.** La distribución de una variable **solo para un grupo** definido por la otra. Se escribe con una barra vertical "|", que se lee "condicionado a" o "sabiendo que".

- X | Y = Presencial → "departamentos **de los que trabajan en presencial**": es la **columna** de Presencial.
- Y | X = Producción → "modalidades **de los de Producción**": es la **fila** de Producción.

| X \| Y = Presencial | nᵢ |
|:---|---:|
| RRHH | 8 |
| Finanzas | 5 |
| Producción | 10 |
| Total | 23 |

| Y \| X = Producción | nⱼ |
|:---|---:|
| Presencial | 10 |
| Híbrido | 6 |
| Remoto | 1 |
| Total | 17 |

Para comparar grupos, se pasan a **porcentajes dentro del grupo** (dividiendo entre el total de esa fila o columna): de los 17 de Producción, 10/17 = 58,8 % son presenciales.

::: {custom-style="Truco"}
**💡 Truco para no perderte.** Lo que va **detrás** de la barra "|" es el grupo al que te restringes. Tapa con la mano todo lo demás de la tabla y quédate solo con esa fila o columna.
:::

::: {custom-style="Otra"}
Condicionar es **hacer zoom en un grupo**. "Modalidad de los de Producción" significa: olvídate de RRHH y de Finanzas y mira solo la fila de Producción: 10 presenciales, 6 híbridos y 1 en remoto, de 17 personas.

Para comparar grupos de distinto tamaño, pásalo a porcentajes **dentro del grupo**: 10 ÷ 17 = 59 % presenciales.
:::

**Condicionar a varios valores.** Si te piden "Y condicionada a que X vale 2 o 3", **sumas** esas filas.

**Ejercicio de los apuntes.** X = días de ausencia, Y = días de asuntos propios.

| X \\ Y | 2 | 3 | 5 | Total |
|:---|---:|---:|---:|---:|
| 1 | 1 | 3 | 2 | 6 |
| 2 | 4 | 1 | 5 | 10 |
| 3 | 3 | 3 | 2 | 8 |
| 4 | 1 | 4 | 3 | 8 |
| Total | 9 | 11 | 12 | 32 |

Y | X ∈ {2, 3}: sumamos las filas del 2 y del 3.

| Y \| X = 2 o 3 | nⱼ | fⱼ |
|:---:|---:|---:|
| 2 | 4 + 3 = 7 | 7/18 = 0,389 |
| 3 | 1 + 3 = 4 | 4/18 = 0,222 |
| 5 | 5 + 2 = 7 | 7/18 = 0,389 |
| **Total** | **18** | **1** |

::: {custom-style="Mano"}
**✍️ A mano: la media de una condicionada.** Con la tabla de Y | X ∈ {2, 3} que acabas de hacer:

ȳ = (2·7 + 3·4 + 5·7) ÷ 18 = (14 + 12 + 35) ÷ 18 = 61 ÷ 18 = **3,39 días** de asuntos propios, de media, entre los que faltan 2 o 3 días.

La receta es la del Tema 1, usando solo las frecuencias de esa fila (o de la suma de filas) y dividiendo entre **su** total (18), no entre n = 32.
:::


::: {custom-style="Excel"}
**🖥️ En Excel.** En la tabla dinámica: clic derecho → **Mostrar valores como** → **% del total de filas** (te da las condicionadas por fila, Y|X) o **% del total de columnas** (X|Y). Para condicionar a varios valores, usa el filtro de la etiqueta de filas y deja marcados solo esos valores.
:::

## 2.4. Independencia

**Qué es.** Dos variables son **independientes** si saber el valor de una **no te dice nada** sobre la otra. Por ejemplo, si el porcentaje de presenciales fuera exactamente el mismo en todos los departamentos, la modalidad no dependería del departamento.

**Cómo se comprueba.** X e Y son independientes si, **en todas las casillas**:

$$f_{ij}=f_{i\cdot}\cdot f_{\cdot j}$$

Es decir: la frecuencia relativa de la casilla = (total de su fila / n) × (total de su columna / n).

Forma equivalente, más cómoda: las distribuciones condicionadas son todas iguales (los porcentajes de cada fila son iguales entre filas).

**Receta:**

1. Calcula la frecuencia relativa conjunta de una casilla: nᵢⱼ / n.
2. Calcula el producto de sus marginales: (nᵢ. / n) × (n.ⱼ / n).
3. Si **alguna** casilla no cumple la igualdad → **no son independientes** (son dependientes). Basta con una.
4. Para decir que **sí** son independientes, tiene que cumplirse en **todas**.

::: {custom-style="Otra"}
Dos variables son independientes si **el grupo no cambia nada**. Si en todos los departamentos hubiera el mismo % de presenciales, saber el departamento de alguien no te daría ninguna pista sobre su modalidad.

La fórmula fᵢⱼ = fᵢ.·f.ⱼ es solo la forma matemática de decir "los porcentajes son iguales en todas las filas". Por eso lo más fácil es calcular los % por filas y mirar si coinciden.
:::

**Ejemplo 1 (departamento y modalidad).** Primera casilla: f₁₁ = 8/40 = 0,20. Producto: (13/40) × (23/40) = 0,325 × 0,575 = 0,187. Como 0,20 ≠ 0,187, **no son independientes**.

Mirando las condicionadas por fila: RRHH tiene 61,5 % presencial, Finanzas 50 %, Producción 58,8 %. Son distintas, así que la modalidad depende algo del departamento.

::: {custom-style="Mano"}
**✍️ A mano: comprobar la independencia sin tantos decimales.** Hay una forma equivalente que da números más cómodos: comparar cada casilla con la **frecuencia esperada** si fueran independientes.

$$\text{esperada}_{ij}=\frac{n_{i\cdot}\cdot n_{\cdot j}}{n}$$

1. Para cada casilla: (total de su fila × total de su columna) ÷ n.
2. Compárala con la que hay en la tabla (nᵢⱼ).
3. Si coinciden **todas** → independientes. Si **alguna** no coincide → dependientes.

**Ejemplo 1**, casilla RRHH-Presencial: 13 × 23 ÷ 40 = **7,475**. En la tabla hay **8**. No coinciden → **no son independientes**. Con una casilla basta para decir que no.

**Ejemplo 7**, casilla Hombre-Indefinido: 180 × 120 ÷ 240 = 90, y en la tabla hay 90 ✔. Hay que repetirlo en las seis casillas para decir que sí son independientes (salen todas iguales).

Es la misma comprobación que fᵢⱼ = fᵢ. · f.ⱼ, multiplicada por n en los dos lados.
:::


**Ejemplo 7 (sexo y tipo de contrato, 240 empleados).**

| Sexo \\ Contrato | Indefinido | Temporal | Parcial | Total |
|:---|---:|---:|---:|---:|
| Hombre | 90 | 60 | 30 | 180 |
| Mujer | 30 | 20 | 10 | 60 |
| Total | 120 | 80 | 40 | 240 |

Hombres: 90/180 = 50 % indefinido, 33 % temporal, 17 % parcial. Mujeres: 30/60 = 50 %, 20/60 = 33 %, 10/60 = 17 %. **Exactamente iguales**. Comprobación de una casilla: 90/240 = 0,375 y (180/240)·(120/240) = 0,75 × 0,5 = 0,375 ✔. Lo mismo pasa en todas: **son independientes**. El tipo de contrato no depende del sexo.

::: {custom-style="Excel"}
**🖥️ En Excel: tabla de "lo que habría si fueran independientes"** (como la tabla «fᵢ. × f.ⱼ» de clase).

1. Haz la tabla de frecuencias relativas conjuntas (cada casilla dividida entre n). Supón que queda en B3:D5, con los totales de fila (fᵢ.) en E3:E5 y los de columna (f.ⱼ) en B6:D6.
2. En otra zona, en la primera casilla escribe `=$E3*B$6` y arrastra a toda la tabla.
3. Compara las dos tablas casilla a casilla. Si son iguales en todas, independientes. Si no, dependientes.

Fíjate en los **$ a medias**: `$E3` fija la columna E (siempre el total de fila) y `B$6` fija la fila 6 (siempre el total de columna). Así, al arrastrar, cada casilla usa su fila y su columna.
:::

::: {custom-style="Ojo"}
**⚠️ Ojo.** En la vida real casi nunca sale exactamente igual. En esta asignatura, si las frecuencias no coinciden, se concluye que **no son independientes** (dependientes). Una forma muy rápida de demostrar la dependencia: si hay una casilla con **0** pero su fila y su columna tienen totales distintos de 0, ya no pueden ser independientes (0 ≠ algo positivo).
:::

## ✔ Comprueba que sabes hacer (Tema 2)

- Construir una tabla de doble entrada **a mano** (con palotes) y en Excel con tabla dinámica.
- Sacar las distribuciones marginales (los totales) y calcular con ellas medias, medianas... como en el Tema 1.
- Sacar una distribución condicionada (una fila o una columna, o la suma de varias).
- Comprobar si dos variables son independientes comparando fᵢⱼ con fᵢ. × f.ⱼ, con las frecuencias esperadas (a mano) o comparando los porcentajes por filas.
- Calcular la media de una marginal y de una condicionada con calculadora.
