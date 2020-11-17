nota = int( input('Ingrese un número del 1 al 10: ') )

while nota < 1 or nota > 10:
  print('Fuera de rango!')
  nota = int( input('Ingrese un número del 1 al 10: ') )

print( nota >= 4 )