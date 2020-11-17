""" class Vehiculo:
    def __init__(self, nombre, velocidad_maxima, kilometraje):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def capacidad_asientos(self, capacidad):
        return f"La capacidad de asientos de {self.nombre} es de {capacidad} pasajeros"


class Colectivo(Vehiculo):
    def capacidad_asientos(self, capacidad=50):
        return super().capacidad_asientos(capacidad=50) """

class Vehiculo:
    def __init__(self, nombre, velocidad_maxima, kilometraje):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Colectivo(Vehiculo):
    pass

Colectivo_escolar = Colectivo("Mercedez Benz 1114 Escolar", 12, 50)
#print(type(Vehiculo))
#print(type(Colectivo))
#print(type(Colectivo_escolar))
print(isinstance(Colectivo_escolar, Vehiculo))