"""Generadores de ejercicios autocorregidos (8 tipos, 3 niveles)."""
import numpy as np, math

NIV = {1: 'Nivel 1 · Con guía', 2: 'Nivel 2 · Con cabeceras', 3: 'Nivel 3 · Sin ayuda'}


def pct_rank_manual(vals, cnts, p):
    """cuantil con la receta de clase (datos no agrupados)"""
    n = sum(cnts); t = p * n; N = 0
    for i, c in enumerate(cnts):
        N += c
        if N > t + 1e-9:
            return vals[i]
        if abs(N - t) < 1e-9:
            return (vals[i] + vals[i + 1]) / 2
    return vals[-1]


def gq(L, n, p):
    N = np.cumsum(n); t = p * sum(n)
    for i in range(len(n)):
        if N[i] >= t - 1e-9:
            prev = N[i - 1] if i else 0
            return L[i] + (t - prev) / n[i] * (L[i + 1] - L[i])


def gmode(L, n, use_density=True):
    a = np.diff(L); d = np.array(n, float) / (a if use_density else 1)
    i = int(np.argmax(d)); dm = d[i - 1] if i else 0; dp = d[i + 1] if i < len(d) - 1 else 0
    return L[i] + (d[i] - dm) / ((d[i] - dm) + (d[i] - dp)) * a[i]


# ---------------------------------------------------------------- 1. Variable discreta
def t_discreta(sh, lvl, rng, data=None, ctx=None):
    ctx = ctx or {}
    if data is None:
        p = [[.30, .28, .2, .12, .06, .04], [.18, .3, .25, .15, .08, .04], [.4, .25, .15, .1, .06, .04]][lvl - 1]
        data = list(rng.choice(range(6), size=30, p=p))
        data = [int(x) for x in data]
    var = ctx.get('var', 'Número de días de teletrabajo a la semana de 30 empleados')
    x = np.array(data); vals = sorted(set(data)); cnts = [data.count(v) for v in vals]; n = len(data)
    sh.p(var + '.', bold=True)
    R = sh.data_row(data)
    if lvl in (1, 2):
        sh.h('Paso 1 · Tabla de frecuencias')
        if lvl == 1:
            sh.hint('Escribe en la fila de pistas lo que pondrías en la primera fila. Usa CONTAR.SI sobre los datos de arriba (fíjalos con $).')
        given = [[v] for v in vals]
        N = np.cumsum(cnts)
        keys = [[c, c / n, int(N[i]), v * c, v * v * c] for i, (v, c) in enumerate(zip(vals, cnts))]
        hints = ['=CONTAR.SI(datos;A…)', '=nᵢ / n', '=Nᵢ₋₁ + nᵢ', '=xᵢ*nᵢ', '=xᵢ^2*nᵢ'] if lvl == 1 else None
        sh.work_table(['xᵢ', 'nᵢ', 'fᵢ', 'Nᵢ', 'xᵢ·nᵢ', 'xᵢ²·nᵢ'], given, keys, hints, dec=[0, 3, 0, 0, 0])
        sh.h('Paso 2 · Medidas')
    else:
        sh.h('Preguntas')
    mean = x.mean(); S2 = x.var(); s2 = x.var(ddof=1)
    q1 = float(np.percentile(x, 25)); q3 = float(np.percentile(x, 75))
    q1m = pct_rank_manual(vals, cnts, .25); q3m = pct_rank_manual(vals, cnts, .75)
    k = ctx.get('k', 2)
    sh.ask('Tamaño de la muestra (n)', n, 0)
    sh.ask('Media', mean, 2, alts=[(np.mean(vals), 'Has hecho la media de los valores distintos. Cada valor cuenta tantas veces como se repite.')])
    sh.ask('Mediana', float(np.median(x)), 2)
    sh.ask('Moda', vals[int(np.argmax(cnts))], 0, alts=[(max(cnts), 'Eso es la frecuencia más alta. La moda es el VALOR que tiene esa frecuencia.')])
    alt1 = [(q1m, 'Eso es con la receta de clase. Aquí se pide con =CUARTIL.INC(…;1).')] if abs(q1m - q1) > .01 else []
    sh.ask('Primer cuartil (con CUARTIL.INC)', q1, 2, alts=alt1)
    alt3 = [(q3m, 'Eso es con la receta de clase. Aquí se pide con =CUARTIL.INC(…;3).')] if abs(q3m - q3) > .01 else []
    sh.ask('Tercer cuartil (con CUARTIL.INC)', q3, 2, alts=alt3)
    sh.ask('Varianza S² (la de clase)', S2, 3, alts=[(s2, 'Has calculado la cuasivarianza (VAR.S). Aquí se pide VAR.P.'), ((x * x).mean(), 'Te falta restar la media al cuadrado.')])
    sh.ask('Cuasivarianza s²', s2, 3, alts=[(S2, 'Esa es la varianza (VAR.P). La cuasivarianza es VAR.S.')])
    sh.ask('Desviación típica S', math.sqrt(S2), 3, alts=[(math.sqrt(s2), 'Has usado DESVEST.S. La desviación típica de clase es DESVEST.P.'), (S2, 'Eso es la varianza. La desviación típica es su raíz.')])
    cv = math.sqrt(S2) / mean
    sh.ask('Coeficiente de variación (en decimal)', cv, 3, kind='pct', alts=[(math.sqrt(s2) / mean, 'Usa DESVEST.P en el CV, no DESVEST.S.'), (mean / math.sqrt(S2), 'Está al revés: CV = desviación típica ÷ media.')])
    gt = (x > k).mean(); ge = (x >= k).mean()
    sh.ask(f'Proporción de empleados con más de {k} (en decimal o %)', gt, 3, kind='pct', alts=[(ge, f'"Más de {k}" no incluye el {k}.'), ((x > k).sum(), 'Eso es cuántos son. Piden la proporción: divide entre n.')])


