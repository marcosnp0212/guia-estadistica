# ¿Qué me están pidiendo? Traductor de enunciados

::: {custom-style="Idea"}
**🧠 Para qué sirve.** Muchas veces lo difícil no es la cuenta, sino saber **qué cuenta** hay que hacer. Busca en el enunciado una frase parecida a las de la izquierda. La columna del medio te dice qué calcular; la de la derecha, con qué función y dónde está explicado.
:::

::: {custom-style="Truco"}
**💡 Truco.** Con el buscador de la guía (tecla /) puedes escribir una palabra del enunciado, por ejemplo «homogéneo» o «términos reales», y te trae esta tabla y el apartado que lo explica.
:::

## Tema 1: una variable

| Si el enunciado dice… | Te están pidiendo… | Cómo / dónde |
|:---|:---|:---|
| "valor medio", "promedio", "por término medio" | La **media** | `=PROMEDIO(datos)` · con tabla, `SUMAPRODUCTO`. [Ver 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "el más frecuente", "el más habitual", "el que más se repite" | La **moda**. Con intervalos de distinta amplitud, por **densidad** | `=MODA.UNO(datos)` · fórmula de la moda. [Ver 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "valor central", "la mitad tiene menos de…" | La **mediana** | `=MEDIANA(datos)` · primera Nᵢ ≥ n/2. [Ver 1.5](#medidas-de-posición-central-media-mediana-y-moda) |
| "el 25 % que menos…" | **Primer cuartil** (P₂₅) | `=CUARTIL.INC(datos;1)`. [Ver 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "estar entre el 25 % que más…" | **Tercer cuartil** (P₇₅) | `=CUARTIL.INC(datos;3)`. [Ver 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "el X % que más…", "a partir de cuánto se está en el X % superior" | **Percentil 100 − X** | `=PERCENTIL.INC(datos;0,9)` para el 10 % que más. [Ver 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "como mucho, para estar en el X % que menos…" | **Percentil X** | `=PERCENTIL.INC(datos;X/100)`. [Ver 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "entre qué valores está el 50 % central" | **C₁ y C₃** | [Ver 1.6](#cuantiles-cuartiles-deciles-y-percentiles) |
| "entre qué valores está el 30 % central" | **P₃₅ y P₆₅** (deja 35 % a cada lado) | Ejercicio 13 del boletín |
| "cuántos tienen más de k" · "al menos k" · "menos de k" | Contar. **"Más de" no incluye k**; "al menos" sí | `=CONTAR.SI(datos;">k")` · `">=k"` · `"<k"` |
| "dispersión", "variabilidad", "cuánto se separan" | **Varianza** o **desviación típica** | `=VAR.P` · `=DESVEST.P`. [Ver 1.7](#medidas-de-dispersión) |
| "más homogéneo", "media más representativa", "variabilidad relativa", grupos con medias distintas | **Coeficiente de variación**. El menor es el más homogéneo | `=DESVEST.P(r)/PROMEDIO(r)`. [Ver 1.7](#medidas-de-dispersión) |
| "cuasivarianza", "varianza muestral corregida" | Dividir entre **n − 1** | `=VAR.S` · `=DESVEST.S` |
| "forma", "simétrica", "cola" | **Asimetría** (mira el signo) | `=COEFICIENTE.ASIMETRIA.P`. [Ver 1.8](#medidas-de-forma-asimetría-y-curtosis) |
| "picuda", "aplanada", "apuntamiento" | **Curtosis** (mira el signo) | `=CURTOSIS`. [Ver 1.8](#medidas-de-forma-asimetría-y-curtosis) |
| "valores atípicos", "diagrama de caja" | Límites C₁ − 1,5·IQR y C₃ + 1,5·IQR | [Ver 1.10](#valores-atípicos-y-diagrama-de-caja-boxplot) |
| "comparar la nota (o el salario) de alguien en dos grupos distintos" | **Tipificar**: z = (x − media)/S | `=NORMALIZACION(x;media;S)`. [Ver 1.9](#tipificar-estandarizar-una-variable) |
| "media de toda la empresa" con medias de grupos de distinto tamaño | **Media ponderada** | `=SUMAPRODUCTO(medias;tamaños)/SUMA(tamaños)` |
| "varianza de todos" a partir de grupos | **Varianza dentro + varianza entre** | [Ver 1.7](#medidas-de-dispersión) |
| "% de la variabilidad debido a las diferencias entre grupos", "desigualdad" | Varianza **entre** ÷ varianza **total** | Ejercicio 21 del boletín |
| "todos suben X €" / "suben un X %": ¿qué pasa con media y varianza? | Sumar: la media sube X y la varianza **no cambia**. Multiplicar por a: media × a, varianza × **a²** | Ejercicio 22 del boletín |

## Tema 2: dos variables

| Si el enunciado dice… | Te están pidiendo… | Cómo / dónde |
|:---|:---|:---|
| "distribución marginal de X" | Los **totales** de las filas (o de las columnas, para Y) | [Ver 2.2](#distribuciones-marginales) |
| "distribución de Y condicionada a X = …", "de los que…, ¿qué %…?" | Esa **fila** (o columna) dividida entre **su** total | [Ver 2.3](#distribuciones-condicionadas) |
| "¿son independientes?", "¿influye X en Y?", "¿depende…?" | Comparar fᵢⱼ con fᵢ.·f.ⱼ en **todas** las casillas | [Ver 2.4](#independencia) |
| "frecuencias relativas" de una tabla de doble entrada | Cada casilla ÷ n | `=B3/$E$6` |

## Tema 3: regresión

| Si el enunciado dice… | Te están pidiendo… | Cómo / dónde |
|:---|:---|:---|
| "recta que explica Y a partir de X", "Y en función de X" | **Recta de Y sobre X**: Ŷ = a + b·X | `=PENDIENTE(Y;X)` · `=INTERSECCION.EJE(Y;X)`. [Ver 3.3](#la-recta-de-regresión) |
| "cuánto cambia Y por cada unidad de X" | La **pendiente** b | [Ver 3.3](#la-recta-de-regresión) |
| "grado o intensidad de la relación lineal", "sentido" | **Correlación** r | `=COEF.DE.CORREL(X;Y)`. [Ver 3.4](#coeficiente-de-correlación-r-y-de-determinación-r²) |
| "bondad del ajuste", "% explicado", "¿es fiable la recta?" | **R²** (en %) | `=COEFICIENTE.R2(Y;X)`. [Ver 3.4](#coeficiente-de-correlación-r-y-de-determinación-r²) |
| "% que NO explica" | **1 − R²** | Ejercicio 3 del boletín del Tema 3 |
| "¿cuánto se espera de Y si X vale…?", "estima", "predice" | **Sustituir X** en la recta | `=PRONOSTICO.LINEAL(x;Y;X)`. [Ver 3.5](#predicciones) |
| "¿relación directa o inversa?", "variación conjunta" | **Covarianza** (signo) | `=COVARIANZA.P(X;Y)`. [Ver 3.2](#la-covarianza) |
| Te dan medias, S y Sxy (o r) pero no los datos | b = Sxy/Sx² · a = ȳ − b·x̄ · r = Sxy/(Sx·Sy) | [Ver 3.6](#fórmulas-útiles-para-ejercicios-sin-datos) |

## Tema 4: números índices

| Si el enunciado dice… | Te están pidiendo… | Cómo / dónde |
|:---|:---|:---|
| "índice con base 20XX", "evolución respecto a 20XX" | **Índice simple**: valor ÷ valor del año base × 100 | `=B3/$B$2*100`. [Ver 4.1](#índice-simple) |
| "tasa de variación", "cuánto ha subido o bajado" | Valor ÷ anterior − 1 | `=B3/B2-1`. [Ver 4.2](#tasa-de-variación) |
| "cambia la base a 20XX" | Dividir toda la serie entre el índice de 20XX | [Ver 4.4](#cambio-de-base) |
| "subió un X % y luego bajó un Y %" (en total) | **Multiplicar**: (1 + X)·(1 − Y) | [Ver 4.3](#propiedades-de-los-índices) |
| "tasa media anual", "crecimiento medio por año" | **Media geométrica**: (1 + T)^(1/años) − 1 | `=MEDIA.GEOM` · `=(1+T)^(1/k)-1`. [Ver 4.5](#media-geométrica-y-tasas-medias) |
| "tasa mensual equivalente" a una anual | (1 + anual)^(1/12) − 1 | [Ver 4.5](#media-geométrica-y-tasas-medias) |
| "A superó en un X % a B" | A = (1 + X/100)·B → **B = A ÷ (1 + X/100)** | Ejercicios 1 y 2 del Tema 4 |
| "índice de precios con las cantidades del año base" | **Laspeyres** | [Ver 4.6](#índices-complejos-de-varios-productos) |
| "con las cantidades actuales" | **Paasche** | [Ver 4.6](#índices-complejos-de-varios-productos) |
| "índice de Fisher" | √(Laspeyres · Paasche) | [Ver 4.6](#índices-complejos-de-varios-productos) |
| "en términos reales", "euros constantes", "poder adquisitivo", "deflactar" | Nominal ÷ IPC × 100 | `=B2/C2*100`. [Ver 4.7](#deflactar-de-euros-nominales-a-euros-reales) |
| "¿está bien actualizado el salario (o el alquiler)?" | Comparar con: valor × IPC nuevo ÷ IPC viejo | Ejercicios 4 y 11 del Tema 4 |

# Tus archivos para el examen

En el examen puedes usar el ordenador, **tus prácticas de clase** y **un solucionario**. Conviene llegar sabiendo qué hay en cada archivo, para encontrarlo en segundos.

## Las prácticas de clase

| Archivo | Qué tiene dentro | Te sirve para |
|:---|:---|:---|
| Tema1_semana_1 | *Hermanos*: tabla de frecuencias, media, mediana, moda, cuantiles. *Longitudes*: contar por intervalos con FRECUENCIA, densidades. *EncuestaPresupuestosFamiliares*: porcentajes de gasto. | Tablas de frecuencias, medidas de posición, intervalos |
| Tema1_semana2 | Lo anterior y además: dispersión en *Hermanos* (rango, IQR, varianza, cuasivarianza, desviaciones, CV). *Hoja1*: CV de dos sectores. *Salarios_cambios_origen_escala*: cambios de origen y escala y la media ponderada («MEDIA MAL»). *EJEMPLO3_MODA_MEDIANA_TABLAS*: moda y mediana con intervalos. | Todo el Tema 1 |
| DatosTema2_semana_3 y _4 | *tabla_correlación*: edad y antigüedad con tabla dinámica y formato condicional. *tabla_contingencia*: departamento y modalidad, frecuencias relativas y fᵢ.×f.ⱼ. *tabla_contingencia_sexo_contrat*: ejemplo de independencia. | Tema 2 |
| DatosTema3_semana_4 | Lo del Tema 2 y la hoja *Antig_Salario*: covarianza, correlación, R², recta y predicción. | Tema 3 |

::: {custom-style="Ojo"}
**⚠️ Ojo.** Del Tema 4 no hay práctica de clase entre los archivos de esta guía. Si en clase hicisteis alguna, añádela a la carpeta. Si no, practica con los ejercicios del Tema 4 y con las prácticas autocorregidas 7 y 8.
:::

## Tu solucionario

::: {custom-style="Ojo"}
**⚠️ Si el examen es en papel.** Si al final no se puede llevar ordenador ni material, el solucionario y las prácticas de clase no se usan en el examen. Siguen siendo útiles para estudiar: para comprobar en Excel lo que hayas hecho a mano.
:::

Tu solucionario es el archivo **Solucionario_estadistica**, que descargas en el apartado siguiente. Es un único Excel con tres partes:

- El **traductor de enunciados**, con enlaces a la calculadora y al ejercicio resuelto de cada tipo de pregunta.
- **12 calculadoras**: pegas los datos y salen los resultados (media, cuartiles, varianzas, moda y mediana con intervalos, grupos, tablas de doble entrada, regresión, índices, Laspeyres, deflactar…).
- **Todos los ejercicios resueltos** de los apuntes y de los boletines, con las fórmulas a la vista.

En el examen: busca la frase en el traductor, salta a la hoja, **haz una copia de la hoja** (clic derecho en la pestaña → Mover o copiar → Crear una copia) y cambia los datos por los del examen. Úsalo también durante estas semanas para comprobar tus resultados: así el día del examen ya sabrás moverte por él.

::: {custom-style="Truco"}
**💡 Antes del examen.** Crea una carpeta «Examen estadística» con tus prácticas de clase y tu solucionario. Pon a cada archivo un nombre que entiendas, por ejemplo «T1 dispersión» o «T3 regresión». Ábrelos todos al empezar el examen.
:::

# Descargas

Todos los archivos van guardados dentro de esta guía. Pulsa para descargarlos.

::: {.descarga data-file="Solucionario_estadistica.xlsx"}
**Solucionario** (el que llevas al examen si se permite). Traductor, calculadoras y todos los ejercicios resueltos en un solo Excel.
:::

::: {.descarga data-file="Practicas_autocorregidas.xlsx"}
**Prácticas en Excel.** Las mismas prácticas de esta guía, para hacerlas dentro de Excel; las casillas se ponen verdes o rojas.
:::

::: {.descarga data-file="Simulacros_autocorregidos.xlsx"}
**Simulacros en Excel.** Los simulacros 1 y 2, con nota automática. (El 3, en papel, está solo en esta guía.)
:::

::: {.descarga data-file="Plantillas_estadistica.xlsx"}
**Calculadoras** sueltas, con el traductor (también están dentro del solucionario).
:::

::: {.descarga data-file="Estadistica_ejercicios_resueltos.xlsx"}
**Ejercicios resueltos** sueltos (también están dentro del solucionario).
:::
