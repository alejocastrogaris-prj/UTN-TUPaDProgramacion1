# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_limite = int(input("Ingrese un numero limite"))
suma = 0
for i in range(1 , (numero_limite + 1), 1 ):
   suma = suma + i
    
print(f"La suma de todos los enteros es de: {suma}")