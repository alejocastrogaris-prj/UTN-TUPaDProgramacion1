# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
# Inicializamos la variable de control para que el bucle se ejecute al menos una vez

decision_usuario = "S"
while decision_usuario.upper() == "S":
    numero_Usuario = input("Ingrese un numero para contar sus digitos ")
    cantidad_Digitos = len(numero_Usuario)
    print(f"El numero {numero_Usuario} tiene {cantidad_Digitos} digitos")
    decision_usuario = input("Desea continuar? S/N ")
    
print("Adios")
    
    
     
    
    
     
    
    