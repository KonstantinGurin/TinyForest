from gpiozero import LED
from time import sleep

red = LED(17)

while True:
    led1 = str(input("1 = LED Paalle, 2 = LED Pois, 3 tai muu = Sammutetaan ohjelma, 4 = Blink: "))

    if led1 == "1":
        print("LED kytketaan paalle")
        red.on()

    elif led1 == "2":
        print("LED kytketaan pois paalta")
        red.off()
    elif led1 == "4":
        print("Disco time!!!")
        red.blink()

### Molemmat sammuttaa ohjelma, jompikumpi voi poista.
    elif led1 == "3":
        print("Sammutetaan ohjelma")
        break
    else:
        print("Sammutetaan ohjelma")
        break
