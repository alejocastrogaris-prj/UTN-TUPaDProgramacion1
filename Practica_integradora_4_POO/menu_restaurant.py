from plato import Plato
from ingrediente import Ingrediente

class MenuRestaurant:
    def main(self):
        platos_menu = []
        
        while True:
            print("\n--- CARGA DE PLATO O BEBIDA ---")
            
            nombre_plato = input("Nombre del Plato/Bebida (o 'listo' para terminar): ").strip()
            if nombre_plato.upper() == "LISTO":
                break
                
            try:
                precio_plato = float(input("Precio (Solo números!): $"))
            except ValueError:
                print("El precio debe ser un número. Plato no cargado, ERROR.")
                continue
                
            es_bebida_str = input("Es Bebida? (S/N/No): ").strip().upper()
            es_bebida = es_bebida_str == 'S'
            
            nuevo_plato = Plato(nombre_plato, precio_plato, es_bebida)
            
            ingredientes_cargados = 0
            
            if not es_bebida:
                print("\n-- Carga de Ingredientes (Si es plato) --")
                while True:
                    nombre_ing = input("Nombre del Ingrediente (o Enter para terminar): ").strip()
                    if not nombre_ing:
                        break
                        
                    try:
                        cantidad_ing = float(input("Cantidad (decimal): "))
                        unidad_ing = input("Unidad de Medida (ej. gramos, unidades, kg): ").strip()
                        
                        nuevo_ingrediente = Ingrediente(nombre_ing, cantidad_ing, unidad_ing)
                        nuevo_plato.agregar_ingrediente(nuevo_ingrediente)
                        ingredientes_cargados += 1
                        
                    except ValueError:
                        print("La cantidad debe ser un número. ¡Dale de nuevo!")
                        continue
                        
            if not es_bebida and ingredientes_cargados == 0:
                print("AVISO: Plato sin ingredientes. La consigna dice que es obligatorio al menos 1, pero lo voy a cargar igual.")

            platos_menu.append(nuevo_plato)
            print(f"Plato/Bebida '{nombre_plato}' cargado. OK.")
            
            continuar = input("\n¿Cargar otro? (S/N): ").strip().upper()
            if continuar == 'N':
                break

        print("\n\n==================================")
        print("                 MENÚ RESTAURANT                 ")
        print("   ====================================")
        
        for plato in platos_menu:
            print(plato) 
            print("-------------------------------------------------")
            
# Ejecución del main
if __name__ == "__main__":
    app = MenuRestaurant()
    app.main()