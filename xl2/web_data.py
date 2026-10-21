"""Genera los datos de prácticas y simulacros para la guía web, con los mismos generadores y semillas que los Excel."""
import sys, json, numpy as np
sys.path.insert(0, '/home/claude/xl2')
from openpyxl import Workbook
import make_books as mb

def clean(v):
    if isinstance(v, (np.integer,)): return int(v)
    if isinstance(v, (np.floating,)): return float(v)
    if isinstance(v, float) and v.is_integer(): return v
    return v

class JSheet:
    def __init__(self, book, name, title, color, subtitle):
        self.name, self.title, self.color, self.subtitle = name, title, color, subtitle
        self.blocks = []; self.n_answers = 0
    def h(self, t): self.blocks.append({'t': 'h', 'text': t})
    def p(self, text, italic=False, color=None, bold=False, size=11): self.blocks.append({'t': 'p', 'text': text, 'b': bold, 'i': italic})
    def hint(self, t): self.blocks.append({'t': 'hint', 'text': t})
    def gap(self, n=1): pass
    def data_row(self, values, per_row=10, label='Datos'):
        self.blocks.append({'t': 'datos', 'values': [clean(v) for v in values]}); return ''
    def data_table(self, headers, rows, col=1):
        self.blocks.append({'t': 'tabla', 'headers': headers, 'rows': [[clean(v) for v in r] for r in rows]}); return (0, 0)
    def work_table(self, headers, given, keys, hints=None, dec=None, col=1):
        self.blocks.append({'t': 'trabajo', 'headers': headers, 'given': [[clean(v) for v in g] for g in given],
                            'keys': [[float(k) for k in row] for row in keys], 'hints': hints, 'dec': dec or [2] * len(keys[0])}); return 0
    def ask(self, label, key, dec=2, alts=(), kind='num', accept=None, note=None, unit=''):
        tol = None
        if kind != 'text':
            key = float(key)
            t = max(0.5 * 10 ** (-dec) * 1.02, abs(key) * 0.001)
            alts = [(float(v), h) for v, h in alts if abs(float(v) - key) > t * 1.5]
            tol = t
        else:
            alts = list(alts)
        self.blocks.append({'t': 'ask', 'label': label, 'key': key, 'dec': dec, 'tol': tol, 'kind': kind,
                            'accept': accept or ([key] if kind == 'text' else None),
                            'alts': [[a if kind == 'text' else a, h] for a, h in alts]})
        self.n_answers += 1; return ''
    def finish(self): return ''

class JBook:
    def __init__(self):
        self.wb = Workbook(); self.sheets = []; self.registry = []
    def sheet(self, name, title, color='tx', subtitle=None):
        s = JSheet(self, name, title, color, subtitle); self.sheets.append(s); return s
    def save(self, path):
        json.dump([{'id': s.name, 'title': s.title, 'color': s.color, 'subtitle': s.subtitle, 'blocks': s.blocks} for s in self.sheets],
                  open(path, 'w'), ensure_ascii=False)

mb.Book = JBook
mb.practicas('/home/claude/xl2/practicas.json')
mb.simulacros('/home/claude/xl2/simulacros.json')
P = json.load(open('/home/claude/xl2/practicas.json')); S = json.load(open('/home/claude/xl2/simulacros.json'))
print(len(P), len(S), sum(1 for s in P for b in s['blocks'] if b['t'] == 'ask'), sum(1 for s in S for b in s['blocks'] if b['t'] == 'ask'))
print(P[0]['id'], [b['t'] for b in P[0]['blocks']])
