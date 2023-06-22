from gpiozero import LED
from time import sleep

pinList = [20,25,8,7]
leds = []

for ledNum in pinList:
  leds.append(LED(ledNum))

for led in leds:
  led.off()

decimal = int(input("Ingresa un número decimal: "))

binario = ""
ledID = 0
while decimal > 0:
  residuo = int(decimal % 2)
  decimal = int(decimal / 2)
  binario = str(residuo) + binario
  if residuo:
    leds[ledID].on()
  ledID += 1
print(binario)