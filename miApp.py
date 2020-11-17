
#Clases
class Punto():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

p = Punto(10.2, 3.5)
print(p.numero1)
print(p.numero2)

#EJERCICIO
class Vuelo():
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.pasajeros = []

    def agregar_pasajeros(self, nombre):
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(nombre)
        return True

    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

vuelo147 = Vuelo(147, 200)
print(vuelo147.capacidad)
print(vuelo147.numero)
vuelo147.agregar_pasajeros("Juan Carlos")
vuelo147.agregar_pasajeros("José Perez")
print(vuelo147.pasajeros)
print(vuelo147.asientos_disponibles())
vuelo147.agregar_pasajeros("Jon Doe")

personas = ["Harry", "Ron", "Hermione"]
for unaPersona in personas:
    if vuelo147.agregar_pasajeros(unaPersona):
        print(f"se agregó a {unaPersona} al vuelo número {vuelo147.numero}")
    else:
        print(f"No se pudo agregar a {unaPersona} por limite de capacidad del vuelo")

#HERENCIA
class Empleado():
    num_empleado= 0
    porcentaje_aumento= 1.04
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.email = nombre + '.' + apellido + '@miempresa.com'
        Empleado.num_empleado += 1    

    def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)
    def aplicar_aumento(self):
        self.sueldo = int(self.sueldo * self.porcentaje_aumento)

class Desarrolador(Empleado):
    pass
    def __init__(self,nombre,apellido,sueldo, lenguaje):
        super().__init__(nombre,apellido,sueldo)
        self.lenguaje= lenguaje

empleado1 = Desarrolador("Harry", "Potter", 9990, "python")
print(empleado1.email)
print(empleado1.lenguaje)

#Polimorfismo
class Tomate():
    def tipo(self):
        print("vegetal")
    def color(self):
        print("Rojo")

class Manzana():
    def tipo(self):
        print("Fruta")
    def color(self):
        print("Rojo")

def func(obj):
    obj.tipo()
    obj.color()

unTomate = Tomate()
unaManzana = Manzana()

func(unTomate)
func(unaManzana)

class Argentina():
    def capital(self):
        print("CABA")
    def idioma(self):
        print("Español")

class EEUU():
    def capital(self):
        print("Washington DC")
    def idioma(self):
        print("Ingles")

paisArgentina = Argentina()
paisEEUU =EEUU()

for unPais in (paisArgentina, paisEEUU):
    unPais.capital()
    unPais.idioma()


class Ave: 
    def introduccion(self):
        print("existen muchos tipos de aves")
    def vuelo(self):
        print("algunas aves pueden volar y otras no")

class perico(Ave):
    def vuelo(self):
        print("los pericos pueden volar")

class pinguino(Ave):
    def vuelo(self):
        print("los pinguinos no pueden volar")

unAve = Ave()
unPerico = perico()
unPinguino = pinguino()

unAve.introduccion()
unAve.vuelo()

unPerico.introduccion()
unPerico.vuelo()

unPinguino.introduccion()
unPinguino.vuelo()


