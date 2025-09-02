#Primer ejercicio
print("Hola mundo")

#Segundo ejercicio
Nombre=input("Cual es tu nombre?")
print(f"Hola {Nombre}")

#Tercer ejercicio
Nombre_2=input("Cual es tu nombre?")
Apellido=input("Cual es tu apellido")
Edad=int(input("Que edad tenes?"))
Residencia=input("Donde vivis?")
print(f"Hola soy {Nombre_2}{Apellido} tengo {Edad} años y vivo en {Residencia}")

#Cuarto ejercicio
Radio=float(input("Cual es el radio de su circulo?"))
Area= 3.1416 * Radio * Radio
Perimetro= 2 * 3.1416 * Radio
print(f"El area de su circulo es{Area} y el perimetro es de {Perimetro}")

#Quinto ejercicio
Segundos = float(input("Ingrese una cantidad de segundos para ver su equivalente en horas"))
Horas = Segundos / 3600
print(f"La cantidad ingresada de segundos:{Segundos}. Es equivalente a {Horas} Horas")

#Sexto Ejercicio
numero_multiplicar = int(input("Ingrese un numero para mostrar su tabla de multiplicacion"))
print(f"La tabla de multiplicar de {numero_multiplicar} es:")
print(f"{numero_multiplicar} * 1 = {numero_multiplicar * 1}")
print(f"{numero_multiplicar} * 2 = {numero_multiplicar * 2}")
print(f"{numero_multiplicar} * 3 = {numero_multiplicar * 3}")
print(f"{numero_multiplicar} * 4 = {numero_multiplicar * 4}")
print(f"{numero_multiplicar} * 5 = {numero_multiplicar * 5}")
print(f"{numero_multiplicar} * 6 = {numero_multiplicar * 6}")
print(f"{numero_multiplicar} * 7 = {numero_multiplicar * 7}")
print(f"{numero_multiplicar} * 8 = {numero_multiplicar * 8}")
print(f"{numero_multiplicar} * 9 = {numero_multiplicar * 9}")
print(f"{numero_multiplicar} * 10 = {numero_multiplicar * 10}")

#Septimo Ejercicio
primer_numero = int(input("Ingrese el primer numero"))
segundo_numero = int(input("Ingrese el segundo numero"))
print(f"Su suma= {primer_numero + segundo_numero}")
print(f"Su resta = {primer_numero - segundo_numero}")
print(f"Su multiplicacion = {primer_numero * segundo_numero}")
print(f"Su division = {primer_numero / segundo_numero}")

#Octavo Ejercicio
Peso_kg = float(input("Ingrese su peso en kilogramos"))
altura = float(input("Ingrese su altura en metros"))
print(f"Su indice de masa corporal es= {Peso_kg / altura ** 2}")

#Noveno Ejercicio
grados_celsius = float(input("Ingrese la temperatura en grados celsius"))
fahrenheit_grados = (grados_celsius * 9/5) + 32
print(f"Los grados celsius ingresados: {grados_celsius} son equivalentes a {fahrenheit_grados} en grados fahrenheit")

#Decimo Ejercicio
print("Ingrese 3 numeros a continuacion para calcular su promedio")
primer_numero = float(input("Ingrese el primero:"))
segundo_numero = float(input("Ingrese el segundo numero"))
tercer_numero = float(input("Ingrese el tercer numero"))
Total = primer_numero + segundo_numero + tercer_numero
print(f"El promedio entre los 3 numeros es: {Total / 3}") 