# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(Peso,Altura):
    imc = Peso / (Altura**2)
    return imc




Peso = float(input("Ingrese su peso exacto en KG"))
Altura = float(input("Ingrese su altura exacta"))

print(f"Su indice de masa corporal es: {calcular_imc(Peso, Altura)}")