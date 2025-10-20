# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

from collections import Counter
#Solicito la frase
print("\n##-----------------------##")
frase = input("Ingrese una frase ->")
print("##-----------------------##")
palabras_frases = frase.split()

set_frase = set(palabras_frases)
print("\n##-----------------------##")
print(f"Estas son las palabras unicas: \n{set_frase}")
print("##-----------------------##")

cantidad_repeticiones = Counter(palabras_frases)
print("\n##-----------------------##")
print(f"Estas son las veces que se repiten cada palabra:  \n{cantidad_repeticiones}")
print("##-----------------------##")