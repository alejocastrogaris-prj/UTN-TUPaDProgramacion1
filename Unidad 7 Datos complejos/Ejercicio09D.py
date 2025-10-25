# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo

agenda = {
    ("lunes","10:00"): "Reunion Familiar",
    ("martes","17:00"):"Partido de futbol",
    ("miercoles","15:00"):"Clases de guitarra",
    ("jueves","Sin horarios"): "Sin actividades",
    ("viernes","Sin horarios"):"Sin actividades",
    ("sabado","18:00"):"Gimnasio",
    ("domingo","Sin horarios"):"Sin actividades"
}

#---------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    dia_consultado = input("Ingrese el dia del que desea saber las actividades (o 'salir'): ").lower()

    if dia_consultado == 'salir':
        print("Saliendo de la agenda.")
        break
    
    encontrado = False

    for (dia, horario), actividad in agenda.items():
        if dia_consultado == dia:
            encontrado = True
            
            if actividad == "Sin actividades":
                print(f"El {dia} no tiene actividades programadas.")
                break
            
            else:
                horario_consultado = input(f"\nEl {dia} tiene actividad. Ingrese el horario exacto ({horario}): ")
                
                if horario_consultado == horario:
                    print(f"El dia {dia} a las {horario} tiene programado ----> | {actividad} |")
                else:
                    print(f"Horario incorrecto o no coincide. La actividad es a las {horario}.")
                
                break
    
    if not encontrado:
        print(f"Día '{dia_consultado}' no encontrado. Por favor, ingrese un día válido de la semana.")

