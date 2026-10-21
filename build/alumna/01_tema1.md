# Tema 1. Análisis descriptivo de una variable

::: {.video data-v="t1"}
:::

::: {custom-style="Idea"}
**🧠 La idea del tema.** Tenemos un montón de datos de **una sola característica** (por ejemplo, cuántos hermanos tiene cada persona). Queremos **resumirlos**: ordenarlos en una tabla, dibujarlos, y dar unos pocos números que cuenten cómo son. ¿Dónde está el centro? ¿Están muy dispersos? ¿Tienen forma rara?
:::

## 1.1. Vocabulario básico

Estas palabras salen en preguntas de teoría. Con una frase de cada una vas bien.

**Individuo.** Cada "cosa" de la que tomamos datos: una persona, una empresa, una provincia.

**Población.** Todos los individuos que nos interesan. Ejemplo: todos los trabajadores de España.

**Muestra.** Un trozo de la población que estudiamos porque no podemos preguntar a todos. Ejemplo: 500 trabajadores elegidos al azar. Si estudiamos a **todos**, se llama **censo**.

**Parámetro.** Un número que describe a la **población** (la media de todos). **Estadístico.** El mismo tipo de número, pero calculado en la **muestra**.

::: {custom-style="Truco"}
**💡 Truco.** **P**arámetro → **P**oblación. **E**stadístico → mu**E**stra.
:::

**Variable.** La característica que medimos: el salario, el sexo, el número de hijos.

## 1.2. Tipos de variables

Es lo primero que hay que mirar en cualquier ejercicio, porque **según el tipo se pueden hacer unas cosas u otras**.

| Tipo | Cómo son sus valores | Ejemplos |
|:---|:---|:---|
| **Cuantitativa discreta** | Números que se cuentan (0, 1, 2...). Sin decimales "intermedios". | Nº de hijos, nº de hermanos, nº de lesiones |
| **Cuantitativa continua** | Números que se miden, pueden tener decimales. | Salario, altura, superficie de una vivienda |
| **Cualitativa nominal** | Categorías sin orden. | Sexo, departamento, estado civil |
| **Cualitativa ordinal** | Categorías con un orden lógico. | Nivel de estudios, satisfacción (baja, media, alta) |

::: {custom-style="Truco"}
**💡 Truco para distinguirlas.** Pregúntate: ¿la respuesta es un número? → cuantitativa. ¿Se cuenta con los dedos (1, 2, 3)? → discreta. ¿Se mide con una regla, una báscula o en euros? → continua. ¿La respuesta es una palabra? → cualitativa. ¿Esas palabras tienen un orden natural? → ordinal. Si no → nominal.
:::

::: {custom-style="Ojo"}
**⚠️ Ojo.** Con una variable **nominal** (por ejemplo, departamento) solo se puede calcular la **moda** y hacer gráficos de barras o sectores. No tiene sentido calcular media ni mediana: no existe "el departamento medio".
:::

**Estudio unidimensional** = una variable cada vez (Tema 1). **Estudio bidimensional** = dos variables juntas (Temas 2 y 3).

## 1.3. La tabla de frecuencias

### Qué es

Una tabla que dice **cuántas veces aparece cada valor**. Es el primer paso siempre.

### Las columnas de la tabla

| Símbolo | Nombre | Qué significa | Cómo se calcula |
|:---:|:---|:---|:---|
| xᵢ | Valor | Cada valor distinto, **ordenado de menor a mayor** | — |
| nᵢ | Frecuencia absoluta | Cuántas veces aparece ese valor | Contando |
| fᵢ | Frecuencia relativa | Qué parte del total es | nᵢ ÷ n |
| %ᵢ | Porcentaje | La relativa en % | fᵢ × 100 |
| Nᵢ | Frecuencia absoluta acumulada | Cuántos datos hay **hasta** ese valor (incluido) | Suma de las nᵢ desde arriba hasta esa fila |
| Fᵢ | Frecuencia relativa acumulada | Qué proporción hay hasta ese valor | Nᵢ ÷ n |

**n** es el número total de datos (el **tamaño muestral**).

Comprobaciones que siempre se cumplen: la suma de las nᵢ es n; la suma de las fᵢ es 1; la suma de los % es 100; la última Nᵢ es n; la última Fᵢ es 1.

::: {custom-style="Ojo"}
**⚠️ Ojo.** Las frecuencias **acumuladas** solo tienen sentido si los valores se pueden ordenar (cuantitativas u ordinales). Para el departamento o el sexo no se calculan.
:::

### Ejemplo de clase: número de hermanos (44 personas)

Se preguntó a 44 personas cuántos hermanos tenían. Los datos están en el Excel de clase (hoja *Hermanos*).

| xᵢ | nᵢ | fᵢ | %ᵢ | Nᵢ | Fᵢ |
|---:|---:|---:|---:|---:|---:|
| 0 | 21 | 0,477 | 47,73 | 21 | 0,477 |
| 1 | 12 | 0,273 | 27,27 | 33 | 0,750 |
| 2 | 6 | 0,136 | 13,64 | 39 | 0,886 |
| 3 | 2 | 0,045 | 4,55 | 41 | 0,932 |
| 4 | 2 | 0,045 | 4,55 | 43 | 0,977 |
| 5 | 1 | 0,023 | 2,27 | 44 | 1 |
| **Total** | **44** | **1** | **100** | | |

Cómo se lee una fila: "21 personas (el 47,7 %) no tienen hermanos" o "33 personas (el 75 %) tienen 1 hermano o ninguno" (esta segunda frase sale de la acumulada).

::: {custom-style="Excel"}
**🖥️ En Excel: tabla de frecuencias de una variable discreta.** Suponemos los 44 datos en **B2:B45**.

1. En **D2:D7** escribe los valores distintos: 0, 1, 2, 3, 4, 5.
2. En **E2** (nᵢ): `=CONTAR.SI($B$2:$B$45;D2)` y arrastra hasta E7.
3. En **E8** (total): `=SUMA(E2:E7)` → debe dar 44.
4. En **F2** (fᵢ): `=E2/$E$8` y arrastra.
5. En **G2** (%): `=F2*100` y arrastra.
6. En **H2** (Nᵢ): `=E2`. En **H3**: `=H2+E3` y arrastra hasta H7.
7. En **I2** (Fᵢ): `=H2/$E$8` y arrastra.
:::

::: {custom-style="Truco"}
**💡 Truco.** El `$` en `$B$2:$B$45` y en `$E$8` es para que, al arrastrar, Excel no mueva el rango de datos ni el total. Si se te olvida, verás resultados raros o errores `#¡DIV/0!` en las filas de abajo.
:::

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


### Agrupar en intervalos (variables continuas)

Si la variable es continua (alturas, salarios), casi nunca se repite exactamente un valor. Entonces se agrupan los datos en **intervalos** y se cuenta cuántos caen en cada uno.