# ---------------------------------------------------------------- 2. Intervalos
def t_intervalos(sh, lvl, rng, data=None, ctx=None):
    ctx = ctx or {}
    if data is None:
        sets = [([800, 1000, 1200, 1500, 2000, 3000], [9, 21, 34, 26, 10]),
                ([20, 30, 40, 60, 80, 120], [6, 15, 38, 27, 14]),
                ([0, 5, 10, 20, 30, 50], [12, 18, 31, 22, 7])]
        L, n = sets[lvl - 1]
        n = [int(v + rng.integers(-2, 3)) for v in n]
    else:
        L, n = data
    var = ctx.get('var', ['Salario mensual (€) de los empleados de una empresa', 'Superficie (m²) de viviendas de alquiler', 'Antigüedad (años) del personal de un hospital'][lvl - 1])
    k = len(n); N = np.cumsum(n); tot = sum(n)
    sh.p(var + '.', bold=True)
    rows = [[f'{"[" if i == 0 else "("}{L[i]}, {L[i+1]}]', n[i]] for i in range(k)]
    a = np.diff(L); mk = [(L[i] + L[i + 1]) / 2 for i in range(k)]; d = np.array(n) / a
    if lvl in (1, 2):
        sh.h('Paso 1 · Tabla de trabajo')
        if lvl == 1:
            sh.hint('Marca = punto medio. Amplitud = extremo superior − inferior. Densidad = nᵢ ÷ amplitud (las amplitudes NO son iguales).')
        keys = [[mk[i], a[i], d[i], mk[i] * n[i], mk[i] ** 2 * n[i], int(N[i])] for i in range(k)]
        hints = ['=(Linf+Lsup)/2', '=Lsup−Linf', '=nᵢ/aᵢ', '=xᵢ*nᵢ', '=xᵢ^2*nᵢ', '=Nᵢ₋₁+nᵢ'] if lvl == 1 else None
        sh.work_table(['Intervalo', 'nᵢ', 'Marca xᵢ', 'Amplitud aᵢ', 'Densidad dᵢ', 'xᵢ·nᵢ', 'xᵢ²·nᵢ', 'Nᵢ'], rows, keys, hints, dec=[2, 2, 3, 2, 0, 0])
        sh.h('Paso 2 · Medidas')
    else:
        sh.data_table(['Intervalo', 'nᵢ'], rows)
        sh.h('Preguntas')
    mean = sum(m * c for m, c in zip(mk, n)) / tot
    S2 = sum(m * m * c for m, c in zip(mk, n)) / tot - mean ** 2
    mo = gmode(L, n, True); mo_f = gmode(L, n, False)
    me = gq(L, n, .5)
    hi = ctx.get('hi', 20)
    p_hi = gq(L, n, 1 - hi / 100); p_lo = gq(L, n, hi / 100)
    sh.ask('n (total)', tot, 0)
    sh.ask('Media', mean, 2, alts=[(np.mean(mk), 'Has promediado las marcas sin multiplicar por las frecuencias.')])
    sh.ask('Varianza S²', S2, 1, alts=[(S2 + mean ** 2, 'Te falta restar la media al cuadrado.'), (S2 * tot / (tot - 1), 'Esa es la cuasivarianza (divide entre n−1). Aquí se pide la varianza.')])
    sh.ask('Desviación típica S', math.sqrt(S2), 2)
    sh.ask('Coeficiente de variación (decimal)', math.sqrt(S2) / mean, 3, kind='pct')
    alts = [(mo_f, 'Has usado las frecuencias. Con amplitudes distintas, el intervalo modal se elige por la DENSIDAD.')] if abs(mo_f - mo) > .01 else []
    sh.ask('Moda (fórmula de intervalos)', mo, 2, alts=alts)
    sh.ask('Mediana', me, 2, alts=[((L[int(np.searchsorted(N, tot / 2))] + L[int(np.searchsorted(N, tot / 2)) + 1]) / 2, 'Eso es la marca del intervalo. Aplica la fórmula: Linf + (n/2 − Nᵢ₋₁)/nᵢ · aᵢ.')])
    sh.ask(f'¿A partir de qué valor se está en el {hi} % con valores más altos?', p_hi, 2, alts=[(p_lo, f'Ese es el percentil {hi}. "El {hi} % de arriba" empieza en el percentil {100 - hi}.')])


