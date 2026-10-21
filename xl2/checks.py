"""Comprobaciones de cada apartado de la guía (se corrigen en la página)."""
import json, math


def num(q, ans, dec=2, alts=(), explain='', kind='num', data=None):
    tol = max(0.5 * 10 ** (-dec) * 1.02, abs(ans) * 0.001)
    return {'type': kind, 'q': q, 'ans': ans, 'tol': tol, 'dec': dec, 'alts': [[a, h] for a, h in alts], 'explain': explain, 'data': data}


def pct(q, ans, dec=3, alts=(), explain='', data=None):
    return num(q, ans, dec, alts, explain, 'pct', data)


def mc(q, opts, ok, explain='', why=None, data=None):
    """why: dict índice_opción_errónea -> pista"""
    return {'type': 'mc', 'q': q, 'opts': opts, 'ok': ok, 'explain': explain, 'why': {str(k): v for k, v in (why or {}).items()}, 'data': data}


TAB = 'Valores 0, 1, 2 y 3 con frecuencias 5, 8, 4 y 3 (n = 20).'
CT = 'Tabla: Hombres: teletrabajan 10, no 5. Mujeres: teletrabajan 15, no 20. Total n = 50.'

C = {
# ---------------- Parte 0
'el-orden-de-las-operaciones': [
    num('¿Cuánto da 3 + 2 × 5?', 13, 0, [(25, 'Primero se multiplica (2 × 5 = 10) y después se suma el 3.')], 'La multiplicación va antes que la suma: 3 + 10 = 13.'),
    mc('Quieres la media de las celdas A1 y A2. ¿Qué escribes?', ['=A1+A2/2', '=(A1+A2)/2', '=A1+(A2/2)'], 1,
       'El paréntesis hace que primero se sume y después se divida.', {0: 'Sin paréntesis, Excel divide solo A2 entre 2.', 2: 'Así divides solo A2 entre 2.'}),
],
'decimales-y-redondeo': [
    num('Redondea 2,4761 a dos decimales.', 2.48, 2, [(2.47, 'La tercera cifra es un 6: la segunda sube uno.')], 'La tercera cifra decimal (6) es 5 o más, así que 2,47 pasa a 2,48.'),
    mc('¿Cuándo conviene redondear en un ejercicio?', ['En cada paso', 'Solo al final', 'Nunca'], 1, 'Si redondeas a mitad, el resultado final se desvía. Deja que Excel trabaje con todos los decimales.'),
],
'fracciones-y-divisiones': [
    num('9 de 36 personas tienen coche. ¿Qué proporción es (en decimal)?', 0.25, 2, [(4, 'Está al revés: es 9 ÷ 36, la parte entre el total.')], '9 ÷ 36 = 0,25.'),
],
'porcentajes': [
    num('Un salario sube un 5 %. ¿Por qué número lo multiplicas?', 1.05, 2, [(0.05, 'Así te quedarías solo con el 5 %. Subir un 5 % es multiplicar por 1 + 0,05.'), (5, 'Los porcentajes en las fórmulas van en decimal: 5 % = 0,05.')], 'Subir un 5 % = multiplicar por 1,05.'),
    num('¿Y si baja un 3 %?', 0.97, 2, [(1.03, 'Eso sería subir. Bajar un 3 % es 1 − 0,03.')], 'Bajar un 3 % = multiplicar por 0,97.'),
],
'potencias-el-al-cuadrado': [
    num('¿Cuánto es (−4)²?', 16, 0, [(-16, 'Negativo por negativo da positivo: (−4)·(−4) = 16.'), (-8, 'Elevar al cuadrado no es multiplicar por 2.')], '(−4) × (−4) = 16.'),
    mc('¿Cómo escribes 3 al cuadrado en Excel?', ['=3^2', '=3*2', '=3²'], 0, 'El símbolo ^ es la potencia.', {1: 'Eso es 3 por 2 = 6.'}),
],
'raíz-cuadrada': [
    num('¿Cuánto es la raíz cuadrada de 81?', 9, 0, [(40.5, 'La raíz no es la mitad: es el número que multiplicado por sí mismo da 81.')], '9 × 9 = 81.'),
    mc('Raíz cúbica de 27 en Excel:', ['=27^(1/3)', '=27^1/3', '=RAIZ(27)'], 0, 'Las raíces se escriben como potencia con el exponente entre paréntesis.', {1: 'Sin paréntesis Excel hace 27¹ ÷ 3 = 9.', 2: 'RAIZ es solo la raíz cuadrada.'}),
],
'el-símbolo-σ-sumatorio': [
    num('Valores 2, 4 y 6 con frecuencias 1, 3 y 2. ¿Cuánto es Σxᵢ·nᵢ?', 26, 0, [(12, 'Esa es la suma de los valores. Multiplica cada valor por su frecuencia y suma.'), (6, 'Esa es la suma de las frecuencias.')], '2·1 + 4·3 + 6·2 = 2 + 12 + 12 = 26.'),
],
'los-subíndices': [
    mc('Si los datos son 7, 3, 9, 4, ¿qué es x₃?', ['3', '9', 'El número 3 multiplicado por x'], 1, 'El subíndice solo numera: x₃ es el tercer dato.'),
],
'los-intervalos-y-sus-corchetes': [
    mc('¿Entra el 20 en el intervalo (10, 20]?', ['Sí', 'No'], 0, 'El corchete ] indica que el 20 sí entra.'),
    num('Marca de clase de (40, 60]:', 50, 0, [(20, 'Eso es la amplitud. La marca es el punto medio.')], '(40 + 60) ÷ 2 = 50.'),
    num('Amplitud de [15, 25):', 10, 0, [(20, 'Esa es la marca de clase.')], '25 − 15 = 10.'),
],
'lo-básico-de-una-hoja': [
    mc('¿Qué celdas abarca B2:B5?', ['Solo B2 y B5', 'B2, B3, B4 y B5', 'B2 y C5'], 1, 'Los dos puntos significan "desde… hasta".'),
],
'escribir-una-fórmula': [
    mc('En Excel en español, ¿con qué se separan las partes de una función?', ['Coma ( , )', 'Punto y coma ( ; )', 'Punto ( . )'], 1, 'La coma es el decimal, por eso se usa el punto y coma.'),
],
'arrastrar-una-fórmula-copiar-hacia-abajo': [
    mc('En C2 escribes =B2*2 y arrastras hasta C5. ¿Qué hay en C5?', ['=B2*2', '=B5*2', '=B5*5'], 1, 'Al arrastrar, la fila cambia sola.'),
],
'fijar-una-celda-con-referencia-absoluta': [
    mc('Quieres dividir cada frecuencia entre el total, que está en B9. En la primera fila escribes…', ['=B2/B9', '=B2/$B$9', '=$B$2/B9'], 1, 'Se fija el total para que no se mueva al arrastrar.', {0: 'Al arrastrar, B9 pasaría a B10, B11… y daría error.', 2: 'Has fijado la celda equivocada.'}),
],
'las-funciones-que-vas-a-usar': [
    mc('¿Qué función da la varianza que se usa en clase?', ['VAR.S', 'VAR.P', 'DESVEST.P'], 1, '.P divide entre n, como en clase.', {0: 'VAR.S es la cuasivarianza.', 2: 'DESVEST.P es la desviación típica (la raíz de la varianza).'}),
    mc('¿Y la cuasivarianza?', ['VAR.S', 'VAR.P', 'DESVEST.S'], 0, '.S divide entre n − 1.'),
],
'insertar-un-gráfico': [
    mc('¿Qué gráfico usas para un salario agrupado en intervalos?', ['Sectores', 'Histograma', 'Barras separadas'], 1, 'Variable continua en intervalos → histograma (barras que se tocan).'),
],
'tabla-dinámica-para-contar-por-categorías': [
    mc('Arrastras "Departamento" a Valores y sale "Suma de Departamento". ¿Qué haces?', ['Nada, está bien', 'Configuración de campo de valor → Cuenta', 'Borrar la tabla'], 1, 'Para contar personas hay que elegir Cuenta.'),
],
# ---------------- Tema 1
'vocabulario-básico': [
    mc('Una empresa tiene 3000 empleados y se encuesta a 200. Esos 200 son…', ['La población', 'La muestra', 'Un parámetro'], 1, 'La muestra es el trozo que se estudia.'),
    mc('La media de salario de los 3000 empleados es un…', ['Parámetro', 'Estadístico'], 0, 'Parámetro → población. Estadístico → muestra.'),
],
'tipos-de-variables': [
    mc('Número de hijos:', ['Cuantitativa discreta', 'Cuantitativa continua', 'Cualitativa ordinal'], 0, 'Es un número que se cuenta.'),
    mc('Nivel de estudios (primaria, secundaria, universidad):', ['Cualitativa nominal', 'Cualitativa ordinal', 'Cuantitativa discreta'], 1, 'Son palabras con un orden natural.'),
    mc('Salario mensual:', ['Cuantitativa discreta', 'Cuantitativa continua', 'Cualitativa'], 1, 'Se mide en euros y puede tener decimales.'),
],
'la-tabla-de-frecuencias': [
    num('¿Cuál es la frecuencia relativa del valor 1?', 0.4, 2, [(8, 'Esa es la absoluta. La relativa es 8 ÷ 20.')], '8 ÷ 20 = 0,4.', data=TAB),
    num('¿Cuál es la frecuencia acumulada Nᵢ del valor 2?', 17, 0, [(4, 'Esa es su frecuencia. La acumulada suma desde arriba: 5 + 8 + 4.')], '5 + 8 + 4 = 17.', data=TAB),
],
'gráficos': [
    num('Un intervalo (10, 30] tiene 20 datos. ¿Qué densidad tiene?', 1, 2, [(20, 'Esa es la frecuencia. La densidad es frecuencia ÷ amplitud (20 ÷ 20).')], 'Amplitud 20, frecuencia 20 → densidad 1.'),
    mc('¿Cuándo hay que usar densidades en un histograma?', ['Siempre', 'Cuando los intervalos tienen distinta amplitud', 'Nunca'], 1, 'Si todos miden lo mismo, la frecuencia ya sirve como altura.'),
],
'medidas-de-posición-central-media-mediana-y-moda': [
    num('Media:', 1.25, 2, [(1.5, 'Has hecho la media de los valores 0, 1, 2 y 3. Cada valor cuenta tantas veces como se repite.')], '(0·5 + 1·8 + 2·4 + 3·3) ÷ 20 = 25 ÷ 20 = 1,25.', data=TAB),
    num('Mediana:', 1, 2, [(1.5, 'n/2 = 10. Mira las acumuladas: 5, 13… La primera que llega a 10 es la del valor 1.')], 'Acumuladas 5, 13, 17, 20. La primera ≥ 10 es 13 → mediana 1.', data=TAB),
    mc('Para describir los salarios de una empresa donde el director cobra muchísimo, ¿qué es mejor?', ['La media', 'La mediana'], 1, 'La mediana no se deja arrastrar por valores extremos.'),
],
'cuantiles-cuartiles-deciles-y-percentiles': [
    mc('Estar en el percentil 90 de salario significa que…', ['Ganas el 90 % del salario medio', 'El 90 % gana lo mismo o menos que tú', 'El 90 % gana más que tú'], 1, 'Solo el 10 % gana más.'),
    num('Intervalos [0, 10] con 10 datos, (10, 20] con 30 y (20, 30] con 10 (n = 50). ¿Tercer cuartil?', 19.17, 2,
        [(20, 'Ese es el extremo del intervalo. Aplica la fórmula: Linf + (3n/4 − Nᵢ₋₁)/nᵢ · aᵢ.')], '3n/4 = 37,5 → intervalo (10, 20]: 10 + (37,5 − 10)/30 · 10 = 19,17.'),
],
'medidas-de-dispersión': [
    num('Datos 2, 4, 6 y 8. ¿Varianza (la de clase)?', 5, 2, [(20 / 3, 'Esa es la cuasivarianza (divide entre n − 1).'), (30, 'Te falta restar la media al cuadrado (30 − 25).')], 'Media 5. Σx²/n = 120/4 = 30. 30 − 25 = 5.'),
    mc('Grupo A: media 1000 € y desviación 100 €. Grupo B: media 50 € y desviación 10 €. ¿Cuál es más homogéneo?', ['A', 'B', 'Iguales'], 0, 'CV de A = 0,10; CV de B = 0,20. Menor CV = más homogéneo.', {1: 'Su desviación es menor, pero su media también: compara el CV.'}),
    num('Dos grupos de 10 personas con medias 20 y 30. ¿Media global?', 25, 2, explain='Mismo tamaño: (20·10 + 30·10) ÷ 20 = 25.'),
    mc('Si todos los salarios suben 100 €, la varianza…', ['Sube 100', 'No cambia', 'Se multiplica por 100'], 1, 'Sumar lo mismo a todos no los separa más.'),
],
'medidas-de-forma-asimetría-y-curtosis': [
    mc('Media 2400 € y mediana 1900 €. La distribución tiene…', ['Asimetría positiva', 'Asimetría negativa', 'Simetría'], 0, 'Algunos salarios muy altos tiran de la media hacia arriba: cola a la derecha.'),
    mc('Curtosis = −0,8. La distribución es…', ['Leptocúrtica', 'Mesocúrtica', 'Platicúrtica'], 2, 'Negativa → más aplanada que la normal.'),
],
'tipificar-estandarizar-una-variable': [
    num('Sacas un 8; la media es 6 y la desviación típica 2. ¿Cuánto vale z?', 1, 2, [(2, 'Divide la diferencia (8 − 6) entre la desviación (2).')], '(8 − 6) ÷ 2 = 1.'),
],
'valores-atípicos-y-diagrama-de-caja-boxplot': [
    num('C₁ = 10 y C₃ = 20. ¿Límite superior para atípicos?', 35, 2, [(30, 'Es C₃ + 1,5 × IQR = 20 + 15.'), (50, 'Se suma a C₃, no se multiplica.')], 'IQR = 10. 20 + 1,5·10 = 35.'),
    mc('Con esos datos, ¿es atípico un 34?', ['Sí', 'No'], 1, 'Solo es atípico si supera 35.'),
],
'interpretar-las-salidas-de-un-programa': [
    mc('En las salidas de R de los apuntes, "sd" es…', ['La varianza', 'La desviación típica (dividiendo entre n)', 'La cuasidesviación típica (dividiendo entre n − 1)'], 2, 'R da la cuasidesviación.'),
    mc('En esas salidas, 0 % y 100 % son…', ['El mínimo y el máximo', 'La media y la mediana'], 0, ''),
],
# ---------------- Tema 2
'la-tabla-de-doble-entrada': [
    num('¿Cuánto vale f₁₁ (hombres que teletrabajan entre el total)?', 0.2, 3, [(10, 'Esa es la frecuencia absoluta. Divide entre n = 50.')], '10 ÷ 50 = 0,2.', data=CT),
],
'distribuciones-marginales': [
    num('Distribución marginal: ¿cuántas personas teletrabajan en total?', 25, 0, [(10, 'Esos son solo los hombres. Suma toda la columna.')], '10 + 15 = 25.', data=CT),
],
'distribuciones-condicionadas': [
    pct('De las mujeres, ¿qué proporción teletrabaja?', 15 / 35, 3, [(0.3, 'En una condicionada se divide entre el total de la fila (35 mujeres), no entre n.'), (0.6, 'Eso es "de los que teletrabajan, cuántos son mujeres": has dividido entre la columna.')], '15 ÷ 35 = 0,429.', data=CT),
],
'independencia': [
    pct('¿Cuánto vale f₁. × f.₁ (lo que habría si fueran independientes)?', 0.15, 3, explain='(15/50) × (25/50) = 0,3 × 0,5 = 0,15.', data=CT),
    mc('Como f₁₁ = 0,20 y f₁.·f.₁ = 0,15, sexo y teletrabajo…', ['Son independientes', 'No son independientes'], 1, 'Basta una casilla que no cumpla la igualdad.'),
],
# ---------------- Tema 3
'la-nube-de-puntos-diagrama-de-dispersión': [
    mc('Una nube de puntos que baja hacia la derecha indica…', ['Relación directa', 'Relación inversa', 'Ninguna relación'], 1, 'Cuando X sube, Y baja.'),
],
'la-covarianza': [
    mc('Covarianza = −35. La relación es…', ['Directa', 'Inversa', 'Muy fuerte'], 1, 'Solo se mira el signo.', {2: 'El valor de la covarianza no dice la fuerza; para eso está r.'}),
],
'la-recta-de-regresión': [
    num('x̄ = 10, ȳ = 50, Sx² = 4, Sxy = 6. ¿Pendiente b?', 1.5, 2, [(3, 'b = Sxy ÷ Sx² (la varianza, 4), no entre Sx (2).')], '6 ÷ 4 = 1,5.'),
    num('¿Y el término independiente a?', 35, 2, [(65, 'a = ȳ − b·x̄: se resta.')], '50 − 1,5·10 = 35.'),
],
'coeficiente-de-correlación-r-y-de-determinación-r²': [
    pct('r = −0,8. ¿Cuánto vale R²?', 0.64, 2, [(-0.64, 'Un cuadrado nunca es negativo.')], '(−0,8)² = 0,64.'),
    mc('R² = 0,64 significa que…', ['La recta acierta el 64 % de las veces', 'El 64 % de la variabilidad de Y se explica por X', 'r = 0,64'], 1, ''),
],
'predicciones': [
    num('Recta Ŷ = 35 + 1,5X. ¿Predicción para X = 12?', 53, 2, explain='35 + 18 = 53.'),
    mc('Los datos de X van de 1 a 20. ¿Es fiable predecir para X = 200?', ['Sí, si R² es alto', 'No, está muy fuera del rango de los datos'], 1, 'Fuera del rango no sabemos si la relación sigue siendo una recta.'),
],
'fórmulas-útiles-para-ejercicios-sin-datos': [
    num('b = 2, Sx = 3 y Sy = 10. ¿Cuánto vale r?', 0.6, 2, [(2 * 9 / 100, 'r = b · Sx / Sy usa desviaciones, no varianzas.')], 'r = 2 · 3 ÷ 10 = 0,6.'),
    num('r = 0,5, Sx = 4 y Sy = 6. ¿Covarianza Sxy?', 12, 2, explain='Sxy = r · Sx · Sy = 0,5 · 4 · 6 = 12.'),
],
# ---------------- Tema 4
'índice-simple': [
    num('Un precio pasa de 80 € (2020) a 92 € (2025). ¿Índice de 2025 con base 2020?', 115, 2, [(1.15, 'Multiplica por 100.'), (86.96, 'Está al revés: 92 ÷ 80.')], '92 ÷ 80 × 100 = 115.'),
    mc('Un índice de 96 significa que…', ['Subió un 96 %', 'Bajó un 4 %', 'Bajó un 96 %'], 1, '96 − 100 = −4.'),
],
'tasa-de-variación': [
    pct('Un valor baja de 250 a 200. ¿Tasa de variación (en decimal)?', -0.2, 3, [(0.2, 'Fíjate en el signo: ha bajado.'), (-0.25, 'Se divide entre el valor INICIAL (250).')], '200 ÷ 250 − 1 = −0,2.'),
],
'propiedades-de-los-índices': [
    num('Algo sube un 10 % y luego baja un 10 %. ¿Índice final (inicio = 100)?', 99, 2, [(100, 'Los porcentajes no se compensan: 100 × 1,10 × 0,90.')], '100 × 1,10 × 0,90 = 99.'),
],
'cambio-de-base': [
    num('Con base 2015, 2019 vale 125 y 2022 vale 150. ¿Índice de 2022 con base 2019?', 120, 2, [(125, 'Divide entre el índice del nuevo año base: 150 ÷ 125 × 100.'), (25, 'No se restan: se divide.')], '150 ÷ 125 × 100 = 120.'),
],
'media-geométrica-y-tasas-medias': [
    pct('Crecimientos del 20 % y del 5 % en dos años. ¿Tasa media anual?', math.sqrt(1.2 * 1.05) - 1, 4, [(0.125, 'Esa es la media aritmética. Usa la geométrica: √(1,20 · 1,05) − 1.')], '√1,26 − 1 = 0,1225 (12,25 %).'),
    pct('Una tasa anual del 12 %, ¿qué tasa mensual equivale?', 1.12 ** (1 / 12) - 1, 5, [(0.01, 'No se divide entre 12: (1,12)^(1/12) − 1.')], '1,12^(1/12) − 1 = 0,00949.'),
],
'índices-complejos-de-varios-productos': [
    num('Producto A: p₀ = 2, q₀ = 10, pₜ = 3. Producto B: p₀ = 5, q₀ = 4, pₜ = 5. ¿Índice de Laspeyres?', 125, 2, [(80, 'Está al revés: arriba van los precios actuales.')], '(3·10 + 5·4) ÷ (2·10 + 5·4) × 100 = 50 ÷ 40 × 100 = 125.'),
    mc('El índice de Paasche usa las cantidades…', ['Del año base', 'Del año actual'], 1, 'Laspeyres: año base. Paasche: actuales.'),
],
'deflactar-de-euros-nominales-a-euros-reales': [
    num('Un salario de 1500 € con IPC 120 (base 100). ¿Salario real?', 1250, 2, [(1800, 'Para deflactar se DIVIDE entre el IPC.')], '1500 ÷ 120 × 100 = 1250.'),
    mc('El salario sube un 3 % y los precios un 5 %. El poder adquisitivo…', ['Sube', 'Baja', 'No cambia'], 1, 'Los precios suben más que el salario.'),
],
'aplicaciones-el-ipc-y-el-ibex-35': [
    mc('El IPC es un índice tipo…', ['Paasche', 'Laspeyres encadenado', 'Fisher'], 1, ''),
],
}
json.dump(C, open('/home/claude/xl2/checks.json', 'w'), ensure_ascii=False)
print(len(C), sum(len(v) for v in C.values()))
