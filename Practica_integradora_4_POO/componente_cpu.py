class ComponenteCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.nombre_comp = componente 
        self.marca = marca
        self.cantidad_usada = cantidad 
        self.precio_unitario = precio

    def calcular_subtotal(self):
        return self.precio_unitario * self.cantidad_usada
    
    def __str__(self):
        return f"Comp: {self.nombre_comp}, SubTotal: ${self.calcular_subtotal():.2f}"