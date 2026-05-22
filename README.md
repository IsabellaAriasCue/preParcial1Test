# Preparcial

Proyecto desarrollado para la asignatura Pruebas de Software aplicando TDD, BDD y CI/CD. 

## Tecnologías utilizadas

- Python 3.12
- UV
- Pytest
- Pytest-BDD
- GitHub Actions

## Justificación de tecnologías

Se eligió Python porque es el lenguaje que actualmente más se me facilita.

## PARTE 1 — Análisis escrito
- Restricción del mínimo y máximo de la nota que se puede ingresar: 0.0 y 5.0.
- La nota minima para aprobar es 3.0 - RN
- No se puede registrar dos notas para la misma materia. - RN
- El sistema determina si el estudiante aprueba o reprueba una materia basandose en las restricciones y reglas mencionadas anteriormente.
- El sistema calcula el promedio.

## 1.1 — Particiones de equivalencia
| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida inferior a 3.0 | 0.0 a 2.9 | 2.5 | Registro exitoso |
| Válida aprobación  >= 3 | 3.0 a 5.0 | 4.0 | Registro exitoso |
| Inválida menor    < 0 | Menor a 0.0 | -1.0 | Error de validación |
| Inválida mayor     > 5 | Mayor a 5.0 | 5.5 | Error de validación |

## 1.2 - Análisis de valores límite

| Valor | Dentro/Fuera | Resultado esperado |
|---|---|---|
| -0.1 | Fuera | Error |
| 0.0 | Dentro | Registro exitoso |
| 0.1 | Dentro | Registro exitoso |
| 2.9 | Dentro | Reprueba |
| 3.0 | Dentro | Aprueba |
| 3.1 | Dentro | Aprueba |
| 4.9 | Dentro | Registro exitoso |
| 5.0 | Dentro | Registro exitoso |
| 5.1 | Fuera | Error |

## 1.3 — Preguntas al Product Owner

### Pregunta 1
¿La validación de duplicados debe tener en cuenta diferencias entre mayúsculas y minúsculas?

Justificación:
Esto afecta los casos de prueba relacionados con materias como “Programación” y “programación”.

### Pregunta 2
¿El estudiante puede registrar nuevamente una nota de la misma materia si ya se encuentra en otro semestre?

Justificación:
Esta pregunta impacta el diseño de los casos de prueba porque permite definir si la validación de duplicados debe hacerse 
únicamente por materia o por la combinación de materia y semestre.

---
## PARTE 2 — Diseño de casos de prueba
| ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | RF1 | Registrar nota válida | Estudiante creado | 4.0 | Registrar nota | Registro exitoso | Positivo |
| CP-02 | RF1 | Registrar nota negativa | Estudiante creado | -1.0 | Registrar nota | Error | Negativo |
| CP-03 | RF1 | Registrar nota límite 5.0 | Estudiante creado | 5.0 | Registrar nota | Registro exitoso | Borde |
| CP-04 | RF2 | Aprobar con 3.0 | Nota registrada | 3.0 | Consultar estado | Aprueba | Borde |
| CP-05 | RF2 | Reprobar con 2.9 | Nota registrada | 2.9 | Consultar estado | Reprueba | Borde |
| CP-06 | RF2 | Aprobar con 4.5 | Nota registrada | 4.5 | Consultar estado | Aprueba | Positivo |
| CP-07 | RF3 | Calcular promedio | Varias notas registradas | 3.0, 4.0 | Calcular promedio | 3.5 | Positivo |
| CP-08 | RF3 | Promedio sin notas | Sin notas | Ninguna | Calcular promedio | 0 | Negativo |
| CP-09 | RF3 | Promedio con una nota | Nota registrada | 5.0 | Calcular promedio | 5.0 | Positivo |
| CP-10 | RF4 | Duplicar materia mismo semestre | Nota existente | Matemáticas - 2025-1 | Registrar nuevamente | Error | Negativo |
| CP-11 | RF4 | Registrar misma materia diferente semestre | Nota existente | Matemáticas - 2025-2 | Registrar nota | Registro exitoso | Positivo |
| CP-12 | RF4 | Registrar materia diferente | Nota existente | Física - 2025-1 | Registrar nota | Registro exitoso | Positivo |

## PARTE 3 — Evidencia TDD

Se implementó cada requerimiento siguiendo el ciclo:

1. RED → creación de tests fallando
2. GREEN → implementación mínima
3. REFACTOR → mejora del código

El historial de commits evidencia este proceso.

## PARTE 4 — BDD

Se implementaron escenarios Gherkin para:

- Aprobación y reprobación
- Cálculo de promedio
- Validación de materias duplicadas

Todos los escenarios fueron automatizados mediante pytest-bdd.

## PARTE 5 — Pipeline CI/CD 

Configurado en GitHub Actions para que los tests corran automáticamente en cada push a la rama principal.

---

## PARTE 6 — Reflexión 


##### ¿Qué diferencia notaste entre diseñar los casos de prueba en la tabla antes de escribir código versus simplemente ponerte a programar directamente?

- Personalmente yo creo que ayuda a no pasarse cosas importantes por alto y facilita la generación de las pruebas en código ya que al leer los casos de prueba la mente tiene MAYOR facilidad de plasmarlos
en código debido a la estructura que brinda cada campo de la tabla a la prueba.
  

##### ¿Qué fue lo más difícil de seguir el ciclo TDD y en qué momento sentiste la tentación de saltarte algún paso?

- Considero que en el **Green**, ya que o veo la necesidad de dejarlo ya "Refactorizado" o no encuentro otra manera diferente de hacer el **green** y cuando 
paso a **Refactor** no encuentro otra manera de hacerlo.
