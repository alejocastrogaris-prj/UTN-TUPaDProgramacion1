# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

def agregar_producto(productos_stocks): #Esto agrega productos y verifica que el nombre no sea un digito y se ingrese str
    while True:
        try:
            producto_nuevo = str(input("Ingrese el nuevo producto: ")).lower()
            if producto_nuevo.isdigit():
                print("No puede ingresar numeros como nombre del producto")
                continue
            if producto_nuevo in productos_stocks:
                print(f"El producto --{producto_nuevo}-- ya existe.")
            elif producto_nuevo not in productos_stocks:
                productos_stocks[producto_nuevo] = 0
                print(f"El producto nuevo: --{producto_nuevo}-- no tiene stock")
                print("\n\Agregar stock desde el sistema/")
                break
    
        except ValueError:
            print("Solo puede ingresar nombres(str). Vuelva a ingresar")
            continue



def agregar_stock(productos_stocks):
    while True:
        producto = input("A que producto desea agregar stock? -> ")
        if producto.lower() not in productos_stocks:
            print("Ese producto no existe")
            continue
        elif producto.lower() in productos_stocks:
            stock_agregar = int(input(f"Eliga la cantidad de {producto.lower()} a agregar: "))
            productos_stocks[producto.lower()] += stock_agregar
            print(f"\nSe agrego {stock_agregar} unidades de {producto}")
            break



def consultar_stock(productos_stocks):
    print("\n---PRODUCTOS y STOCK---")
    for producto,stock in productos_stocks.items():
        print(f"{producto} Stock: {stock}")


def Menu():
    print("\n\--MENU PRINCIPAL--/")
    print("\n1) Consultar stock.")
    print("\n2) Agregar stock.")
    print("\n3) Agregar producto.")
    print("\n4) Finalizar programa")


    print("#-------------#")
    try:
        opcion = int(input("Ingrese la opcion: "))
        if opcion < 0 or opcion > 4:
            print(f"❌Ingrese una opcion valida❌")
            Menu()
        #-------------------------------------------
        if opcion == 1:
            return consultar_stock(productos_stocks)
        
        if opcion == 2:
            return agregar_stock(productos_stocks)
        
        if opcion == 3:
            return agregar_producto(productos_stocks)
        
        if opcion == 4:
            print("Finalizando programa....")
            exit()
        
    except ValueError:
        print("❌Ingrese una opcion valida❌")
        Menu()

#Diccionario de la consigna

productos_stocks = {
    "manzana" : 100,
    "banana" : 200,
    "pera" : 50,
    "alfajores" : 20,
    "lays" : 35
}

#Programa Principal
while True:
    Menu()




