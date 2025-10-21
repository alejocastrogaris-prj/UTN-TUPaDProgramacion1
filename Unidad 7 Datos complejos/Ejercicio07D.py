# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {101,102,103,105}
parcial2 = {101,104,105,106}
ambos_aprobados = parcial1 & parcial2
print(f"Estos son los alumnos que aprobaron ambos parciales: \n{ambos_aprobados}")

aprobaron_uno = parcial1 ^ parcial2 
print(f"Estos son los alumnos que aprobaron unicamente un parcial: {aprobaron_uno}")

aprobados_total = parcial1 | parcial2
print(f"Estos son los aprobados totales: {aprobados_total}")
