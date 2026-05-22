class Estudiante:

    def __init__(self):
        self.notas = []

    def registrar_nota(self, materia, semestre, nota):

        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

        self.notas.append({
            "Materia": materia,
            "Semestre": semestre,
            "Nota": nota
        })