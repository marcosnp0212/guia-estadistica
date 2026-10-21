# Repaso exprés: el examen en 3 días

::: {custom-style="Idea"}
**🧠 Si te quedan pocos días, empieza aquí.** El examen es como el modelo de la profesora: 30 preguntas tipo test y 10 de respuesta corta. Casi todo consiste en **saber qué es cada cosa, qué fórmula va en cada caso y qué trampa evitar**. No hace falta leer la guía entera. Aquí tienes lo imprescindible de cada tema, explicado con calma y con un ejemplo. Si algo no se entiende, al final de cada tema hay un enlace al apartado completo.
:::

## El plan de 3 días

Unas 2 horas al día. Mejor en bloques de 25 minutos con 5 de descanso.

| Día | Qué hacer | Tiempo |
|:---|:---|---:|
| **Día 1** | Lee **Tema 1** y **Tema 2** de este repaso. Después, haz las **preguntas 1 a 15 del examen modelo**: decide tu respuesta antes de abrir la solución. | 2 h |
| **Día 2** | Lee **Tema 3** y **Tema 4** de este repaso. Después, las **preguntas 16 a 30 y P1 a P10 del examen modelo**. | 2 h |
| **Día 3** | Haz el **Simulacro tipo test** con reloj (90 minutos). Al entregar, lee la explicación de cada fallo y vuelve aquí al tema que peor te haya salido. | 2 h |
| **Mañana del examen** | Solo **«Las 15 trampas del test»**, al final de este repaso. Nada nuevo. | 15 min |

::: {custom-style="Truco"}
**💡 Los vídeos.** Si te cuesta leer de seguido, el vídeo de cada tema cuenta lo mismo con voz y animaciones. Puedes ponerlo a 1,25× y leer después este repaso para fijarlo.
:::

## Tema 1 en 20 minutos

### Qué tipo de variable es

Es lo primero que hay que mirar, y cae casi seguro en el test.

- ¿La respuesta es una **palabra**? → **cualitativa**. Si esas palabras tienen un orden (bajo, medio, alto), es **ordinal**. Si no lo tienen (departamento, sexo), es **nominal**.
- ¿La respuesta es un **número**? → **cuantitativa**. Si se cuenta con los dedos (hijos, cursos), es **discreta**. Si se mide y puede llevar decimales (salario, altura), es **continua**.

**Parámetro y estadístico.** Un parámetro describe a toda la **población**; un estadístico, a una **muestra**. Truco: **P**arámetro → **P**oblación; **E**stadístico → mu**E**stra.

### El centro: media, mediana y moda

- **Media (x̄).** Sumas todo y divides entre cuántos hay. Si los datos vienen en una tabla, cada valor cuenta tantas veces como se repite: x̄ = Σxᵢ·nᵢ / n.
- **Mediana (Me).** El dato que queda **justo en el medio** cuando los ordenas.
- **Moda (Mo).** El valor que **más se repite**.

**Ejemplo.** Salarios: 1200, 1300, 1350, 1400 y 9000 €. La media es 2850 €, pero nadie cobra eso: el 9000 la ha arrastrado hacia arriba. La mediana, 1350 €, sí representa lo "normal".

::: {custom-style="Ojo"}
**⚠️ Pregunta típica.** Cuando hay valores extremos (atípicos), es mejor la **mediana** o la **media truncada** (la que quita un trozo de datos de cada punta). Se dice que son **robustas**: los extremos no las mueven.
:::

**La moda con intervalos de distinto ancho.** Si los intervalos no miden lo mismo, no se elige el que tiene más datos, sino el que tiene más datos **por unidad de ancho**: la **densidad**, dᵢ = nᵢ / aᵢ. Ejemplo: 0–10 con 20 datos (densidad 2) y 10–40 con 30 datos (densidad 1). El intervalo modal es 0–10, aunque tenga menos datos. Por la misma razón, en un histograma con anchos distintos, la altura de cada barra es la densidad.

### La dispersión: cuánto se separan los datos