- **¿Cuántos intervalos?** Una regla habitual: el número entero más cercano a √n. Con 16 datos, √16 = 4 intervalos.
- **¿De qué amplitud?** Aproximadamente (máximo − mínimo) ÷ nº de intervalos, redondeando a un número cómodo.
- **Marca de clase** (xᵢ): el punto medio de cada intervalo. Representa a todo el intervalo en los cálculos.

**Ejemplo de clase: 16 alturas (cm)**

163, 167, 169, 172, 174, 176, 177, 178, 179, 181, 182, 184, 186, 189, 193, 198

√16 = 4 intervalos. Rango = 198 − 163 = 35. Amplitud cómoda: 10.

| Intervalo | Marca xᵢ | nᵢ | fᵢ | % | Nᵢ | Fᵢ |
|:---:|---:|---:|---:|---:|---:|---:|
| [160, 170] | 165 | 3 | 0,188 | 18,75 | 3 | 0,188 |
| (170, 180] | 175 | 6 | 0,375 | 37,50 | 9 | 0,563 |
| (180, 190] | 185 | 5 | 0,313 | 31,25 | 14 | 0,875 |
| (190, 200] | 195 | 2 | 0,125 | 12,50 | 16 | 1 |
| **Total** | | **16** | **1** | **100** | | |

::: {custom-style="Excel"}
**🖥️ En Excel: contar datos por intervalos con FRECUENCIA.** Datos en A2:A17. Escribe en **C2:C5** el **extremo superior** de cada intervalo: 170, 180, 190, 200.

1. Selecciona las celdas **D2:D5** (tantas como intervalos).
2. Escribe `=FRECUENCIA(A2:A17;C2:C5)`.
3. Pulsa **Intro** (en Excel 365). En versiones antiguas, pulsa **Ctrl + Mayús + Intro**.

FRECUENCIA cuenta cuántos datos son **menores o iguales** que cada extremo superior y mayores que el anterior, es decir, intervalos del tipo (a, b]. Es lo que hizo la profesora en la hoja *Longitudes* con 449 datos.

Alternativa sin FRECUENCIA: `=CONTAR.SI.CONJUNTO(A2:A17;">170";A2:A17;"<=180")` cuenta los datos de (170, 180].
:::

::: {custom-style="Mano"}
**✍️ A mano: agrupar en intervalos.**

1. Calcula el número de intervalos: √n redondeado. Con 16 datos, 4.
2. Calcula la amplitud: (máximo − mínimo) ÷ nº de intervalos, y redondea **hacia arriba** a un número cómodo: (198 − 163) ÷ 4 = 8,75 → 10.
3. Escribe los intervalos empezando en un número redondo por debajo del mínimo: [160, 170], (170, 180], (180, 190], (190, 200].
4. Cuenta con palotes cuántos datos caen en cada uno. **Cuidado con los extremos:** un dato que vale justo 170 va en [160, 170], no en (170, 180], porque el paréntesis dice que el 170 no entra.
5. Marca de clase de cada intervalo: (abajo + arriba) ÷ 2. Amplitud: arriba − abajo.
6. Termina la tabla igual que antes: fᵢ, %, Nᵢ y Fᵢ.
:::


## 1.4. Gráficos

### Para variables no agrupadas (cualitativas y discretas)

**Diagrama de barras.** En el eje horizontal, los valores o categorías. En el vertical, la frecuencia (absoluta, relativa o %). Las barras **no se tocan**. Es el gráfico más útil.

![Diagrama de barras del ejemplo de los hermanos](img/t1_barras_hermanos.png){width=80%}

**Diagrama de sectores (o circular, o "quesito").** Un círculo dividido en trozos proporcionales a la frecuencia. El ángulo de cada trozo es 360 × fᵢ. Solo es recomendable si hay pocas categorías.

Ejemplo: en el ejemplo de los grados, Ingeniería tiene fᵢ = 0,270, así que su sector mide 360 × 0,27 = 97,2 grados.

**Gráfico radial (o de araña, o de radar).** Una "estrella" con un radio por cada categoría. Sobre cada radio se marca un punto más o menos lejos del centro según su valor, y se unen los puntos. Sirve para comparar perfiles: por ejemplo, las competencias de un trabajador, o el gasto de dos provincias en varias partidas.

**Pictograma.** Dibujos (iconos) en lugar de barras. Cada icono vale una cantidad fija.

### Para variables agrupadas en intervalos

**Histograma.** Como un diagrama de barras, pero **las barras se tocan** (porque los intervalos van seguidos) y lo que importa es el **área** de cada rectángulo.

- Si todos los intervalos miden lo mismo, la altura de cada barra = la frecuencia.
- Si los intervalos miden distinto, la altura es la **densidad**: dᵢ = nᵢ ÷ aᵢ (frecuencia dividida entre amplitud).

**Polígono de frecuencias.** Una línea que une los puntos medios de la parte de arriba de cada barra del histograma.

![Histograma y polígono de frecuencias de las alturas](img/t1_histograma_alturas.png){width=80%}

::: {custom-style="Ojo"}
**⚠️ Ojo con la densidad.** Si un intervalo es el doble de ancho que los demás, es normal que tenga más datos solo por ser más ancho. Por eso se divide entre la amplitud: así comparamos "cuántos datos hay por cada unidad". En la hoja *Longitudes* de clase: [10,20] con 30 datos y amplitud 10 → d = 3; (20,40] con 18 datos y amplitud 20 → d = 0,9; (40,100] con 20 datos y amplitud 60 → d = 0,33.
:::

::: {custom-style="Excel"}
**🖥️ En Excel: los gráficos.**

- **Barras:** selecciona valores y frecuencias → Insertar → Gráfico de columnas → Columna agrupada.
- **Sectores:** selecciona categorías y frecuencias → Insertar → Gráfico circular.
- **Radial:** selecciona categorías y valores → Insertar → Otros gráficos → Radial.
- **Histograma (intervalos iguales):** selecciona la columna de **datos sin agrupar** → Insertar → Gráfico estadístico → Histograma. Para cambiar los intervalos: clic derecho sobre el eje horizontal → Dar formato al eje → "Ancho del rango".
- **Histograma desde una tabla ya agrupada:** haz un gráfico de columnas con las frecuencias (o densidades) y luego clic derecho en una barra → Dar formato a serie de datos → **Ancho del intervalo = 0 %**, para que las barras se toquen.
:::

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


## 1.5. Medidas de posición central: media, mediana y moda

### La media (x̄)

**Qué es.** El "promedio" de toda la vida: sumas todos los datos y divides entre cuántos hay. Se escribe x̄ ("x barra").

**Datos sueltos (sin tabla):**

$$\bar{x}=\frac{\sum x_i}{n}=\frac{x_1+x_2+\dots+x_n}{n}$$

**Datos en tabla de frecuencias:** cada valor se multiplica por las veces que aparece.

$$\bar{x}=\frac{\sum x_i\cdot n_i}{n}=\sum x_i\cdot f_i$$

**Receta con tabla:**

1. Añade una columna xᵢ · nᵢ (valor por frecuencia).
2. Suma esa columna.
3. Divide entre n.

**Ejemplo: hermanos.**

