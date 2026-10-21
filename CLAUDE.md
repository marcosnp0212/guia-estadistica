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
  - Zonas (el índice las muestra con etiquetas, ver `course.js` 2d): **Aprender** `01..05p` (temas, boletines, prácticas; cada tema lleva su vídeo arriba) · **Examen** `05q_repaso.md` (repaso exprés), `05r_modelo.md` (examen modelo resuelto), `05s_simulacros.md` (tipo test S4, papel S3, Excel sin ordenador) · **Herramientas** `06a_chuleta`, `06b_traductor`, `06c_lista`, `06d_plan`, `06e_base` (Parte 0 y 0 bis), `06f_descargas` · **Por si acaso** `07_por_si_acaso.md` (simulacros con Excel S1/S2, archivos, lista con Excel). `00_inicio.md` = Cómo usar esta guía.
  - Tono neutro (para cualquier estudiante), de tú. Sin créditos. La portada está en `web/hero_alumna.html` (pósit con lo de hoy, seguir donde lo dejaste, tarjetas de tema y accesos al examen).
  - Un solo plan, en `06d_plan.md` (`::: {.plan-app}`). La alumna elige **Exprés** o **Completo** («Qué plan quiero», `cfg.mode`); si no elige, se recomienda el exprés cuando el completo pasa de 180 min/día. El exprés **no recorta contenido**: siempre las mismas ~13 h (lista `XP` y `xpBlocks()` en `plan.js`: por tema vídeo → repaso → comprueba → ejercicios clave del boletín → preguntas del modelo; al final P1–P10, Excel sin ordenador, S4, corrección y refuerzo del tema más flojo del S4). Solo cambian las horas por día. Cada tarea tiene casilla (`xp:<id>`); lo de hoy queda fijo (`xp:hoy`); las 15 trampas (en `<details>`, pregunta-respuesta) van 10 min cada día desde el segundo. El repaso exprés solo tiene contenido y enlaza al plan; si cambias tiempos, revisa las cifras de `06d_plan.md` (13 h, 6 h y media con 2 días).
  - Recuadros: `::: {custom-style="Idea|Ojo|Truco|Excel|Mano|Resultado|Enunciado|Otra"}`. Componentes: `::: {.video data-v="t1"}`, `::: {.practica data-tipo=...}`, `::: {.simulacro data-sim="S1"}`, `::: {.testsim data-sim="S4"}`, `::: {.plan-app}`.
- **Navegación (alumna)**: `web/nav.js` convierte la página larga en pantallas. Barra superior con pestañas Inicio · Mi plan · Temas · Examen · Herramientas (en móvil, «Más»). Se ve una pantalla cada vez (un apartado `##`), con desplegable propio «Apartado» (no un `<select>`: número en el color del tema, marca «Hecho», teclado) para saltar a cualquiera, pantalla «Índice» (`#indice`, botón en la barra) con todos los apartados, botones Anterior y Siguiente, y el «atrás» del navegador funcionando (rutas por `#id`; virtuales: `#inicio`, `#temas`, `#tema:N`, `#examen`, `#herramientas`). Cada tema tiene cuatro pestañas: Aprender (teoría), Ejercicios resueltos (boletín), Practica (prácticas) y ¿Lo sé hacer? (comprueba). El mapa está en `TEMAS`, `EXAM` y `TOOLS` de `nav.js`. `features.js` `goTo()` llama a `GuiaNav.show()`. La barra está escrita en `web/tbar_alumna.html` y entra por la plantilla (`-V tbar=…`, con `<body class="tabs-mode at-home">`) para que se vea desde el primer momento, sin parpadeo del diseño antiguo. La guía del tutor sigue con la barra lateral. Nombres sencillos, sin fórmulas («desde cero», «en un minuto»…). Contenido a todo el ancho de la pantalla.
- `web/` — maquetación HTML: `build_web.py` (pandoc + `guia.lua`), `guia.css`, `guia.js`, `features.js`, `course.js` (prácticas, simulacros, vídeos, simulacro tipo test, comprobaciones), `plan.js` (plan de estudio adaptativo), `sheet/` (hoja de cálculo en el navegador). Todo se incrusta en un único HTML.
- **Carga rápida**: la hoja de cálculo (`sheet/`, 1,7 MB) va como texto (`#sheetlib-src`) y solo se ejecuta con `loadSheetLib()` cuando una práctica se ve por primera vez; cada práctica monta su hoja al verse (IntersectionObserver). Los Excel de descarga van en `#guia-files` y se leen al pulsar «Descargar» (`GUIA_DATA.fsize` tiene los tamaños). No vuelvas a montar todo al cargar.
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

## Historia y decisiones (para retomar)
- Empezó como guía personal para una alumna (TDAH, ansiedad, parte de cero). Ahora se comparte con su clase: **tono neutro, de tú, cercano y muy explicado**. Todo lo nuevo tiene que sonar igual que los temas: frases cortas, un ejemplo con números sencillos, recuadros Idea/Ojo/Truco/Excel. Nada de listas secas de fórmulas.
- Examen (21/10/2026, a 3 días): **en papel, 30 preguntas tipo test + 10 de respuesta corta**, como el modelo que la profesora enseñó en clase (`05r_modelo.md`). Calculadora como mucho. Las preguntas de Excel son de elegir/escribir la fórmula.
- El modelo de la profesora se deja visible a propósito. Sin créditos ni nombres.
- Los simulacros con Excel (S1, S2) quedan al final, "por si acaso".
- Modo claro por defecto; contenido a todo el ancho.
- Vídeos: tarjeta mediana al principio de cada tema/boletín; no darles más protagonismo que eso.
- Marcos prefiere ver un boceto o propuesta antes de cambios grandes.

## Pendiente / ideas
- Los vídeos no incluyen todavía lo añadido el 21/10: extrapolación, rectas con S_XY = 0, r y unidades, mosaico, tanto por uno.
- Los .docx de la guía están desactualizados (el usuario dijo que los dejáramos).
