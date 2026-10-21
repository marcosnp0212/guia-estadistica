import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 't1', 'tab': 'Tema 1', 'color': 't1'}

def card(tab, t, s): return [f'<span class="card-tab">{esc(tab)}</span>', f'<h1 class="card-t">{esc(t)}</h1>', f'<p class="card-s">{md(s)}</p>']
def sec_card(num, t, s=''): return [f'<div class="card-num">{esc(num)}</div>', f'<h1 class="card-t">{esc(t)}</h1>'] + ([f'<p class="card-s">{md(s)}</p>'] if s else [])
TOC = '<div class="toc">' + ''.join(f'<div><b>{a}</b><span>{esc(b)}</span></div>' for a, b in [
    ('1.1', 'Vocabulario básico'), ('1.2', 'Tipos de variables'), ('1.3', 'La tabla de frecuencias'), ('1.4', 'Gráficos'),
    ('1.5', 'Media, mediana y moda'), ('1.6', 'Cuantiles'), ('1.7', 'Medidas de dispersión'), ('1.8', 'Asimetría y curtosis'),
    ('1.9', 'Tipificar'), ('1.10', 'Atípicos y diagrama de caja'), ('1.11', 'Interpretar resultados')]) + '</div>'

S = []
# ---------- Portada ----------
S.append(Scene('', '', 'title', card('Tema 1', 'Análisis descriptivo de una variable', 'Estadística · explicado paso a paso, a mano y en Excel'), [
    (3, 'Hola. En este vídeo vamos a ver el Tema 1: el análisis descriptivo de una variable. Vamos despacio y con ejemplos. Para cada cosa verás cómo se hace a mano, con calculadora, cómo se hace en Excel y qué frase escribir en el examen.'),
]))
S.append(Scene('', '', 'card', [f'<h1 class="card-t" style="font-size:80px">Qué vamos a ver</h1>', TOC], [
    (2, 'Estos son los 11 apartados del tema. La idea de todo el tema es sencilla: tenemos muchos datos de una sola característica, por ejemplo cuántos hermanos tiene cada persona, y queremos resumirlos. Ordenarlos en una tabla, dibujarlos y dar unos pocos números que cuenten cómo son: dónde está el centro, cuánto se separan los datos y qué forma tienen.'),
]))

# ---------- 1.1 Vocabulario ----------
S.append(Scene('1.1.', 'Vocabulario básico', 'card', sec_card('1.1', 'Vocabulario básico', 'Las palabras que salen en las preguntas de teoría'), [
    (3, 'Apartado 1.1: vocabulario básico. Son pocas palabras, pero salen en las preguntas de teoría. Con una frase de cada una vas bien.'),
]))
S.append(Scene('1.1.', 'Vocabulario básico', 'teo', [
    Li('**Individuo:** cada «cosa» de la que tomamos datos (una persona, una empresa).'),
    Li('**Población:** todos los individuos que nos interesan.'),
    Li('**Muestra:** un trozo de la población. Si estudias a todos, es un **censo**.'),
    Li('**Parámetro** → de la población. **Estadístico** → de la muestra.'),
    Li('**Variable:** la característica que medimos (salario, sexo, nº de hijos).'),
    Truco('**P**arámetro → **P**oblación · **E**stadístico → mu**E**stra'),
], [
    (1, 'Un individuo es cada cosa de la que tomamos datos. Puede ser una persona, una empresa o una provincia.'),
    (2, 'La población son todos los individuos que nos interesan. Por ejemplo, todos los trabajadores de España.'),
    (3, 'Como casi nunca podemos preguntar a todos, estudiamos un trozo: eso es la muestra. Por ejemplo, 500 trabajadores elegidos al azar. Si estudiamos a todos, se llama censo.'),
    (4, 'Un parámetro es un número que describe a la población, como la media de todos. Un estadístico es ese mismo tipo de número, pero calculado en la muestra.'),
    (5, 'Y la variable es la característica que medimos: el salario, el sexo, el número de hijos.'),
    (6, 'Un truco para no confundirlos: parámetro empieza por P, como población. Estadístico tiene una E, como muestra.'),
]))

# ---------- 1.2 Tipos ----------
S.append(Scene('1.2.', 'Tipos de variables', 'card', sec_card('1.2', 'Tipos de variables', 'Lo primero que hay que mirar en cualquier ejercicio'), [
    (3, 'Apartado 1.2: los tipos de variables. Es lo primero que tienes que mirar en cualquier ejercicio, porque según el tipo se pueden hacer unas cosas u otras.'),
]))
S.append(Scene('1.2.', 'Tipos de variables', 'teo', [
    T(['Tipo', 'Cómo son', 'Ejemplos'], [
        ['**Cuantitativa discreta**', 'Números que se cuentan', 'Nº de hijos, de hermanos'],
        ['**Cuantitativa continua**', 'Números que se miden', 'Salario, altura, superficie'],
        ['**Cualitativa nominal**', 'Palabras sin orden', 'Sexo, departamento'],
        ['**Cualitativa ordinal**', 'Palabras con orden', 'Satisfacción: baja, media, alta']]),
    Truco('¿Es un número? → cuantitativa. ¿Se cuenta con los dedos? → discreta. ¿Se mide? → continua.\n¿Es una palabra? → cualitativa. ¿Tiene orden? → ordinal; si no, nominal.'),
    Ojo('Con una variable **nominal** solo hay **moda** y gráficos de barras o sectores. No existe «el departamento medio».'),
], [
    (1, 'Hay cuatro tipos. Las cuantitativas son números. Si se cuentan, uno, dos, tres, son discretas: el número de hijos. Si se miden y pueden tener decimales, son continuas: el salario o la altura. Las cualitativas son palabras. Si no tienen orden, son nominales, como el sexo o el departamento. Si tienen un orden lógico, son ordinales, como la satisfacción: baja, media y alta.'),
    (2, 'Para distinguirlas, hazte estas preguntas. ¿La respuesta es un número? Entonces es cuantitativa. ¿Se cuenta con los dedos? Discreta. ¿Se mide con una regla, una báscula o en euros? Continua. ¿La respuesta es una palabra? Cualitativa. ¿Esas palabras tienen un orden natural? Ordinal. Si no, nominal.'),
    (3, 'Ojo con esto, que cae en el examen: con una variable nominal solo puedes calcular la moda y hacer gráficos de barras o de sectores. No tiene sentido calcular la media del departamento.'),
]))

