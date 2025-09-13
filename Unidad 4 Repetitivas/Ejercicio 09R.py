# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

media_numeros = 0
numeros = 0
contador = 0
suma = 0
for i in range (100):
    numeros = int(input("Ingrese 3 valores para pasar su media"))
    suma = suma + numeros
    contador = contador + 1
    
print(f"La media es los numeros es {suma / contador}")
    
    
    
