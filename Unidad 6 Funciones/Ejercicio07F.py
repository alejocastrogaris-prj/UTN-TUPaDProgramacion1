# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    
    operaciones = (
        [],
        [],
        [],
        [],
)
    operaciones[0].append(f"Suma = {a + b}")
    operaciones[1].append(f"Resta = {a - b}")
    operaciones[2].append(f"Multiplicacion = {a * b}")
    operaciones[3].append(f"Division = {a / b}")
    
    for i in range(4):
        print(f"\n{operaciones[i]}")
        
    




a = float(input("Ingrese el primer numero"))
b = float(input("Ingrese el segundo numero"))

operaciones_basicas(a,b)