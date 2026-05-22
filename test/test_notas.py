import pytest

from app.estudiante import Estudiante


def test_registrar_nota_valida():
    estudiante = Estudiante()

    estudiante.registrar_nota("Matematicas", "2025-1", 4.0)

    assert len(estudiante.notas) == 1


def test_registrar_nota_invalida_menor_a_cero():
    estudiante = Estudiante()

    with pytest.raises(ValueError):
        estudiante.registrar_nota("Matematicas", "2025-1", -1.0)


def test_registrar_nota_invalida_mayor_a_cinco():
    estudiante = Estudiante()

    with pytest.raises(ValueError):
        estudiante.registrar_nota("Matematicas", "2025-1", 6.0)

#RF2

def test_aprueba_con_nota_tres():
    estudiante = Estudiante()

    assert estudiante.aprobo(3.0) is True

def test_reprueba_con_nota_menor_a_tres():
    estudiante = Estudiante()

    assert estudiante.aprobo(2.9) is False

#RF3

def test_calcular_promedio():
    estudiante = Estudiante()

    estudiante.registrar_nota("Matematicas", "2025-1", 3.0)
    estudiante.registrar_nota("Fisica", "2025-1", 5.0)

    assert estudiante.calcular_promedio() == 4.0



def test_promedio_sin_notas():
    estudiante = Estudiante()

    assert estudiante.calcular_promedio() == 0

#RF4

def test_no_permitir_materia_duplicada():
    estudiante = Estudiante()

    estudiante.registrar_nota("Matematicas", "2025-1", 4.0)

    with pytest.raises(NotaDuplicadaError):
        estudiante.registrar_nota("Matematicas", "2025-1", 3.0)



def test_permitir_misma_materia_distinto_semestre():
    estudiante = Estudiante()

    estudiante.registrar_nota("Matematicas", "2025-1", 4.0)

    estudiante.registrar_nota("Matematicas", "2025-2", 3.5)

    assert len(estudiante.notas) == 2