# ---------------------------------------------------------------- 3. Subpoblaciones + transformaciones
def t_subpob(sh, lvl, rng, data=None, ctx=None):
    sets = [(['Administración', 'Producción', 'Ventas'], [40, 90, 30], [1650, 1480, 1920], [210, 160, 380]),
            (['Hombres', 'Mujeres'], [120, 80], [2350, 2080], [420, 300]),
            (['Centro A', 'Centro B', 'Centro C'], [25, 60, 35], [24.5, 21.0, 27.5], [4.1, 3.2, 6.0])]
    names, T, M, Sd = data or sets[lvl - 1]
    T = np.array(T, float); M = np.array(M, float); Sd = np.array(Sd, float)
    unit = (ctx or {}).get('unit', '€' if lvl < 3 else 'miles de €')
    sh.p(f'Salario medio por grupo ({unit}). Te dan el tamaño, la media y la DESVIACIÓN TÍPICA de cada grupo.', bold=True)
    sh.data_table(['Grupo', 'Tamaño T', 'Media', 'Desv. típica'], [[a, int(b), c, d] for a, b, c, d in zip(names, T, M, Sd)])
    gm = (T * M).sum() / T.sum(); V = Sd ** 2
    within = (T * V).sum() / T.sum(); between = (T * (M - gm) ** 2).sum() / T.sum(); total = within + between
    cv = Sd / M
    if lvl in (1, 2):
        sh.h('Paso 1 · Tabla de trabajo')
        if lvl == 1:
            sh.hint('Varianza = desviación típica al cuadrado. Para la "entre" necesitas antes la media global (pregunta 1).')
        keys = [[V[i], V[i] * T[i], cv[i], (M[i] - gm) ** 2 * T[i]] for i in range(len(T))]
        hints = ['=Desv^2', '=Varianza*T', '=Desv/Media', '=(Media−global)^2*T'] if lvl == 1 else None
        sh.work_table(['Grupo', 'Varianza', 'Varianza·T', 'CV', '(media−global)²·T'], [[a] for a in names], keys, hints, dec=[1, 0, 3, 0])
    sh.h('Preguntas')
    best = names[int(np.argmin(cv))]
    worst_sd = names[int(np.argmin(Sd))]
    sh.ask('¿Qué grupo es más homogéneo? (escribe el nombre)', best, kind='text', accept=[best], alts=[(worst_sd, 'Ese tiene la menor desviación típica, pero las medias son distintas: compara el CV.')] if worst_sd != best else [])
    sh.ask('Media global', gm, 2, alts=[(M.mean(), 'Has hecho la media de las medias sin ponderar por el tamaño de cada grupo.')])
    sh.ask('Varianza dentro de los grupos', within, 1, alts=[((T * Sd).sum() / T.sum(), 'Has usado las desviaciones típicas. Hay que elevarlas al cuadrado (varianzas).')])
    sh.ask('Varianza entre los grupos', between, 1)
    sh.ask('Varianza total', total, 1)
    sh.ask('Desviación típica total', math.sqrt(total), 2, alts=[(total, 'Eso es la varianza. Haz la raíz cuadrada.')])
    sh.ask('% de la variabilidad debido a las diferencias entre grupos', between / total, 3, kind='pct', alts=[(within / total, 'Ese es el % de dentro de los grupos.')])
    ctx = ctx or {}
    a_, b_ = ctx.get('ab', [(1.03, 0), (1.02, 40), (1.0, 1.5)][lvl - 1])
    desc = ctx.get('desc', {1: 'suben un 3 %', 2: 'suben un 2 % y además 40 €', 3: f'aumentan 1,5 ({unit}) a todos'}[lvl])
    sh.gap()
    sh.p(f'Si todos los salarios {desc}:', bold=True)
    sh.ask('Nueva media global', a_ * gm + b_, 2)
    alts = []
    if a_ != 1:
        alts.append((a_ * total, 'La varianza se multiplica por a² (no por a).'))
    if b_:
        alts.append((a_ ** 2 * total + b_, 'Sumar una cantidad fija NO cambia la varianza.'))
    if a_ == 1:
        alts.append((total + b_, 'Sumar una cantidad fija NO cambia la varianza.'))
    sh.ask('Nueva varianza total', a_ ** 2 * total, 1, alts=alts)


