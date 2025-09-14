# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Primero creamos una lista con el nombre "numeros" y le asignamos valores numericos
numeros = [8,15,3,22,7]

#Ahora usando .remove seguido del "max" y la lista seleciconada, borramos el numeros mas grande o con mas "valor de la lista"
numeros.remove(max(numeros))

#Ahora imprimimos la lista para ver los cambios
print(numeros)