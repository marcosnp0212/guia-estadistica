P='/home/claude/build/alumna/05_tema4.md'
s=open(P).read()
def after(anchor,text):
    global s
    i=s.index(anchor);j=i+len(anchor);s=s[:j]+'\n\n'+text.strip()+'\n'+s[j:]
after("""Y en Excel la raíz se escribe como potencia: `=1,06^(1/12)-1`. **El paréntesis en (1/12) es obligatorio.** Sin él, Excel haría 1,06¹ ÷ 12.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: tasas medias con la calculadora.** Todo el Tema 4 se hace bien en papel. Lo único delicado es la raíz n-ésima.

1. Pasa cada porcentaje a "multiplicador": +5 % → 1,05; −3 % → 0,97; +0,5 % → 1,005.
2. Multiplícalos todos: es el crecimiento total.
3. Para la media por año, eleva a **(1 ÷ número de periodos)**. En la calculadora: `1,2474 ^ ( 1 ÷ 3 )` con el paréntesis, o con la tecla de raíz n-ésima (ˣ√): `3 ˣ√ 1,2474`.
4. Resta 1 y pasa a %: 1,0767 − 1 = 0,0767 → **7,67 %**.
5. **Comprueba** elevando: 1,0767³ tiene que dar 1,2474.

**Sin la tecla de raíz n-ésima:** con la de potencia (^ o xʸ) y el exponente entre paréntesis. Con 7 años: `1,408 ^ ( 1 ÷ 7 )` = 1,050.
:::
""")
after("""Si prefieres verlo paso a paso, crea columnas auxiliares con `=D2*C2` (pₜ·q₀), `=B2*C2` (p₀·q₀), etc., súmalas y divide.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: Laspeyres, Paasche y Fisher con una tabla.** Añade cuatro columnas de productos y súmalas. Con el ejemplo de los apuntes:

| Producto | pₜ·q₀ | p₀·q₀ | pₜ·qₜ | p₀·qₜ |
|:---|---:|---:|---:|---:|
| Pan | 1,20·100 = 120 | 1,00·100 = 100 | 1,20·110 = 132 | 1,00·110 = 110 |
| Leche | 1,10·200 = 220 | 0,90·200 = 180 | 1,10·190 = 209 | 0,90·190 = 171 |
| **Suma** | **340** | **280** | **341** | **281** |

- Laspeyres = 340 ÷ 280 × 100 = **121,43**.
- Paasche = 341 ÷ 281 × 100 = **121,35**.
- Fisher = √(121,43 × 121,35) = **121,39**.

Con la tabla delante, Laspeyres es "columna 1 entre columna 2" y Paasche "columna 3 entre columna 4". Así no se confunden.
:::
""")
after("""Para el gráfico: selecciona años, E y F → Insertar → Líneas.
:::""","""
::: {custom-style="Mano"}
**✍️ A mano: deflactar una serie.** Para cada año, tres cuentas con la calculadora (una fila cada vez):

1. **Salario real** = salario ÷ IPC × 100. 2025: 1950 ÷ 119 × 100 = **1638,66**.
2. **Índice nominal** = salario ÷ salario del año base × 100. 2025: 1950 ÷ 1500 × 100 = **130**.
3. **Índice real** = salario real ÷ salario real del año base × 100. 2025: 1638,66 ÷ 1500 × 100 = **109,24**.

**Atajo:** índice real = índice nominal ÷ IPC × 100. 2025: 130 ÷ 119 × 100 = 109,24. Da lo mismo y es una sola cuenta.

**Gráfico en papel:** años en el eje horizontal, índices en el vertical (de 95 a 135, por ejemplo); una línea para el nominal y otra para el real. La separación entre las dos es lo que se ha comido la inflación.
:::
""")
s=s.replace("- Deflactar con el IPC y comparar evolución nominal y real.","- Deflactar con el IPC y comparar evolución nominal y real.\n- Hacer todo lo anterior **a mano con calculadora**, sabiendo usar la potencia (1/n) para las tasas medias.")
open(P,'w').write(s);print(s.count('"Mano"'))
