# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
numeros_pares = 0
numeros_impares = 0
numeros_negativos = 0
numeros_positivos = 0

for i in range(100):
    numeros_ingresados = int(input("Ingrese 100 numeros (Negativos,positivos, par o impar)"))
    if numeros_ingresados < 0:
        numeros_negativos = numeros_negativos + 1
    elif numeros_ingresados > 0:
        numeros_positivos = numeros_positivos + 1
        
    if numeros_ingresados % 2 == 0:
        numeros_pares = numeros_pares + 1
    else: 
        numeros_impares = numeros_impares + 1
        
print(f"Numeros positivos: {numeros_positivos}. Numeros negativos: {numeros_negativos}.")
print(f"Numeros pares: {numeros_pares}. Numeros impares: {numeros_impares}.")



    
    
    
    