| xᵢ | nᵢ | xᵢ · nᵢ |
|---:|---:|---:|
| 0 | 21 | 0 |
| 1 | 12 | 12 |
| 2 | 6 | 12 |
| 3 | 2 | 6 |
| 4 | 2 | 8 |
| 5 | 1 | 5 |
| **Total** | **44** | **43** |

x̄ = 43 ÷ 44 = **0,977 hermanos**.

**Con intervalos** se hace igual, pero usando la **marca de clase** como xᵢ. El resultado es **aproximado**, porque suponemos que todos los datos del intervalo valen lo mismo que su punto medio. En las alturas: (165·3 + 175·6 + 185·5 + 195·2) ÷ 16 = 2860 ÷ 16 = **178,75 cm**. Con los 16 datos sueltos la media exacta es 179,25 cm. Se parecen, pero no son iguales.

::: {custom-style="Excel"}
**🖥️ En Excel: la media.**

- Datos sueltos en B2:B45: `=PROMEDIO(B2:B45)`.
- Desde la tabla (valores en D2:D7, frecuencias en E2:E7): `=SUMAPRODUCTO(D2:D7;E2:E7)/SUMA(E2:E7)`.

SUMAPRODUCTO hace en un paso la columna xᵢ·nᵢ y su suma. Si te da inseguridad, haz la columna auxiliar `=D2*E2`, arrástrala y luego divide su suma entre n. Da lo mismo.
:::

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


**La suma de las desviaciones a la media siempre es 0.** Es decir, Σ(xᵢ − x̄) = 0. Esto lo pide la profesora como ejercicio: "justifica e interpreta".

*Justificación:* Σ(xᵢ − x̄) = Σxᵢ − n·x̄. Como x̄ = Σxᵢ ÷ n, resulta n·x̄ = Σxᵢ. Por tanto Σxᵢ − Σxᵢ = 0.

*Interpretación:* la media es el "punto de equilibrio" de los datos. Lo que unos datos están por encima de la media se compensa exactamente con lo que otros están por debajo. Puedes verlo en la hoja de clase *Hermanos*: la columna xᵢ − x̄ suma prácticamente 0 (sale −4,2·10⁻¹⁵, que es un 0 con error de redondeo del ordenador).

::: {custom-style="Otra"}
Imagina que juntas todo el dinero de un grupo en una caja y lo repartes a partes iguales. Lo que le toca a cada persona es la **media**.

Con los hermanos: 21 personas tienen 0, 12 tienen 1, 6 tienen 2… Si juntas todos los hermanos (0·21 + 1·12 + 2·6 + 3·2 + 4·2 + 5·1 = 43) y los repartes entre las 44 personas, toca a 0,98 por persona. Por eso se multiplica cada valor por su frecuencia: hay que contar **todos** los hermanos, no solo los valores distintos.
:::

### La media ponderada

**Cuándo.** Cuando tienes las medias de varios grupos de distinto tamaño y quieres la media de todos juntos.

$$\bar{x}=\frac{\bar{x}_1T_1+\bar{x}_2T_2+\dots}{T_1+T_2+\dots}$$

Cada media se multiplica por el tamaño de su grupo (T), se suma y se divide entre el total de personas.

**Ejemplo de clase (hoja *Salarios_cambios_origen_escala*):**

| Categoría | Salario medio | Nº personas (T) |
|:---|---:|---:|
| Administrativos | 1900 | 450 |
| Técnicos | 2300 | 328 |
| Jefes de sección | 2580 | 45 |
| Altos cargos | 4000 | 3 |

Media bien hecha: (1900·450 + 2300·328 + 2580·45 + 4000·3) ÷ 826 = 1 737 500 ÷ 826 = **2103,51 €**.

::: {custom-style="Ojo"}
**⚠️ Ojo: la "MEDIA MAL" de clase.** Si haces la media de las cuatro medias sin ponderar, (1900 + 2300 + 2580 + 4000) ÷ 4 = 2695 €, que es falso: los 3 altos cargos pesarían igual que los 450 administrativos. La profesora lo dejó escrito como "MEDIA MAL" en el Excel. Es un error de examen típico.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Medias en B2:B5 y tamaños en C2:C5: `=SUMAPRODUCTO(B2:B5;C2:C5)/SUMA(C2:C5)`.
:::

### La media truncada (o recortada)

**Qué es.** Se quitan los datos más extremos (un porcentaje por arriba y el mismo por abajo) y se hace la media del resto. Sirve cuando hay valores muy raros que "tiran" de la media.

**Ejemplo de clase:** salarios (miles €) 20, 22, 23, 24, 25, 26, 27, 28, 35, 50. Media normal = 280 ÷ 10 = 28. Media truncada al 10 %: con 10 datos, el 10 % es 1 dato por cada lado. Quitamos el 20 y el 50: (22+23+24+25+26+27+28+35) ÷ 8 = 210 ÷ 8 = **26,25**. Refleja mejor el salario "típico".

::: {custom-style="Excel"}
**🖥️ En Excel:** `=MEDIA.ACOTADA(A1:A10;0,2)`. **Atención:** el 0,2 es el **total** que se quita (10 % por abajo + 10 % por arriba = 20 %).
:::

### Cambios de origen y de escala (transformaciones lineales)

Si a todos los datos les **sumas** una cantidad b (cambio de origen) y/o los **multiplicas** por a (cambio de escala), la nueva variable es Y = a·X + b, y su media es:

$$\bar{y}=a\cdot\bar{x}+b$$

Es decir: **a la media le pasa lo mismo que a los datos**.

Ejemplo de clase (salarios 1500, 3900, 980, 2000, 3650; media 2406 €):

- Subida de 200 € a todos: nueva media = 2406 + 200 = **2606 €**.
- Subida del 3 % a todos: nueva media = 1,03 × 2406 = **2478,18 €**.
- Ambas: en el Excel de clase se hizo Y = 1,03·X + 200, y la media = 1,03 × 2406 + 200 = **2678,18 €**.

### La moda (Mo)

**Qué es.** El valor que **más se repite** (el de mayor frecuencia). Puede haber dos modas (distribución **bimodal**) o más.

- Datos no agrupados: miras la columna nᵢ y eliges el valor con la nᵢ más alta. Hermanos: la mayor nᵢ es 21, que corresponde al 0 → **Mo = 0** (lo más frecuente es no tener hermanos).
- Variable cualitativa: la categoría más frecuente (en el ejemplo de los grados, Ingeniería).

**Datos agrupados en intervalos:**

1. Calcula la densidad de cada intervalo: dᵢ = nᵢ ÷ aᵢ. (Si todos los intervalos miden lo mismo, puedes usar directamente las nᵢ.)
2. El **intervalo modal** es el de mayor densidad.
3. Aplica la fórmula:

$$Mo=L_{i-1}+\frac{d_i-d_{i-1}}{(d_i-d_{i-1})+(d_i-d_{i+1})}\cdot a_i$$