# ---------- 1.3 Tabla de frecuencias ----------
S.append(Scene('1.3.', 'La tabla de frecuencias', 'card', sec_card('1.3', 'La tabla de frecuencias', 'Cuántas veces aparece cada valor. Es el primer paso, siempre.'), [
    (3, 'Apartado 1.3: la tabla de frecuencias. Es una tabla que dice cuántas veces aparece cada valor. Es el primer paso de casi todos los ejercicios.'),
]))
S.append(Scene('1.3.', 'La tabla de frecuencias', 'teo', [
    T(['Símbolo', 'Nombre', 'Cómo se calcula'], [
        ['xᵢ', 'Valor', 'Cada valor distinto, ordenado'],
        ['nᵢ', 'Frecuencia absoluta', 'Contando'],
        ['fᵢ', 'Frecuencia relativa', 'nᵢ ÷ n'],
        ['%', 'Porcentaje', 'fᵢ × 100'],
        ['Nᵢ', 'Absoluta acumulada', 'Suma de las nᵢ hasta esa fila'],
        ['Fᵢ', 'Relativa acumulada', 'Nᵢ ÷ n']]),
    P('**Siempre se cumple:** Σnᵢ = n · Σfᵢ = 1 · la última Nᵢ = n · la última Fᵢ = 1', 's'),
], [
    (1, 'Estas son sus columnas. xᵢ son los valores distintos, ordenados de menor a mayor. nᵢ, la frecuencia absoluta: cuántas veces aparece cada valor. fᵢ, la frecuencia relativa: qué parte del total es; se calcula dividiendo nᵢ entre n, el número total de datos. El porcentaje es la relativa por cien. Nᵢ es la acumulada: cuántos datos hay hasta ese valor, incluido. Y Fᵢ, la acumulada relativa.'),
    (2, 'Hay unas comprobaciones que siempre se cumplen: la suma de las frecuencias absolutas es n, la suma de las relativas es 1, y la última acumulada es n. Úsalas para saber si lo has hecho bien.'),
]))
S.append(Scene('1.3.', 'La tabla de frecuencias', 'mano', [
    P('**Ejemplo:** número de hermanos de 44 personas.', 's'),
    Step(1, '**Ordena** o apunta los valores distintos: 0, 1, 2, 3, 4, 5.'),
    Step(2, '**Cuenta con palotes** cuántas veces sale cada uno. Agrupa de 5 en 5.'),
    Step(3, 'Columna **nᵢ**. Súmala: tiene que dar **n = 44**.'),
    Step(4, '**fᵢ** = nᵢ ÷ n con la calculadora. **Nᵢ**: la de arriba + la nᵢ de su fila.'),
    T(['xᵢ', 'nᵢ', 'fᵢ', '%', 'Nᵢ', 'Fᵢ'], [[0, 21, '0,477', '47,73', 21, '0,477'], [1, 12, '0,273', '27,27', 33, '0,750'], [2, 6, '0,136', '13,64', 39, '0,886'],
        [3, 2, '0,045', '4,55', 41, '0,932'], [4, 2, '0,045', '4,55', 43, '0,977'], [5, 1, '0,023', '2,27', 44, '1']], small=True),
], [
    (1, 'Vamos a hacerla a mano con el ejemplo de clase: se preguntó a 44 personas cuántos hermanos tenían.'),
    (2, 'Primero, ordena los datos o apunta los valores distintos que aparecen: 0, 1, 2, 3, 4 y 5.'),
    (3, 'Segundo, recorre la lista una sola vez y pon un palote junto a cada valor cada vez que aparezca. Agrúpalos de 5 en 5 para no perderte.'),
    (4, 'Tercero, cuenta los palotes: esa es la columna nᵢ. Súmala. Tiene que darte 44. Si no te da, has contado mal: repítelo antes de seguir.'),
    (5, 'Cuarto, divide cada nᵢ entre 44 con la calculadora: es la frecuencia relativa. Y la acumulada se va sumando: la primera es 21; la segunda, 21 + 12 = 33; y así hasta llegar a 44.'),
    (6, 'Así queda la tabla. Una fila se lee así: 21 personas, el 47,7 %, no tienen hermanos. Y con la acumulada: 33 personas, el 75 %, tienen un hermano o ninguno.'),
]))
S.append(Scene('1.3.', 'La tabla de frecuencias', 'xl', [
    P('Datos en **B2:B45** y valores 0 a 5 en **D2:D7**.', 's'),
    XL('=CONTAR.SI($B$2:$B$45;D2)', 'nᵢ, y arrastras'),
    XL('=E2/$E$8', 'fᵢ (n en E8)'),
    XL('=H2+E3', 'Nᵢ: la anterior + la nᵢ'),
    Truco('El **$** fija el rango y el total para que **no se muevan al arrastrar**. Sin él, salen números raros o **#¡DIV/0!**'),
], [
    (1, 'En Excel, supón que tienes los 44 datos en la columna B, de la fila 2 a la 45, y los valores del 0 al 5 en la columna D.'),
    (2, 'Para la frecuencia absoluta, escribe CONTAR.SI, el rango de datos fijado con dólares, punto y coma, y la celda del valor. Luego arrastras hacia abajo.'),
    (3, 'Para la relativa, divides cada frecuencia entre el total, que tienes en E8, también fijado con dólares.'),
    (4, 'Y la acumulada: la primera es igual a la primera frecuencia, y cada una de las siguientes es la de arriba más la frecuencia de su fila.'),
    (5, 'El dólar es muy importante. Sirve para que, al arrastrar la fórmula, Excel no mueva el rango de datos ni el total. Si se te olvida, verás números raros o el error dividir entre cero.'),
]))
S.append(Scene('1.3.', 'La tabla de frecuencias', 'mano', [
    P('**Agrupar en intervalos** (variables continuas): 16 alturas, de 163 a 198 cm.', 's'),
    Step(1, 'Nº de intervalos ≈ √n → √16 = **4**.'),
    Step(2, 'Amplitud ≈ (máx − mín) ÷ 4 = 35 ÷ 4 = 8,75 → redondea a **10**.'),
    Step(3, 'Intervalos: [160, 170] (170, 180] (180, 190] (190, 200]. **Marca** = punto medio.'),
    Step(4, 'Cuenta con palotes. Un 170 va en [160, 170]: el **paréntesis** dice que no entra en el siguiente.'),
    T(['Intervalo', 'Marca', 'nᵢ', 'Nᵢ'], [['[160, 170]', 165, 3, 3], ['(170, 180]', 175, 6, 9], ['(180, 190]', 185, 5, 14], ['(190, 200]', 195, 2, 16]], small=True),
], [
    (1, 'Si la variable es continua, como la altura o el salario, casi nunca se repite un valor exacto. Entonces se agrupan los datos en intervalos. Ejemplo de clase: 16 alturas, de 163 a 198 centímetros.'),
    (2, 'Número de intervalos: más o menos la raíz cuadrada de n. Raíz de 16: 4.'),
    (3, 'Amplitud: el máximo menos el mínimo, entre el número de intervalos. 35 entre 4 da 8,75, y lo redondeamos hacia arriba a un número cómodo: 10.'),
    (4, 'Los intervalos quedan así. La marca de clase es el punto medio de cada intervalo, por ejemplo 165. Representa a todo el intervalo en las cuentas.'),
    (5, 'Ahora cuentas cuántos datos caen en cada uno. Cuidado con los extremos: un dato que vale justo 170 va en el primer intervalo, porque el paréntesis del segundo dice que el 170 no entra.'),
    (6, 'Y así queda la tabla de las alturas, con sus marcas y sus acumuladas. En Excel esto se hace con la función FRECUENCIA, que cuenta los datos de cada intervalo a la vez.'),
]))

