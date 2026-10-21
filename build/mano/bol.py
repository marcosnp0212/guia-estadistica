import re
def addto(path, add):
    s=open(path).read()
    parts=re.split(r'(?=\n## )',s)
    for key,text in add.items():
        idx=[i for i,p in enumerate(parts) if p.startswith('\n## '+key)]
        assert len(idx)==1,(path,key,idx)
        i=idx[0]
        parts[i]=parts[i].rstrip('\n')+'\n\n'+text.strip()+'\n'
    open(path,'w').write(''.join(parts))
X=lambda t:'::: {custom-style="Excel"}\n**🖥️ En Excel.** '+t.strip()+'\n:::'
M=lambda title,t:'::: {custom-style="Mano"}\n**✍️ '+title+'** '+t.strip()+'\n:::'

B='/home/claude/build/alumna/03_boletin12.md'
s=open(B).read()
s=s.replace("**🧠 Cómo usar este boletín.** Intenta cada ejercicio primero en Excel, sin mirar. Luego abre la solución, mejor paso a paso.","**🧠 Cómo usar este boletín.** Las soluciones están hechas **a mano, con calculadora**, con todas las cuentas a la vista: así es como lo harías en un examen en papel. El recuadro verde de cada ejercicio te dice cómo hacerlo en Excel. Intenta cada ejercicio primero tú, en papel, sin mirar. Luego abre la solución, mejor paso a paso.")
open(B,'w').write(s)
addto(B,{
"Ejercicio 3.":X("Datos en A2:A21. n: `=CONTAR(A2:A21)`. Tabla: valores 0 a 4 en C2:C6 y en D2 `=CONTAR.SI($A$2:$A$21;C2)`, arrastrando. Media `=PROMEDIO(A2:A21)` → 1,6; mediana `=MEDIANA(A2:A21)` → 1; C₁ `=CUARTIL.INC(A2:A21;1)` → 1. Gráfico: selecciona C1:D6 → Insertar → Columna agrupada."),
"Ejercicio 4.":M("A mano: el diagrama de barras doble.","Pon los dos gráficos uno al lado del otro con el mismo eje horizontal (1 a 7). Fútbol con frecuencias absolutas (eje vertical de 0 a 8). Baloncesto con relativas (de 0 a 0,25). Una barra por valor, sin tocarse. Se ve de un vistazo la «montaña» de fútbol y la «U» de baloncesto."),
"Ejercicio 5.":M("A mano: el histograma con amplitudes distintas.","""
1. Eje horizontal de 7 a 15, **a escala**: cada unidad ocupa lo mismo (si 1 unidad = 1 cm, (12, 15] mide 3 cm).
2. Eje vertical para la densidad, de 0 a 10.
3. Rectángulos pegados con altura = densidad: 3, 6, 9, 4,5 y 1.
4. Comprueba: el **área** de cada rectángulo (base × altura) es su nᵢ. (10, 12]: 2 × 4,5 = 9 ✔."""),
"Ejercicio 7.":X("Linf en A2:A6, Lsup en B2:B6, días en C2:C6. a) `=SUMA(C4:C6)` → 20. b) Parte de (60, 70] por encima de 62 más el último intervalo: `=C5*(B5-62)/(B5-A5)+C6` → 12,2. c) `=(C4*(B4-52)/(B4-A4)+C5*(67-A5)/(B5-A5))/SUMA(C2:C6)` → 0,427 (con formato %)."),
"Ejercicio 9.":X("Marcas en A2:A8 y % en B2:B8. Media: `=SUMAPRODUCTO(A2:A8;B2:B8)/100` → 18,9 (en D2). Varianza: `=SUMAPRODUCTO(A2:A8^2;B2:B8)/100-D2^2` → 30,39. Histograma: columnas con los % y ancho de intervalo 0 %.")+'\n\n'+M("A mano: el histograma.","Todos los intervalos miden 4, así que la altura de cada rectángulo puede ser directamente el %. Eje horizontal de 5 a 33 marcando 5, 9, 13… y vertical de 0 a 35 %. Rectángulos pegados."),
"Ejercicio 10.":X("Valores en A2:A6 y nᵢ en B2:B6. Media (en E2): `=SUMAPRODUCTO(A2:A6;B2:B6)/SUMA(B2:B6)` → 15. Acumuladas en C: `=B2` y `=C2+B3` arrastrando, para buscar la mediana. Moda: `=INDICE(A2:A6;COINCIDIR(MAX(B2:B6);B2:B6;0))` → 12. Desviación típica: `=RAIZ(SUMAPRODUCTO(A2:A6^2;B2:B6)/SUMA(B2:B6)-E2^2)` → 5,29. CV: `=E3/E2` (con S en E3). Con la subida: `=1,05*E2`."),
"Ejercicio 11.":X("Linf en A2:A6, Lsup en B2:B6, nᵢ en C2:C6. Marca en D2: `=(A2+B2)/2`. Media: `=SUMAPRODUCTO(D2:D6;C2:C6)/SUMA(C2:C6)` → 66,75; alquiler `=10*` esa celda. Densidad en E2: `=C2/(B2-A2)`. Moda (el modal es el primero, anterior = 0): `=A2+(E2-0)/((E2-0)+(E2-E3))*(B2-A2)` → 48,33."),
"Ejercicio 13.":X("""Tabla de Pontevedra con Linf (A), Lsup (B), nᵢ (C), marca (D), Nᵢ (E). Media (en H2): `=SUMAPRODUCTO(D2:D7;C2:C7)/SUMA(C2:C7)`. Varianza: `=SUMAPRODUCTO(D2:D7^2;C2:C7)/SUMA(C2:C7)-H2^2`. P₃₅ (intervalo en la fila 4): `=A4+(0,35*110-E3)/C4*(B4-A4)`.

Galicia: tamaños en K2:K5, medias en L2:L5, desviaciones en M2:M5. Varianzas en N2: `=M2^2`. Media global (en P2): `=SUMAPRODUCTO(K2:K5;L2:L5)/SUMA(K2:K5)`. Dentro: `=SUMAPRODUCTO(K2:K5;N2:N5)/SUMA(K2:K5)`. Entre: `=SUMAPRODUCTO(K2:K5;(L2:L5-P2)^2)/SUMA(K2:K5)`."""),
"Ejercicio 14.":X("Tamaños en B2:B4, medias en C2:C4, desviaciones en D2:D4. CV en E2: `=D2/C2` y arrastra. Media global (en G2): `=SUMAPRODUCTO(B2:B4;C2:C4)/SUMA(B2:B4)` → 20,25. Dentro: `=SUMAPRODUCTO(B2:B4;D2:D4^2)/SUMA(B2:B4)` → 19,40. Entre: `=SUMAPRODUCTO(B2:B4;(C2:C4-G2)^2)/SUMA(B2:B4)` → 21,19. Desviación total: `=RAIZ(dentro+entre)`."),
"Ejercicio 15.":X("Tabla en B2:E6 (filas = personas, columnas = superficie), totales de columna en B7:E7 y de fila en F2:F6. Densidades de Y: `=B7/60`, `=C7/30`… Mediana de X: acumuladas de F2:F6. Condicionada «5 o más» (fila 6) con marcas en B9:E9: media `=SUMAPRODUCTO(B9:E9;B6:E6)/F6` → 91,38; varianza `=SUMAPRODUCTO(B9:E9^2;B6:E6)/F6-` media al cuadrado → 1359,23."),
"Ejercicio 16.":X("Tabla en B2:E6, totales de fila en F2:F6, de columna en B7:E7, n en F7. Marcas de X en A2:A6 y de Y en B9:E9. x̄: `=SUMAPRODUCTO(A2:A6;F2:F6)/F7`. ȳ: `=SUMAPRODUCTO(B9:E9;B7:E7)/F7`. Varianzas igual con `^2` y restando la media al cuadrado. Independencia, casilla 1: `=B2/F7` frente a `=(F2/F7)*(B7/F7)`. d) Suma las tres primeras filas con `=SUMA(B2:B4)` en cada columna y aplica la fórmula de los cuartiles con celdas."),
"Ejercicio 17.":X("Frecuencias de cada provincia en B2:F5 (una fila por provincia) y marcas en B1:F1. Media de A Coruña: `=SUMAPRODUCTO($B$1:$F$1;B2:F2)/SUMA(B2:F2)` y arrastra hacia abajo para las demás. Galicia: fila de totales con `=SUMA(B2:B5)`. Norte: `=B2+B3` en cada columna; sur: `=B4+B5`. Desviación típica de una fila: `=RAIZ(SUMAPRODUCTO($B$1:$F$1^2;B7:F7)/SUMA(B7:F7)-H7^2)`, con su media en H7."),
"Ejercicio 18.":X("Tabla en B2:C3, totales de fila en D2:D3, de columna en B4:C4 y n en D4. Relativas: `=B2/$D$4` y arrastra. Condicionada por columna (X | Y): `=B2/B$4`. Por fila (Y | X): `=B2/$D2`. Si fueran independientes: `=$D2*B$4/$D$4` y compara con B2."),
"Ejercicio 20.":M("A mano: el gráfico radial.","Dibuja un radio por partida, todos de la misma longitud (el borde = 12000). Sobre cada radio marca el punto a la fracción que toca (Alimentación al 97 %, Vivienda al 62 %…). Une los puntos en orden. Para Almería y Barcelona, compara solo qué línea llega más lejos en cada radio."),
"Ejercicio 21.":X("Tamaños en B2:B3, medias en C2:C3, varianzas en D2:D3. CV en E2: `=RAIZ(D2)/C2`. Media global (en G2): `=SUMAPRODUCTO(B2:B3;C2:C3)/SUMA(B2:B3)` → 2550. Dentro: `=SUMAPRODUCTO(B2:B3;D2:D3)/SUMA(B2:B3)` → 40400. Entre: `=SUMAPRODUCTO(B2:B3;(C2:C3-G2)^2)/SUMA(B2:B3)` → 96100. % entre: `=entre/(dentro+entre)`."),
"Ejercicio 22.":X("Pon a (el multiplicador) en B y b (lo que se suma) en C para cada propuesta: I → 1 y 50; II → 1,02 y 0; III → 0,99 y 0; IV → 1,01 y 25. Media en D2: `=B2*2550+C2`. Varianza en E2: `=B2^2*136500`. Desviación en F2: `=RAIZ(E2)`. Arrastra."),
})

