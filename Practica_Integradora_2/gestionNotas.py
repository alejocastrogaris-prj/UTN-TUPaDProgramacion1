
#DETERMINAR NOTA MAYOR ENTRE TODAS LAS MATERIAS-------------------    
def mayorNota_listaMaterias(materias,notaMaxima,nombreMateriaMaxima):
    
    for i in range(0,5):
        for j in range(1,3):
            if materias[i][j] > notaMaxima:
                notaMaxima = materias[i][j]
                nombreMateriaMaxima = materias[i][0]
            else:
                pass
    
    return nombreMateriaMaxima, notaMaxima
        

#LINEAMIENTOS SOLICITADOS -----------------------

alumnos = {
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales",
}
materias = [
        ["Ciencias"," "," "," "],
        ["Historia"," "," "," "],
        ["Geografia"," "," "," "],
        ["Matematicas"," "," "," "],
        ["Fisica"," "," "," "]
    ]
    
notasFinales = [
    ["Rodolfo Fernandez"," "],
    ["Luis Gomez"," "],
    ["Andrea Pereira"," "],
    ["Juan Cruz Gonzales"," "]
]

#-----------------------------------------------
sumaNotasFinales = 0
notaMaxima = -1
nombreMateriaMaxima = " "
#BUCLE PROGRAMA PRINCIPAL  ###---###---###---###---###---### 
for i in range(60902,61853):
        if i in alumnos:
            print("###################")
            print(f"------Alumno------: {alumnos[i]}")
            for j in range(0,5):
                print("///////////////////")
                print(f"-----Materia------: {materias[j][0]}")
                print("Ingrese las notas de la materia")
                nota1 = float(input("Nota 1: "))
                nota2 = float(input("Nota 2: "))
                if nota1 < 0 or nota1 > 10:
                    print("Datos invalidos. Finalizando programa")
                    exit()
                elif nota2 < 0 or nota2 > 10:
                    print("Datos invalidos. Finalizando programa")
                    exit()
                else:
                    materias[j][1] = nota1
                    materias[j][2] = nota2
                    notaFinal = (nota1 + nota2) / 2
                    materias[j][3] = notaFinal
                    print(f"Nota final: {notaFinal}")
                    sumaNotasFinales = sumaNotasFinales + notaFinal
                     
            if j == 4:
                print(materias)
                nombreMateriaMaxima, notaMaxima = mayorNota_listaMaterias (materias, notaMaxima, nombreMateriaMaxima)
                print(f"\nMejor nota general:{notaMaxima}  Materia:{nombreMateriaMaxima}")
          
            if i == 60902:
                        sumaNotasFinales = sumaNotasFinales / 5
                        notasFinales[0][1] = sumaNotasFinales
            elif i == 61654:
                        sumaNotasFinales = sumaNotasFinales / 5
                        notasFinales[1][1] = sumaNotasFinales
            elif i == 61852:
                        sumaNotasFinales = sumaNotasFinales / 5
                        notasFinales[2][1] = sumaNotasFinales
            elif i == 61754:
                        sumaNotasFinales = sumaNotasFinales / 5
                        notasFinales[3][1] = sumaNotasFinales
            else:
                pass
            
            sumaNotasFinales = 0
        else:
            pass

print(notasFinales)

mejorPromedio = 0

if notasFinales[0][1] > mejorPromedio:
    mejorPromedio = notasFinales[0][1]
elif notasFinales [1][1] > mejorPromedio:
    mejorPromedio = notasFinales[1][1]
elif notasFinales[2][1] > mejorPromedio:
    mejorPromedio = notasFinales[2][1]
elif notasFinales[3][1] > mejorPromedio:
    mejorPromedio = notasFinales[3][1]
else:
    pass
          

    