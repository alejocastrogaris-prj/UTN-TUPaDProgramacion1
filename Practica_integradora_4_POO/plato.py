class Plato:
    def __init__(self, nombre_completo, precio, es_bebida):
        self.nombreCompleto_plato = nombre_completo 
        self.precio = precio
        self.esBebida = es_bebida
        self.lista_ingredientes = [] 

    def agregar_ingrediente(self, ingrediente):
        self.lista_ingredientes.append(ingrediente)

    def __str__(self):
        info = f"\n{self.nombreCompleto_plato}"
        info += f"\nPrecio: $ {self.precio:.2f}"
        
        if not self.esBebida:
            info += "\nIngredientes:"
            info += "\nNombre          Cantidad Unidad de Medida" 
            if self.lista_ingredientes:
                for ingrediente in self.lista_ingredientes:
                    info += f"\n{ingrediente}" 
            else:
                info += "\n[No hay ingredientes, pero no es bebida... Raro.]"

        return info