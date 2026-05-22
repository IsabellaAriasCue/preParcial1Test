Feature: Registro de notas académicas
  Como coordinador académico
  Quiero registrar notas de estudiantes
  Para controlar su rendimiento académico

  Background:
    Given un estudiante registrado

  @smoke
  Scenario Outline: Verificar aprobación de estudiantes
    When el estudiante obtiene una nota de <nota>
    Then el resultado debe ser "<estado>"

    Examples:
      | nota | estado    |
      | 2.9  | Reprueba  |
      | 3.0  | Aprueba   |
      | 4.5  | Aprueba   |

  @critical
  Scenario: Calcular promedio de notas
    Given que el estudiante tiene varias notas registradas
    When el sistema calcula el promedio
    Then el promedio debe ser 4.0

  @regression
  Scenario: No permitir materia duplicada en el mismo semestre
    Given que el estudiante ya registró una materia
    When intenta registrar nuevamente la misma materia y semestre
    Then el sistema debe mostrar un error

  @smoke
  Scenario: Permitir misma materia en diferente semestre
    Given que el estudiante ya registró una materia
    When registra la misma materia en otro semestre
    Then el registro debe realizarse correctamente

  @critical
  Scenario: Promedio sin notas
    When el sistema calcula el promedio
    Then el promedio debe ser 0.0

  @regression
  Scenario: Registrar nota inválida
    When el estudiante intenta registrar una nota de 6.0
    Then el sistema debe rechazar la nota