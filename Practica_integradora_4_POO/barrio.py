from vivienda import Vivienda, SuperficieCubiertaExcepcion

class Barrio:
    def __init__(self, nombre, empresa_constructora):
        self.nombre_barrio = nombre 
        self.constructora = empresa_constructora 
        self.lista_viviendas = []
        
    def agregar_vivienda(self, vivienda):
        self.lista_viviendas.append(vivienda)

    # Método a) getSuperficieTotalTerreno()
    def getSuperficieTotalTerreno(self):
        total_terreno = 0.0
        for viv in self.lista_viviendas:
            total_terreno += viv.sup_terreno
        return total_terreno

    # Método b) getSuperficieTotalTerrenoXManzana(manzana)
    def getSuperficieTotalTerrenoXManzana(self, manzana_buscada):
        total_terreno_manzana = 0.0
        
        if manzana_buscada is None:
            print("AVISO: Manzana vacía, se devuelve 0.")
            return 0.0
            
        for vivienda in self.lista_viviendas:
            if vivienda.manzana_id.upper() == manzana_buscada.upper(): 
                total_terreno_manzana += vivienda.sup_terreno
        return total_terreno_manzana
        
    # Método d) getSuperficieTotalCubierta()
    def getSuperficieTotalCubierta(self):
        total_cubierta = 0.0
        for viv in self.lista_viviendas:
            try:
                total_cubierta += viv.getMetrosCuadradosCubiertos()
            except SuperficieCubiertaExcepcion as e:
                print(f"[ERROR CUBIERTA] No se pudo sumar la vivienda en {viv.calle}. Mensaje: {e}") 
        return total_cubierta