# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {
    "Argentina": "Buenos Aires",
    "Chile":"Santiago",
    "Francia":"Paris",
}

print(f"Este es el diccionario original: \n{original} \n------------------")

invertido = {
    clave : valor
for valor,clave in original.items()
}

print(f"Este es el diccionario invertido: \n{invertido} \n------------------")