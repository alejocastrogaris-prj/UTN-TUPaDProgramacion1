# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


celsius = float(input("Ingrese la temperatura en grados celsius para mostrar su equivalente en Fahrenheit"))

print(f"La temperatura ingresada equivale a {celsius_a_fahrenheit(celsius)} grados en Fahrenheit")