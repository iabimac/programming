from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

button = Button(21)
ligths = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)

num = int(input("Enter a number:"))
print(num,bin(num),len(bin(num)))

while True:
    ligths.green.on()
    sleep(4)
    ligths.green.off()
    ligths.amber.on()
    sleep(2)
    ligths.amber.off()
    ligths.green.off()
    ligths.red.on()
    sleep(4)
    ligths.red.off()