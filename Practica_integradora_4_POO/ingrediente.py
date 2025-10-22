class Ingrediente:
    def __init__(self, nombre, cantidad, unidad_medida):
        self.nombre = nombre
        self.cant_decimal = cantidad
        self.unidad_de_medida = unidad_medida 

    def __str__(self):
        # salida para el menu
        return f"{self.nombre:<15} {self.cant_decimal:>8.2f} {self.unidad_de_medida}"