# ---------------------------------------------------------------- 4. Tabla de contingencia
def t_conting(sh, lvl, rng, data=None, ctx=None):
    sets = [(['Mañana', 'Tarde', 'Noche'], ['Alta', 'Media', 'Baja'], [[22, 18, 8], [14, 20, 16], [5, 11, 26]], 'Turno', 'Satisfacción'),
            (['RRHH', 'Ventas', 'Producción'], ['Indefinido', 'Temporal', 'Parcial'], [[18, 6, 6], [30, 10, 10], [42, 14, 14]], 'Departamento', 'Contrato'),
            (['18-30', '31-45', '46-65'], ['Presencial', 'Híbrido', 'Remoto'], [[10, 14, 16], [20, 18, 12], [28, 9, 3]], 'Edad', 'Modalidad')]
    rn, cn, tab, X, Y = data or sets[lvl - 1]
    t = np.array(tab, float); n = t.sum(); fr = t.sum(1); fc = t.sum(0)
    sh.p(f'{int(n)} trabajadores según {X.lower()} (filas) y {Y.lower()} (columnas).', bold=True)
    sh.data_table([f'{X} \\ {Y}'] + cn, [[r] + [int(v) for v in row] for r, row in zip(rn, tab)])
    if lvl in (1, 2):
        sh.h('Paso 1 · Totales y frecuencias relativas fᵢⱼ = nᵢⱼ / n')
        if lvl == 1:
            sh.hint('Total de fila = suma de la fila. fᵢⱼ = cada casilla ÷ n. Independencia: compara fᵢⱼ con fᵢ.·f.ⱼ en TODAS las casillas.')
        keys = [[fr[i]] + list(t[i] / n) for i in range(3)]
        sh.work_table(['', 'Total fila'] + [f'f · {c}' for c in cn], [[r] for r in rn], keys, ['=SUMA(fila)'] + ['=nᵢⱼ/n'] * 3 if lvl == 1 else None, dec=[0, 3, 3, 3])
        sh.p('Ahora lo que habría si fueran independientes, fᵢ. × f.ⱼ:', italic=True)
        keys = [list(fr[i] / n * fc / n) for i in range(3)]
        sh.work_table([''] + [f'fᵢ.·f.ⱼ · {c}' for c in cn], [[r] for r in rn], keys, ['=(total fila/n)*(total col/n)'] * 3 if lvl == 1 else None, dec=[3, 3, 3])
    sh.h('Preguntas')
    sh.ask('n (total)', n, 0)
    sh.ask(f'Distribución marginal: total de "{cn[1]}"', fc[1], 0)
    sh.ask(f'f₁₁ (proporción de {rn[0]} y {cn[0]}, en decimal)', t[0, 0] / n, 3, kind='pct')
    sh.ask(f'f₁. × f.₁ (lo que habría si fueran independientes)', fr[0] / n * fc[0] / n, 3, kind='pct')
    sh.ask(f'De los de {rn[2]}, ¿qué proporción es "{cn[2]}"? ({Y} | {X} = {rn[2]})', t[2, 2] / fr[2], 3, kind='pct',
           alts=[(t[2, 2] / n, 'En una condicionada se divide entre el total de la FILA, no entre n.'), (t[2, 2] / fc[2], f'Eso es {X} | {Y}: has dividido entre el total de la columna.')])
    sh.ask(f'De los "{cn[0]}", ¿qué proporción es de {rn[1]}? ({X} | {Y} = {cn[0]})', t[1, 0] / fc[0], 3, kind='pct',
           alts=[(t[1, 0] / fr[1], 'Eso es la condicionada por fila. Aquí te restringes a la COLUMNA.'), (t[1, 0] / n, 'Divide entre el total de la columna, no entre n.')])
    indep = np.allclose(t / n, np.outer(fr, fc) / n / n)
    sh.ask('¿Son independientes? (Sí / No)', 'Sí' if indep else 'No', kind='text', accept=['SÍ', 'SI'] if indep else ['NO'],
           alts=[('SI' if not indep else 'NO', 'Compara fᵢⱼ con fᵢ.×f.ⱼ en todas las casillas (o los % de cada fila).'), ('SÍ' if not indep else 'NO', 'Compara fᵢⱼ con fᵢ.×f.ⱼ en todas las casillas (o los % de cada fila).')])


