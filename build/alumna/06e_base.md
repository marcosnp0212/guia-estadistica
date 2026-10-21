# Parte 0. Repaso de base: números y calculadora

Antes de entrar en la estadística, repasamos las pocas operaciones que vamos a usar. Si alguna ya la dominas, salta a la siguiente.

## 0.1. El orden de las operaciones

Cuando una cuenta tiene varias operaciones, no se hacen de izquierda a derecha sin más. Se sigue este orden:

1. Primero lo que está **entre paréntesis**.
2. Después las **potencias y raíces** (el "al cuadrado", la raíz).
3. Después **multiplicaciones y divisiones**.
4. Por último **sumas y restas**.

Ejemplo: 2 + 3 × 4 = 2 + 12 = **14** (no 20, porque la multiplicación va antes).

Ejemplo: (2 + 3) × 4 = 5 × 4 = **20** (el paréntesis manda).

::: {custom-style="Ojo"}
**⚠️ Ojo.** Excel sigue exactamente este mismo orden. Si escribes `=2+3*4` te da 14. Si quieres que sume primero, tienes que poner paréntesis: `=(2+3)*4`. Muchos errores en el examen vienen de un paréntesis olvidado, sobre todo al dividir: `=A1+A2/2` no es lo mismo que `=(A1+A2)/2`.
:::

## 0.2. Decimales y redondeo

En España (y en tu Excel) los decimales se escriben con **coma**: 0,477. En los apuntes de la profesora a veces aparecen con punto (0.477) porque están hechos con un programa en inglés. Es lo mismo.

Para redondear a 2 decimales, mira la tercera cifra decimal. Si es 0, 1, 2, 3 o 4, la segunda cifra se queda igual. Si es 5, 6, 7, 8 o 9, la segunda cifra sube uno.

- 1,2521 → la tercera cifra es 2 → se queda **1,25**.
- 0,4772 → la tercera cifra es 7 → sube → **0,48**.
- 2,3456 → la tercera cifra es 5 → sube → **2,35**.

En Excel: `=REDONDEAR(A1;2)` redondea el contenido de A1 a 2 decimales. También puedes dejar el número como está y usar los botones de "Aumentar/Disminuir decimales" de la pestaña Inicio, que solo cambian lo que se ve.

::: {custom-style="Truco"}
**💡 Truco.** No redondees a mitad de un ejercicio. Deja que Excel trabaje con todos los decimales y redondea solo el resultado final. Si redondeas antes, el resultado final se desvía un poco.
:::

## 0.3. Fracciones y divisiones

Una fracción es una división. 3/4 significa 3 ÷ 4 = 0,75.

En estadística casi todo es "algo dividido entre el total". Por ejemplo, si 21 de 44 personas no tienen hermanos, la proporción es 21/44 = 0,477.

## 0.4. Porcentajes

Un porcentaje es una proporción multiplicada por 100.

- Proporción 0,477 → porcentaje **47,7 %**.
- Porcentaje 12 % → proporción **0,12**.

Para pasar de % a número decimal, divide entre 100. Para pasar de decimal a %, multiplica por 100.

**Subir un porcentaje.** Subir un 5 % es multiplicar por 1,05. Subir un 20 % es multiplicar por 1,20. Bajar un 10 % es multiplicar por 0,90. Bajar un 2 % es multiplicar por 0,98.

::: {custom-style="Truco"}
**💡 Truco.** "Subir un 3 %" = "multiplicar por 1 + 0,03 = 1,03". "Bajar un 3 %" = "multiplicar por 1 − 0,03 = 0,97". Esto lo usarás muchísimo en el Tema 4.
:::

## 0.5. Potencias (el "al cuadrado")

Elevar al cuadrado es multiplicar un número por sí mismo: 5² = 5 × 5 = 25.

Un número negativo al cuadrado da positivo: (−3)² = (−3) × (−3) = 9. Esto es importante para la varianza.

En Excel, el cuadrado se escribe con el símbolo `^` (acento circunflejo, tecla a la derecha de la P, y se pulsa con Mayúsculas): `=5^2` da 25. Para que salga el símbolo a veces hay que pulsar la tecla y luego la barra espaciadora.

## 0.6. Raíz cuadrada

