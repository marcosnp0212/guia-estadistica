# ======================================================= Portada
ws = wb.create_sheet('Inicio', 0)
ws.sheet_view.showGridLines = False
widths(ws, {'A': 3, 'B': 22, 'C': 54, 'D': 60})
ws['B2'] = 'Plantillas de estadística'; ws['B2'].font = Font(bold=True, size=18, color=INK)
lines = ['Calculadoras listas: pegas los datos del ejercicio en las celdas amarillas y los resultados salen en las verdes.',
         'Úsalas para COMPROBAR lo que haces tú. En el examen, solo si la profesora permite llevar archivos propios.',
         'Para cada hoja: primero lee la frase de la fila 3. Si algo sale #N/A o #¡DIV/0!, revisa que los datos estén en las columnas correctas.',
         'Empieza por la hoja «Traductor»: te dice qué plantilla usar según lo que diga el enunciado.']
for i, t in enumerate(lines):
    ws.cell(4 + i, 2, t).font = Font(size=11)
head(ws, 9, 2, ['Hoja', 'Para qué', 'Cómo'])
items = [('Traductor', '¿Qué me están pidiendo?', 'Frases típicas del enunciado → qué calcular')] + TOC
for i, (nm, t, d) in enumerate(items):
    r = 10 + i
    c = ws.cell(r, 2, nm); c.hyperlink = f"#'{nm}'!A1"; c.font = Font(color='0563C1', underline='single')
    ws.cell(r, 3, t); ws.cell(r, 4, d).alignment = Alignment(wrap_text=True)
for w in wb.worksheets:
    w.freeze_panes = w.freeze_panes or None
wb.save('/home/claude/xl2/Plantillas_estadistica.xlsx')
print('ok', wb.sheetnames)