# ---------- 1.4 Gráficos ----------
S.append(Scene('1.4.', 'Gráficos', 'card', sec_card('1.4', 'Gráficos', 'Barras, sectores, histograma y polígono'), [
    (3, 'Apartado 1.4: los gráficos. Qué gráfico va con cada tipo de variable, cómo se dibuja en papel y cómo se hace en Excel.'),
]))
S.append(Scene('1.4.', 'Gráficos', 'teo', [
    Li('**Barras:** cualitativas y discretas. Las barras **no se tocan**.'),
    Img('t1_barras_hermanos.svg', 900),
], [
    (1, 'Para variables cualitativas y para las discretas se usa el diagrama de barras: en el eje horizontal, los valores; en el vertical, la frecuencia. Las barras no se tocan.'),
    (2, 'Este es el de los hermanos. Se ve de un vistazo que lo más frecuente es no tener hermanos, y que a partir de ahí las barras bajan.'),
]))
S.append(Scene('1.4.', 'Gráficos', 'teo', [
    Li('**Sectores:** un círculo repartido. Ángulo = **360 × fᵢ**. Solo con pocas categorías.'),
    Li('**Radial (de araña):** un radio por categoría. Sirve para comparar perfiles.'),
    Li('**Pictograma:** dibujos en lugar de barras.'),
    Li('**Histograma:** para intervalos. Las barras **se tocan** y lo que cuenta es el **área**.'),
    Li('Si los intervalos miden distinto, la altura es la **densidad**: dᵢ = nᵢ ÷ aᵢ.'),
    Li('**Polígono de frecuencias:** une los centros de los techos del histograma.'),
], [
    (1, 'El diagrama de sectores es un círculo repartido en trozos. El ángulo de cada trozo es 360 por la frecuencia relativa. Solo es recomendable con pocas categorías.'),
    (2, 'El gráfico radial, o de araña, tiene un radio por categoría y sirve para comparar perfiles, por ejemplo el gasto de dos provincias en varias partidas.'),
    (3, 'El pictograma usa dibujos en lugar de barras.'),
    (4, 'Para variables agrupadas en intervalos se usa el histograma. Se parece a las barras, pero aquí las barras se tocan, porque los intervalos van seguidos. Y lo que importa es el área de cada rectángulo.'),
    (5, 'Por eso, si los intervalos no miden lo mismo, la altura no es la frecuencia, sino la densidad: la frecuencia dividida entre la amplitud. Si un intervalo es el doble de ancho, es normal que tenga más datos solo por eso.'),
    (6, 'Y el polígono de frecuencias es una línea que une los puntos medios de los techos del histograma.'),
]))
S.append(Scene('1.4.', 'Gráficos', 'mano', [
    Step(1, '**Barras:** dos ejes; valores en el horizontal, escala en el vertical (de 0 a 25, de 5 en 5).'),
    Step(2, '**Sectores:** ángulo de cada trozo = 360 × fᵢ. Hermanos: 171,8° · 98,2° · 49,1° · 16,4° · 16,4° · 8,2°.'),
    Step(3, '**Histograma:** eje horizontal **a escala**. Altura = nᵢ (o la densidad si las amplitudes son distintas).'),
    Step(4, '**Polígono:** un punto en el centro de cada techo y únelos con la regla.'),
    Step(5, 'Pon **título** y nombre a los **ejes**.'),
], [
    (1, 'En papel, para las barras: dibuja los dos ejes. En el horizontal, los valores separados por el mismo espacio. En el vertical, una escala que llegue un poco por encima de la frecuencia más alta; con los hermanos, de 0 a 25, marcando de 5 en 5.'),
    (2, 'Para los sectores, calcula el ángulo de cada trozo, 360 por la frecuencia relativa, y mídelo con el transportador, uno detrás de otro. Con los hermanos salen estos ángulos, que suman 360.'),
    (3, 'Para el histograma, el eje horizontal va a escala: un intervalo el doble de ancho ocupa el doble. Y la altura es la frecuencia, o la densidad si los intervalos miden distinto. Los rectángulos van pegados.'),
    (4, 'Para el polígono, marca un punto en el centro del techo de cada rectángulo y únelos con líneas rectas.'),
    (5, 'Y no olvides el título y el nombre de cada eje.'),
]))
S.append(Scene('1.4.', 'Gráficos', 'xl', [
    Li('**Barras:** selecciona valores y frecuencias → Insertar → **Columna agrupada**.'),
    Li('**Sectores:** Insertar → **Gráfico circular**.'),
    Li('**Histograma:** datos sin agrupar → Insertar → Gráfico estadístico → **Histograma**.'),
    Li('Desde una tabla ya agrupada: columnas y **ancho del intervalo = 0 %** para que se toquen.'),
], [
    (1, 'En Excel, para las barras, selecciona los valores y las frecuencias, y ve a Insertar, gráfico de columnas, columna agrupada.'),
    (2, 'Para los sectores, Insertar, gráfico circular.'),
    (3, 'Para un histograma con los datos sin agrupar: Insertar, gráfico estadístico, histograma.'),
    (4, 'Y si ya tienes la tabla agrupada, haz un gráfico de columnas y pon el ancho del intervalo al 0 por ciento, para que las barras se toquen.'),
]))

