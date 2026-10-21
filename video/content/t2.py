import sys; sys.path.insert(0, '/home/claude/video')
from engine import *
TEMA = {'id': 't2', 'tab': 'Tema 2', 'color': 't2'}
S = []
TAB1 = T(['Dpto. \\ Modalidad', 'Presencial', 'Híbrido', 'Remoto', 'Total'], [['RRHH', 8, 3, 2, '**13**'], ['Finanzas', 5, 4, 1, '**10**'], ['Producción', 10, 6, 1, '**17**'], ['**Total**', '**23**', '**13**', '**4**', '**40**']])
S.append(Scene('', '', 'title', card('Tema 2', 'Análisis descriptivo de dos variables', 'Tablas de doble entrada, marginales, condicionadas e independencia'), [
    (3, 'Tema 2: el análisis descriptivo de dos variables. Ahora miramos dos características a la vez de cada persona, por ejemplo su departamento y si teletrabaja, y queremos saber si están relacionadas.'),
]))
S.append(Scene('', '', 'card', ['<h1 class="card-t" style="font-size:80px">Qué vamos a ver</h1>', toc([('2.1', 'La tabla de doble entrada'), ('2.2', 'Distribuciones marginales'), ('2.3', 'Distribuciones condicionadas'), ('2.4', 'Independencia')])], [
    (2, 'Son cuatro apartados: la tabla de doble entrada, las distribuciones marginales, las condicionadas y la independencia. ¿En unos departamentos se teletrabaja más que en otros, o da igual el departamento? Eso es lo que vamos a aprender a contestar.'),
]))
# 2.1
S.append(Scene('2.1.', 'La tabla de doble entrada', 'teo', [
    P('**Filas** = valores de X · **Columnas** = valores de Y · cada casilla = **nᵢⱼ**, la frecuencia **conjunta**.'),
    TAB1,
    Res('«**8** empleados son de RRHH **y** trabajan en presencial.»'),
    Li('Alguna cualitativa → **tabla de contingencia**. Las dos cuantitativas → **tabla de correlación**.'),
    Li('**Frecuencia relativa conjunta:** fᵢⱼ = nᵢⱼ ÷ n. 8 ÷ 40 = **0,20**.'),
], [
    (1, 'Apartado 2.1: la tabla de doble entrada. Es una tabla de frecuencias con filas para los valores de una variable y columnas para los de la otra. En cada casilla va el número de personas que tienen a la vez ese valor de las dos. Se llama frecuencia conjunta.'),
    (2, 'Ejemplo de clase: 40 empleados según su departamento y su modalidad de trabajo.'),
    (3, 'Cómo se lee una casilla: 8 empleados son de Recursos Humanos y, a la vez, trabajan en presencial.'),
    (4, 'Si alguna de las variables es cualitativa, se llama tabla de contingencia. Si las dos son cuantitativas, tabla de correlación.'),
    (5, 'Y la frecuencia relativa conjunta es cada casilla dividida entre el total: 8 entre 40, 0,20. El 20 por ciento de los empleados son de Recursos Humanos y presenciales.'),
]))
S.append(Scene('2.1.', 'La tabla de doble entrada', 'mano', [
    Step(1, 'Dibuja la cuadrícula: una **fila** por valor de X, una **columna** por valor de Y, y una más para los totales.'),
    Step(2, 'Recorre los datos **persona a persona** y pon un **palote** donde se cruzan su X y su Y.'),
    Step(3, 'Cuenta los palotes: son las **nᵢⱼ**.'),
    Step(4, 'Suma cada fila y cada columna. **Comprobación:** los dos totales dan **n**.'),
], [
    (1, 'A mano: dibuja una cuadrícula con una fila por cada valor de X y una columna por cada valor de Y. Deja una fila y una columna más para los totales.'),
    (2, 'Recorre los datos persona a persona. Para cada una, mira su X y su Y y pon un palote en la casilla donde se cruzan.'),
    (3, 'Cuenta los palotes de cada casilla: esas son las frecuencias conjuntas.'),
    (4, 'Suma cada fila y cada columna. La comprobación: la suma de los totales de las filas y la de los totales de las columnas tienen que dar lo mismo, n.'),
]))
S.append(Scene('2.1.', 'La tabla de doble entrada', 'xl', [
    Step(1, 'Datos en dos columnas con título, una fila por persona.'),
    Step(2, '**Insertar → Tabla dinámica**.'),
    Step(3, 'Departamento a **Filas**, Modalidad a **Columnas**.'),
    Step(4, 'Departamento otra vez a **Valores** → «Cuenta de…» = las nᵢⱼ.'),
    Step(5, 'Relativas: clic derecho → **Mostrar valores como → % del total general**.'),
], [
    (1, 'En Excel se hace con una tabla dinámica. Ten los datos en dos columnas con título, una fila por persona.'),
    (2, 'Haz clic en los datos y ve a Insertar, Tabla dinámica.'),
    (3, 'Arrastra Departamento a Filas y Modalidad a Columnas.'),
    (4, 'Arrastra Departamento otra vez a Valores. Saldrá «Cuenta de Departamento»: esas son las frecuencias conjuntas.'),
    (5, 'Para las relativas: clic derecho en un número, Mostrar valores como, por ciento del total general. Un truco visual de clase: formato condicional con escala de colores, para ver de un vistazo dónde se concentra la gente.'),
]))
# 2.2
S.append(Scene('2.2.', 'Distribuciones marginales', 'teo', [
    P('La distribución de **una sola** variable, olvidando la otra: son los **totales** de los márgenes.'),
    TAB1,
    Li('Marginal de X (departamento): **13 · 10 · 17** (columna Total).'),
    Li('Marginal de Y (modalidad): **23 · 13 · 4** (fila Total).'),
    Res('Una marginal es una tabla de frecuencias normal: se le aplica **todo el Tema 1**.'),
], [
    (1, 'Apartado 2.2: las distribuciones marginales. Son la distribución de una sola de las dos variables, olvidándote de la otra. Están en los márgenes de la tabla: son los totales.'),
    (2, 'En nuestra tabla.'),
    (3, 'La marginal del departamento es la columna de totales: 13, 10 y 17.'),
    (4, 'Y la de la modalidad, la fila de totales: 23, 13 y 4.'),
    (5, 'Una marginal es una tabla de frecuencias normal y corriente, así que se le aplica todo el Tema 1: media, mediana, moda, varianza.'),
]))
S.append(Scene('2.2.', 'Distribuciones marginales', 'mano', [
    P('X = días de ausencia (marginal de una tabla de los apuntes):', 's'),
    T(['xᵢ', 'nᵢ.', 'xᵢ·nᵢ.', 'xᵢ²·nᵢ.'], [[1, 6, 6, 6], [2, 10, 20, 40], [3, 8, 24, 72], [4, 8, 32, 128], ['**Σ**', '**32**', '**82**', '**246**']], small=True),
    Step(1, 'x̄ = 82 ÷ 32 = **2,5625 días**'),
    Step(2, 'S² = 246 ÷ 32 − 2,5625² = 7,6875 − 6,5664 = **1,121**'),
], [
    (1, 'A mano, la media de una marginal. Ejemplo de los apuntes: X son los días de ausencia.'),
    (2, 'La columna de totales hace de frecuencia. Montas la tabla del Tema 1: valor por frecuencia y valor al cuadrado por frecuencia.'),
    (3, 'La media: 82 entre 32, 2,5625 días.'),
    (4, 'Y la varianza: 246 entre 32, menos la media al cuadrado: 1,121.'),
]))
# 2.3
S.append(Scene('2.3.', 'Distribuciones condicionadas', 'teo', [
    P('La distribución de una variable **solo para un grupo** de la otra. Se escribe con **|** («sabiendo que»).'),
    Li('**Y | X = Producción** → la **fila** de Producción: 10, 6, 1 (total 17).'),
    Li('**X | Y = Presencial** → la **columna** de Presencial: 8, 5, 10 (total 23).'),
    Res('Para comparar, en **% dentro del grupo**: de los 17 de Producción, 10 ÷ 17 = **58,8 %** son presenciales.'),
    Truco('Lo que va **detrás** de la «|» es el grupo. Tapa con la mano el resto de la tabla.'),
], [
    (1, 'Apartado 2.3: las distribuciones condicionadas. Son la distribución de una variable solo para un grupo definido por la otra. Se escriben con una barra vertical, que se lee «sabiendo que».'),
    (2, 'Y condicionada a que X sea Producción es la fila de Producción: 10 presenciales, 6 híbridos y 1 en remoto, de 17 personas.'),
    (3, 'Y X condicionada a que Y sea presencial es la columna de presencial: 8, 5 y 10, de 23 personas.'),
    (4, 'Para comparar grupos se pasan a porcentaje dentro del grupo, dividiendo entre el total de esa fila o columna: de los 17 de Producción, 10 entre 17, el 58,8 por ciento, son presenciales.'),
    (5, 'El truco: lo que va detrás de la barra es el grupo al que te restringes. Tapa con la mano todo lo demás de la tabla y quédate con esa fila o columna.'),
]))
S.append(Scene('2.3.', 'Distribuciones condicionadas', 'mano', [
    T(['X \\ Y', '2', '3', '5', 'Total'], [[1, 1, 3, 2, 6], [2, 4, 1, 5, 10], [3, 3, 3, 2, 8], [4, 1, 4, 3, 8]], hl_row=[1, 2], small=True),
    Step(1, '**Y | X ∈ {2, 3}**: **suma** las filas del 2 y del 3 → 7 · 4 · 7 (total 18).'),
    Step(2, 'fⱼ = 7/18 = 0,389 · 4/18 = 0,222 · 7/18 = 0,389'),
    Step(3, 'ȳ = (2·7 + 3·4 + 5·7) ÷ 18 = 61 ÷ 18 = **3,39 días**'),
    Ojo('Se divide entre **su** total (18), no entre n = 32.'),
    XL('=B2/$E2', 'Y | X: % de la fila (en la tabla dinámica, «% del total de filas»)'),
], [
    (1, 'Y si te piden condicionar a varios valores, sumas esas filas. Ejercicio de los apuntes: X son días de ausencia e Y días de asuntos propios.'),
    (2, 'Y condicionada a que X valga 2 o 3: sumas las filas del 2 y del 3. Sale 7, 4 y 7, con un total de 18.'),
    (3, 'Sus frecuencias relativas, dividiendo entre 18: 0,389, 0,222 y 0,389.'),
    (4, 'Y su media: 2 por 7, más 3 por 4, más 5 por 7, entre 18. Da 3,39 días de asuntos propios entre los que faltan 2 o 3 días.'),
    (5, 'Cuidado: se divide entre el total del grupo, 18, no entre el total de la tabla, 32.'),
    (6, 'En Excel, cada casilla entre el total de su fila, con el dólar delante de la columna del total. En la tabla dinámica es Mostrar valores como, por ciento del total de filas.'),
]))
# 2.4
S.append(Scene('2.4.', 'Independencia', 'teo', [
    P('X e Y son **independientes** si saber una **no dice nada** de la otra.'),
    F('fᵢⱼ = fᵢ. · f.ⱼ &nbsp;&nbsp;en **todas** las casillas'),
    P('Lo mismo: los **porcentajes por filas** son iguales en todas las filas.', 's'),
    Step(1, 'Una casilla: fᵢⱼ = nᵢⱼ ÷ n.'),
    Step(2, 'Su producto de marginales: (nᵢ. ÷ n) · (n.ⱼ ÷ n).'),
    Step(3, '**Alguna** no coincide → **dependientes**. Para decir que sí, **todas**.'),
], [
    (1, 'Apartado 2.4: la independencia. Dos variables son independientes si saber el valor de una no te dice nada de la otra. Si el porcentaje de presenciales fuera el mismo en todos los departamentos, la modalidad no dependería del departamento.'),
    (2, 'Matemáticamente: la frecuencia relativa de cada casilla tiene que ser igual al producto de las marginales de su fila y su columna, en todas las casillas.'),
    (3, 'Es lo mismo que decir que los porcentajes por filas son iguales en todas las filas. Por eso lo más fácil, muchas veces, es mirar los porcentajes.'),
    (4, 'La receta: calcula la frecuencia relativa de una casilla.'),
    (5, 'Calcula el producto de sus marginales: el total de su fila entre n, por el total de su columna entre n.'),
    (6, 'Si alguna casilla no cumple la igualdad, no son independientes: basta con una. Para decir que sí lo son, tiene que cumplirse en todas.'),
]))
S.append(Scene('2.4.', 'Independencia', 'mano', [
    F('esperada = ' + frac('nᵢ. · n.ⱼ', 'n')),
    Step(1, 'Departamento y modalidad, casilla RRHH–Presencial: 13 · 23 ÷ 40 = **7,475**. En la tabla hay **8** → **no son independientes**.'),
    T(['Sexo \\ Contrato', 'Indefinido', 'Temporal', 'Parcial', 'Total'], [['Hombre', 90, 60, 30, 180], ['Mujer', 30, 20, 10, 60], ['Total', 120, 80, 40, 240]], small=True),
    Step(2, 'Hombre–Indefinido: 180 · 120 ÷ 240 = **90** = 90 ✔. Las seis casillas coinciden → **independientes**.'),
    Ojo('Atajo: una casilla con **0** cuya fila y columna no suman 0 → seguro que **no** son independientes.'),
    XL('=$E3*B$6', 'tabla «si fueran independientes», y comparas'),
], [
    (1, 'A mano hay una forma equivalente con números más cómodos: la frecuencia esperada si fueran independientes. Es el total de la fila por el total de la columna, entre n.'),
    (2, 'En departamento y modalidad, la casilla Recursos Humanos y presencial: 13 por 23 entre 40, 7,475. Pero en la tabla hay 8. No coinciden, así que no son independientes.'),
    (3, 'Otro ejemplo de clase: sexo y tipo de contrato, 240 empleados.'),
    (4, 'Hombre e indefinido: 180 por 120 entre 240, 90. Y en la tabla hay 90. Si lo repites en las seis casillas, coinciden todas: son independientes. El tipo de contrato no depende del sexo.'),
    (5, 'Un atajo: si hay una casilla con 0 pero su fila y su columna no suman 0, ya no pueden ser independientes.'),
    (6, 'En Excel se hace la tabla de lo que habría si fueran independientes, con los dólares a medias: dólar E fija la columna de totales de fila, y dólar 6 la fila de totales de columna. Luego comparas casilla a casilla.'),
]))
S.append(Scene('', '', 'title', card('Tema 2', 'Fin del Tema 2', 'Ahora: las comprobaciones, el boletín (ejercicios 15 a 18) y la **Práctica 4**.'), [
    (3, 'Y hasta aquí el Tema 2. En la guía tienes las comprobaciones, los ejercicios 15 a 18 del boletín y la práctica 4. Hazlos primero en papel.'),
]))

