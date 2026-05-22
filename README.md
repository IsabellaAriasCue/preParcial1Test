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

## 1.2 Análisis de valores límite

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

---
