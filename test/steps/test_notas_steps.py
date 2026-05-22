from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from app.estudiante import Estudiante, NotaDuplicadaError

scenarios("../features/notas.feature")


@given("un estudiante registrado", target_fixture="estudiante")
def estudiante():
    return Estudiante()


@given("que el estudiante tiene varias notas registradas")
def estudiante_con_notas(estudiante):
    estudiante.registrar_nota("Matematicas", "2025-1", 3.0)
    estudiante.registrar_nota("Fisica", "2025-1", 5.0)
    return estudiante


@given("que el estudiante ya registró una materia")
def estudiante_con_materia(estudiante):
    estudiante.registrar_nota("Matematicas", "2025-1", 4.0)
    return estudiante


@when(parsers.parse("el estudiante obtiene una nota de {nota:f}"))
def obtener_nota(estudiante, nota):
    estudiante.resultado = estudiante.aprobo(nota)


@then(parsers.parse('el resultado debe ser "{estado}"'))
def validar_resultado(estudiante, estado):

    if estado == "Aprueba":
        assert estudiante.resultado is True
    else:
        assert estudiante.resultado is False


@when("el sistema calcula el promedio")
def calcular_promedio(estudiante):
    estudiante.promedio = estudiante.calcular_promedio()


@then(parsers.parse("el promedio debe ser {promedio:f}"))
def validar_promedio(estudiante, promedio):
    assert estudiante.promedio == promedio


@when("intenta registrar nuevamente la misma materia y semestre")
def duplicar_materia(estudiante):

    with pytest.raises(NotaDuplicadaError):
        estudiante.registrar_nota("Matematicas", "2025-1", 3.0)


@then("el sistema debe mostrar un error")
def validar_error():
    assert True


@when("registra la misma materia en otro semestre")
def registrar_otro_semestre(estudiante):
    estudiante.registrar_nota("Matematicas", "2025-2", 3.5)


@then("el registro debe realizarse correctamente")
def validar_registro(estudiante):
    assert len(estudiante.notas) == 2


@when("el estudiante intenta registrar una nota de 6.0")
def nota_invalida(estudiante):

    with pytest.raises(ValueError):
        estudiante.registrar_nota("Fisica", "2025-1", 6.0)


@then("el sistema debe rechazar la nota")
def validar_rechazo():
    assert True