# ---------------------------------------------------------------- 5. Regresión con datos
def t_reg(sh, lvl, rng, data=None, ctx=None):
    if data is None:
        sets = [(np.array([2, 4, 5, 7, 8, 10, 12, 15]), 'Años de experiencia (X)', 'Salario (cientos de €) (Y)', 14, 2.1, 12, 3),
                (np.array([10, 15, 20, 25, 30, 35, 40, 50, 60]), 'Horas de formación (X)', 'Errores al mes (Y)', 40, -0.45, 3, 45),
                (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 'Inversión en publicidad, miles € (X)', 'Ventas, miles € (Y)', 50, 8.5, 6, 11)]
        x, xl, yl, a0, b0, sd, x0 = sets[lvl - 1]
        y = np.round(a0 + b0 * x + rng.normal(0, sd, len(x)), 1)
    else:
        x, y, xl, yl, x0 = data
    x = np.array(x, float); y = np.array(y, float)
    sh.p(f'{xl} y {yl} de {len(x)} casos.', bold=True)
    if lvl in (1, 2):
        sh.h('Paso 1 · Tabla de trabajo')
        if lvl == 1:
            sh.hint('Covarianza = Σxy/n − x̄·ȳ. Pendiente b = Sxy / Sx². Comprueba con PENDIENTE(Y;X) y con la línea de tendencia del gráfico.')
        keys = [[xi * yi, xi * xi, yi * yi] for xi, yi in zip(x, y)]
        sh.work_table(['X', 'Y', 'X·Y', 'X²', 'Y²'], [[xi, yi] for xi, yi in zip(x, y)], keys, ['=X*Y', '=X^2', '=Y^2'] if lvl == 1 else None, dec=[1, 1, 1])
    else:
        sh.data_table(['X', 'Y'], [[xi, yi] for xi, yi in zip(x, y)])
    mx, my = x.mean(), y.mean(); vx, vy = x.var(), y.var(); cov = (x * y).mean() - mx * my
    b = cov / vx; a = my - b * mx; r = cov / math.sqrt(vx * vy); bp = cov / vy; ap = mx - bp * my
    sh.h('Preguntas')
    sh.ask('Media de X', mx, 2); sh.ask('Media de Y', my, 2)
    sh.ask('Covarianza', cov, 2, alts=[(cov * len(x) / (len(x) - 1), 'Has usado COVARIANZA.M (divide entre n−1). En clase se usa COVARIANZA.P.')])
    sh.ask('Pendiente b (recta de Y sobre X)', b, 3, alts=[(bp, 'Esa es la pendiente de X sobre Y. En PENDIENTE va primero la Y: =PENDIENTE(Y;X).'), (cov / math.sqrt(vx), 'b = Sxy / Sx² (la VARIANZA de X, no la desviación).')])
    sh.ask('Término independiente a', a, 2, alts=[(ap, 'Ese es el de la recta de X sobre Y. Usa =INTERSECCION.EJE(Y;X).')])
    sh.ask('Coeficiente de correlación r', r, 3, alts=[(abs(r), 'Fíjate en el signo: r tiene el mismo signo que la pendiente.') if r < 0 else (r * r, 'Eso es R². r es la raíz (con el signo de b).')])
    sh.ask('Coeficiente de determinación R² (decimal)', r * r, 3, kind='pct', alts=[(r, 'Eso es r. R² es r al cuadrado.')])
    sh.ask(f'Predicción de Y para X = {x0}', a + b * x0, 2, alts=[(ap + bp * x0, 'Has usado la recta de X sobre Y.')])
    sh.ask('% de la variabilidad de Y que NO explica la recta', 1 - r * r, 3, kind='pct', alts=[(r * r, 'Ese es el % que SÍ explica (R²). El no explicado es 1 − R².')])


