# Guía de Estadística (Excel) — proyecto

Guía de estudio de Estadística (RRLL y RRHH, UVigo, Temas 1 a 4) para una alumna que parte de cero, con TDAH y ansiedad. El tutor es Marcos (dueño del repositorio).

## Cómo trabajar con Marcos
- Español, de **tú**. Pregunta antes de suponer. Propuestas antes del resultado final.
- Nada de "formato IA" (tríadas, viñetas todas iguales, conectores inflados). Frases cortas.
- Cuando pide un test: siempre 30 preguntas.
- Los números de la guía tienen que cuadrar: comprueba cada cálculo ejecutándolo.

## Primero
```bash
bash setup.sh   # enlaza /home/claude/{build,web,video,xl2,xl3,entrega} con el repo y regenera los .wav
```
Todos los scripts usan rutas absolutas bajo `/home/claude/`.

## Estructura
- `build/alumna/*.md` — el texto de la guía de la alumna (se concatenan por orden de nombre). `build/tutor/00_tutor.md` — guía del tutor.
  - `00_inicio.md` Antes de empezar + vídeos + **Repaso exprés** + Parte 0. `01..05` temas, boletines, prácticas. `05r_modelo.md` examen modelo de la profesora con solucionario. `05s_simulacros.md` simulacros (S4 = tipo test). `06_anexos.md` chuleta, listas y plan.
  - Recuadros: `::: {custom-style="Idea|Ojo|Truco|Excel|Mano|Resultado|Enunciado|Otra"}`. Componentes: `::: {.video data-v="t1"}`, `::: {.practica data-tipo=...}`, `::: {.simulacro data-sim="S1"}`, `::: {.testsim data-sim="S4"}`, `::: {.plan-app}`.
- `web/` — maquetación HTML: `build_web.py` (pandoc + `guia.lua`), `guia.css`, `guia.js`, `features.js`, `course.js` (prácticas, simulacros, vídeos, simulacro tipo test, comprobaciones), `plan.js` (plan de estudio adaptativo), `sheet/` (hoja de cálculo en el navegador). Todo se incrusta en un único HTML.
- `xl2/` — generadores de los Excel (solucionario, prácticas, simulacros, plantillas) y los JSON de prácticas/simulacros/comprobaciones. `xl3/` — simulacro en papel (S3), preguntas de Excel sin ordenador, simulacro tipo test S4 (`mk_s4.py` → `sim_test.json`).
- `entrega/*.xlsx` — los Excel descargables que van dentro de la guía.
- `video/` — motor de los vídeos: `content/*.py` (guiones por escena: t1–t4 temas, b12/b3/b4 boletines), `engine.py` (estático) y `engine_anim.py` (animado, el que se usa: `python3 run_anim.py t1 b12 ...`). `audio_opus/` son las voces (Google Chirp 3 HD, voz es-ES Iapetus, velocidad 1); cada fragmento se llama `f` + sha1(texto hablado)[:12]. Si cambias un texto, ese fragmento necesita voz nueva: `nuevos.py` genera el guion de lo que falta y `voz_parte2/` es el kit de Windows que lo locuta (el usuario pone su clave de API en `clave.txt`; **nunca** la subas al repo).
- `docs/index.html` — la guía publicada (GitHub Pages).

## Construir y publicar
```bash
cd /home/claude/web && python3 build_web.py          # genera web/alumna.html y web/tutor.html
cd <raíz del repo> && cp web/alumna.html docs/index.html   # luego commit y push: GitHub Pages publica docs/
```
Comprueba con Playwright (Chromium en /opt/pw-browsers/chromium) que no hay errores de consola, y prueba en 390 px de ancho.

## Vídeos publicados (YouTube, ocultos)
t1 qFxCvatJA7s · b12 rRuCQaWuUSg · t2 bZ2RDTQ483I · t3 HULRqZML5gU · b3 XRN-ahfALUc · t4 25iXVSxnfoU · b4 Evhy1CFN7HU (mapa `VID` en `web/course.js`).

## Pendiente / ideas
- Los vídeos no incluyen todavía lo añadido el 21/10: extrapolación, rectas con S_XY = 0, r y unidades, mosaico, tanto por uno.
- Los .docx de la guía están desactualizados (el usuario dijo que los dejáramos).