- **Varianza (S²).** La media de lo que se separa cada dato de la media, al cuadrado. A mano: S² = Σxᵢ²·nᵢ / n − x̄².
- **Desviación típica (S).** La raíz de la varianza. Está en las mismas unidades que los datos.
- **Cuasivarianza.** Lo mismo, pero dividiendo entre n − 1. En Excel: `VAR.P` es la varianza (entre n) y `VAR.S` es la cuasivarianza (entre n − 1).

**Coeficiente de variación: CV = S / x̄.** Sirve para **comparar** la dispersión de dos grupos con medias o unidades distintas. No tiene unidades. **Cuanto más pequeño, más homogéneo.** Ejemplo: el grupo A tiene media 50 y S = 5 (CV = 0,10) y el B, media 10 y S = 2 (CV = 0,20). Aunque la S de B es menor, el más homogéneo es A.

### Cuartiles, diagrama de caja y atípicos

- **C₁** deja por debajo el 25 % de los datos; **C₃**, el 75 %. La mediana es C₂.
- **IQR = C₃ − C₁**: el ancho del 50 % central.
- **Atípicos:** los datos que se salen de **C₁ − 1,5·IQR** por abajo o de **C₃ + 1,5·IQR** por arriba.

**Ejemplo.** C₁ = 20 y C₃ = 30, así que IQR = 10 y el límite de arriba es 30 + 15 = 45. Un dato de 47 es atípico.

**Leer la caja.** Si la mediana está más cerca del borde de abajo de la caja y el bigote de arriba es más largo, la distribución tiene cola a la derecha: **asimetría positiva**.

### La forma: asimetría y curtosis

- **Asimetría (CA).** CA > 0: cola a la **derecha** (unos pocos valores muy altos; la media queda por encima de la mediana). CA < 0: cola a la izquierda. CA = 0: simétrica.
- **Curtosis.** Mayor que 0: muy apuntada (leptocúrtica). Menor que 0: aplastada (platicúrtica).

### Grupos y cambios en los datos

**Varianza de varios grupos:** total = dentro + entre. La de **dentro** mide lo que varían los datos dentro de cada grupo; la de **entre**, lo que se separan las medias de los grupos. Si la de "entre" es una parte grande del total, los grupos son muy distintos entre sí.

**Si a todos los datos les haces Y = a·X + b** (por ejemplo, subir un 3 % y sumar 50 €): la media pasa a ȳ = a·x̄ + b, pero la varianza solo nota la multiplicación: S²ᵧ = a²·S²ₓ. **Sumar una cantidad no cambia la dispersión**: todos se mueven lo mismo.

::: {custom-style="Excel"}
**🖥️ En Excel.** Media de una tabla: `=SUMAPRODUCTO(x;n)/SUMA(n)`. Tipificar el dato de A2 con la media en B1 y S en B2, para copiar hacia abajo: `=(A2-$B$1)/$B$2`. El dato va sin dólares porque cambia en cada fila; la media y S, con dólares porque son siempre las mismas.
:::