# ---------- 1.5 Media, mediana, moda ----------
S.append(Scene('1.5.', 'Media, mediana y moda', 'card', sec_card('1.5', 'Media, mediana y moda', 'Las medidas de posición central: dónde está el centro de los datos'), [
    (3, 'Apartado 1.5: las medidas de posición central. Media, mediana y moda. Las tres dicen dónde está el centro de los datos, cada una a su manera.'),
]))
S.append(Scene('1.5.', 'La media', 'teo', [
    F('x̄ = ' + frac('Σxᵢ', 'n') + '&nbsp;&nbsp;&nbsp;(datos sueltos)'),
    F('x̄ = ' + frac('Σxᵢ·nᵢ', 'n') + '&nbsp;&nbsp;&nbsp;(con tabla)'),
    Truco('Juntas todo y lo repartes a partes iguales: lo que le toca a cada uno es la **media**.'),
], [
    (1, 'La media es el promedio de toda la vida: sumas todos los datos y divides entre cuántos hay. Se escribe equis barra.'),
    (2, 'Si los datos vienen en una tabla de frecuencias, cada valor se multiplica por las veces que aparece, se suma todo y se divide entre n.'),
    (3, 'Una forma de entenderla: imagina que juntas todo, por ejemplo todos los hermanos del grupo, y lo repartes a partes iguales. Lo que le toca a cada persona es la media.'),
]))
S.append(Scene('1.5.', 'La media', 'mano', [
    T(['xᵢ', 'nᵢ', 'xᵢ · nᵢ'], [[0, 21, 0], [1, 12, 12], [2, 6, 12], [3, 2, 6], [4, 2, 8], [5, 1, 5], ['**Total**', '**44**', '**43**']], hl_col=2, small=True),
    Step(1, 'Columna **xᵢ · nᵢ**: cada valor por su frecuencia.'),
    Step(2, 'Súmala: **Σxᵢnᵢ = 43**.'),
    Step(3, 'Divide entre n: 43 ÷ 44 = **0,977 hermanos**.'),
    Ojo('Con intervalos, xᵢ es la **marca de clase**. La media sale **aproximada**: alturas 178,75 con la tabla y 179,25 con los datos.'),
], [
    (1, 'A mano, con la tabla de los hermanos.'),
    (2, 'Añade una columna con cada valor por su frecuencia: 0 por 21, 1 por 12, 2 por 6, y así.'),
    (3, 'Suma esa columna: da 43. Son todos los hermanos juntos.'),
    (4, 'Y divide entre el número de personas: 43 entre 44, 0,977. De media, casi un hermano por persona.'),
    (5, 'Con intervalos se hace igual, pero usando la marca de clase como valor. El resultado es aproximado, porque suponemos que todos los datos del intervalo valen su punto medio. En las alturas, con la tabla sale 178,75, y con los datos sueltos, 179,25. Se parecen, pero no son iguales.'),
]))
S.append(Scene('1.5.', 'La media', 'xl', [
    XL('=PROMEDIO(B2:B45)', 'datos sueltos'),
    XL('=SUMAPRODUCTO(D2:D7;E2:E7)/SUMA(E2:E7)', 'desde la tabla'),
    Truco('SUMAPRODUCTO hace en un paso la columna xᵢ·nᵢ y su suma.'),
], [
    (1, 'En Excel, con los datos sueltos, la función es PROMEDIO.'),
    (2, 'Si solo tienes la tabla, con los valores en D y las frecuencias en E: SUMAPRODUCTO de valores y frecuencias, dividido entre la suma de las frecuencias.'),
    (3, 'SUMAPRODUCTO hace en un solo paso la columna de valor por frecuencia y la suma. Si te da inseguridad, haz la columna auxiliar y divide: da lo mismo.'),
]))
S.append(Scene('1.5.', 'Media ponderada y media truncada', 'teo', [
    F('x̄ = ' + frac('x̄₁·T₁ + x̄₂·T₂ + …', 'T₁ + T₂ + …')),
    T(['Categoría', 'Salario medio', 'Personas'], [['Administrativos', 1900, 450], ['Técnicos', 2300, 328], ['Jefes de sección', 2580, 45], ['Altos cargos', 4000, 3]], small=True),
    Res('(1900·450 + 2300·328 + 2580·45 + 4000·3) ÷ 826 = **2103,51 €**'),
    Ojo('**MEDIA MAL:** (1900 + 2300 + 2580 + 4000) ÷ 4 = 2695 €. Los 3 altos cargos pesarían igual que los 450 administrativos.'),
    P('**Media truncada:** quitas los extremos y haces la media del resto. 20, 22, …, 35, **50** → sin el 20 y el 50: **26,25**.', 's'),
], [
    (1, 'Cuando tienes las medias de varios grupos de distinto tamaño, la media de todos juntos es la media ponderada: cada media por el tamaño de su grupo, se suma y se divide entre el total.'),
    (2, 'Ejemplo de clase: cuatro categorías con su salario medio y su número de personas.'),
    (3, 'La media bien hecha es 1900 por 450, más 2300 por 328, más 2580 por 45, más 4000 por 3, todo entre 826 personas: 2103,51 euros.'),
    (4, 'El error típico es hacer la media de las cuatro medias sin ponderar: daría 2695 euros, y es falso, porque los 3 altos cargos pesarían lo mismo que los 450 administrativos. La profesora lo dejó escrito en el Excel de clase como media mal.'),
    (5, 'Y la media truncada: se quitan los datos más extremos, el mismo porcentaje por arriba y por abajo, y se hace la media del resto. Con estos 10 salarios, quitando el más bajo y el más alto, sale 26,25, que refleja mejor el salario típico que la media normal, 28. En Excel es MEDIA.ACOTADA.'),
]))
S.append(Scene('1.5.', 'Cambios de origen y escala', 'teo', [
    F('Y = a·X + b &nbsp;→&nbsp; ȳ = a·x̄ + b'),
    P('**A la media le pasa lo mismo que a los datos.** Media de los salarios: 2406 €.', 's'),
    Li('+200 € a todos → 2406 + 200 = **2606 €**'),
    Li('+3 % a todos → 1,03 × 2406 = **2478,18 €**'),
    Li('Las dos cosas → 1,03 × 2406 + 200 = **2678,18 €**'),
], [
    (1, 'Si a todos los datos les sumas una cantidad, o los multiplicas por un número, la media cambia exactamente igual.'),
    (2, 'Es decir: a la media le pasa lo mismo que a los datos. Ejemplo de clase: unos salarios con media 2406 euros.'),
    (3, 'Si todos suben 200 euros, la media sube 200: 2606.'),
    (4, 'Si todos suben un 3 por ciento, se multiplica por 1,03: 2478,18.'),
    (5, 'Y si suben las dos cosas: 1,03 por 2406, más 200: 2678,18 euros.'),
]))
S.append(Scene('1.5.', 'La moda', 'teo', [
    P('**Moda:** el valor que **más se repite**. Hermanos: la mayor nᵢ es 21, en el 0 → **Mo = 0**.'),
    P('**Con intervalos:** intervalo modal = el de mayor **densidad**.', 's'),
    F('Mo = Lᵢ₋₁ + ' + frac('dᵢ − dᵢ₋₁', '(dᵢ − dᵢ₋₁) + (dᵢ − dᵢ₊₁)') + ' · aᵢ'),
    Res('Alturas: Mo = 170 + ' + '(6 − 3) ÷ ((6 − 3) + (6 − 5)) · 10 = 170 + 7,5 = **177,5 cm**'),
    Ojo('Si el modal es el **primero**, dᵢ₋₁ = 0. Si es el **último**, dᵢ₊₁ = 0.'),
], [
    (1, 'La moda es el valor que más se repite. En los hermanos, la frecuencia más alta es 21, que corresponde al 0. La moda es 0: lo más frecuente es no tener hermanos. Cuidado: la moda es el valor, no la frecuencia.'),
    (2, 'Con intervalos, primero buscas el intervalo modal, que es el de mayor densidad. Si todos los intervalos miden lo mismo, vale con mirar la frecuencia.'),
    (3, 'Y aplicas esta fórmula: el extremo inferior del intervalo modal, más una fracción de su amplitud. Arriba, su densidad menos la del anterior. Abajo, esa misma resta más su densidad menos la del siguiente.'),
    (4, 'En las alturas, el modal es de 170 a 180, con 6 datos; el anterior tiene 3 y el siguiente 5. Mo es 170 más 3 entre 4, por 10: 177,5 centímetros.'),
    (5, 'Si el intervalo modal es el primero, no hay anterior: se pone 0. Y si es el último, el siguiente vale 0.'),
]))
S.append(Scene('1.5.', 'La mediana', 'teo', [
    P('**Mediana:** el valor del **medio** con los datos ordenados. Deja el 50 % por debajo.'),
    Step(1, 'Calcula **n/2**.'),
    Step(2, 'Busca la **primera Nᵢ ≥ n/2**.'),
    Step(3, 'Si Nᵢ **>** n/2 → Me = ese xᵢ. Si Nᵢ **=** n/2 → Me = (xᵢ + xᵢ₊₁) ÷ 2.'),
    Res('Hermanos: n/2 = 22. Acumuladas: 21, **33**… → 33 > 22 → **Me = 1**'),
], [
    (1, 'La mediana es el valor que queda justo en el medio cuando ordenas los datos de menor a mayor. Deja la mitad por debajo y la otra mitad por encima.'),
    (2, 'La receta de los apuntes, con la tabla: primero calcula n entre 2.'),
    (3, 'Luego mira la columna de acumuladas y busca la primera que sea mayor o igual que n entre 2.'),
    (4, 'Si esa acumulada es mayor que n entre 2, la mediana es el valor de esa fila. Si es exactamente igual, la mediana es la media entre ese valor y el siguiente.'),
    (5, 'En los hermanos: n entre 2 es 22. Las acumuladas son 21, 33… La primera que llega a 22 es 33, en el valor 1. Como 33 es mayor que 22, la mediana es 1. La mitad de las personas tiene 1 hermano o ninguno.'),
]))
S.append(Scene('1.5.', 'La mediana', 'mano', [
    P('**Datos sueltos (sin tabla):** ordena y numera.', 's'),
    P('163 · 167 · 169 · 172 · 174 · 176 · 177 · **178** · **179** · 181 · 182 · 184 · 186 · 189 · 193 · 198'),
    Step(1, 'n/2 = 16/2 = **8**, entero → media del 8.º y el 9.º.'),
    Res('Me = (178 + 179) ÷ 2 = **178,5 cm**'),
    P('**Con intervalos:**', 's'),
    F('Me = Lᵢ₋₁ + ' + frac('n/2 − Nᵢ₋₁', 'nᵢ') + ' · aᵢ = 170 + ' + frac('8 − 3', '6') + ' · 10 = 178,33'),
], [
    (1, 'Con datos sueltos, sin tabla, es la misma idea: ordena los datos y numéralos.'),
    (2, 'Las 16 alturas, ya ordenadas.'),
    (3, 'n entre 2 es 8. Si sale un número entero, la mediana es la media del dato que ocupa ese puesto y el siguiente: el octavo y el noveno. Si no sale entero, redondeas hacia arriba y coges ese dato.'),
    (4, 'El octavo es 178 y el noveno 179: la mediana es 178,5 centímetros.'),
    (5, 'Y si los datos vienen en intervalos, se usa una fórmula.'),
    (6, 'El extremo inferior del intervalo mediano, más lo que falta para llegar a n entre 2, dividido entre la frecuencia del intervalo, por su amplitud. En las alturas: 170 más 5 sextos de 10, 178,33. La idea: hasta 170 ya llevamos 3 datos; nos faltan 5 de los 6 del intervalo, así que avanzamos 5 sextos del intervalo.'),
]))
S.append(Scene('1.5.', 'Media, mediana o moda', 'int', [
    XL('=MEDIANA(B2:B45)', 'mediana'),
    XL('=MODA.UNO(B2:B45)', 'moda'),
    Li('La **media** usa todos los datos, pero los **extremos** la arrastran.'),
    Li('La **mediana** es **robusta**: mejor para salarios o precios.'),
    Li('La **moda** es la única para variables **nominales**.'),
], [
    (1, 'En Excel, con datos sueltos, la mediana es MEDIANA.'),
    (2, 'Y la moda, MODA.UNO. Con intervalos, Excel no tiene función: se escribe la fórmula de los apuntes con referencias a las celdas.'),
    (3, '¿Cuál uso? La media usa todos los datos, pero un valor muy extremo la arrastra: un salario de un millón dispara la media.'),
    (4, 'La mediana no se deja arrastrar por los extremos. Para salarios o precios de vivienda suele representar mejor lo normal.'),
    (5, 'Y la moda es la única que sirve para variables nominales, como el departamento.'),
]))

