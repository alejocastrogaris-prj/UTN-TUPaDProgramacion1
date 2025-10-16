# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math
def calcular_area_circulo(radio):
    Area = math.pi * (radio**2)
    return Area
    
    

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
    


radio = float(input("Ingrese el radio del circulo para calcular su area y perimetro"))

print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")   