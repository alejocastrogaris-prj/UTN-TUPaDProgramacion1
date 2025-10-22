from computadora import Computadora
from componente_cpu import ComponenteCPU

class CostoComputadora:
    def main(self):
        
        while True:
            print("\n========================================")
            print("      COTICACIÓN DE PC    ") 
            print("==========================================")
            
            marca_comp = input("Marca de la PC: ").strip()
            modelo_comp = input("Modelo de la PC: ").strip()
            
            nueva_computadora = Computadora(marca_comp, modelo_comp)
            
            componentes_cargados = 0
            while True:
                componente_nombre = input("Nombre del Componente (o 'listo' para terminar): ").strip() 
                if componente_nombre.upper() == "LISTO":
                    break
                    
                marca_comp_cpu = input("Marca del Componente (Fabricante): ").strip()
                
                try:
                    cantidad_comp = int(input("Cantidad de unidades (entero): ")) 
                    precio_comp = float(input("Precio individual: $"))
                    
                    nuevo_componente = ComponenteCPU(componente_nombre, marca_comp_cpu, cantidad_comp, precio_comp)
                    
                    nueva_computadora.agregar_componente(nuevo_componente)
                    componentes_cargados += 1
                    
                except ValueError:
                    print("Error en cantidad o precio, debe ser número. Componente no se carga.")
                    continue
            
            if componentes_cargados == 0:
                print("No se cargaron componentes. PC no cotiza.")
            else:
                nueva_computadora.mostrar_cotizacion()
            
            respuesta = input("\n¿Quiere cotizar otra PC (SI/NO)? ").strip().upper()
            if respuesta == 'NO':
                print("Fin del sistema de cotizacion. ¡Hasta la próxima!")
                break
                
# Ejecución del main
if __name__ == "__main__":
    app = CostoComputadora()
    app.main()