# ---------- 1.6 Cuantiles ----------
S.append(Scene('1.6.', 'Cuantiles', 'card', sec_card('1.6', 'Cuantiles', 'Cuartiles, deciles y percentiles: puntos de corte'), [
    (3, 'Apartado 1.6: los cuantiles. Son puntos de corte que dividen los datos ordenados en partes iguales. La mediana es uno de ellos.'),
]))
S.append(Scene('1.6.', 'Cuantiles', 'teo', [
    Li('**Cuartiles** C₁, C₂, C₃: cortan en **4** partes. C₁ deja el 25 % por debajo; C₂ = mediana; C₃ el 75 %.'),
    Li('**Deciles** D₁ … D₉: en **10** partes. **Percentiles** P₁ … P₉₉: en **100**.'),
    Li('C₁ = P₂₅ · C₂ = D₅ = P₅₀ = Me · C₃ = P₇₅'),
    T(['Medida', 'Busco la primera Nᵢ ≥ …'], [['C₁', 'n/4'], ['C₃', '3n/4'], ['Pᵣ', 'r·n/100']], small=True),
    F('Pᵣ = Lᵢ₋₁ + ' + frac('r·n/100 − Nᵢ₋₁', 'nᵢ') + ' · aᵢ'),
], [
    (1, 'Los cuartiles cortan en cuatro partes. El primero, C1, deja el 25 por ciento de los datos por debajo. El segundo es la mediana. El tercero, C3, deja el 75 por ciento por debajo.'),
    (2, 'Los deciles cortan en diez partes, y los percentiles en cien. El percentil 98 deja el 98 por ciento por debajo.'),
    (3, 'Hay equivalencias útiles: C1 es el percentil 25, la mediana es el percentil 50 y C3 el percentil 75.'),
    (4, 'Se calculan exactamente igual que la mediana, cambiando n entre 2 por la proporción que toque: n entre 4 para C1, 3n entre 4 para C3, y r por n entre 100 para el percentil r.'),
    (5, 'Con intervalos, la fórmula es la de la mediana, cambiando n entre 2 por ese valor.'),
]))
S.append(Scene('1.6.', 'Cuantiles', 'mano', [
    P('**Hermanos (tabla):** acumuladas 21, 33, 39, 41, 43, 44.', 's'),
    Step(1, 'C₁: n/4 = 11 → primera Nᵢ ≥ 11 es 21 (valor 0), y 21 > 11 → **C₁ = 0**.'),
    Step(2, 'C₃: 3n/4 = 33 → Nᵢ = 33, **igual** → C₃ = (1 + 2) ÷ 2 = **1,5**.'),
    P('**Alturas (16 datos sueltos):**', 's'),
    Step(3, 'C₁: 16/4 = 4, entero → (4.º + 5.º) ÷ 2 = (172 + 174) ÷ 2 = **173**.'),
    Step(4, 'P₉₀: 0,9 · 16 = 14,4 → redondeo a 15 → el 15.º dato = **193**.'),
    Ojo('Excel (`CUARTIL.INC`) usa otro método: en los hermanos da C₃ = 1,25, no 1,5. **En papel, la receta.**'),
], [
    (1, 'A mano, con la tabla de los hermanos. Las acumuladas son 21, 33, 39, 41, 43 y 44.'),
    (2, 'C1: n entre 4 es 11. La primera acumulada que llega a 11 es 21, en el valor 0. Como 21 es mayor que 11, C1 es 0.'),
    (3, 'C3: 3n entre 4 es 33. La primera acumulada que llega es justo 33, en el valor 1. Como es exactamente igual, se hace la media con el valor siguiente: 1 más 2, entre 2, 1,5.'),
    (4, 'Con datos sueltos, por ejemplo las 16 alturas ordenadas, es igual que la mediana.'),
    (5, 'C1: 16 entre 4 es 4, un número entero. Entonces es la media del cuarto y el quinto dato: 172 y 174, que da 173.'),
    (6, 'Percentil 90: 0,9 por 16 es 14,4. No es entero: redondeas hacia arriba, 15, y es el dato número 15: 193.'),
    (7, 'Ojo: Excel usa otro método para los cuartiles y a veces da algo distinto. En los hermanos, CUARTIL.INC da 1,25 en vez de 1,5. Los dos son correctos según el método. En papel, usa la receta de los apuntes.'),
]))
S.append(Scene('1.6.', 'Cuantiles', 'mano', [
    T(['Intervalo', 'nᵢ', 'Nᵢ'], [['[10, 13]', 15, 15], ['(13, 18]', 29, 44], ['(18, 25]', 56, 100]], small=True),
    Step(1, 'C₁: 100/4 = 25 → intervalo (13, 18] → 13 + (25 − 15)/29 · 5 = **14,72**'),
    Step(2, 'Me: 50 → (18, 25] → 18 + (50 − 44)/56 · 7 = **18,75**'),
    Step(3, 'P₇₀: 70 → (18, 25] → 18 + (70 − 44)/56 · 7 = **21,25**'),
], [
    (1, 'Y con intervalos, el ejercicio de los apuntes: 100 datos en tres intervalos.'),
    (2, 'C1: 100 entre 4 es 25. La primera acumulada que llega a 25 es 44, el intervalo de 13 a 18. Aplicamos la fórmula: 13 más, 25 menos 15, entre 29, por 5. Da 14,72.'),
    (3, 'La mediana: 50 cae en el intervalo de 18 a 25. 18 más, 50 menos 44, entre 56, por 7: 18,75.'),
    (4, 'Y el percentil 70: 70 cae en el mismo intervalo. 18 más, 70 menos 44, entre 56, por 7: 21,25.'),
]))
S.append(Scene('1.6.', 'Cuantiles', 'int', [
    XL('=CUARTIL.INC(B2:B45;1)', 'C₁ (3 para C₃)'),
    XL('=PERCENTIL.INC(B2:B45;0,97)', 'P₉₇, en tanto por uno'),
    Res('«Está en el **percentil 98**»: el 98 % gana **menos o igual** que él; solo el 2 % gana más.'),
    Res('«**C₃ = 1,5** hermanos»: el 75 % tiene 1,5 hermanos o menos.'),
], [
    (1, 'En Excel, CUARTIL.INC con el rango y el número de cuartil: 1 o 3.'),
    (2, 'Y PERCENTIL.INC con el porcentaje en tanto por uno: 0,97 para el percentil 97.'),
    (3, 'Cómo se interpreta, que es lo que te pedirán: si un trabajador está en el percentil 98, el 98 por ciento de los trabajadores gana menos o igual que él, y solo el 2 por ciento gana más.'),
    (4, 'Y si C3 es 1,5 hermanos: el 75 por ciento de las personas tiene 1,5 hermanos o menos; en la práctica, uno o ninguno.'),
]))

