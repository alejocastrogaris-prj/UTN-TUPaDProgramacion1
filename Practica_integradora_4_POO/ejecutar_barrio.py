from barrio import Barrio
from vivienda import Vivienda, SuperficieCubiertaExcepcion
from habitacion import Habitacion

class EjecutarBarrio:
    def main(self):
        print("--- INICIO DE LA ASOCIACIÓN DE BARRIO Y VIVIENDAS ---")
        
        # 1. Crear Habitaciones
        h1 = Habitacion("Dormitorio Ppal", 15.0)
        h2 = Habitacion("Baño", 5.0)
        h3 = Habitacion("Cocina-Comedor", 25.0)
        h4 = Habitacion("Quincho", 30.0)

        # 2. Crear Viviendas
        v1 = Vivienda("Los Pinos", 101, "A", 1, 150.0)
        v1.agregar_habitacion(h1)
        v1.agregar_habitacion(h2)
        v1.agregar_habitacion(h3)
        
        v2 = Vivienda("Los Pinos", 102, "B", 5, 120.0)
        v2.agregar_habitacion(h1)
        v2.agregar_habitacion(h3)
        
        # Vivienda 3: Cubierta MAYOR al Terreno (15+5+30 = 50.0, Terreno 40.0)
        v3 = Vivienda("Los Pinos", 103, "A", 10, 40.0)
        v3.agregar_habitacion(h1)
        v3.agregar_habitacion(h2)
        v3.agregar_habitacion(h4)
        
        # 3. Crear Barrio y asociar Viviendas
        barrio_utn = Barrio("El Retiro", "Constructora UTN")
        barrio_utn.agregar_vivienda(v1)
        barrio_utn.agregar_vivienda(v2)
        barrio_utn.agregar_vivienda(v3)
        
        print(f"\nBarrio cargado: {barrio_utn.nombre_barrio}")
        
        print("\n--- RESULTADOS DE LOS MÉTODOS ---")

        # Ejecución a)
        total_terreno = barrio_utn.getSuperficieTotalTerreno()
        print(f"a) Terreno Total del Barrio: {total_terreno:.2f} m²")
        
        # Ejecución b)
        manzana_a = "A"
        terreno_manzana_a = barrio_utn.getSuperficieTotalTerrenoXManzana(manzana_a)
        print(f"b) Terreno de la Manzana '{manzana_a}': {terreno_manzana_a:.2f} m²")
        
        # Ejecución c)
        print("\nc) Metros Cubiertos por Vivienda (con validación):")
        
        try:
            cubierta_v1 = v1.getMetrosCuadradosCubiertos()
            print(f"   V1 (Manz A) - Cubierta: {cubierta_v1:.2f} m²")
        except SuperficieCubiertaExcepcion as e:
            print(f"   V1 - ERROR: {e}")
            
        try:
            cubierta_v3 = v3.getMetrosCuadradosCubiertos()
            print(f"   V3 (Manz A) - Cubierta: {cubierta_v3:.2f} m²")
        except SuperficieCubiertaExcepcion as e:
            print(f"   V3 - ERROR: {e}")

        # Ejecución d)
        total_cubierta = barrio_utn.getSuperficieTotalCubierta()
        print(f"\nd) Cubierta Total del Barrio: {total_cubierta:.2f} m² (La V3 debería haber fallado y no se suma!)")
        
# Ejecución del main
if __name__ == "__main__":
    app = EjecutarBarrio()
    app.main()