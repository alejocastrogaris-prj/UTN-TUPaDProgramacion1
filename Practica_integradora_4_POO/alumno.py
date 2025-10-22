class Alumno:
    # Atributos: nombreCompleto (cadena), legajo (entero), lista de objetos notas[]
    def __init__(self, nombre_completo, legajo):
        self.nombreCompleto = nombre_completo
        self.legajo_nro = legajo
        self.listade_notas = []

    # Agrega una nota a la lista del alumno
    def agregar_nota(self, nota):
        self.listade_notas.append(nota)

    # Metodo que calcule el promedio de las notas que posee
    def calcular_promedio(self):
        if not self.listade_notas:
            return 0.0
        
        suma_notas = 0.0
        for n in self.listade_notas:
            suma_notas += n.notaExamen
            
        promedio = suma_notas / len(self.listade_notas)
        return promedio

    # Para mostrar la info del alumno
    def __str__(self):
        info = f"\nALUMNO: {self.nombreCompleto}, Legajo: {self.legajo_nro}" 
        info += "\n--- Notas del Alumno ---"
        # Muestra todas las notas
        if self.listade_notas:
            for nota_actual in self.listade_notas:
                info += f"\n- {nota_actual}"
        else:
            info += "\n- No tiene notas cargadas. Cero promedio."
            
        # Muestra el promedio
        info += f"\nEl promedio del alumno es: {self.calcular_promedio():.2f}"
        return info