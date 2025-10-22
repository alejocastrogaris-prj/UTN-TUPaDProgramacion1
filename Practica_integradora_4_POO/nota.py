class Nota:
    # Atributos: catedra (cadena), notaExamen (decimal)
    def __init__(self, catedra, nota_examen):
        self.catedra_name = catedra
        self.notaExamen = nota_examen

    def __str__(self):
        return f"Catedra: {self.catedra_name}, Nota: {self.notaExamen}"