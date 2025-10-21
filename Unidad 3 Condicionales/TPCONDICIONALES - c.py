#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input("Ingrese su edad para determinar si es mayor o no"))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
#------------------------------------------------------------------------------------------------    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

NotaAlumno=int(input("Ingrese su nota"))

if NotaAlumno >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
#------------------------------------------------------------------------------------------------
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

Numero_ingresado=int(input("Ingrese un numero"))
if Numero_ingresado % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")
    
#------------------------------------------------------------------------------------------------
# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece: Niño, Adolescente, Adulto Joven, Adulto

edad=int(input("Ingrese su edad"))

if edad < 12:
    print("Usted es un niño")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")
else:
    print("Usted es un adulto")
    
#------------------------------------------------------------------------------------------------
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

Contraseña_ingresada = input("Ingrese una contraseña")
Longitud_contraseña = len(Contraseña_ingresada)
if Longitud_contraseña < 8 or Longitud_contraseña > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else: 
    print("Ha ingresado una contraseña correcta")

#------------------------------------------------------------------------------------------------
#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana
#y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
#Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"La moda es ",[mode(numeros_aleatorios)],", la mediana es ",[median(numeros_aleatorios)]," y la media es ",[mean(numeros_aleatorios)])
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Es sesgo es positivo")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Es sesgo es negativo")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios) and mode(numeros_aleatorios) == mean(numeros_aleatorios):
    print("Sin sesgo")
else:
    pass

#------------------------------------------------------------------------------------------------
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla
frase_usuario = str(input("Ingrese una frase"))
ultima_letra = frase_usuario[-1]

if (ultima_letra in ("a","e","i","o","u","A","E","I","O","U")):
    print(f"Frase ingresada:,{frase_usuario}!")
else:
    print(f"Frase ingresada:,{frase_usuario}") 
    
#------------------------------------------------------------------------------------------------
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas 

Nombre_usuario = str(input("Ingrese su nombre"))  
opcion = int(input("Seleccione un numero entre 1 y 3"))

if opcion == 1:
    Nombre_usuario = Nombre_usuario.upper()
elif opcion == 2:
    Nombre_usuario = Nombre_usuario.lower()
elif opcion == 3:
    Nombre_usuario = Nombre_usuario.title()
    
print(Nombre_usuario)

#------------------------------------------------------------------------------------------------
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

magnitud_ingresada = float(input("Ingrese la magnitud del terremoto"))

if magnitud_ingresada < 3:
    print("Muy leve")
elif magnitud_ingresada >= 3 and magnitud_ingresada < 4:
    print("Leve")
elif magnitud_ingresada >= 4 and magnitud_ingresada < 5:
    print("Moderado")
elif magnitud_ingresada >= 5 and magnitud_ingresada < 6:
    print("Fuerte")
elif magnitud_ingresada >= 6 and magnitud_ingresada < 7:
    print("Muy fuerte")
elif magnitud_ingresada >=7:
    print ("Extremo")
    
#------------------------------------------------------------------------------------------------
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.    

hemisferio=input("ingrese su hemisferio (N o S): ")
mes=int(input("Ingrese el mes: "))
dia=int(input("Ingrese el dia: "))
if hemisferio=="N" or hemisferio=="n":
    if (mes>=12 and dia>=21) or (mes<=3 and dia<=20):
        print("Es invierno")
    elif (mes>=3 and dia>=21) or (mes<=6 and dia<=20):
        print("Es primavera")
    elif (mes>=6 and dia>=21) or (mes<=9 and dia<=20):
        print("Es verano")
    elif(mes>=9 and dia>=21) or (mes<=12 and dia<=20):
        print("Es otoño")
if hemisferio=="S" or hemisferio=="s":
    if (mes>=12 and dia>=21) or (mes<=3 and dia<=20):
        print("Es verano")
    elif (mes>=3 and dia>=21) or (mes<=6 and dia<=20):
        print("Es otoño")
    elif (mes>=6 and dia>=21) or (mes<=9 and dia<=20):
        print("Es invierno")
    elif(mes>=9 and dia>=21) or (mes<=12 and dia<=20):
        print("Es primavera")
    
