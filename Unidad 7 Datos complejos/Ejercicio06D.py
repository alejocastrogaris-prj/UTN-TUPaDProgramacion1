# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

notas = ()
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1} ")
    print(f"\nNotas de {nombre}: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    
    if i == 0:
        notas = (nota1,nota2,nota3)
        alumnos[nombre] = notas
    
    if i == 1:
        notas = (nota1,nota2,nota3)
        alumnos[nombre] = notas
        
    if i == 2:
        notas = (nota1,nota2,nota3)
        alumnos[nombre] = notas
        

for alumno, notas in alumnos.items():
    promedio = sum(notas)/3
    print(f"El promedio de {alumno} es de: {promedio}") 
    
        
    