# ---------- 1.7 Dispersión ----------
S.append(Scene('1.7.', 'Medidas de dispersión', 'card', sec_card('1.7', 'Medidas de dispersión', 'Cuánto se separan los datos del centro'), [
    (3, 'Apartado 1.7: las medidas de dispersión. Dos clases pueden tener la misma nota media, un 5, y ser muy distintas: en una todos sacan un 5 y en la otra la mitad saca un 0 y la otra mitad un 10. Las medidas de dispersión dicen cuánto se separan los datos del centro.'),
]))
S.append(Scene('1.7.', 'Rango e IQR', 'teo', [
    F('Rango = máx − mín'),
    P('Hermanos: 5 − 0 = **5** · Alturas: 198 − 163 = **35**. Se deja engañar por un solo dato extremo.', 's'),
    F('IQR = C₃ − C₁'),
    P('La anchura del **50 % central**. No le afectan los extremos. Hermanos: 1,5 − 0 = **1,5**.', 's'),
], [
    (1, 'La más sencilla es el rango: el máximo menos el mínimo.'),
    (2, 'En los hermanos, 5 menos 0, 5. En las alturas, 35. Es fácil, pero un solo dato extremo lo cambia todo.'),
    (3, 'El rango intercuartílico es C3 menos C1.'),
    (4, 'Es la anchura del 50 por ciento central de los datos, y no le afectan los extremos. En los hermanos, 1,5 menos 0: 1,5.'),
]))
S.append(Scene('1.7.', 'Varianza y desviación típica', 'teo', [
    F('S² = ' + frac('Σ(xᵢ − x̄)²·nᵢ', 'n') + '&nbsp;=&nbsp;' + frac('Σxᵢ²·nᵢ', 'n') + ' − x̄²'),
    Li('**Varianza S²:** la media de las distancias **al cuadrado** a la media.'),
    Li('**Desviación típica S = √S²:** en las **mismas unidades** que los datos.'),
    Li('**Cuasivarianza s² = S² · n/(n − 1)** y cuasidesviación s = √s²: para muestras.'),
    Ojo('Fallo clásico: hacer (Σxᵢnᵢ)² en vez de Σxᵢ²nᵢ. Y olvidar restar x̄².'),
], [
    (1, 'La varianza es la media de las distancias al cuadrado de cada dato a la media. La fórmula de la izquierda es la definición; la de la derecha, la práctica, que es la que usarás a mano: la suma de los cuadrados por su frecuencia, entre n, menos la media al cuadrado.'),
    (2, '¿Por qué al cuadrado? Porque si sumas las distancias tal cual, las de arriba y las de abajo se anulan y siempre da 0. Al elevar al cuadrado, todas son positivas.'),
    (3, 'La varianza queda en unidades al cuadrado, euros al cuadrado, y cuesta interpretarla. Por eso se hace la raíz: la desviación típica, que está en las mismas unidades que los datos.'),
    (4, 'La cuasivarianza divide entre n menos 1 en vez de entre n. Se usa cuando los datos son una muestra. Se saca multiplicando la varianza por n entre n menos 1. Y su raíz es la cuasidesviación típica.'),
    (5, 'El fallo más típico: elevar al cuadrado la suma entera en vez de cada valor. Primero cada valor al cuadrado, luego por su frecuencia, luego se suma. Y no olvides restar la media al cuadrado al final.'),
]))
S.append(Scene('1.7.', 'Varianza y desviación típica', 'mano', [
    T(['xᵢ', 'nᵢ', 'xᵢ·nᵢ', 'xᵢ²·nᵢ'], [[0, 21, 0, 0], [1, 12, 12, 12], [2, 6, 12, 24], [3, 2, 6, 18], [4, 2, 8, 32], [5, 1, 5, 25], ['**Σ**', '**44**', '**43**', '**111**']], hl_col=3, small=True),
    Step(1, 'x̄ = 43 ÷ 44 = 0,9773'),
    Step(2, 'S² = 111 ÷ 44 − 0,9773² = 2,5227 − 0,9551 = **1,568**'),
    Step(3, 'S = √1,568 = **1,252 hermanos**'),
    Step(4, 's² = 1,568 · 44/43 = **1,604** · s = **1,266**'),
    Truco('xᵢ²·nᵢ = xᵢ · (xᵢ·nᵢ): multiplica cada valor por lo que ya tienes al lado. Y **no redondees la media** antes de elevarla.'),
], [
    (1, 'A mano, con los hermanos. La tabla lleva una columna más: equis al cuadrado por su frecuencia. Su suma es 111.'),
    (2, 'La media ya la teníamos: 43 entre 44, 0,9773.'),
    (3, 'La varianza: 111 entre 44 es 2,5227. Menos la media al cuadrado, 0,9551. Da 1,568.'),
    (4, 'La desviación típica es la raíz: 1,252 hermanos. Se interpreta así: los datos se separan de la media, en promedio, unos 1,25 hermanos.'),
    (5, 'Y si te piden las cuasi: la varianza por 44 entre 43, 1,604; y su raíz, 1,266.'),
    (6, 'Un truco para la columna de cuadrados: equis al cuadrado por ene es equis por la columna de equis por ene, que ya tienes al lado. Y usa la media sin redondear al elevarla al cuadrado: guárdala en la memoria de la calculadora.'),
]))
S.append(Scene('1.7.', 'Varianza y desviación típica', 'xl', [
    T(['Medida', 'Función', 'Hermanos'], [['Varianza S²', '`=VAR.P(B2:B45)`', '1,5677'], ['Cuasivarianza s²', '`=VAR.S(B2:B45)`', '1,6041'], ['Desviación típica S', '`=DESVEST.P(B2:B45)`', '1,2521'], ['Cuasidesviación s', '`=DESVEST.S(B2:B45)`', '1,2665']]),
    Truco('**.P = Población**, divide entre n · **.S = muestra («Sample»)**, divide entre n − 1'),
    Ojo('En las salidas del programa R de los apuntes, «**sd**» es la **cuasidesviación** s.'),
], [
    (1, 'En Excel hay una función para cada una: VAR.P para la varianza, VAR.S para la cuasivarianza, DESVEST.P para la desviación típica y DESVEST.S para la cuasidesviación.'),
    (2, 'Para acordarte: punto P es de población y divide entre n. Punto S es de sample, muestra en inglés, y divide entre n menos 1. La de clase, la ese cuadrado, es VAR.P.'),
    (3, 'Y cuidado con las salidas del programa R de los apuntes: cuando pone sd, es la cuasidesviación, no la desviación típica.'),
]))
S.append(Scene('1.7.', 'Coeficiente de variación', 'teo', [
    F('CV = ' + frac('S', 'x̄')),
    P('Dispersión **relativa**, sin unidades: sirve para **comparar** grupos con medias distintas.', 's'),
    T(['Sector', 'Media', 'S', 'CV'], [['Energético', 550, '40,82', '**0,074**'], ['Creativo', '4,33', '2,867', '**0,662**']], small=True),
    Res('Más **CV** → más dispersión relativa → la media es **menos representativa**. El creativo es mucho más disperso.'),
    XL('=DESVEST.P(B2:B45)/PROMEDIO(B2:B45)'),
], [
    (1, 'El coeficiente de variación es la desviación típica dividida entre la media.'),
    (2, 'Es una dispersión relativa, sin unidades. Sirve para comparar grupos con medias o unidades muy distintas.'),
    (3, 'Ejemplo de clase: un sector energético que factura entre 500 y 600 millones y uno creativo que factura entre 1 y 8 millones. La desviación típica del energético es mucho mayor, 40,82, pero porque sus cifras son enormes. En términos relativos, el creativo tiene un CV de 0,66 frente a 0,07.'),
    (4, 'La interpretación: cuanto mayor es el CV, más dispersión relativa hay y menos representativa es la media. El sector creativo es mucho más disperso: una empresa factura 8 veces más que otra.'),
    (5, 'En Excel, la desviación típica entre la media.'),
]))
S.append(Scene('1.7.', 'Cambios de escala y dispersión', 'teo', [
    F('Y = a·X + b &nbsp;→&nbsp; S²ᵧ = a²·S²ₓ &nbsp;·&nbsp; Sᵧ = a·Sₓ'),
    Li('**Sumar** b: la dispersión **no cambia**. Todos se mueven igual.'),
    Li('**Multiplicar** por a: S se multiplica por a, y S² por **a²**.'),
    Li('El **CV** no cambia si solo multiplicas. **Sí** cambia si sumas.'),
], [
    (1, 'Y si cambias los datos sumando o multiplicando, ¿qué le pasa a la dispersión?'),
    (2, 'Si sumas una cantidad a todos, la dispersión no cambia: todos se mueven lo mismo y siguen igual de separados.'),
    (3, 'Si multiplicas por un número, la desviación típica se multiplica por ese número, y la varianza por ese número al cuadrado.'),
    (4, 'Y el CV no cambia si solo multiplicas, porque la media y la desviación se multiplican igual. Pero sí cambia si sumas, porque la media se mueve y la desviación no.'),
]))
S.append(Scene('1.7.', 'Varianza dentro y entre grupos', 'teo', [
    F('Dentro = ' + frac('S²₁·T₁ + S²₂·T₂ + …', 'T₁ + T₂ + …'), 'l'),
    F('Entre = ' + frac('(x̄₁ − x̄)²·T₁ + (x̄₂ − x̄)²·T₂ + …', 'T₁ + T₂ + …'), 'l'),
    F('Total = Dentro + Entre'),
    P('**% debido a los grupos** = Entre ÷ Total × 100', 's'),
], [
    (1, 'Último caso de dispersión: te dan varios grupos, por ejemplo departamentos, con su tamaño, su media y su varianza, y te piden la varianza de todos juntos. La varianza dentro de los grupos es la media ponderada de las varianzas: lo dispersos que están los datos dentro de cada grupo.'),
    (2, 'La varianza entre los grupos mide lo distintas que son las medias de los grupos: cada media menos la media global, al cuadrado, por el tamaño del grupo; se suma y se divide entre el total.'),
    (3, 'La varianza total es la suma de las dos.'),
    (4, 'Y el porcentaje debido a las diferencias entre grupos es la varianza entre, dividida entre la total, por cien.'),
]))
S.append(Scene('1.7.', 'Varianza dentro y entre grupos', 'mano', [
    T(['', 'A', 'B', 'C'], [['Tamaño', 150, 200, 150], ['Media', 10, 10, 12], ['Varianza', 10, 25, 16]], small=True),
    Step(1, 'Media global = (10·150 + 10·200 + 12·150) ÷ 500 = **10,6**'),
    Step(2, 'Dentro = (10·150 + 25·200 + 16·150) ÷ 500 = **17,8**'),
    Step(3, 'Entre = ((10 − 10,6)²·150 + (10 − 10,6)²·200 + (12 − 10,6)²·150) ÷ 500 = **0,84**'),
    Step(4, 'Total = 17,8 + 0,84 = **18,64** · % entre = 0,84 ÷ 18,64 = **4,5 %**'),
    Ojo('Si te dan **desviaciones típicas**, elévalas al cuadrado primero.'),
], [
    (1, 'El ejemplo de los apuntes: tres submuestras con su tamaño, su media y su varianza.'),
    (2, 'Primero, la media global, que es la media ponderada: 5300 entre 500, 10,6.'),
    (3, 'La varianza dentro: cada varianza por su tamaño, sumado y entre 500: 17,8.'),
    (4, 'La varianza entre: cada media menos 10,6, al cuadrado, por su tamaño. Sale 54, 72 y 294; sumado, 420; entre 500, 0,84.'),
    (5, 'La total es 18,64, y solo el 4,5 por ciento se debe a las diferencias entre grupos. Interpretación: casi toda la variabilidad está dentro de los grupos; las tres submuestras tienen medias parecidas.'),
    (6, 'Cuidado: si el enunciado te da desviaciones típicas en vez de varianzas, primero elévalas al cuadrado. Es un error muy común.'),
]))