La raíz cuadrada es lo contrario del cuadrado: √25 = 5, porque 5² = 25.

En Excel: `=RAIZ(25)` da 5.

Hay otras raíces (cúbica, raíz 12...). Las usarás en el Tema 4. Una raíz se puede escribir como potencia de una fracción: la raíz cúbica de 8 es 8^(1/3) = 2. En Excel: `=8^(1/3)`.

## 0.7. El símbolo Σ (sumatorio)

Σ es la letra griega "sigma" mayúscula. Solo significa **"suma todo esto"**.

Si ves Σ xᵢ, lee: "suma todos los valores x". Si ves Σ xᵢ·nᵢ, lee: "multiplica cada valor por su frecuencia y suma todos esos resultados".

En Excel, Σ es la función `=SUMA( )`.

## 0.8. Los subíndices

La letra pequeña de abajo (el subíndice) solo sirve para numerar. x₁ es el primer valor, x₂ el segundo... xᵢ significa "un valor cualquiera, el que toque". No es una operación.

## 0.9. Los intervalos y sus corchetes

Un intervalo es un tramo de números. Los corchetes y paréntesis dicen si los extremos entran o no:

| Se escribe | Se lee | ¿Entra el 10? | ¿Entra el 20? |
|:---|:---|:---:|:---:|
| [10, 20] | de 10 a 20, ambos incluidos | Sí | Sí |
| (10, 20] | más de 10 y hasta 20 | No | Sí |
| [10, 20) | desde 10 y menos de 20 | Sí | No |

**Corchete [ ]** = el número entra. **Paréntesis ( )** = el número no entra.

**Amplitud** de un intervalo = extremo de arriba − extremo de abajo. La amplitud de (10, 20] es 20 − 10 = 10.

**Marca de clase** = el punto medio del intervalo = (abajo + arriba) / 2. La marca de clase de (10, 20] es (10 + 20)/2 = 15.

## 0.10. La calculadora

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

**Pasos generales** (en las Casio, que son las más habituales; en otras marcas es parecido):

1. Entra en el modo estadístico y elige **1 variable** (1-VAR).
2. Si tienes una tabla de frecuencias, activa la columna de **frecuencias** (FREQ) en la configuración. Así metes cada valor una vez con su nᵢ.
3. Escribe los datos (y sus frecuencias) en la tabla de la pantalla.
4. Sal de la tabla (AC) y busca en el menú de opciones el **cálculo de 1 variable**: ahí salen x̄, σx, sx, n…

::: {custom-style="Ojo"}
**⚠️ Ojo.** σx es la desviación típica **S** de los apuntes (la que divide entre n). sx es la cuasidesviación **s**. Y si la calculadora te da cuartiles (Q1, Q3), pueden no coincidir con la receta de los apuntes: en el examen, usa la receta.
:::

Cada modelo tiene las teclas en un sitio distinto. Practica con **tu** calculadora con el ejemplo de los hermanos: tiene que salirte x̄ = 0,977 y σx = 1,252. Si no sale, pide ayuda a alguien de clase la primera vez: es solo encontrar las teclas.

# Parte 0 bis. Excel desde cero

## 0.11. Lo básico de una hoja

Una hoja de Excel es una cuadrícula. Las **columnas** tienen letras (A, B, C...) y las **filas** números (1, 2, 3...). Cada casilla es una **celda** y se nombra por su columna y su fila: **B3** es la celda de la columna B, fila 3.

Un **rango** es un grupo de celdas seguidas. `B2:B45` significa "desde B2 hasta B45".

## 0.12. Escribir una fórmula

1. Haz clic en la celda donde quieres el resultado.
2. Escribe **siempre** primero el signo **=**.
3. Escribe la operación o la función.
4. Pulsa **Intro**.

Si no pones el `=`, Excel lo toma como texto y no calcula nada.

::: {custom-style="Ojo"}
**⚠️ Ojo. Excel en español usa punto y coma.** Dentro de una función, las partes se separan con **;** y no con coma, porque la coma es el decimal. Ejemplo: `=CONTAR.SI(B2:B45;0)`. Si escribes una coma, Excel dará error.
:::

## 0.13. Arrastrar una fórmula (copiar hacia abajo)