Donde Lᵢ₋₁ es el **extremo inferior** del intervalo modal, dᵢ su densidad, dᵢ₋₁ la densidad del intervalo **anterior**, dᵢ₊₁ la del **siguiente**, y aᵢ la amplitud del intervalo modal.

**Ejemplo: alturas.** Todos miden 10, así que usamos las nᵢ. Intervalo modal: (170, 180], con nᵢ = 6. Anterior: 3. Siguiente: 5.

$$Mo=170+\frac{6-3}{(6-3)+(6-5)}\cdot 10=170+\frac{3}{4}\cdot 10=177{,}5\ \mathrm{cm}$$

::: {custom-style="Ojo"}
**⚠️ Ojo.** Si el intervalo modal es el **primero**, no hay anterior: se pone dᵢ₋₁ = 0. Si es el **último**, no hay siguiente: dᵢ₊₁ = 0.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Datos sueltos: `=MODA.UNO(B2:B45)`. Con intervalos, Excel no tiene función: se escribe la fórmula con referencias a las celdas, como en la hoja de clase *EJEMPLO3_MODA_MEDIANA_TABLAS*. Si Linf está en A3, aᵢ en E3, y las densidades del anterior, modal y siguiente en D2, D3 y D4: `=A3+(D3-D2)/((D3-D2)+(D3-D4))*E3` → 177,5.
:::

### La mediana (Me)

**Qué es.** El valor que queda **justo en el medio** cuando ordenas los datos de menor a mayor. Deja la mitad (50 %) de los datos por debajo y la otra mitad por encima.

**Receta para datos no agrupados (con tabla):**

1. Calcula n/2.
2. Mira la columna de acumuladas Nᵢ y busca la **primera** que sea **mayor o igual** que n/2.
3. Si esa Nᵢ es **mayor** que n/2 → la mediana es el valor xᵢ de esa fila.
4. Si esa Nᵢ es **exactamente igual** a n/2 → la mediana es la media entre ese valor y el siguiente: (xᵢ + xᵢ₊₁)/2.

**Ejemplo: hermanos.** n/2 = 44/2 = 22. Acumuladas: 21, 33, 39... La primera ≥ 22 es 33 (fila del 1). 33 > 22 → **Me = 1**. Interpretación: la mitad de las personas tiene 1 hermano o ninguno, y la otra mitad tiene 1 o más.

**Receta para datos agrupados:**

1. Calcula n/2 y busca el **intervalo mediano** (la primera Nᵢ ≥ n/2).
2. Aplica:

$$Me=L_{i-1}+\frac{\frac{n}{2}-N_{i-1}}{n_i}\cdot a_i$$

Lᵢ₋₁ = extremo inferior del intervalo mediano. Nᵢ₋₁ = acumulada del intervalo **anterior**. nᵢ = frecuencia del intervalo mediano. aᵢ = su amplitud.

**Ejemplo: alturas.** n/2 = 8. Acumuladas: 3, 9, 14, 16. La primera ≥ 8 es 9 → intervalo (170, 180]. Anterior acumulada = 3.

$$Me=170+\frac{8-3}{6}\cdot 10=170+8{,}33=178{,}33\ \mathrm{cm}$$

::: {custom-style="Truco"}
**💡 Para entender la fórmula.** Necesitamos llegar al dato número 8. Hasta 170 ya llevamos 3 datos. Nos faltan 8 − 3 = 5 de los 6 que hay en el intervalo. Así que avanzamos 5/6 del intervalo: 5/6 × 10 = 8,33 cm desde 170.
:::

::: {custom-style="Excel"}
**🖥️ En Excel.** Datos sueltos: `=MEDIANA(B2:B45)`. Con intervalos, se escribe la fórmula con celdas (hoja de clase *EJEMPLO3*): si n está en C7, Linf en A3, la acumulada anterior en E2, nᵢ en C3 y aᵢ en D3: `=A3+(C7/2-E2)/C3*D3` → 178,33.
:::

::: {custom-style="Mano"}
**✍️ A mano: la mediana con datos sueltos (sin tabla).** Es la misma receta de los apuntes: n/2 y buscar en qué dato caes.

1. **Ordena** los datos de menor a mayor y numéralos: 1.º, 2.º, 3.º…
2. Calcula n/2.
3. Si n/2 **no es un número entero**, redondéalo hacia arriba: la mediana es el dato que ocupa ese puesto. Con 15 datos, n/2 = 7,5 → el dato 8.º.
4. Si n/2 **es entero**, la mediana es la media del dato que ocupa ese puesto y el siguiente. Con 16 datos, n/2 = 8 → media del 8.º y del 9.º.

**Alturas** (ya ordenadas): 163, 167, 169, 172, 174, 176, 177, **178**, **179**, 181, 182, 184, 186, 189, 193, 198. n/2 = 8 → Me = (178 + 179) ÷ 2 = **178,5 cm**.

Con la tabla de intervalos salía 178,33: es una aproximación, porque ahí no conocemos los datos exactos.
:::


::: {custom-style="Otra"}
Pon a las 44 personas **en fila**, de menos a más hermanos. La mediana es lo que tiene la persona **del medio**. Como son 44, el medio está entre la persona 22 y la 23.

La columna de acumuladas te dice hasta qué puesto de la fila llega cada valor: los de 0 hermanos ocupan los puestos 1 a 21; los de 1 hermano, del 22 al 33. Las personas 22 y 23 tienen 1 hermano: mediana = 1.

Con intervalos no sabes el valor exacto de cada persona, así que se supone que dentro del intervalo están repartidas a la misma distancia, como los postes de una valla. La fórmula solo calcula cuánto hay que avanzar dentro del intervalo hasta llegar a la persona del medio.
:::

### Media, mediana o moda: ¿cuál uso?

- La **media** usa todos los datos, pero es muy **sensible a valores extremos**. Un salario de un millón dispara la media.
- La **mediana** no se deja arrastrar por los extremos (es **robusta**). Para salarios o precios de vivienda suele representar mejor "lo normal".
- La **moda** es la única que sirve para variables nominales.

## 1.6. Cuantiles: cuartiles, deciles y percentiles

### Qué son

Son "puntos de corte" que dividen los datos ordenados en partes iguales. La mediana es un caso particular (corta en dos mitades).

- **Cuartiles** (C₁, C₂, C₃): dividen en 4 partes. C₁ deja el 25 % por debajo, C₂ = mediana (50 %), C₃ deja el 75 % por debajo.
- **Deciles** (D₁ ... D₉): dividen en 10 partes. D₇ deja el 70 % por debajo.
- **Percentiles** (P₁ ... P₉₉): dividen en 100 partes. P₉₈ deja el 98 % por debajo.

Relaciones útiles: C₁ = P₂₅, C₂ = D₅ = P₅₀ = mediana, C₃ = P₇₅, D₇ = P₇₀.

### Cómo se calculan

Exactamente igual que la mediana, pero cambiando n/2 por la proporción que toque:

| Medida | Busco la primera Nᵢ ≥ ... |
|:---|:---|
| C₁ | n/4 (= 0,25·n) |
| C₃ | 3n/4 (= 0,75·n) |
| Dᵣ | r·n/10 |
| Pᵣ | r·n/100 |

