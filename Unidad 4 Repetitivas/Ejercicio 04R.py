# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0
numero_iniciador = int(input("Ingrese 2 para entrar al bucle o 0 para finalizar el programa"))
suma = 0
while numero_iniciador != 0:
    numero_ingresado = int(input("Ingrese numeros, estos se iran sumando"))
    suma = suma + numero_ingresado
    numero_iniciador = int(input("Ingrese 0 si quiere detener el bucle. De otro modo ingrese 2"))


print(f"La suma total de los numeros ingresados es: {suma}")