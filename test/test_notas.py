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