[Ver el Tema 1 completo](#tema-1.-análisis-descriptivo-de-una-variable)

## Tema 2 en 10 minutos

Ahora miramos **dos características a la vez** de cada persona, en una tabla de doble entrada: una variable en las filas y otra en las columnas.

### Las tres formas de leer la tabla

- **Conjunta (nᵢⱼ).** Una casilla: "8 personas son de RRHH **y** trabajan en presencial". En relativa, fᵢⱼ = nᵢⱼ / n.
- **Marginal.** Los totales de los márgenes. El total de una fila es nᵢ. y el de una columna, n.ⱼ. Es la distribución de **una sola** variable, olvidándote de la otra.
- **Condicionada.** Hacer zoom en un grupo: "de los de Producción, ¿cuántos trabajan en presencial?". Coges **solo esa fila** y la divides entre **su total**.

### ¿Son independientes?

Dos variables son independientes si **el grupo no cambia nada**. Por ejemplo, si en todos los departamentos hubiera el mismo % de presenciales, saber el departamento de alguien no te daría ninguna pista.

En fórmula: fᵢⱼ = fᵢ. · f.ⱼ **en todas las casillas**. Dicho de otra forma: **todas las condicionadas son iguales entre sí e iguales a la marginal**.

**Ejemplo (pregunta del modelo).** Si el 70 % del total trabaja a jornada completa y género y jornada son independientes, entonces el 70 % de los hombres trabaja a jornada completa. Y el 70 % de las mujeres, también.

::: {custom-style="Truco"}
**💡 Frecuencia esperada.** Si fueran independientes, en una casilla habría nᵢ. · n.ⱼ / n. Ejemplo: fila de 40 y columna de 50 con n = 100 → 40 · 50 / 100 = 20.
:::

### Gráficos

Para dos variables cualitativas: barras agrupadas o apiladas, y el **mosaico**. En el mosaico, el **ancho** de cada columna es la frecuencia marginal y el **alto** de cada trozo es la condicionada.

[Ver el Tema 2 completo](#tema-2.-análisis-descriptivo-de-dos-variables)

## Tema 3 en 15 minutos

Dos variables numéricas de cada persona, por ejemplo antigüedad y salario. Queremos saber si van juntas y predecir una con la otra.

### La nube de puntos y la covarianza

Cada persona es un punto. Si la nube **sube** de izquierda a derecha, la relación es **directa**: cuando una crece, la otra también. Si **baja**, es **inversa**.

La **covarianza** (S_XY) lo dice con un número: S_XY = Σxᵢyᵢ / n − x̄·ȳ. **Solo hay que mirar su signo**: positiva, relación directa; negativa, inversa. Su tamaño no dice nada, porque depende de las unidades.

### La recta de regresión

Ŷ = a + b·X es la regla para **adivinar Y cuando sabes X**.

- **b = S_XY / S²ₓ** (la pendiente): cuánto sube Y, de media, por cada unidad más de X. Lleva la varianza de la **X** abajo.
- **a = ȳ − b·x̄**: el punto de partida, lo que valdría Y con X = 0.

**Ejemplo (pregunta del modelo).** Salario = 1390 + 78,5 · Antigüedad. Con 10 años: 1390 + 78,5 · 10 = **2175 €**. Por cada año más, el salario sube de media 78,5 €.

**Cosas que caen en el test:**

- La recta siempre **pasa por (x̄, ȳ)**. También la de X sobre Y, así que **las dos rectas se cortan ahí**.
- Si S_XY = 0, las pendientes son 0: la recta de Y sobre X es **horizontal** (Ŷ = ȳ) y la de X sobre Y es **vertical** (X̂ = x̄). No hay relación lineal.
- **No predigas fuera de los datos.** Si las antigüedades van de 1 a 15 años, la recta no sirve para 40 años: no sabemos si la relación sigue siendo recta tan lejos. Eso se llama **extrapolar**.

### r y R²: ¿la relación es fuerte?

- **r = S_XY / (Sₓ · Sᵧ)**, entre −1 y 1. Cerca de 1, relación directa fuerte; cerca de −1, inversa fuerte; cerca de 0, débil. **Tiene el mismo signo que b.** No tiene unidades: si pasas X de euros a miles de euros, **r no cambia**.
- **R² = r²**, entre 0 y 1. Es el **porcentaje de la variabilidad de Y que explica la recta**. Ejemplo: r = −0,85 → R² = 0,7225 → la recta explica el **72,25 %**. El signo desaparece al elevar al cuadrado.

::: {custom-style="Ojo"}
**⚠️ r = 0 no significa "ninguna relación".** Significa que no hay relación **lineal**. Puede haber una relación curva, por ejemplo en forma de U.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** `=PENDIENTE(Y;X)`, `=INTERSECCION.EJE(Y;X)`, `=COEF.DE.CORREL(X;Y)`, `=COEFICIENTE.R2(Y;X)`. En las dos primeras, **primero va la Y**.
:::

[Ver el Tema 3 completo](#tema-3.-regresión-y-correlación)

## Tema 4 en 15 minutos

Un índice dice **cuánto ha cambiado algo** respecto a un año de referencia, el año base, que vale 100.

### Leer un índice

Al índice le restas 100 y tienes la variación en %.

- Índice 125,4 → ha subido un **25,4 %**.
- Índice 92 → ha bajado un **8 %**.

Un índice no son euros: 125,4 no quiere decir que algo cueste 125,4 €.

### Los porcentajes se multiplican

Es la idea más importante del tema. Subir un 10 % es multiplicar por **1,10**; bajar un 20 % es multiplicar por **0,80**. Cada subida se aplica sobre lo que ya tienes, así que los porcentajes **nunca se suman**:

- Sube un 10 % y luego un 20 %: 1,10 · 1,20 = 1,32 → **+32 %**, no +30 %.
- Sube un 10 % y luego baja un 10 %: 1,10 · 0,90 = 0,99 → **pierdes un 1 %**.

Por eso:

- **Tasa media de varios años:** se usa la **media geométrica**: multiplicas los factores, haces la raíz y restas 1. En Excel, `=MEDIA.GEOM(rango)-1`.
- **De anual a mensual:** 6 % anual → (1,06)^(1/12) − 1 = **0,487 % al mes**, no 0,5 %.
- **Inversión:** el índice "al revés" es el inverso, 1/I (en tanto por uno).
- **Cambio de base:** cada índice entre el del nuevo año base, por 100. Ejemplo: 150 / 125 · 100 = 120.

### Índices de varios productos

- **Laspeyres:** usa las cantidades del **año base** (q₀). Como mantiene la cesta antigua, tiende a **exagerar** la subida de precios.
- **Paasche:** usa las cantidades del **año actual** (qₜ).
- **Fisher:** la media geométrica de los dos, √(L · P).

Truco: **L**aspeyres = cantidades de **L**a base.

### Deflactar: euros reales

Para quitar el efecto de la inflación, **se divide** entre el IPC: valor real = nominal / IPC, con el IPC en tanto por uno (o nominal / IPC × 100 si está en base 100).

**Ejemplo.** Un salario de 1800 € con el IPC en 1,20 equivale a 1800 / 1,20 = **1500 €** del año base. Y si el salario sube un 5 % y los precios un 3 %, el salario real sube 1,05 / 1,03 − 1 = **1,94 %**, no un 2 %.

[Ver el Tema 4 completo](#tema-4.-números-índices)

## Las 15 trampas del test

Para leer la mañana del examen. Cada una es un error que se repite mucho.

1. **Intervalos de distinto ancho:** la moda va por **densidad**, no por el que tiene más datos.
2. **VAR.P** divide entre n (varianza); **VAR.S**, entre n − 1 (cuasivarianza).
3. **¿Te dan S o S²?** Para la pendiente hace falta la varianza: si te dan S, elévala al cuadrado.
4. Para comparar grupos con medias o unidades distintas, se usa el **CV**, no S.
5. La suma de las desviaciones a la media es **siempre 0**.
6. **Sumar una cantidad** a todos no cambia la varianza; multiplicar por a la multiplica por a².
7. Varianza total = dentro **+** entre. Se suman.
8. CA > 0 = cola a la **derecha**.
9. Atípicos: más allá de **1,5 · IQR** por fuera de C₁ o de C₃.
10. Independencia = todas las condicionadas **iguales a la marginal**.
11. r = 0 → no hay relación **lineal**, pero puede haber una curva. r no cambia con las unidades.
12. R² es r al cuadrado: pierde el signo. r lleva el signo de la pendiente.
13. b = S_XY / S²ₓ (la X abajo) y a = ȳ − b · x̄.
14. Los porcentajes se **multiplican**; la tasa media es la **geométrica**; 6 % anual no es 0,5 % al mes.
15. Laspeyres = cantidades del año **base**. Deflactar = **dividir** entre el IPC.

::: {custom-style="Truco"}
**💡 En el test, descarta primero.** Lee las cuatro opciones antes de elegir. Muchas veces dos se descartan solas porque dicen algo **imposible**: un CV negativo, un R² mayor que 1, una varianza negativa, "la suma de desviaciones es siempre positiva". Entre las dos que quedan, piensa en un ejemplo pequeño con números.
:::
