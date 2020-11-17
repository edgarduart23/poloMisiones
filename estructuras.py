

nombre = "Harry"
print(nombre[0])
#LISTAS
nombres = ["Harry", "Ron", "hermione"]
print(nombres)
#agregar un elemento a la lista
nombres.append("Draco")
print(nombres)
#ordenar la lista
nombres.sort()
print(nombres)
#borar la lista
nombres.clear()
print(nombres)

#SET: no agrega elementos repetidos
conjunto = set()
#add: agrega elemento al conjunto
conjunto.add(1.0)
conjunto.add(2.0)
conjunto.add(1.0)
print(conjunto)
#remove: elimina elemento del conjunto
conjunto.remove(2.0)
#len: la longitud del conjunto
print(f"El conjunto {conjunto} tiene {len(conjunto)} elemento")

#DICCIONARIO
casas = {"Harry" : "Gryffindor", "Draco" : "Slytherin"}
print(casas["Harry"])
print(casas["Draco"])
#agregar un nuevo elemento
casas["Hermione"] = "Gryffindor"
print(casas["Hermione"])

#EVALUACION 3

ejemploSet = {"Amarillo", "Naranja", "Negro"}
ejemploList = ["Azul", "Verde", "Rojo"]
ejemploSet = ejemploSet.add(ejemploList )
print(ejemploSet)

conjunto1 = {10, 20, 30, 40, 50}
conjunto2 = {30, 40, 50, 60, 70}
print(conjunto1.intersection(conjunto2))

conjunto1 = {10, 20, 30}
conjunto2 = {20, 40, 50}
conjunto1.difference_update(conjunto2)
print(conjunto1)

ejemploDiccionario = { 
   "clase":{ 
      "estudiante":{ 
         "nombre":"Marcos",
         "examenes":{ 
            "matematica":70,
            "geografia":80
         }
      }
   }
}
print(ejemploDiccionario['clase']['estudiante']['examenes']['matematica'])

from datetime import datetime, timedelta
fecha_dada = datetime(2020, 3, 22, 10, 00, 00)
fecha_limite = fecha_dada + timedelta(days=7, hours=12)
print(fecha_limite)