# ---------- 1.8 Forma ----------
S.append(Scene('1.8.', 'Asimetría y curtosis', 'card', sec_card('1.8', 'Medidas de forma', 'Asimetría y curtosis: el dibujo de la distribución'), [
    (3, 'Apartado 1.8: las medidas de forma. Describen el dibujo de la distribución: si tiene una cola hacia un lado, y si es más picuda o más plana.'),
]))
S.append(Scene('1.8.', 'Asimetría', 'teo', [
    Img('t1_asimetria.svg', 1300),
    T(['CA', 'Significa'], [['≈ 0', 'Simétrica: media, mediana y moda casi coinciden'], ['> 0', 'Asimetría **positiva**: cola a la **derecha** (salarios)'], ['< 0', 'Asimetría **negativa**: cola a la **izquierda**']], small=True),
], [
    (1, 'La asimetría mira si la distribución es igual a los dos lados o tiene una cola larga hacia uno de ellos.'),
    (2, 'Se mide con el coeficiente de asimetría. Si es casi 0, es simétrica. Si es positivo, hay una cola hacia la derecha: unos pocos valores muy altos, como en los salarios, donde la mayoría gana poco y unos pocos ganan muchísimo; la media queda por encima de la mediana. Si es negativo, la cola va hacia los valores bajos.'),
]))
S.append(Scene('1.8.', 'Curtosis', 'teo', [
    Img('t1_curtosis.svg', 1300),
    T(['CC', 'Nombre', 'Significa'], [['= 0', 'Mesocúrtica', 'Como la normal'], ['> 0', 'Leptocúrtica', 'Más **picuda**'], ['< 0', 'Platicúrtica', 'Más **plana**']], small=True),
    Truco('**Lepto** suena a salto (picuda) · **Plati** suena a plato (plana) · **Meso** = en medio'),
], [
    (1, 'La curtosis mira si la distribución es muy picuda, con muchos datos amontonados cerca de la media, o más plana, comparada con la campana de la distribución normal.'),
    (2, 'Si el coeficiente es 0, mesocúrtica, como la normal. Si es positivo, leptocúrtica, más picuda. Si es negativo, platicúrtica, más plana.'),
    (3, 'Un truco para recordarlo: lepto suena a salto, picuda. Plati suena a plato, plana. Meso es en medio.'),
]))
S.append(Scene('1.8.', 'Asimetría y curtosis', 'mano', [
    F('CA = ' + frac('Σ(xᵢ − x̄)³·nᵢ / n', 'S³') + '&nbsp;&nbsp;&nbsp;CC = ' + frac('Σ(xᵢ − x̄)⁴·nᵢ / n', 'S⁴') + ' − 3'),
    Step(1, 'Columna dᵢ = xᵢ − x̄, y después dᵢ³·nᵢ y dᵢ⁴·nᵢ. Súmalas.'),
    Step(2, 'Hermanos: Σdᵢ³nᵢ = 123,70 → CA = (123,70 ÷ 44) ÷ 1,2521³ = **1,43** → positiva'),
    Step(3, 'Σdᵢ⁴nᵢ = 488,03 → CC = (488,03 ÷ 44) ÷ 1,2521⁴ − 3 = **1,51** → leptocúrtica'),
    Truco('**Atajo:** media claramente mayor que la mediana → asimetría positiva.'),
    XL('=COEFICIENTE.ASIMETRIA.P(B2:B45)', '· =CURTOSIS(B2:B45)'),
], [
    (1, 'Las fórmulas usan las distancias a la media elevadas al cubo, para la asimetría, y a la cuarta, para la curtosis.'),
    (2, 'A mano es largo, y en papel suelen darte la tabla hecha o pedirte solo la interpretación. Si te lo piden entero: una columna con la distancia de cada valor a la media, y luego esa distancia al cubo por la frecuencia y a la cuarta por la frecuencia. Sumas las dos columnas.'),
    (3, 'En los hermanos, la suma de los cubos es 123,70. Dividido entre 44, y entre la desviación típica al cubo, da 1,43: asimetría positiva.'),
    (4, 'Y la curtosis: 488,03 entre 44, entre S a la cuarta, menos 3: 1,51. Leptocúrtica, muy concentrada en los valores bajos.'),
    (5, 'Un atajo sin cuentas: si la media es claramente mayor que la mediana, la asimetría es positiva.'),
    (6, 'En Excel: COEFICIENTE.ASIMETRIA.P y CURTOSIS. Pueden diferir un poco en los decimales, pero el signo, que es lo que se interpreta, coincide.'),
]))

# ---------- 1.9 Tipificar ----------
S.append(Scene('1.9.', 'Tipificar', 'teo', [
    F('z = ' + frac('x − x̄', 'S')),
    P('Cuántas desviaciones típicas está un dato **por encima (+)** o **por debajo (−)** de la media. Sirve para **comparar** datos de grupos distintos.', 's'),
    Step(1, 'Examen 1: nota 6, media 7, S = 2 → z = (6 − 7) ÷ 2 = **−0,5**'),
    Step(2, 'Examen 2: nota 5, media 4,5, S = 1 → z = (5 − 4,5) ÷ 1 = **+0,5**'),
    Res('Aunque el 6 parece mejor nota, **relativamente** le fue mejor en el segundo examen.'),
    XL('=NORMALIZACION(A2;media;desviación)'),
], [
    (1, 'Apartado 1.9: tipificar. Tipificar un dato es restarle la media y dividir entre la desviación típica.'),
    (2, 'El resultado, la puntuación z, dice cuántas desviaciones típicas está el dato por encima o por debajo de la media. Sirve para comparar datos de grupos distintos.'),
    (3, 'Ejemplo de clase: un alumno saca un 6 en un examen donde la media es 7 y la desviación 2. Su z es menos 0,5: medio punto típico por debajo de su clase.'),
    (4, 'En otro examen saca un 5, con media 4,5 y desviación 1. Su z es más 0,5.'),
    (5, 'Así que, aunque el 6 parece mejor nota, relativamente le fue mejor en el segundo examen.'),
    (6, 'En Excel, NORMALIZACION, con el dato, la media y la desviación típica.'),
]))