# ---------------------------------------------------------------- 6. Regresión sin datos
def t_reg_res(sh, lvl, rng, data=None, ctx=None):
    sets = [dict(mx=40, my=620, sx=12, sy=150, sxy=1440, xl='gasto en formación (miles €)', yl='productividad (unidades)', x0=55, x0txt='55000 €'),
            dict(mx=8, my=1800, sx=3, sy=300, sxy=-540, xl='años de antigüedad', yl='días de baja al año ×10', x0=10, x0txt='10 años'),
            dict(mx=150, my=210, sx=30, sy=40, r=0.85, xl='tasación (miles €)', yl='precio de venta (miles €)', x0=180, x0txt='180000 €')]
    d = data or sets[lvl - 1]
    mx, my, sx, sy = d['mx'], d['my'], d['sx'], d['sy']
    sxy = d.get('sxy', d.get('r', 0) * sx * sy)
    sh.p(f"X = {d['xl']}, Y = {d['yl']}. Datos resumidos:", bold=True)
    rows = [['x̄', mx], ['ȳ', my]]
    if lvl == 1:
        rows += [['Sx² (varianza de X)', sx * sx], ['Sy² (varianza de Y)', sy * sy], ['Sxy (covarianza)', sxy]]
    elif lvl == 2:
        rows += [['Sx (desviación típica de X)', sx], ['Sy (desviación típica de Y)', sy], ['Sxy (covarianza)', sxy]]
    else:
        rows += [['Sx (desviación típica de X)', sx], ['Sy (desviación típica de Y)', sy], ['r (correlación)', d['r']]]
    sh.data_table(['Dato', 'Valor'], rows)
    if lvl == 1:
        sh.hint('b = Sxy / Sx² · a = ȳ − b·x̄ · r = Sxy / (Sx·Sy) · R² = r²')
    elif lvl == 2:
        sh.hint('Cuidado: aquí te dan desviaciones típicas (S), no varianzas (S²).')
    else:
        sh.hint('Primero saca la covarianza: Sxy = r·Sx·Sy.')
    b = sxy / sx ** 2; a = my - b * mx; r = sxy / (sx * sy)
    sh.h('Preguntas')
    if lvl == 3:
        sh.ask('Covarianza Sxy', sxy, 2)
    sh.ask('Pendiente b', b, 3, alts=[(sxy / sx, 'b = Sxy / Sx² : divide entre la VARIANZA de X (Sx al cuadrado).'), (sxy / sy ** 2, 'Esa es la pendiente de X sobre Y (divides entre Sy²).')])
    sh.ask('Término independiente a', a, 2)
    if lvl < 3:
        sh.ask('Correlación r', r, 3)
    sh.ask('R² (decimal)', r * r, 3, kind='pct')
    alts = []
    if d['x0'] != float(d['x0txt'].split()[0]):
        alts.append((a + b * float(d['x0txt'].split()[0]), 'Cuidado con las unidades: si X está en miles, 55000 € es X = 55.'))
    sh.ask(f"Predicción de Y para {d['x0txt']}", a + b * d['x0'], 2, alts=alts)


