# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

lista_vacia = []

import random
for i in range(5):
    lista_vacia.append(random.randint(0,5))
    
print(lista_vacia)