Para datos agrupados, la fórmula es la de la mediana cambiando n/2 por ese valor:

$$P_r=L_{i-1}+\frac{\frac{r\cdot n}{100}-N_{i-1}}{n_i}\cdot a_i$$

**Ejemplo: hermanos.** n/4 = 11. Primera acumulada ≥ 11: 21 (valor 0) y 21 > 11 → **C₁ = 0**. 3n/4 = 33. Primera acumulada ≥ 33: 33 (valor 1), y es **exactamente igual** → C₃ = (1 + 2)/2 = **1,5**.

**Ejemplo: P₇₀ de las alturas.** 70 × 16 / 100 = 11,2. Primera acumulada ≥ 11,2: 14 → intervalo (180, 190]. Anterior: 9.

$$P_{70}=180+\frac{11{,}2-9}{5}\cdot 10=184{,}4\ \mathrm{cm}$$

::: {custom-style="Otra"}
Es la misma **fila de personas** de la mediana. En vez de buscar a la del medio, buscas a la que está a un cuarto de la fila (C₁), a tres cuartos (C₃) o en el puesto que quieras (percentil).

Con 200 personas, el percentil 90 es lo que tiene la persona del puesto 180: el 90 % de la fila está por detrás de ella.
:::

### Cómo se interpretan

- "La renta de un trabajador está en el **percentil 98**" significa que el 98 % de los trabajadores gana **menos o igual** que él, y solo el 2 % gana más.
- "C₃ = 1,5 hermanos": el 75 % de las personas tiene 1,5 hermanos o menos (en la práctica, 1 o menos).
- "D₇ = 184,4 cm" (es lo mismo que P₇₀): el 70 % de las personas mide 184,4 cm o menos.

**¿Hay que ordenar los datos?** Sí, siempre. Los cuantiles hablan de "cuántos quedan por debajo", y eso solo tiene sentido con los datos ordenados. La tabla de frecuencias ya los ordena.

::: {custom-style="Excel"}
**🖥️ En Excel.** `=CUARTIL.INC(B2:B45;1)` para C₁ (3 para C₃). `=PERCENTIL.INC(B2:B45;0,97)` para P₉₇ (el porcentaje va en tanto por uno: 0,97). En el Excel de clase: C₁ = 0 y P₉₇ = 4.
:::

::: {custom-style="Ojo"}
**⚠️ Ojo: Excel y la receta "a mano" pueden dar cuartiles algo distintos.** Excel usa otro método (interpola entre datos). En los hermanos, la receta de los apuntes da C₃ = 1,5, pero `=CUARTIL.INC` da 1,25. Por eso en el Excel de clase el rango intercuartílico sale 1,25 y en los apuntes 1,5. Los dos son correctos según el método. En papel, usa la receta. En un examen con Excel, la función, salvo que te pidan expresamente hacerlo con la tabla. Si dudas, pon los dos y di cuál es cuál.
:::

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


### Ejercicio de los apuntes: cuartiles y P₃₀, P₇₀

| Intervalo | nᵢ | Nᵢ | aᵢ |
|:---:|---:|---:|---:|
| [10, 13] | 15 | 15 | 3 |
| (13, 18] | 29 | 44 | 5 |
| (18, 25] | 56 | 100 | 7 |

n = 100.

- **C₁:** n/4 = 25 → primera Nᵢ ≥ 25 es 44 → (13, 18]. C₁ = 13 + (25 − 15)/29 · 5 = 13 + 1,724 = **14,72**.
- **C₂ (mediana):** 50 → primera Nᵢ ≥ 50 es 100 → (18, 25]. C₂ = 18 + (50 − 44)/56 · 7 = 18 + 0,75 = **18,75**.
- **C₃:** 75 → (18, 25]. C₃ = 18 + (75 − 44)/56 · 7 = 18 + 3,875 = **21,875**.
- **P₃₀:** 30 → (13, 18]. P₃₀ = 13 + (30 − 15)/29 · 5 = 13 + 2,586 = **15,59**.
- **P₇₀:** 70 → (18, 25]. P₇₀ = 18 + (70 − 44)/56 · 7 = 18 + 3,25 = **21,25**.

## 1.7. Medidas de dispersión

::: {custom-style="Idea"}
**🧠 La idea.** Dos clases pueden tener la misma nota media (un 5) y ser muy distintas: en una todos sacan un 5, en la otra la mitad saca un 0 y la otra mitad un 10. Las medidas de dispersión dicen **cuánto se separan los datos** del centro.
:::

### Rango (o recorrido)

Rango = máximo − mínimo. Hermanos: 5 − 0 = **5**. Alturas: 198 − 163 = **35**.

Es muy sencillo pero se deja engañar por un solo dato extremo.

Excel: `=MAX(B2:B45)-MIN(B2:B45)`.

### Rango intercuartílico (IQR)

IQR = C₃ − C₁. Es la anchura del **50 % central** de los datos. No le afectan los extremos.

Hermanos (receta de clase): 1,5 − 0 = **1,5**. Alturas (cuartiles exactos con todos los datos): 184,5 − 173,5 = **11 cm**. Con la tabla agrupada saldría C₁ = 171,67 y C₃ = 186, así que IQR = 14,33 (aproximado).

Excel: `=CUARTIL.INC(B2:B45;3)-CUARTIL.INC(B2:B45;1)`.

### Varianza (S²)

**Qué es.** La media de las distancias **al cuadrado** de cada dato a la media. Cuanto más grande, más dispersos están los datos.

¿Por qué al cuadrado? Porque si sumamos las distancias tal cual, se anulan (ya vimos que suman 0). Al elevar al cuadrado, todas son positivas.

Fórmula de definición:

$$S^2=\frac{\sum (x_i-\bar{x})^2\cdot n_i}{n}$$

Fórmula práctica (la más cómoda a mano):

$$S^2=\frac{\sum x_i^2\cdot n_i}{n}-\bar{x}^2$$

**Receta con la fórmula práctica:**

1. Calcula la media x̄.
2. Añade una columna xᵢ² · nᵢ (el valor al cuadrado, por su frecuencia).
3. Suma esa columna y divide entre n.
4. Réstale la media al cuadrado.

**Ejemplo: hermanos** (x̄ = 0,977).

| xᵢ | nᵢ | xᵢ² | xᵢ²·nᵢ |
|---:|---:|---:|---:|
| 0 | 21 | 0 | 0 |
| 1 | 12 | 1 | 12 |
| 2 | 6 | 4 | 24 |
| 3 | 2 | 9 | 18 |
| 4 | 2 | 16 | 32 |
| 5 | 1 | 25 | 25 |
| **Total** | **44** | | **111** |

S² = 111/44 − 0,977² = 2,5227 − 0,9551 = **1,568**.

Las unidades de la varianza son "al cuadrado" (hermanos², euros²...), por eso cuesta interpretarla directamente. Para eso está la desviación típica.