Si en C2 escribes `=B2*2` y quieres lo mismo en C3, C4, C5...:

1. Selecciona C2.
2. Pon el ratón en la esquina inferior derecha de la celda: aparece una cruz negra pequeña.
3. Arrastra hacia abajo (o haz doble clic en esa cruz).

Excel cambia solo las referencias: en C3 pondrá `=B3*2`, en C4 `=B4*2`...

## 0.14. Fijar una celda con $ (referencia absoluta)

A veces quieres que al arrastrar una celda **no cambie**. Por ejemplo, para dividir cada frecuencia entre el total, que está siempre en B9: `=B2/$B$9`.

El símbolo **$** "congela" la celda. Truco: escribe B9 y pulsa la tecla **F4**; Excel pone los $ solo.

::: {custom-style="Truco"}
**💡 Truco.** Regla práctica: el **total** y la **media** casi siempre se fijan con $, porque se usan en todas las filas.
:::

## 0.15. Las funciones que vas a usar

No te las aprendas ahora. Aparecerán cuando toque y tienes una chuleta completa al final.

| Para... | Función en Excel (español) |
|:---|:---|
| Sumar | `=SUMA(rango)` |
| Contar cuántos datos hay | `=CONTAR(rango)` |
| Contar cuántas veces sale un valor | `=CONTAR.SI(rango;valor)` |
| Media | `=PROMEDIO(rango)` |
| Mediana | `=MEDIANA(rango)` |
| Moda | `=MODA.UNO(rango)` |
| Máximo y mínimo | `=MAX(rango)` y `=MIN(rango)` |
| Cuartil | `=CUARTIL.INC(rango;1)` (o 2, 3) |
| Percentil | `=PERCENTIL.INC(rango;0,97)` |
| Varianza (la de clase) | `=VAR.P(rango)` |
| Cuasivarianza | `=VAR.S(rango)` |
| Desviación típica | `=DESVEST.P(rango)` |
| Cuasidesviación típica | `=DESVEST.S(rango)` |
| Multiplicar dos columnas y sumar | `=SUMAPRODUCTO(rango1;rango2)` |
| Raíz cuadrada | `=RAIZ(número)` |
| Covarianza | `=COVARIANZA.P(rangoX;rangoY)` |
| Correlación | `=COEF.DE.CORREL(rangoX;rangoY)` |
| Pendiente de la recta | `=PENDIENTE(rangoY;rangoX)` |
| Término independiente | `=INTERSECCION.EJE(rangoY;rangoX)` |
| Predicción | `=PRONOSTICO.LINEAL(x;rangoY;rangoX)` |
| Media geométrica | `=MEDIA.GEOM(rango)` |

## 0.16. Insertar un gráfico

1. Selecciona los datos (por ejemplo, la columna de valores y la de frecuencias).
2. Pestaña **Insertar** → grupo **Gráficos**.
3. Elige el tipo: columnas (barras), circular (sectores), histograma, cuadro y bigotes (caja), dispersión, radial.
4. Con el gráfico seleccionado, el botón **+** que aparece al lado permite añadir **títulos de ejes**, **etiquetas de datos** y **línea de tendencia**.

## 0.17. Tabla dinámica (para contar por categorías)

Sirve para contar automáticamente cuántas veces aparece cada valor o cada combinación de valores. La usó la profesora en el Tema 2.

1. Haz clic en cualquier celda de tus datos (con su fila de títulos).
2. **Insertar** → **Tabla dinámica** → Aceptar (en una hoja nueva).
3. A la derecha aparece una lista con los nombres de tus columnas.
4. Arrastra la variable que quieres contar a **Filas**.
5. Arrastra esa misma variable (u otra) a **Valores**. Si sale "Suma de...", haz clic encima → **Configuración de campo de valor** → elige **Cuenta**.
6. Para una tabla de doble entrada, arrastra la segunda variable a **Columnas**.

::: {custom-style="Truco"}
**💡 Truco.** Para ver porcentajes en vez de recuentos: clic derecho sobre un número de la tabla dinámica → **Mostrar valores como** → **% del total general** (o % del total de fila / de columna, para las condicionadas del Tema 2).
:::
