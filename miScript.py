""" from misFunciones import cuadrado

for i in range(10):
    print(f"el cuadrado de {i} = {cuadrado(i)}")


for i in range(10):
    miCuadrado = cuadrado(i)
    print(f"El cuadrado de {i} = {miCuadrado}") """

import misFunciones
for i in range(10):
    miCuadrado = misFunciones.cuadrados(i)
    print(f"El cuadrado de {i} = {miCuadrado}")
    

    