::: {custom-style="Ojo"}
**⚠️ Ojo.** Fallo clásico: hacer (Σxᵢ·nᵢ)² en vez de Σxᵢ²·nᵢ. Primero se eleva **cada valor** al cuadrado, luego se multiplica por su nᵢ, luego se suma. Y no olvides restar x̄² al final.
:::

::: {custom-style="Otra"}
Piensa en dos clases que sacan de media un 5. En una, todos sacan entre 4 y 6. En la otra, la mitad saca un 0 y la otra mitad un 10.

La **varianza** mide esa diferencia: mira lo lejos que está cada alumno del 5, lo eleva al cuadrado (para que los de abajo no resten a los de arriba) y hace la media. Primera clase: distancias de 1 → varianza 1. Segunda clase: distancias de 5 → varianza 25.

Como la varianza queda en "unidades al cuadrado", se hace la raíz y sale la **desviación típica**: 1 punto frente a 5 puntos, que ya se entiende de un vistazo.
:::

### Cuasivarianza (s²)

Es casi lo mismo, pero dividiendo entre **n − 1** en lugar de n. Se usa cuando los datos son una muestra y queremos estimar la varianza de la población.

$$s^2=\frac{\sum (x_i-\bar{x})^2\cdot n_i}{n-1}=\frac{n}{n-1}\cdot S^2$$

Hermanos: s² = 44/43 × 1,568 = **1,604**.

Con muchos datos, varianza y cuasivarianza casi coinciden (44/43 ≈ 1,02). Con pocos datos se nota la diferencia (por ejemplo, 5/4 = 1,25).

### Desviación típica (S) y cuasidesviación típica (s)

Son las **raíces cuadradas** de la varianza y la cuasivarianza. Tienen las **mismas unidades** que los datos, así que se interpretan mejor.

Hermanos: S = √1,568 = **1,252 hermanos**. s = √1,604 = **1,266**.

Interpretación: "Los datos se separan de la media, en promedio, aproximadamente 1,25 hermanos".

::: {custom-style="Excel"}
**🖥️ En Excel: las cuatro medidas.**

| Medida | Función | Hermanos |
|:---|:---|---:|
| Varianza S² | `=VAR.P(B2:B45)` | 1,5677 |
| Cuasivarianza s² | `=VAR.S(B2:B45)` | 1,6041 |
| Desviación típica S | `=DESVEST.P(B2:B45)` | 1,2521 |
| Cuasidesviación s | `=DESVEST.S(B2:B45)` | 1,2665 |

**.P = Población** (divide entre n). **.S = muestra, "Sample"** (divide entre n − 1).

Si solo tienes la tabla de frecuencias (valores en D2:D7, nᵢ en E2:E7) y la media en una celda, por ejemplo J2: `=SUMAPRODUCTO(D2:D7^2;E2:E7)/SUMA(E2:E7)-J2^2`.
:::

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


::: {custom-style="Ojo"}
**⚠️ Ojo con las salidas del programa R de los apuntes.** Cuando los apuntes muestran "sd", es la **cuasidesviación típica** (divide entre n − 1). Por ejemplo, en los hermanos sale sd = 1,26654, que es s, no S.
:::

### Coeficiente de variación (CV)

**Qué es.** La desviación típica dividida entre la media. Es una dispersión **relativa** (no tiene unidades), así que permite **comparar** grupos con medias o unidades muy diferentes.

$$CV=\frac{S}{\bar{x}}$$

Se suele dar en %. Cuanto **mayor** el CV, **más dispersión relativa** (menos homogéneo, la media es menos representativa).

**Ejemplo de clase (hoja *Hoja1*).** Sector energético: facturan 500, 550 y 600 millones. Sector creativo: 1, 4 y 8 millones.

- Energético: media 550, S² = 1666,67, S = 40,82 → CV = 40,82/550 = **0,074** (7,4 %).
- Creativo: media 4,33, S² = 8,22, S = 2,867 → CV = 2,867/4,33 = **0,662** (66,2 %).

La varianza es mucho mayor en el sector energético, pero eso es porque sus cifras son enormes. En términos **relativos**, el sector creativo es mucho más disperso: una empresa factura 8 veces más que otra.

Excel: `=DESVEST.P(rango)/PROMEDIO(rango)`. Hermanos: 1,2521/0,9773 = 1,28.

::: {custom-style="Otra"}
Que tu sueldo varíe 40 € de un mes a otro es poquísimo si ganas 3000 €, y muchísimo si ganas 200 €.

El **CV** compara la dispersión con el tamaño de la media: 40 ÷ 3000 = 1,3 %, frente a 40 ÷ 200 = 20 %. Por eso, para comparar grupos con medias distintas, se usa el CV y no la desviación típica.
:::

### Cómo afectan los cambios de origen y escala a la dispersión

Si Y = a·X + b:

- **Sumar** una cantidad (b) **no cambia** la dispersión: todos se mueven igual, siguen igual de separados.
- **Multiplicar** por a: la desviación típica se multiplica por a, y la varianza por **a²**.

$$S_Y^2=a^2\cdot S_X^2 \qquad S_Y=a\cdot S_X$$

El CV no cambia si solo multiplicas (los dos, S y media, se multiplican por a). Sí cambia si sumas (la media cambia y S no).

### Varianza en subpoblaciones (varianza dentro y entre grupos)

**Cuándo.** Te dan varios grupos (hombres/mujeres, departamentos, provincias) con su tamaño, su media y su varianza, y te piden la varianza de todos juntos.

La idea: la dispersión total tiene dos partes.

- **Varianza dentro de los grupos** (intrapoblacional): lo dispersos que están los datos **dentro** de cada grupo. Es la media ponderada de las varianzas.
- **Varianza entre los grupos** (interpoblacional): lo distintas que son las **medias** de los grupos entre sí.

$$\mathrm{Var.\ dentro}=\frac{S_1^2T_1+S_2^2T_2+\dots}{T_1+T_2+\dots}$$

$$\mathrm{Var.\ entre}=\frac{(\bar{x}_1-\bar{x})^2T_1+(\bar{x}_2-\bar{x})^2T_2+\dots}{T_1+T_2+\dots}$$

$$\mathrm{Varianza\ total}=\mathrm{Var.\ dentro}+\mathrm{Var.\ entre}$$

Y además: **% debido a las diferencias entre grupos** = Var. entre ÷ Varianza total × 100.

**Receta:**

1. Calcula la media global x̄ (media ponderada de las medias).
2. Varianza dentro: multiplica cada varianza por su tamaño, suma, divide entre el total.
3. Varianza entre: para cada grupo, (su media − media global)², por su tamaño; suma; divide entre el total.
4. Suma las dos.

**Ejemplo de los apuntes:**

| Submuestra | A | B | C |
|:---|---:|---:|---:|
| Tamaño | 150 | 200 | 150 |
| Media | 10 | 10 | 12 |
| Varianza | 10 | 25 | 16 |

