# Por si el examen fuera con ordenador

Según el modelo de la profesora, el examen es en papel y tipo test. Esto queda aquí **por si acaso**: si al final se permitiera el ordenador, aquí están los simulacros con Excel, qué archivos llevar y una lista de comprobación.

## Simulacro con Excel 1

::: {.simulacro data-sim="S1"}
:::

## Simulacro con Excel 2

::: {.simulacro data-sim="S2"}
:::


## Tus archivos para el examen

En el examen puedes usar el ordenador, **tus prácticas de clase** y **un solucionario**. Conviene llegar sabiendo qué hay en cada archivo, para encontrarlo en segundos.

### Las prácticas de clase

| Archivo | Qué tiene dentro | Te sirve para |
|:---|:---|:---|
| Tema1_semana_1 | *Hermanos*: tabla de frecuencias, media, mediana, moda, cuantiles. *Longitudes*: contar por intervalos con FRECUENCIA, densidades. *EncuestaPresupuestosFamiliares*: porcentajes de gasto. | Tablas de frecuencias, medidas de posición, intervalos |
| Tema1_semana2 | Lo anterior y además: dispersión en *Hermanos* (rango, IQR, varianza, cuasivarianza, desviaciones, CV). *Hoja1*: CV de dos sectores. *Salarios_cambios_origen_escala*: cambios de origen y escala y la media ponderada («MEDIA MAL»). *EJEMPLO3_MODA_MEDIANA_TABLAS*: moda y mediana con intervalos. | Todo el Tema 1 |
| DatosTema2_semana_3 y _4 | *tabla_correlación*: edad y antigüedad con tabla dinámica y formato condicional. *tabla_contingencia*: departamento y modalidad, frecuencias relativas y fᵢ.×f.ⱼ. *tabla_contingencia_sexo_contrat*: ejemplo de independencia. | Tema 2 |
| DatosTema3_semana_4 | Lo del Tema 2 y la hoja *Antig_Salario*: covarianza, correlación, R², recta y predicción. | Tema 3 |

::: {custom-style="Ojo"}
**⚠️ Ojo.** Del Tema 4 no hay práctica de clase entre los archivos de esta guía. Si en clase hicisteis alguna, añádela a la carpeta. Si no, practica con los ejercicios del Tema 4 y con las prácticas autocorregidas 7 y 8.
:::

### Tu solucionario

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


## Lista de comprobación del examen con Excel

**Antes de empezar**

- Abre tus prácticas de clase y tu solucionario antes de empezar. Ten el traductor a mano.
- Lee todo el examen una vez, sin calcular. Marca qué tema es cada pregunta. Si dudas qué te piden, mira el traductor de enunciados.
- Empieza por la que te dé más seguridad. Sumar puntos pronto quita nervios.

**Para cada ejercicio**

1. Escribe en una celda el **título** del ejercicio y del apartado (así no te pierdes y quien corrige lo encuentra).
2. Copia o escribe los datos en **columnas con título**.
3. Haz una columna por cada paso (marca de clase, xᵢ·nᵢ, xᵢ²·nᵢ, Nᵢ...). Ver los pasos te tranquiliza y, si hay un error, se localiza.
4. Pon al lado de cada resultado una **etiqueta** ("Media =", "Varianza =").
5. Escribe la **frase de interpretación** en una celda de texto. Muchas veces vale tanto como el número.

**Comprobaciones rápidas antes de entregar**

- ¿Las frecuencias relativas suman 1? ¿La última acumulada es n?
- ¿La media está entre el mínimo y el máximo?
- ¿La varianza es positiva? (Si sale negativa, hay un error seguro: probablemente olvidaste el cuadrado o el orden de la resta.)
- ¿r está entre −1 y 1? ¿R² entre 0 y 1? ¿r tiene el mismo signo que la pendiente?
- ¿El año base vale 100?
- ¿Has usado **VAR.P** (no VAR.S) salvo que pidan cuasivarianza?
- ¿En PENDIENTE e INTERSECCION.EJE pusiste **primero la Y**?
- Guarda el archivo cada poco (**Ctrl + G**).

**Atajos que ayudan**

| Atajo | Para qué |
|:---|:---|
| Ctrl + Z | Deshacer |
| Ctrl + G | Guardar |
| F4 | Poner los $ en una referencia mientras la escribes |
| F2 | Editar la celda (ver la fórmula) |
| Pestaña Fórmulas → Mostrar fórmulas | Ver todas las fórmulas de la hoja en vez de los resultados (pulsa otra vez para volver) |
| Doble clic en la esquina de una celda | Arrastrar la fórmula hasta el final de los datos |

**Errores que te puede mostrar Excel y qué significan**

| Error | Qué ha pasado |
|:---|:---|
| `#¡DIV/0!` | Estás dividiendo entre una celda vacía o 0. Suele ser un $ olvidado. |
| `#¿NOMBRE?` | Has escrito mal el nombre de una función (por ejemplo, PROMEDIO sin tilde está bien; MEDIA no existe). |
| `#¡VALOR!` | Hay texto donde debería haber un número (por ejemplo, un número escrito con punto en vez de coma). |
| `#N/A` | Falta un dato o un rango no tiene el tamaño correcto. |
| `####` | La columna es estrecha. Ensánchala con doble clic en el borde. |