# ---------------------------------------------------------------- 7. Índices y tasas
def t_indices(sh, lvl, rng, data=None, ctx=None):
    if lvl == 1:
        yrs = [2020, 2021, 2022, 2023, 2024]; v = [1250, 1300, 1365, 1350, 1420]
        sh.p('Ventas anuales de una empresa (miles de €).', bold=True)
        sh.hint('Índice base 2020 = valor/valor 2020 × 100. Tasa = valor/anterior − 1. Tasa media anual = (1 + tasa total)^(1/nº de años) − 1.')
        keys = [[x / v[0] * 100, (x / v[i - 1] - 1) if i else 0, x / v[2] * 100] for i, x in enumerate(v)]
        sh.work_table(['Año', 'Ventas', 'Índice base 2020', 'Tasa vs año anterior', 'Índice base 2022'], [[y, x] for y, x in zip(yrs, v)], keys,
                      ['=B/B$2020*100', '=B/B anterior−1', '=índice/índice 2022*100'], dec=[2, 4, 2])
        tt = v[-1] / v[0] - 1
        sh.h('Preguntas')
        sh.ask('Tasa de variación total 2020-2024 (decimal)', tt, 4, kind='pct')
        rates = [v[i] / v[i - 1] - 1 for i in range(1, 5)]
        sh.ask('Tasa media anual 2020-2024 (decimal)', (1 + tt) ** (1 / 4) - 1, 4, kind='pct', alts=[(np.mean(rates), 'Has hecho la media aritmética de las tasas. Hay que usar la media geométrica: (1+T)^(1/4) − 1.'), (tt / 4, 'No se divide la tasa entre 4: (1+T)^(1/4) − 1.'), ((1 + tt) ** (1 / 5) - 1, 'De 2020 a 2024 hay 4 años, no 5.')])
    elif lvl == 2:
        rates = [0.04, 0.06, -0.03, 0.05, 0.02]
        sh.p('Tasas de variación anual del número de afiliados a un sindicato: 2021 +4 %, 2022 +6 %, 2023 −3 %, 2024 +5 %, 2025 +2 %. Base 2020 = 100.', bold=True)
        idx = np.cumprod([1] + [1 + r for r in rates]) * 100
        sh.work_table(['Año', 'Tasa', 'Índice (2020 = 100)'], [[2020 + i, (rates[i - 1] if i else None)] for i in range(6)], [[x] for x in idx], None, dec=[2])
        sh.h('Preguntas')
        sh.ask('Tasa acumulada 2020-2025 (decimal)', idx[-1] / 100 - 1, 4, kind='pct', alts=[(sum(rates), 'Los porcentajes no se suman: se multiplican (1,04 × 1,06 × …).')])
        sh.ask('Tasa media anual (decimal)', (idx[-1] / 100) ** (1 / 5) - 1, 4, kind='pct', alts=[(np.mean(rates), 'Usa la media geométrica, no la aritmética.')])
        sh.ask('Índice de 2020 con base 2025 (propiedad de inversión)', 100 / idx[-1] * 100, 2)
    else:
        sh.p('En 2023 la plantilla creció un 25 % respecto a 2022. En 2024 bajó un 10 % respecto a 2023. La de 2024 superó en un 8 % a la de 2025.', bold=True)
        sh.p('Calcula los índices con base 2022 = 100.', italic=True)
        i23 = 125; i24 = 125 * 0.9; i25 = i24 / 1.08
        sh.h('Preguntas')
        sh.ask('Índice 2023', i23, 2)
        sh.ask('Índice 2024', i24, 2, alts=[(125 - 10, 'Los porcentajes no se restan: 125 × 0,90.')])
        sh.ask('Índice 2025', i25, 2, alts=[(i24 * 0.92, '"2024 superó en un 8 % a 2025" → 2024 = 1,08 × 2025. Hay que DIVIDIR entre 1,08.')])
        sh.gap()
        sh.p('Una cuenta da un 4,5 % anual.', bold=True)
        sh.ask('Tasa mensual equivalente (decimal)', 1.045 ** (1 / 12) - 1, 5, kind='pct', alts=[(0.045 / 12, 'No se divide entre 12: (1,045)^(1/12) − 1.')])