1. Media global = (10·150 + 10·200 + 12·150)/500 = 5300/500 = **10,6**.
2. Dentro = (10·150 + 25·200 + 16·150)/500 = 8900/500 = **17,8**.
3. Entre = ((10 − 10,6)²·150 + (10 − 10,6)²·200 + (12 − 10,6)²·150)/500 = (54 + 72 + 294)/500 = **0,84**.
4. Total = 17,8 + 0,84 = **18,64**. % entre = 0,84/18,64 × 100 = **4,51 %**.

Interpretación: casi toda la variabilidad está **dentro** de los grupos. Las tres submuestras tienen medias parecidas; las diferencias entre grupos explican solo el 4,5 % de la variabilidad.

::: {custom-style="Ojo"}
**⚠️ Ojo.** Si te dan **desviaciones típicas** en vez de varianzas, primero elévalas al cuadrado. Y si te piden la desviación típica total, haz la raíz de la varianza total al final.
:::

::: {custom-style="Otra"}
Piensa en los salarios de una empresa con dos departamentos. Los salarios varían por dos motivos:

- Dentro de cada departamento no todos cobran lo mismo: es la **varianza dentro**.
- Además, un departamento cobra de media más que el otro: es la **varianza entre**.

La varianza total es la suma de las dos. Si casi toda la variación es "entre", el departamento explica buena parte de las diferencias de sueldo. Si casi toda es "dentro", el departamento importa poco.
:::

## 1.8. Medidas de forma: asimetría y curtosis

### Asimetría

**Qué mira.** Si la distribución es simétrica (igual a los dos lados) o tiene una "cola" larga hacia un lado.

![Tipos de asimetría](img/t1_asimetria.png){width=95%}

- **Asimetría positiva (a la derecha):** hay algunos valores muy **altos** que forman una cola a la derecha. Típico de salarios: la mayoría gana poco y unos pocos ganan muchísimo. La media queda por encima de la mediana.
- **Asimetría negativa (a la izquierda):** cola hacia valores **bajos**.
- **Simétrica:** media, mediana y moda prácticamente coinciden.

Se mide con el **coeficiente de asimetría de Fisher (CA)**:

$$CA=\frac{\frac{1}{n}\sum (x_i-\bar{x})^3n_i}{S^3}$$

| CA | Significa |
|:---:|:---|
| = 0 (o muy cerca) | Simétrica |
| > 0 | Asimétrica positiva (cola a la derecha) |
| < 0 | Asimétrica negativa (cola a la izquierda) |

También existe el coeficiente de Pearson, Aₚ = (x̄ − Mo)/S, solo para distribuciones con una sola moda.

### Curtosis (apuntamiento)

**Qué mira.** Si la distribución es muy **picuda** (muchos datos amontonados cerca de la media) o **aplanada**, comparada con la "campana" de la distribución normal.

![Tipos de curtosis](img/t1_curtosis.png){width=95%}

$$CC=\frac{\frac{1}{n}\sum (x_i-\bar{x})^4n_i}{S^4}-3$$

| CC | Nombre | Significa |
|:---:|:---|:---|
| = 0 | Mesocúrtica | Apuntamiento como la normal |
| > 0 | Leptocúrtica | Más picuda que la normal |
| < 0 | Platicúrtica | Más aplanada que la normal |

::: {custom-style="Truco"}
**💡 Truco para recordarlo.** **Lepto** suena a "salto" (picuda, alta). **Plati** suena a "plato" (plana). **Meso** = en medio.
:::

Asimetría y curtosis **no cambian** con transformaciones lineales (sumar o multiplicar todos los datos por un número positivo).

**Asimetría vs curtosis (pregunta de teoría típica):** la asimetría mira si la distribución está **equilibrada a izquierda y derecha** (hacia qué lado tiene cola). La curtosis mira **cómo de puntiaguda o plana** es, cuánto se concentran los datos en el centro.

::: {custom-style="Excel"}
**🖥️ En Excel.** `=COEFICIENTE.ASIMETRIA.P(rango)` calcula el CA de los apuntes. `=CURTOSIS(rango)` da la curtosis ya restando 3, aunque con una pequeña corrección para muestras, así que puede salir algo distinta de la fórmula de los apuntes. El signo, que es lo que se interpreta, coincide casi siempre.
:::

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


**Ejercicio de los apuntes:** skewness = 0,2534 y kurtosis = −0,1912 (alturas). Interpretación: la asimetría es positiva pero muy pequeña, así que la distribución es **casi simétrica**, con una ligera cola a la derecha. La curtosis es negativa y pequeña: **ligeramente platicúrtica**, un poco más plana que la normal.

## 1.9. Tipificar (estandarizar) una variable

**Qué es.** Transformar cada dato en "cuántas desviaciones típicas está por encima o por debajo de la media". El resultado se llama puntuación z.

$$z_i=\frac{x_i-\bar{x}}{S}$$

La variable tipificada siempre tiene media 0 y varianza 1. z positivo = por encima de la media; z negativo = por debajo.

**Para qué sirve.** Para **comparar datos de grupos distintos**.

**Ejemplo de clase.** Un alumno saca un 6 en un examen (media de la clase 7, S = 2) y un 5 en otro (media 4,5, S = 1).

- Examen 1: z = (6 − 7)/2 = **−0,5** (medio punto típico por debajo de su clase).
- Examen 2: z = (5 − 4,5)/1 = **+0,5** (medio punto típico por encima).

Aunque el 6 parece mejor nota, **relativamente** le fue mejor en el segundo examen.

Excel: `=NORMALIZACION(x;media;desv_típica)`, o directamente `=(A2-$B$10)/$B$11` con la media en B10 y la desviación típica en B11.

## 1.10. Valores atípicos y diagrama de caja (boxplot)

**Valor atípico (outlier):** un dato muy alejado del resto.

**Diagrama de caja:** un dibujo que resume la distribución con 5 números y marca los atípicos.

![Anatomía del diagrama de caja con las alturas](img/t1_caja_anatomia.png){width=95%}

**Cómo se construye:**

1. La **caja** va de C₁ a C₃. Dentro, una línea gruesa marca la **mediana**.
2. Se calculan los **límites** para detectar atípicos:

$$L_I=C_1-1{,}5\cdot(C_3-C_1) \qquad L_S=C_3+1{,}5\cdot(C_3-C_1)$$

3. Un dato es **atípico** si es menor que Lᵢ o mayor que Lₛ. Se dibuja como un puntito suelto.
4. Los **bigotes** (las líneas) llegan hasta el dato más extremo que **no** es atípico (si no hay atípicos, hasta el mínimo y el máximo).

**Ejemplo: hermanos.** C₁ = 0, C₃ = 1,5, IQR = 1,5. Lᵢ = 0 − 1,5·1,5 = −2,25. Lₛ = 1,5 + 2,25 = 3,75. Nadie tiene menos de −2,25 hermanos, así que no hay atípicos por abajo. Los valores 4 y 5 son mayores que 3,75: hay **3 atípicos** (dos personas con 4 hermanos y una con 5). El bigote de arriba llega hasta 3.

