# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
print(f"Lista inicial: {dobles}")
#--------------------------------- SOLUCION 1
dobles.append(5)
dobles.append(5)
dobles.append(10)
dobles.append(10)
dobles.append(15)
dobles.append(15)
#--------------------------------- SOLUCION 2
# for i in range(2):
#     dobles.append(5)
    
# for i in range(2):
#     dobles.append(10)
    
# for i in range(2):
#     dobles.append(15)
#---------------------------------
print(f"Esta es la lista con los dobles: {dobles}")
