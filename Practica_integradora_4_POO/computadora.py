from componente_cpu import ComponenteCPU

class Computadora:
    def __init__(self, marca, modelo):
        self.marca_pc = marca 
        self.modelo = modelo
        self.lista_componentes = []

    def agregar_componente(self, componente):
        self.lista_componentes.append(componente)

    def calcular_costo_total(self):
        costo_total = 0.0
        for comp in self.lista_componentes:
            costo_total += comp.precio_unitario * comp.cantidad_usada #
        return costo_total

    def calcular_precio_sugerido(self):
        costo_total = self.calcular_costo_total()
        
        if costo_total <= 50000.00001: # <-- Puse un decimal extra por las dudas
            porcentaje = 0.40 
        else:
            porcentaje = 0.30
            
        precio_sugerido = costo_total + (costo_total * porcentaje)
        return precio_sugerido

    def mostrar_cotizacion(self):
        costo = self.calcular_costo_total()
        precio_sugerido = self.calcular_precio_sugerido()

        print("\n--- Detalles de la PC Cotizada ---")
        print(f"Marca: {self.marca_pc}")
        print(f"Modelo: {self.modelo}")

        print("\nComponentes:")
        if not self.lista_componentes:
            print("No se cargaron componentes. No hay cotizacion.")
            return

        print("-" * 75)
        print(f"{'Componente':<25}{'Marca':<10}{'Cant.':>8}{'Precio X Ud.':>15}{'SubTotal':>15}")
        print("-" * 75)
        
        for comp in self.lista_componentes:
            print(
                f"{comp.nombre_comp:<25}{comp.marca:<10}"
                f"{comp.cantidad_usada:>8}{comp.precio_unitario:>15.2f}"
                f"{comp.calcular_subtotal():>15.2f}"
            )

        print("-" * 75)
        print(f"{'Costo Total':>58}: ${costo:>14.2f}")
        print(f"El precio sugerido de venta es: ${precio_sugerido:>13.2f}")