# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = 0
numero_invertido = " "
contador = 0

while True:
    contador = contador + 1
    numero = int(input("Ingrese un numero"))
    numero = str(numero)
    numero_invertido = numero[::-1]
    print(f"Este es el numero invertido: {numero_invertido}")
    
    if contador == 3:
        break


    
    