# ---------- 1.10 Caja ----------
S.append(Scene('1.10.', 'Atípicos y diagrama de caja', 'teo', [
    Img('t1_caja_anatomia.svg', 1250),
    F('Lᵢ = C₁ − 1,5·IQR &nbsp;&nbsp;&nbsp; Lₛ = C₃ + 1,5·IQR'),
], [
    (1, 'Apartado 1.10: los valores atípicos y el diagrama de caja. La caja va de C1 a C3, con una raya gruesa en la mediana. Los bigotes llegan hasta el dato más extremo que no es atípico, y los atípicos se dibujan como puntitos sueltos.'),
    (2, 'Un dato es atípico si está por debajo del límite inferior, C1 menos 1,5 veces el rango intercuartílico, o por encima del superior, C3 más 1,5 veces el rango intercuartílico.'),
]))
S.append(Scene('1.10.', 'Atípicos y diagrama de caja', 'mano', [
    Step(1, 'Hermanos: C₁ = 0, C₃ = 1,5 → IQR = 1,5'),
    Step(2, 'Lᵢ = 0 − 1,5·1,5 = −2,25 · Lₛ = 1,5 + 2,25 = **3,75**'),
    Step(3, 'Los valores 4 y 5 superan 3,75 → **3 atípicos** (dos personas con 4 y una con 5). El bigote de arriba llega a 3.'),
    Step(4, 'Dibujo: eje con escala → **caja** de C₁ a C₃ → raya en la **mediana** → **bigotes** → **puntos** para los atípicos.'),
    Res('Leer cajas: **dónde** está la caja (nivel) · **la raya** (mediana, asimetría) · **lo larga** que es (dispersión) · **los puntos** (atípicos).'),
], [
    (1, 'A mano, con los hermanos: C1 es 0 y C3 es 1,5, así que el rango intercuartílico es 1,5.'),
    (2, 'Los límites: abajo, 0 menos 1,5 por 1,5, menos 2,25. Arriba, 1,5 más 2,25, 3,75.'),
    (3, 'Nadie tiene menos de menos 2,25 hermanos, así que no hay atípicos por abajo. Pero 4 y 5 superan 3,75: hay 3 atípicos, dos personas con 4 hermanos y una con 5. El bigote de arriba llega hasta 3, el dato más alto que no es atípico.'),
    (4, 'Para dibujarlo: un eje con escala; la caja de C1 a C3; una raya en la mediana; los bigotes hasta los datos más extremos que no son atípicos; y los atípicos como puntitos sueltos. En Excel: Insertar, gráfico estadístico, cuadro y bigotes.'),
    (5, 'Y para leer un diagrama de caja: dónde está la caja te dice el nivel; la raya, el valor central, y si no está en medio de la caja, hay asimetría; lo larga que es la caja, la dispersión; y los puntos, los atípicos.'),
]))

# ---------- 1.11 Interpretar ----------
S.append(Scene('1.11.', 'Interpretar resultados', 'int', [
    T(['Palabra', 'Significa'], [['mean', 'Media'], ['sd', 'Cuasidesviación típica'], ['IQR', 'Rango intercuartílico'], ['0 % · 25 % · 50 % · 75 % · 100 %', 'Mín · C₁ · Me · C₃ · Máx'], ['skewness · kurtosis', 'Asimetría · curtosis']], small=True),
    Step(1, '**Qué variable** y cuántos datos.'),
    Step(2, '**Centro:** media y mediana. Si se parecen, bastante simétrica.'),
    Step(3, '**Dispersión:** desviación típica y el 50 % central (C₁ a C₃).'),
    Step(4, '**Rango, forma** (signo de asimetría y curtosis) y **atípicos**.'),
], [
    (1, 'Último apartado, el 1.11: interpretar las salidas de un programa. Los apuntes muestran resúmenes del programa R. Mean es la media; sd, la cuasidesviación; los porcentajes son el mínimo, los cuartiles y el máximo; skewness es la asimetría y kurtosis la curtosis.'),
    (2, 'Y esta es la plantilla para escribir cualquier análisis descriptivo. Primero: qué variable es y cuántos datos hay.'),
    (3, 'Segundo, el centro: la media y la mediana. Si se parecen, la distribución es bastante simétrica; si la media es mayor, hay valores altos que tiran de ella.'),
    (4, 'Tercero, la dispersión: la desviación típica, y entre qué valores está el 50 por ciento central.'),
    (5, 'Y por último, el rango, la forma, con el signo de la asimetría y de la curtosis, y los atípicos, si hay.'),
]))
S.append(Scene('1.11.', 'Interpretar resultados', 'int', [
    P('mean = 179,25 · sd = 9,42 · skewness = 0,25 · kurtosis = −0,19 · 25 % = 173,5 · 50 % = 178,5 · 75 % = 184,5 · mín 163 · máx 198 · n = 16', 's'),
    Res('Se han medido **16 personas**. La altura media es **179,25 cm** y la mediana **178,5**: al parecerse, la distribución es bastante **simétrica**. Las alturas se separan de la media unos **9,4 cm** de promedio. El **50 % central** mide entre 173,5 y 184,5 cm. Asimetría pequeña y positiva; curtosis algo negativa (algo más plana que la normal). **No hay atípicos.**'),
], [
    (1, 'Un ejemplo con las alturas. Estos son los números que da el programa.'),
    (2, 'Y esta la respuesta modelo: se han medido 16 personas. La altura media es 179,25 centímetros y la mediana 178,5; al parecerse, la distribución es bastante simétrica. Las alturas se separan de la media unos 9,4 centímetros de promedio. El 50 por ciento central mide entre 173,5 y 184,5. La asimetría es positiva pero pequeña, casi simétrica, y la curtosis algo negativa, un poco más plana que la normal. No hay atípicos.'),
]))
S.append(Scene('', '', 'title', card('Tema 1', 'Fin del Tema 1', 'Ahora: las comprobaciones de cada apartado y la **Práctica 1** de la guía.'), [
    (3, 'Y hasta aquí el Tema 1. Ahora, en la guía, haz las comprobaciones de cada apartado y los ejercicios del boletín, primero en papel. Y cuando lo tengas, las prácticas 1 a 3. Ánimo, que lo más largo del curso ya está.'),
]))

# ---------- añadidos ----------
def _find(title, kind):
    for i, s in enumerate(S):
        if s.title == title and s.kind == kind: return i
    raise KeyError(title)
S.insert(_find('La media', 'xl') + 1, Scene('1.5.', 'La suma de las desviaciones a la media', 'teo', [
    F('Σ(xᵢ − x̄) = 0'),
    P('**Justificación:** Σ(xᵢ − x̄) = Σxᵢ − n·x̄. Como x̄ = Σxᵢ ÷ n, resulta n·x̄ = Σxᵢ. Por tanto: Σxᵢ − Σxᵢ = **0**.'),
    Res('**Interpretación:** la media es el **punto de equilibrio**. Lo que unos datos están por encima se compensa exactamente con lo que otros están por debajo.'),
    P('En la hoja *Hermanos* de clase, la columna xᵢ − x̄ suma −4,2·10⁻¹⁵: es un 0 con error de redondeo del ordenador.', 's'),
], [
    (1, 'Una propiedad de la media que la profesora pide como ejercicio de «justifica e interpreta»: la suma de las desviaciones a la media siempre es 0. Es decir, si a cada dato le restas la media y sumas todo, da 0.'),
    (2, 'La justificación: la suma de equis sub i menos equis barra es la suma de los datos menos n veces la media. Pero n por la media es justo la suma de los datos, porque la media es esa suma entre n. Así que queda la suma de los datos menos la suma de los datos: 0.'),
    (3, 'Y la interpretación: la media es el punto de equilibrio de los datos. Lo que unos datos están por encima de la media se compensa exactamente con lo que otros están por debajo.'),
    (4, 'En la hoja de los hermanos de clase, esa columna suma un número rarísimo, menos 4,2 por 10 elevado a menos 15. Es un 0 con un error de redondeo del ordenador.'),
]))
