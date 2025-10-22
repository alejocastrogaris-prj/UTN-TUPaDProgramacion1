from alumno import Alumno
from nota import Nota

class CargaNotas:
    def main(self):
        alumnos_guardados = []
        
        while True:
            print("\n--- INGRESO DE NUEVO ALUMNO ---")
            
            nombre_completo = input("INGRESE NOMBRE COMPLETO: ").strip()
            if not nombre_completo:
                print("El nombre no puede estar vacío, se sale de la carga.")
                break
            
            try:
                legajo = int(input("INGRESE LEGAJO: "))
            except ValueError:
                print("El legajo debe ser un número entero. Error. Se saltea este alumno.")
                continue

            nuevo_alumno = Alumno(nombre_completo, legajo)
            
            notas_cargadas = 0
            while True:
                print("\n- Ingreso de Nueva Nota -")
                nombre_catedra = input("INGRESE NOMBRE CATEDRA (o Enter para salir YA): ").strip()
                
                if not nombre_catedra:
                    break
                    
                try:
                    nota_examen = float(input("Nota (usar punto para decimal): "))
                    
                    nueva_nota = Nota(nombre_catedra, nota_examen)
                    
                    nuevo_alumno.agregar_nota(nueva_nota)
                    notas_cargadas += 1
                    
                except ValueError:
                    print("La nota debe ser un número decimal. **Error de tipeo**")
                    continue
                salir_notas = input("DESEA SALIR DE LA CARGA DE NOTAS (S/N)?: ").strip().upper()
                if salir_notas == 'S' or salir_notas == 'SI':
                    break

            # Valide que se ingrese al menos 1 nota
            if notas_cargadas < 1:
                print("ADVERTENCIA: No se ingresó ninguna nota. Alumno no vale.")
            else:
                alumnos_guardados.append(nuevo_alumno)
                print(f"Cargado alumno {nombre_completo} con {notas_cargadas} notas.")

            salir_alumno = input("\nDESEA SALIR DE CARGA DE ALUMNOS? (S/N): ").strip().upper()
            if salir_alumno == 'S':
                break

        print("\n\n#################################################")
        print("### RESUMEN DE ALUMNOS Y PROMEDIOS CARGADOS ###")
        
        for alumno in alumnos_guardados:
            print(alumno)

# Ejecución del main
if __name__ == "__main__":
    app = CargaNotas()
    app.main()