#PRACTICA INTEGRADORA 1 – PYTHON

golosinas = (
    [1, "KitKat", 20],
    [2,"Chicles", 50],
    [3,"Caramelos de menta",50],
    [4,"Huevo kinder",10],
    [5, "Chetoos", 10],
    [6,"Twix",10],
    [7,"M&M'S",10],
    [8,"Papas Lays",2],
    [9,"Milkybar",10],
    [10,"Alfajor tofi",15],
    [11,"Lata coca", 20],
    [12,"Chitos",10],
)

#Creo diccionario de "empleados"

empleados = {
    1100: "Jose Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gaston Garcia",                          
}

#Creo la tupla "clavesTecnico"

clavesTecnico = ("admin","CCCDDD","2020")

#Creo golosinasPedidas

golosinasPedidas = [
    
    
    
]


while True:
    print("----MAQUINA DE GOLOSINAS----")
    print("            MENU            ")
    print("A) Pedir golosinas ")
    print("B) Mostrar golosinas")
    print("C) Rellenar golosinas")
    print("D) Apagar maquina")
    opcionElegida = str(input("Seleccione una opcion: "))
    legajo_ingresado = 0
    codigo_golosina = 0
    denominacionGolosina = " "
    if opcionElegida == "A" or opcionElegida == "a":
        legajo_ingresado = int(input("Ingrese su legajo"))
        if legajo_ingresado in empleados:
            print(f"Bienvenido {empleados[legajo_ingresado]}")
            while True:
                print("Para salir ingrese 0")
                
                codigo_golosina = int(input("Ingrese el codigo de la golosina que desea: "))
                
                if codigo_golosina == 0:
                    break
                
                if codigo_golosina > 12:
                    print("Codigo invalido vuelva a ingresarlo ")
                    continue
                
                codigo_golosina = codigo_golosina - 1 #Restamos 1 para que el codigo de la golosina coincida con la lista
                
                print(f"Usted selecciono 1 {golosinas[codigo_golosina][1]}")   #Mensaje señalando la seleccion de golosina
                
                golosinas[codigo_golosina][2] = golosinas[codigo_golosina][2] - 1 #Segun el codigo restamos 1 del stock de la golosina seleccionada
                
                if golosinas[codigo_golosina][2] < 0:
                    golosinas[codigo_golosina][2] = golosinas[codigo_golosina][2] + 1
                
                print(f"Disponibles: {golosinas[codigo_golosina][2]}") #Mostramos el restante de ESA golosina
               #----------------------------------------------------------------------------------------------------------------------------------------- 
                # ------------------//////  Parte de codigo donde se agregan las golosinas a la lista golosinaPedidas ////////--------------------------
                
                #Tengo que corregir esta parte
                
                
               
               #--------------------------------------------------------------------------------------------------------------------------------------             
                
                if golosinas[codigo_golosina][2] == 0:
                    print(f"No hay mas stock de {golosinas[codigo_golosina][1]}")
                    print("Seleccione otra golosina o salir si no desea ninguna mas")
                continue
        else:
            print("Usted no pertenece a la empresa")
            continue
    elif opcionElegida == "B" or opcionElegida == "b":
        print("-----GOLOSINAS-----")
        print("-Codigo--Nombre--Stock-")
        print(golosinas[0])
        print(golosinas[1])
        print(golosinas[2])
        print(golosinas[3])
        print(golosinas[4])
        print(golosinas[5])
        print(golosinas[6])
        print(golosinas[7])
        print(golosinas[8])
        print(golosinas[9])
        print(golosinas[10])
        print(golosinas[11])
    elif opcionElegida == "C" or opcionElegida == "c":
        # clavesTecnico = ("admin","CCCDDD","2020")
       claveIngresada1 = input("Ingrese la primera clave ")
       claveIngresada2 = input("Ingrese la segunda clave ")
       claveIngresada3 = input("Ingrese la tercera clave ")
       cantidadARellenar = 0
       if claveIngresada1 == clavesTecnico[0] and claveIngresada2 == clavesTecnico[1] and claveIngresada3 == clavesTecnico[2]:
           while True:
               print("Ingrese 0 para salir")
               codigo_golosina = int(input("Ingrese el codigo de la golosina a rellenar: "))
               codigo_golosina = codigo_golosina - 1
               if codigo_golosina == 0 or codigo_golosina < 0:
                   break
               elif codigo_golosina <= 12:
                   cantidadARellenar = int(input(f"Ingrese la cantidad de {golosinas[codigo_golosina][1]} a rellenar deseada: "))
                   golosinas[codigo_golosina][2] = golosinas[codigo_golosina][2] + cantidadARellenar
               else:
                   print("Seleccion invalida. Intentelo de nuevo")
                   continue
       else: print("No tiene permiso para ejecutar la función de recarga")
       continue
    elif opcionElegida == "D" or opcionElegida == "d":
        print("---GOLOSINAS PEDIDAS---")
        print("CODIGO--DENOMINACION--TOTAL PEDIDAS")
        print(golosinasPedidas)
        break
        
    
         
       
       
            
        
    
    
      
        
        
        
        
        
        
        
                
            
                   
        