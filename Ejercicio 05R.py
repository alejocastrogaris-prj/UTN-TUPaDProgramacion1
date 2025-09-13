# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeros_aleatorios = [random.randint(0, 9) for i in range(9)]
numero_a_encontrar = random.choice(numeros_aleatorios)
contador = 1
while True:
    adivinar_numero = int(input("Ingrese el numero a adivinar"))
    if adivinar_numero == numero_a_encontrar:
        print(f"Adivinaste el numero!!. Numero encontrado: ___{numero_a_encontrar}___")
        print(f"Tus intentos fueron: {contador}")
        break
    else:
        contador = contador + 1
        print("Intenta de nuevo!!")



