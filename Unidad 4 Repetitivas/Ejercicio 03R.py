# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Ingrese dos valores para sumar todos los numeros enteros entre ellos, excluyendo los asignados")
primer_Valor = int(input("Primer valor: "))
segundo_Valor = int(input("Segundo valor: "))
primer_Valor = primer_Valor + 1
suma = 0

for primer_Valor in range(primer_Valor, segundo_Valor,1):
    suma = suma + primer_Valor

print(f"La suma de los numeros enteros es: {suma}")