T3='/home/claude/build/alumna/04_tema3.md'
addto(T3,{
"Ejercicio 2.":X("Pon n y las sumas en celdas: n en B1, ΣX en B2, ΣY en B3, ΣX² en B4, ΣY² en B5, ΣXY en B6. x̄ `=B2/B1`, ȳ `=B3/B1` (en B8 y B9). S²ₓ `=B4/B1-B8^2`. S_XY `=B6/B1-B8*B9`. b `=S_XY/S²ₓ`; a `=B9-b*B8`. Mismo método que a mano, con celdas."),
"Ejercicio 3.":X("X en A2:A6, Y en B2:B6. `=PENDIENTE(B2:B6;A2:A6)` → −9,244. `=INTERSECCION.EJE(B2:B6;A2:A6)` → 263,05. `=COEFICIENTE.R2(B2:B6;A2:A6)` → 0,664; no explicado: `=1-` esa celda. Gráfico: Insertar → Dispersión y línea de tendencia con ecuación y R².")+'\n\n'+M("A mano: la nube de puntos.","Eje X de 20 a 24 (euros/hora) y eje Y de 40 a 85 (clientes). Cinco puntos. Para la recta, calcula Ŷ en X = 20 (78,2) y en X = 24 (41,2) y únelos: baja, relación inversa."),
"Ejercicio 4.":X("Igual que el ejercicio 1: x̄, ȳ, Sₓ, Sᵧ y S_XY en celdas (B1 a B5). b `=B5/B3^2` → 1,2. a `=B2-b*B1` → −8. r `=B5/(B3*B4)` → 0,96. Predicción `=a+b*100`."),
"Ejercicio 5.":X("X en A2:A8, Y en B2:B8. `=PENDIENTE(B2:B8;A2:A8)` → 707,14. `=INTERSECCION.EJE(B2:B8;A2:A8)` → −457,14. `=COEF.DE.CORREL(A2:A8;B2:B8)` → 0,960. `=PRONOSTICO.LINEAL(2,2;B2:B8;A2:A8)` → 1098,57."),
"Ejercicio 6.":X("Sin datos sueltos se usan celdas: b en B1, R² en B2, x̄ en B3, Sᵧ en B4. ȳ `=2+B1*B3` (con a = 2). r `=SIGNO(B1)*RAIZ(B2)` → −0,9. Sₓ `=r*B4/B1` → 3. S_XY `=B1*Sₓ^2` → −27."),
"Ejercicio 7.":X("r en B1, x̄ en B2, ȳ en B3, S²ₓ en B4, S²ᵧ en B5. S_XY `=B1*RAIZ(B4)*RAIZ(B5)` → 1,68 (en B7). Y sobre X: b `=B7/B4`, a `=B3-b*B2`. X sobre Y: b' `=B7/B5`, a' `=B2-b'*B3`."),
})
T4='/home/claude/build/alumna/05_tema4.md'
s=open(T4).read()
s=s.replace("Excel: en C3 `=B3/B2-1` con formato %, y arrastrar.","::: {custom-style=\"Excel\"}\n**🖥️ En Excel.** En C3 `=B3/B2-1` con formato %, y arrastrar.\n:::")
open(T4,'w').write(s)
addto(T4,{
"Ejercicio 1.":X("En B2 escribe 100 (2019). 2020: `=B2*1,4`. 2021: `=B3*0,8`. 2022: `=B4/1,15`. Es la misma idea que a mano: multiplicar o dividir por (1 + tasa)."),
"Ejercicio 2.":X("2019 en C2 = 100. 2020: `=C2*1,2`. 2018: `=C3/0,8`. 2021: `=C3/0,5`."),
"Ejercicio 4.":X("Salarios en B2 (2023) y B3 (2024), IPC 2024 en C3. Lo que debería cobrar: `=B2*C3/100` → 448,62. Valor real: `=B3/C3*100` → 427,25. Variación real: `=B4/B2-1` (con el valor real en B4) → −1,43 %."),
"Ejercicio 6.":X("Producción en B2:B6. Base 2020 en C2: `=B2/$B$2*100`. Base 2022 en D2: `=C2/$C$4*100` (o `=B2/$B$4*100`). Arrastra."),
"Ejercicio 7.":X("Cantidades en B2:B4 y precios en C2:C4 (2015, 2022, 2025). Tasa de cantidad 2015-2022: `=B3/B2-1`. Anual: `=(B3/B2)^(1/7)-1`. Valor en D2: `=B2*C2`. Índice del valor: `=D2/$D$2*100`."),
"Ejercicio 8.":X("Tasas en B2:B4 (5 %, 4 %, 3 %). Trimestre: `=(1+B2)*(1+B3)*(1+B4)-1` → 12,48 %. Media mensual: `=((1+B2)*(1+B3)*(1+B4))^(1/3)-1` → 4,00 %."),
"Ejercicio 9.":X("p₂₀ en B, q₂₀ en C, p₂₅ en D, q₂₅ en E (filas 2 a 6). Laspeyres: `=SUMAPRODUCTO(D2:D6;C2:C6)/SUMAPRODUCTO(B2:B6;C2:C6)*100` → 121,07. Paasche: `=SUMAPRODUCTO(D2:D6;E2:E6)/SUMAPRODUCTO(B2:B6;E2:E6)*100` → 121,06."),
"Ejercicio 10.":X("Sueldo en B2:B6 e IPC en C2:C6. IPC base 1992 en D2: `=C2/$C$2*100`. Sueldo real en E2: `=B2/D2*100`. Variación nominal `=B6/B2-1`; real `=E6/E2-1`."),
"Ejercicio 11.":X("Alquiler en B1, IPC 2020, 2021 y 2022 en B2:B4. 2021: `=$B$1*B3/$B$2`. 2022: `=$B$1*B4/$B$2`. b) `=1300*B2/B4`."),
})
print('ok')