def _find(title, kind):
    for i, s in enumerate(S):
        if s.title == title and s.kind == kind: return i
    raise KeyError(title)
S.insert(_find('La tabla de doble entrada', 'xl') + 1, Scene('2.1.', 'Gráficos para dos variables', 'teo', [
    Li('**Barras agrupadas:** para cada departamento, una barra por modalidad, una al lado de otra.'),
    Li('**Barras apiladas:** una barra por departamento, partida en trozos por modalidad.'),
    Li('**Mosaico:** rectángulos de tamaño proporcional a la frecuencia; para **dos cualitativas**.'),
    XL('Insertar → Columnas → Columna 100 % apilada', 'imita el mosaico'),
    Truco('La barra **100 % apilada** muestra justo las **distribuciones condicionadas**: cada barra suma 100 %.'),
], [
    (1, 'Antes de seguir, los gráficos para dos variables. El más usado es el diagrama de barras agrupadas: para cada departamento, una barra por cada modalidad, una al lado de otra.'),
    (2, 'O barras apiladas: una sola barra por departamento, partida en trozos, uno por modalidad.'),
    (3, 'El gráfico de mosaico usa rectángulos de tamaño proporcional a la frecuencia. Se usa con dos variables cualitativas.'),
    (4, 'Excel no tiene mosaico, pero se puede imitar con un gráfico de columnas al 100 por ciento apiladas.'),
    (5, 'Ese gráfico tiene una ventaja: cada barra suma 100 por ciento, así que muestra justo las distribuciones condicionadas, que vemos en el apartado 2.3.'),
]))
S.insert(_find('Gráficos para dos variables', 'teo') + 1, Scene('2.1.', 'Gráficos para dos variables', 'mano', [
    Step(1, 'Eje horizontal: los **departamentos**. Vertical: la **frecuencia** (de 0 a 10).'),
    Step(2, 'Sobre cada departamento, **una barra por modalidad**, pegadas entre sí. RRHH: 8 · 3 · 2.'),
    Step(3, 'Un **color o rayado** por modalidad, y una **leyenda**.'),
    Step(4, 'Para el 100 % apilado: cada barra mide 100 %, partida según los % de su fila. RRHH: 61,5 % · 23,1 % · 15,4 %.'),
], [
    (1, 'En papel: en el eje horizontal, los departamentos; en el vertical, la frecuencia, de 0 a 10.'),
    (2, 'Sobre cada departamento dibujas una barra por modalidad, pegadas entre sí. Para Recursos Humanos: 8, 3 y 2.'),
    (3, 'Cada modalidad con un color o un rayado distinto, y una leyenda que diga cuál es cuál.'),
    (4, 'Y para el de 100 por ciento apilado: todas las barras miden lo mismo, el 100 por ciento, y se parten según los porcentajes de su fila. Recursos Humanos: 61,5, 23,1 y 15,4 por ciento.'),
]))
