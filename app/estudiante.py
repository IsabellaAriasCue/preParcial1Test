class Estudiante:

    NOTA_MINIMA = 0.0
    NOTA_MAXIMA = 5.0
    NOTA_APROBACION = 3.0

    def __init__(self):
        self.notas = []

    def registrar_nota(self, materia, semestre, nota):

        if nota < self.NOTA_MINIMA or nota > self.NOTA_MAXIMA:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

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

        suma = 0

        for registro in self.notas:
            suma += registro["nota"]

        return suma / len(self.notas)