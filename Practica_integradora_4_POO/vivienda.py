from habitacion import Habitacion

class SuperficieCubiertaExcepcion(Exception):
    pass

class Vivienda:
    def __init__(self, calle, numero, manzana, nro_casa, sup_terreno):
        self.calle = calle
        self.numero = numero
        self.manzana_id = manzana 
        self.nroCasa = nro_casa
        self.sup_terreno = sup_terreno 
        self.habitaciones_lista = []
        
    def agregar_habitacion(self, habitacion):
        self.habitaciones_lista.append(habitacion)

    def getMetrosCuadradosCubiertos(self):
        metros_cubiertos = 0.0
        for hab in self.habitaciones_lista: 
            metros_cubiertos += hab.m2 
            
        if metros_cubiertos > self.sup_terreno:
            raise SuperficieCubiertaExcepcion(
                f"La superficie cubierta ({metros_cubiertos} m²) es MAYOR que la superficie del terreno ({self.sup_terreno} m²). Revisar!"
            )
            
        return metros_cubiertos