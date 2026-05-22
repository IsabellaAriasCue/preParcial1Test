class NotaDuplicadaError(Exception):
    pass


class Estudiante:

    NOTA_MINIMA = 0.0
    NOTA_MAXIMA = 5.0
    NOTA_APROBACION = 3.0

    def __init__(self):
        self.notas = []

    def existe_nota(self, materia, semestre):

        for registro in self.notas:
            if (
                registro["materia"] == materia
                and registro["semestre"] == semestre
            ):
                return True

        return False

    def registrar_nota(self, materia, semestre, nota):

        if nota < self.NOTA_MINIMA or nota > self.NOTA_MAXIMA:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

        if self.existe_nota(materia, semestre):
            raise NotaDuplicadaError(
                "La materia ya tiene una nota registrada"
            )

        self.notas.append({
            "materia": materia,
            "semestre": semestre,
            "nota": nota
        })

    def aprobo(self, nota):
        return nota >= self.NOTA_APROBACION

    def calcular_promedio(self):

        if len(self.notas) == 0:
            return 0

        suma = sum(registro["nota"] for registro in self.notas)

        return suma / len(self.notas)