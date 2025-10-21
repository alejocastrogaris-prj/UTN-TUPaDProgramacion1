# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

while True:
    print("\nIngrese |1| -> Para agregar contactos \nIngrese |2| -> Para consultar contactos \nIngrese |3| -> Para salir del programa")
    
    try:
        opcion = int(input("##-----------## \nIngrese aquí: "))
        
    except ValueError:
        print("❌ Valor inválido. Debe ingresar un número ||(1 o 2)||.")
        continue  
    if opcion == 3:
        print("Saliendo del programa!!")
        break
    
    if opcion == 1:
        while True:
            try:
                print(" \nPara guardar el contacto ingrese Nombre y Numero")
                nombre = input("Nombre: ")
                numero = int(input("\nNumero: "))
                contactos[nombre] = numero  
                print("Continuar? S|N ")
                opcion = input("\nIngrese aqui: ")
                opcion = opcion.lower()
                if opcion == "s":
                    continue
                elif opcion == "n":
                    break
            
            except ValueError:
                print("Error❌ Solo puede utilizar numeros para -|Numero|-.Vuelva a ingresar los datos")
                continue   
    
    
    if opcion == 2:
        if not contactos:
            print("\n❌  La lista esta vacia. Agregue contactos primero.")
            continue
        while  True:
            contacto_a_buscar = input("Ingrese el contacto a buscar ")
            if contacto_a_buscar in contactos.keys():
                numero_Asociado = contactos.get(contacto_a_buscar)
                print(f"\nNombre: {contacto_a_buscar} --- Numero: {numero_Asociado} ")
                break
            else:
                print("El contacto no existe")
                continue     
        
        

                
    
                