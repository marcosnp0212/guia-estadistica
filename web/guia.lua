local stringify = pandoc.utils.stringify

local labels = {
  Truco = "Truco", Ojo = "Ojo", Excel = "En Excel", Resultado = "Resultado",
  Idea = "La idea", Enunciado = "Enunciado", Mano = "A mano, con calculadora"
}

local function strip_lead(s)
  local out, started = {}, false
  for _, cp in utf8.codes(s) do
    if not started then
      local letter = (cp >= 65 and cp <= 90) or (cp >= 97 and cp <= 122) or (cp >= 0xC0 and cp <= 0x24F) or cp == 0xBF or cp == 0xA1
      if letter then started = true end
    end
    if started then out[#out+1] = utf8.char(cp) end
  end
  local r = table.concat(out)
  r = r:gsub("[%.:]%s*$", "")
  return r
end

local function tema_class(s)
  if s:match("^Tema 1") then return "t1" end
  if s:match("^Tema 2") then return "t2" end
  if s:match("Temas 1 y 2") then return "t2" end
  if s:match("^Tema 3") or s:match("Tema 3") then return "t3" end
  if s:match("^Tema 4") or s:match("Tema 4") then return "t4" end
  if s:match("^Parte 0") or s:match("^Antes de empezar") then return "t0" end
  return "tx"
end

function Header(h)
  local s = stringify(h.content)
  if h.level == 1 then
    h.classes:insert(tema_class(s))
    local n, rest = s:match("^Tema (%d)%. (.+)$")
    if n then
      h.content = { pandoc.Span({pandoc.Str("Tema " .. n)}, {class = "tab"}), pandoc.Span(pandoc.Inlines(rest), {class = "ht"}) }
      return h
    end
    local p, rest2 = s:match("^(Parte 0[^%.]*)%. (.+)$")
    if p then
      h.content = { pandoc.Span({pandoc.Str(p)}, {class = "tab"}), pandoc.Span(pandoc.Inlines(rest2), {class = "ht"}) }
      return h
    end
    local pr = s:match("^Prácticas (.+)$")
    if pr then
      h.content = { pandoc.Span({pandoc.Str("Prácticas")}, {class = "tab"}), pandoc.Span(pandoc.Inlines((pr:gsub("^de los ", ""):gsub("^del ", ""))), {class = "ht"}) }
      return h
    end
    if s:match("^Examen modelo") then
      h.content = { pandoc.Span({pandoc.Str("Examen")}, {class = "tab"}), pandoc.Span(pandoc.Inlines("El modelo de la profesora"), {class = "ht"}) }
      return h
    end
    if s:match("^Simulacros") then
      h.content = { pandoc.Span({pandoc.Str("Examen")}, {class = "tab"}), pandoc.Span(pandoc.Inlines("Simulacros"), {class = "ht"}) }
      return h
    end
    if s:match("^Boletín") then
      local nice = s:match("Temas 1 y 2") and "Ejercicios de los Temas 1 y 2" or (s:match("Tema 3") and "Ejercicios del Tema 3" or "Ejercicios del Tema 4")
      h.content = { pandoc.Span({pandoc.Str("Boletín")}, {class = "tab"}), pandoc.Span(pandoc.Inlines(nice), {class = "ht"}) }
      return h
    end
    if false then
      local rest3 = s:gsub("^Boletín ", "")
      h.content = { pandoc.Span({pandoc.Str("Boletín")}, {class = "tab"}), pandoc.Span(pandoc.Inlines(rest3:sub(1,1):upper() .. rest3:sub(2)), {class = "ht"}) }
      return h
    end
    h.content = { pandoc.Span(h.content, {class = "ht"}) }
    return h
  elseif h.level == 2 then
    local t = s:match("^Tema (%d)$")
    if t then h.classes:insert("t" .. t) end
    local pn, prest = s:match("^Práctica (%d+)%. (.+)$")
    if pn then
      h.classes:insert("ej"); h.classes:insert("prac")
      h.content = { pandoc.Span({pandoc.Str(pn)}, {class = "num"}), pandoc.Span(pandoc.Inlines(prest), {class = "ht"}) }
      return h
    end
    local n, rest = s:match("^Ejercicio (%d+)%. (.+)$")
    if n then
      h.classes:insert("ej")
      h.content = { pandoc.Span({pandoc.Str(n)}, {class = "num"}), pandoc.Span(pandoc.Inlines(rest), {class = "ht"}) }
      return h
    end
    local num, rest2 = s:match("^(%d+%.%d+)%. (.+)$")
    if num then
      h.content = { pandoc.Span({pandoc.Str(num)}, {class = "secnum"}), pandoc.Span(pandoc.Inlines(rest2), {class = "ht"}) }
      return h
    end
    local w = s:match("^Semana (%d)")
    if w then h.classes:insert("week") end
    return h
  end
end

function Div(d)
  local cs = d.attributes["custom-style"]
  if cs == "Otra" then
    local out = { pandoc.RawBlock("html", '<details class="otra"><summary>No lo entiendo: explícamelo de otra forma</summary><div class="otra-body">') }
    for _, b in ipairs(d.content) do out[#out + 1] = b end
    out[#out + 1] = pandoc.RawBlock("html", "</div></details>")
    return out
  end
  if not cs or not labels[cs] then return nil end
  d.attributes["custom-style"] = nil
  d.classes:insert("co")
  d.classes:insert("co-" .. cs:lower())
  local title = nil
  local first = d.content[1]
  if first and (first.t == "Para" or first.t == "Plain") and first.content[1] and first.content[1].t == "Strong" then
    title = strip_lead(stringify(first.content[1]))
    first.content:remove(1)
    while first.content[1] and (first.content[1].t == "Space" or first.content[1].t == "SoftBreak") do first.content:remove(1) end
    if #first.content == 0 then d.content:remove(1) end
  end
  if title == nil or title == "" then title = labels[cs] end
  d.content:insert(1, pandoc.Div({pandoc.Plain({pandoc.Str(title)})}, {class = "co-t"}))
  return d
end

function Table(t)
  return pandoc.Div({t}, {class = "tw"})
end

function Image(img)
  img.src = img.src:gsub("%.png$", ".svg")
  return img
end
