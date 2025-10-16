# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,10):
        print(f"{numero} x {i} = {numero * i}")


numero = int(input("Ingrese un numero para mostrar su tabla de multiplicacion"))

tabla_multiplicar(numero)