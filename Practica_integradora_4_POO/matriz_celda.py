# Definicion de la clase Celda
class Celda:
    # Atributos: fila (entero), columna (entero), valor (cadena)
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor_contenido = valor 

    def __str__(self):
        return f"Celda: ({self.fila}, {self.columna}) -> '{self.valor_contenido}'" 

# ----------------------------------------------------------------------

# Definicion de la clase Matriz
class Matriz:
    def __init__(self):
        self.celdas_Matriz = []
        self.contador_celdas = 0

    # Metodo para validar si la celda ya existe
    def existe_celda(self, fila, columna):
        for celda in self.celdas_Matriz:
            if celda.fila == fila and celda.columna == columna:
                return True
        return False

    # Metodo para agregar una celda si no existe
    def agregar_celda(self, celda):
        if not self.existe_celda(celda.fila, celda.columna):
            self.celdas_Matriz.append(celda)
            self.contador_celdas += 1
            print("Celda agregada correctamente.")
            return True
        else:
            print("ERROR: La celda en esa posición ya fue cargada. No se agregó.")
            return False

    # Metodo para mostrar todas las celdas cargadas
    def mostrar_celdas(self):
        print("\n--- Valores Cargados en la Lista celdas. ---")
        if not self.celdas_Matriz:
            print("La matriz está vacía.")
            return
        for celda_item in self.celdas_Matriz:
            print(celda_item) 
        print(f"Total de celdas cargadas: {self.contador_celdas}")

    # Metodo para retornar el valor de una celda por su posicion
    def obtener_valor(self, fila_buscada, columna_buscada):
        
        for celda in self.celdas_Matriz:
            if celda.fila == fila_buscada and celda.columna == columna_buscada:
                return celda.valor_contenido
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

# ----------------------------------------------------------------------

# Programa principal
if __name__ == "__main__":
    matriz = Matriz()

    while True:
        print("\n*** Carga de Celda ***")
        valor_celda = input("Ingrese el VALOR para la celda (o 'FIN' para terminar): ").strip()
        
        if valor_celda.upper() == "FIN":
            break
            
        try:
            fila_celda = int(input("Ingrese la FILA (entero): "))
            columna_celda = int(input("Ingrese la COLUMNA (entero): "))
            
            confirmacion = input("Confirmas la carga de valores (S/N)? ").upper() 
            if confirmacion != 'S':
                print("Carga de celda cancelada por el usuario.")
                continue
            
            nueva_celda = Celda(fila_celda, columna_celda, valor_celda)
            
            matriz.agregar_celda(nueva_celda)
            
        except ValueError:
            print("La fila y la columna tienen que ser números enteros. Intenta de nuevo.")
        
    matriz.mostrar_celdas()
    
    # Prueba del metodo obtener_valor
    print("\n--- Prueba de Búsqueda ---")
    try:
        fila_b = int(input("Ingrese FILA para buscar su valor: "))
        columna_b = int(input("Ingrese COLUMNA para buscar su valor: "))
        
        resultado = matriz.obtener_valor(fila_b, columna_b)
        print(f"El valor en la posicion que pusiste es: {resultado}")
    except ValueError:
        print("La fila y columna de búsqueda deben ser numeros enteros.")