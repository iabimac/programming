#!/usr/bin/python
decimal = int(input("Ingresa un número decimal: "))
if decimal <= 0:
  print(decimal)
  exit(0)
# Aquí almacenamos el resultado
binario = ""
# Mientras se pueda dividir...
numLed = 1
while decimal > 0:
  # Saber si es 1 o 0
  residuo = int(decimal % 2)
  # E ir dividiendo el decimal
  decimal = int(decimal / 2)
  # Ir agregando el número (1 o 0) a la izquierda del resultado
  binario = str(residuo) + binario
  if residuo:
    print("Prende led #",numLed)
  numLed += 1
print(binario)
