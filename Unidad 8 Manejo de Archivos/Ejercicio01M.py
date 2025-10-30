# Definición de funciones para modularizar el código

def leer_productos_a_lista(nombre_archivo="C:\\Users\\Usuario\\OneDrive\\Documentos\\GitHub\\UTN-TUPaDProgramacion1\\Unidad 8 Manejo de Archivos\\productos.txt"):
    """
    Actividad 4: Lee el archivo de productos y carga los datos en una
    lista de diccionarios. Usa 'r' para lectura.
    """
    productos = []
    # Uso de with open() para asegurar que el archivo se cierre automáticamente
    try:
        with open(nombre_archivo, 'r') as archivo: # 'r' modo lectura 
            for linea in archivo:
                # Procesamiento de la línea (Actividad 2)
                # .strip() elimina espacios en blanco y saltos de línea al inicio/final
                # .split(',') divide la línea en una lista por la coma
                datos = linea.strip().split(',')
                
                # Asegurarse de que hay 3 elementos antes de intentar acceder a ellos
                if len(datos) == 3:
                    nombre, precio_str, cantidad_str = datos
                    
                    # Convertir precio y cantidad a tipos numéricos
                    try:
                        precio = float(precio_str)
                        cantidad = int(cantidad_str)
                    except ValueError:
                        print(f"⚠️ Error al convertir datos numéricos en la línea: {linea.strip()}")
                        continue # Saltar a la siguiente línea si hay error de conversión

                    # Creación del diccionario de producto (Actividad 4)
                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }
                    productos.append(producto)
    except FileNotFoundError:
        print(f"⚠️ El archivo {nombre_archivo} no se encontró. Creando una lista vacía.")
    
    return productos

def mostrar_productos(productos):
    """
    Actividad 2: Muestra los productos en el formato solicitado.
    """
    if not productos:
        print("\nLista de productos vacía.")
        return

    print("\n--- Listado de Productos ---")
    for p in productos:
        # Formato de salida: Producto: Lapicera | Precio: $120.5 | Cantidad: 30 [cite: 20]
        print(f"Producto: {p['nombre']} | Precio: \${p['precio']:.2f} | Cantidad: {p['cantidad']}")
    print("----------------------------")

def agregar_producto_a_archivo(nombre_archivo="C:\\Users\\Usuario\\OneDrive\\Documentos\\GitHub\\UTN-TUPaDProgramacion1\\Unidad 8 Manejo de Archivos\\productos.txt"):
    """
    Actividad 3: Pide al usuario un nuevo producto y lo agrega al final del archivo.
    Usa 'a' para anexar sin borrar lo existente. [cite: 14]
    """
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    
    # Bucle para validar el precio
    while True:
        try:
            precio = float(input("Ingrese el precio: ").replace(',', '.'))
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Precio inválido. Por favor, ingrese un número positivo.")
            
    # Bucle para validar la cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Cantidad inválida. Por favor, ingrese un número entero positivo.")

    # Formato a guardar: nombre,precio,cantidad [cite: 18]
    nueva_linea = f"{nombre},{precio},{cantidad}\n"

    try:
        # 'a' modo append (anexar). Agrega al final sin borrar contenido. [cite: 12, 14]
        with open(nombre_archivo, 'a') as archivo: 
            archivo.write(nueva_linea)
        print(f"✅ Producto '{nombre}' agregado exitosamente a {nombre_archivo}.")
    except Exception as e:
        print(f"❌ Error al intentar escribir en el archivo: {e}")

def buscar_producto_por_nombre(productos):
    """
    Actividad 5: Busca un producto por nombre en la lista de diccionarios.
    """
    if not productos:
        print("\nLa lista de productos está vacía, no se puede buscar.")
        return

    print("\n--- Buscar Producto ---")
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrado = None

    # Recorrer la lista (Actividad 5)
    for p in productos:
        if p['nombre'].lower() == nombre_buscado:
            encontrado = p
            break # Detener la búsqueda si se encuentra

    if encontrado:
        print("\n✅ Producto Encontrado:")
        # Mostrar todos sus datos (Actividad 5)
        print(f"Nombre: {encontrado['nombre']}")
        print(f"Precio: \${encontrado['precio']:.2f}")
        print(f"Cantidad: {encontrado['cantidad']}")
    else:
        # Mostrar mensaje de error (Actividad 5)
        print(f"\n❌ Producto con nombre '{nombre_buscado}' NO encontrado.")

def guardar_productos_actualizados(productos, nombre_archivo="C:\\Users\\Usuario\\OneDrive\\Documentos\\GitHub\\UTN-TUPaDProgramacion1\\Unidad 8 Manejo de Archivos\\productos.txt"):
    """
    Actividad 6: Sobrescribe el archivo con el contenido actual de la lista de productos.
    Usa 'w' para escritura, que borra el contenido anterior.
    """
    print(f"\n--- Guardando Cambios en {nombre_archivo} ---")
    try:
        # 'w' modo write (escritura). Sobrescribe el archivo si existe, lo crea si no. 
        with open(nombre_archivo, 'w') as archivo: 
            for p in productos:
                # Formato a guardar: nombre,precio,cantidad [cite: 18]
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                archivo.write(linea)
        print(f"✅ Se han guardado {len(productos)} productos en el archivo (sobrescrito).")
    except Exception as e:
        print(f"❌ Error al intentar guardar los productos: {e}")

# --- Programa Principal ---

NOMBRE_ARCHIVO = "productos.txt"

print("🚀 INICIANDO PRÁCTICA DE ARCHIVOS EN PYTHON")

## 1. Crear archivo inicial (YA CUMPLIDO por el usuario)

## 2 y 4. Leer y cargar productos en lista de diccionarios
# Llama a la función para leer el archivo [cite: 19] y convertir a lista de diccionarios [cite: 22]
productos_en_memoria = leer_productos_a_lista(NOMBRE_ARCHIVO)

# Mostrar los productos cargados (Actividad 2)
mostrar_productos(productos_en_memoria)

## 3. Agregar productos desde teclado
# Modifica el archivo productos.txt con un nuevo producto. Esto se hace
# antes de Guardar, para demostrar el modo 'a'. [cite: 21]
agregar_producto_a_archivo(NOMBRE_ARCHIVO)

# Volver a cargar la lista de productos *después* de la adición para tener la versión más reciente
# Nota: La actividad 6 pide sobrescribir al final, por lo que esta recarga es opcional
# si se sigue estrictamente el orden. Para fines prácticos, se recarga para
# que la búsqueda se haga sobre el producto recién agregado.
productos_en_memoria = leer_productos_a_lista(NOMBRE_ARCHIVO)
mostrar_productos(productos_en_memoria)

## 5. Buscar producto por nombre
buscar_producto_por_nombre(productos_en_memoria)

## 6. Guardar los productos actualizados (Sobrescribir el archivo)
# Esta función toma la lista de diccionarios y la escribe completamente en el archivo,
# borrando el contenido anterior. (Actividad 6) [cite: 33]
guardar_productos_actualizados(productos_en_memoria, NOMBRE_ARCHIVO)

print("\n🎉 PRÁCTICA FINALIZADA")