**Ejemplo: alturas.** C₁ = 173,5, C₃ = 184,5, IQR = 11. Lᵢ = 173,5 − 16,5 = 157. Lₛ = 184,5 + 16,5 = 201. Todos los datos están entre 163 y 198: **no hay atípicos**.

**Cómo leer un diagrama de caja:**

- **Dónde está la caja** → nivel general de los datos (más arriba = valores más altos).
- **Línea de la mediana** → el valor central. Si no está en el centro de la caja, hay asimetría: si está más cerca del borde de abajo, la parte alta está más estirada (asimetría positiva).
- **Tamaño de la caja y bigotes** → dispersión. Caja alargada = mucha dispersión.
- **Puntos sueltos** → atípicos.

::: {custom-style="Excel"}
**🖥️ En Excel.** Selecciona los datos → Insertar → Gráfico estadístico → **Cuadro y bigotes**. Para varios grupos a la vez, pon los grupos en columnas contiguas y selecciónalas todas. Excel dibuja la media con una "x" además de la mediana con una línea.
:::

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


::: {custom-style="Otra"}
La **caja** es donde está la gente "normal": el 50 % del medio. La raya de dentro es la persona del medio (la mediana). Los **bigotes** llegan hasta los que todavía se consideran normales, y los **puntos sueltos** son los raros (atípicos).

Al comparar varias cajas: más arriba significa valores más altos; más larga significa más diferencias entre unos y otros.
:::

### Ejercicio de los apuntes: salarios mensuales en tres sectores

El gráfico muestra tres cajas: Agricultura, un sector central (sin nombre visible, probablemente Industria) y Servicios.

- **Nivel.** El sector central tiene la mediana más alta (unos 1800 €), después Servicios (unos 1600 €) y por último Agricultura (unos 1300 €). En agricultura se cobra claramente menos.
- **Dispersión.** El sector central tiene la caja y los bigotes más largos (de unos 1300 a 2450 €): es el más disperso. Agricultura y Servicios tienen cajas más estrechas.
- **Atípicos.** En el sector central hay un salario atípico bajo (unos 1100 €), muy por debajo del resto de su sector.
- **Forma.** En Servicios y en el sector central el bigote superior es más largo que el inferior: hay salarios altos que estiran la distribución hacia arriba (ligera asimetría positiva).

## 1.11. Interpretar las salidas de un programa

Los apuntes muestran resúmenes del programa R. Cada palabra significa:

| Palabra | Significado |
|:---|:---|
| mean | Media |
| sd | Cuasidesviación típica |
| IQR | Rango intercuartílico |
| 0 % | Mínimo |
| 25 % | Primer cuartil |
| 50 % | Mediana |
| 75 % | Tercer cuartil |
| 100 % | Máximo |
| skewness | Coeficiente de asimetría |
| kurtosis | Coeficiente de curtosis |
| n | Tamaño de la muestra |

**Plantilla para escribir un análisis descriptivo** (sirve para cualquier ejercicio de "interpreta"):

1. **Qué variable es y cuántos datos** (n).
2. **Centro:** la media es..., la mediana es... Si se parecen, la distribución es bastante simétrica. Si la media es mayor que la mediana, hay valores altos que tiran de ella.
3. **Dispersión:** la desviación típica es... (los datos se separan de la media unos ... de promedio). El 50 % central está entre C₁ y C₃.
4. **Rango:** los datos van de ... (mínimo) a ... (máximo).
5. **Forma:** asimetría (signo) y curtosis (signo).
6. **Atípicos**, si hay.

### Ejercicio: interpreta las alturas

mean = 179,25 · sd = 9,42 · skewness = 0,25 · kurtosis = −0,19 · 0 % = 163 · 25 % = 173,5 · 50 % = 178,5 · 75 % = 184,5 · 80 % = 186 · 100 % = 198 · n = 16.

*Respuesta modelo:* Se han medido 16 personas. La altura media es 179,25 cm y la mediana 178,5 cm; al ser parecidas, la distribución es bastante simétrica. Las alturas se separan de la media unos 9,4 cm de promedio. El 50 % central mide entre 173,5 y 184,5 cm. La persona más baja mide 163 cm y la más alta 198 cm. El 80 % mide 186 cm o menos. La asimetría (0,25) es positiva pero pequeña: casi simétrica con una ligera cola hacia las alturas grandes. La curtosis (−0,19) indica una forma algo más plana que la normal. No hay valores atípicos (los límites son 157 y 201).

### Ejercicio: análisis descriptivo de los hermanos

mean = 0,977 · sd = 1,267 · skewness = 1,48 · kurtosis = 1,85 · 0 % = 0 · 25 % = 0 · 50 % = 1 · 60 % = 1 · 75 % = 1,25 · 100 % = 5 · n = 44.

*Respuesta modelo:* Se ha preguntado a 44 personas por su número de hermanos. De media tienen casi 1 hermano (0,98) y la mediana es 1: la mitad tiene como mucho 1 hermano. Al menos el 25 % no tiene hermanos (el primer cuartil es 0) y el 75 % tiene 1,25 o menos, es decir, en la práctica 1 o ninguno. El máximo es 5. La desviación típica (1,27) es grande comparada con la media (CV ≈ 1,3): mucha dispersión relativa. La asimetría es claramente **positiva** (1,48): la mayoría tiene 0 o 1 hermano y unos pocos tienen 4 o 5, formando una cola a la derecha. La curtosis positiva (1,85) indica una distribución **leptocúrtica**, muy concentrada en los valores bajos. Los valores 4 y 5 son atípicos.

### Ejercicio de los apuntes: varianza, cuasivarianza, S y s de las alturas

- Con **todos los datos** (exacto): S² = 83,19 · s² = 83,19 × 16/15 = 88,73 · S = 9,12 · s = 9,42.
- Con la **tabla agrupada** (aproximado, usando marcas de clase): S² = (165²·3 + 175²·6 + 185²·5 + 195²·2)/16 − 178,75² = 85,94 · s² = 91,67 · S = 9,27 · s = 9,57.

Excel con los datos en A2:A17: `=VAR.P(A2:A17)`, `=VAR.S(A2:A17)`, `=DESVEST.P(A2:A17)`, `=DESVEST.S(A2:A17)`.

## ✔ Comprueba que sabes hacer (Tema 1)

- Decir de qué tipo es una variable.
- Montar una tabla de frecuencias con nᵢ, fᵢ, %, Nᵢ y Fᵢ, **a mano y en Excel**.
- Hacer un diagrama de barras, de sectores y un histograma, **en papel y en Excel**.
- Calcular media, mediana y moda, con datos sueltos y con intervalos.
- Calcular cuartiles y percentiles e interpretarlos con una frase.
- Calcular varianza, desviación típica (y sus "cuasi") y el CV, y comparar dos grupos.
- Varianza dentro y entre grupos.
- Dibujar y leer un diagrama de caja y decir si hay atípicos.
- Hacer todo lo anterior **solo con calculadora**, con la tabla en papel.
- Escribir un análisis descriptivo a partir de un resumen de estadísticos.
