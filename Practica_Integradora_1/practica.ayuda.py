

# PRACTICA INTEGRADORA 1 – PYTHON

# Datos iniciales
golosinas = (
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de menta", 50],
    [4, "Huevo kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor tofi", 15],
    [11, "Lata coca", 20],
    [12, "Chitos", 10],
)

empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gaston Garcia",
}

clavesTecnico = ("admin", "CCCDDD", "2020")
golosinasPedidas = [] # Lista de N filas por 3 columnas, inicialmente vacía

# Bucle principal del programa
while True:
    print("\n---- MAQUINA DE GOLOSINAS ----")
    print("           MENU")
    print("A) Pedir golosinas ")
    print("B) Mostrar golosinas")
    print("C) Rellenar golosinas")
    print("D) Apagar maquina")
    opcionElegida = input("Seleccione una opcion: ").upper()

    if opcionElegida == "A":
        try:
            legajo_ingresado = int(input("Ingrese su legajo: "))
            if legajo_ingresado in empleados:
                print(f"Bienvenido {empleados[legajo_ingresado]}")
                while True:
                    try:
                        codigo_golosina_usuario = int(input("Ingrese el codigo de la golosina que desea (0 para salir): "))
                        if codigo_golosina_usuario == 0:
                            break
                        
                        if 1 <= codigo_golosina_usuario <= 12:
                            indice_golosina = codigo_golosina_usuario - 1
                            if golosinas[indice_golosina][2] > 0:
                                golosinas[indice_golosina][2] -= 1
                                print(f"Usted seleccionó 1 {golosinas[indice_golosina][1]}")
                                print(f"Disponibles: {golosinas[indice_golosina][2]}")

                                encontrado = False
                                for i in range(len(golosinasPedidas)):
                                    if golosinasPedidas[i][0] == codigo_golosina_usuario:
                                        golosinasPedidas[i][2] += 1
                                        encontrado = True
                                        break
                                
                                if not encontrado:
                                    nombre_golosina = golosinas[indice_golosina][1]
                                    nueva_fila = [codigo_golosina_usuario, nombre_golosina, 1]
                                    golosinasPedidas.append(nueva_fila)
                            else:
                                print(f"No hay más stock de {golosinas[indice_golosina][1]}. Seleccione otra o 0 para salir.")
                        else:
                            print("Código inválido. Vuelva a ingresarlo.")
                    except ValueError:
                        print("Entrada inválida. Ingrese un número.")
            else:
                print("Usted no pertenece a la empresa.")
        except ValueError:
            print("Entrada inválida. Ingrese un número de legajo.")

    elif opcionElegida == "B":
        print("\n----- GOLOSINAS DISPONIBLES -----")
        print(f"{'Código':<7}{'Nombre':<20}{'Stock':<10}")
        print("="*40)
        for golosina in golosinas:
            print(f"{golosina[0]:<7}{golosina[1]:<20}{golosina[2]:<10}")

    elif opcionElegida == "C":
        print("\nOpción C: Recarga de golosinas")
        clave_correcta = True
        
        for i in range(len(clavesTecnico)):
            clave_ingresada = input(f"Ingrese la clave {i + 1}: ")
            if clave_ingresada != clavesTecnico[i]:
                clave_correcta = False
                print("Acceso denegado. Clave incorrecta.")
                break
        
        if clave_correcta:
            print("Acceso concedido para rellenar golosinas.")
            while True:
                try:
                    codigo_golosina_usuario = int(input("Ingrese el codigo de la golosina a rellenar (0 para salir): "))
                    if codigo_golosina_usuario == 0:
                        break
                    
                    if 1 <= codigo_golosina_usuario <= 12:
                        indice_golosina = codigo_golosina_usuario - 1
                        cantidadARellenar = int(input(f"Ingrese la cantidad de {golosinas[indice_golosina][1]} a rellenar: "))
                        golosinas[indice_golosina][2] += cantidadARellenar
                        print(f"Stock de {golosinas[indice_golosina][1]} actualizado a {golosinas[indice_golosina][2]}.")
                    else:
                        print("Código de golosina inválido.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número.")

    elif opcionElegida == "D":
        print("\n--- INFORME DE GOLOSINAS PEDIDAS ---")
        if not golosinasPedidas:
            print("No se ha pedido ninguna golosina durante esta sesión.")
        else:
            print(f"{'Código':<7}{'Nombre':<20}{'Cantidad':<10}")
            print("="*40)
            
            cantidad_total = 0
            for pedido in golosinasPedidas:
                codigo = pedido[0]
                nombre = pedido[1]
                cantidad = pedido[2]
                print(f"{codigo:<7}{nombre:<20}{cantidad:<10}")
                cantidad_total += cantidad
            
            print("\n--- RESUMEN ---")
            print(f"Total de golosinas pedidas: {cantidad_total}")
        
        break # Finaliza el bucle principal

    else:
        print("Opción no válida. Por favor, seleccione A, B, C o D.")