# ---------------------------------------------------------------- 8. Laspeyres, Paasche y deflactar
def t_complejos(sh, lvl, rng, data=None, ctx=None):
    sets = [(['Pan', 'Leche', 'Fruta', 'Aceite'], [1.1, 0.95, 2.2, 6.5], [320, 210, 150, 30], [1.3, 1.05, 2.5, 9.0], [300, 220, 140, 25]),
            (['Luz', 'Gas', 'Transporte'], [0.15, 0.06, 1.5], [3500, 6000, 400], [0.21, 0.09, 1.6], [3200, 5200, 430]),
            (['Café', 'Menú', 'Cine', 'Libro'], [1.2, 11, 7, 18], [200, 40, 12, 6], [1.5, 13.5, 8.5, 20], [180, 38, 10, 7])]
    names, p0, q0, pt, qt = data or sets[lvl - 1]
    p0, q0, pt, qt = map(lambda a: np.array(a, float), (p0, q0, pt, qt))
    sh.p('Cesta de productos: precios y cantidades en el año base (2020) y en 2025.', bold=True)
    rows = [[a, b, c, d, e] for a, b, c, d, e in zip(names, p0, q0, pt, qt)]
    if lvl in (1, 2):
        if lvl == 1:
            sh.hint('Laspeyres = Σ pₜ·q₀ / Σ p₀·q₀ × 100. Paasche = Σ pₜ·qₜ / Σ p₀·qₜ × 100. La cantidad es la MISMA arriba y abajo.')
        keys = [[pt[i] * q0[i], p0[i] * q0[i], pt[i] * qt[i], p0[i] * qt[i]] for i in range(len(names))]
        sh.work_table(['Producto', 'p₀', 'q₀', 'pₜ', 'qₜ', 'pₜ·q₀', 'p₀·q₀', 'pₜ·qₜ', 'p₀·qₜ'], rows, keys, ['=pₜ*q₀', '=p₀*q₀', '=pₜ*qₜ', '=p₀*qₜ'] if lvl == 1 else None, dec=[2, 2, 2, 2])
    else:
        sh.data_table(['Producto', 'p₀', 'q₀', 'pₜ', 'qₜ'], rows)
    L = (pt * q0).sum() / (p0 * q0).sum() * 100; P = (pt * qt).sum() / (p0 * qt).sum() * 100
    sh.h('Preguntas')
    sh.ask('Índice de Laspeyres de precios', L, 2, alts=[(P, 'Ese es Paasche. Laspeyres usa las cantidades del año BASE (q₀).'), ((p0 * q0).sum() / (pt * q0).sum() * 100, 'Está al revés: arriba van los precios de 2025.')])
    sh.ask('Índice de Paasche de precios', P, 2, alts=[(L, 'Ese es Laspeyres. Paasche usa las cantidades ACTUALES (qₜ).')])
    sh.ask('Índice de Fisher', math.sqrt(L * P), 2, alts=[((L + P) / 2, 'Fisher es la media GEOMÉTRICA: √(L·P), no la aritmética.')])
    sh.gap()
    sal = [[1500, 1560, 1610, 1650], [1800, 1830, 1890, 1950], [2100, 2200, 2250, 2330]][lvl - 1]
    ipc = [[100, 103.2, 106.9, 110.1], [100, 104.5, 108.0, 110.6], [100, 102.0, 105.6, 109.8]][lvl - 1]
    sh.p('Salario mensual (€) e IPC (2022 = 100):', bold=True)
    r1, _ = sh.data_table(['Año', 'Salario', 'IPC'], [[2022 + i, s, c] for i, (s, c) in enumerate(zip(sal, ipc))])
    real = sal[-1] / ipc[-1] * 100
    sh.ask('Salario real de 2025 en € de 2022', real, 2, alts=[(sal[-1] * ipc[-1] / 100, 'Para deflactar se DIVIDE entre el IPC (× 100).')])
    nom = sal[-1] / sal[0] - 1; rv = real / sal[0] - 1
    sh.ask('Variación nominal 2022-2025 (decimal)', nom, 4, kind='pct')
    sh.ask('Variación real 2022-2025 (decimal)', rv, 4, kind='pct', alts=[(nom - (ipc[-1] / 100 - 1), 'Los porcentajes no se restan: compara el salario real con el de 2022.')])


TIPOS = [
    ('1_Discreta', 'Variable discreta: tabla y medidas', 't1', t_discreta),
    ('2_Intervalos', 'Datos en intervalos (amplitudes distintas)', 't1', t_intervalos),
    ('3_Grupos', 'Varianza dentro y entre grupos + cambios de escala', 't1', t_subpob),
    ('4_Contingencia', 'Tabla de doble entrada e independencia', 't2', t_conting),
    ('5_Regresion', 'Regresión con datos', 't3', t_reg),
    ('6_Reg_resumen', 'Regresión a partir de resúmenes', 't3', t_reg_res),
    ('7_Indices', 'Índices y tasas', 't4', t_indices),
    ('8_Laspeyres_IPC', 'Laspeyres, Paasche y deflactar', 't4', t_complejos),
]
