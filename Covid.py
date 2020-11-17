import pandas as pd

url ="https://covid.ourworldindata.org/data/ecdc/full_data.csv"

import wget as w
w.wget(url)

df = pd.read_csv(url)
pd.set_option("display.max_columns",80)

#print(df.shape)
#print(df.size)
#print(df.info())
#print(df)
#paisesFiltrados = df[(df["location"] == "Argentina") & (df["date"] > '2020-07-19')]
#print(paisesFiltrados)
#d = paisesFiltrados.to_dict("list")
#print(d)
#d = df.to_dict("list")


#for x in d['location']:
#    if x == "Argentina":
#        print(x)



bandera = 'S'
paises = []

while (bandera =='S'):
    pais = input("Ingrese un pais\n")
    bandera2 = pais.isalpha()
    while (not bandera2):
        pais = input("Ingrese solo caracteres. Ingrese un pais\n")
        bandera2 = bandera2 = pais.isalpha()

        
    paises.append(pais)
    bandera  = (input("Desea ingresar otro pais? S/N\n")).upper()
    while ((bandera !='S') and (bandera != 'N')  ):
        bandera  = (input("Debe seleccionar S/N. Desea ingresar otro pais? \n")).upper()
        print(bandera)


print(paises)
print(bandera)

from datetime import datetime

while True:
    try:

        fechaDesde = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
        datetime.strptime(fechaDesde, '%Y-%m-%d')
        break
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")

while True:
    try:
        fechaHasta = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
        datetime.strptime(fechaHasta, '%Y-%m-%d')
        break
    except ValueError:
        print("\n No ha ingresado una fecha correcta...")

dic = df.to_dict("records")
#print(dic)
print(paises)

nuevo={}
for x in dic :
    for pais in paises:
        if (x['location']== pais):
            nuevo[pais]  = ( x['new_cases'], x)
            #nuevo = nuevo.fromkeys(paises,x )
            print(nuevo)
"""
base_de_datos2=[]
for pais in paises:
    base_de_datos2.append(dic[pais])
"""
#print(nuevo)

#nuevo: {clave: pais, valor: cantidad de casos, fallecimientos, fecha}

"""base_de_datos2={}
for pais in paises:
    base_de_datos2[pais]=dic[pais]
"""
