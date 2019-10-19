from gpiozero import LED
from time import sleep

waterPump1 = LED(3)
waterPump2 = LED(2)

pumpMode1 = False
pumpMode2 = False

while True:
    pumpSwitch = str(input("1 = waterPump1 Paalle, 2 = waterPump1 Pois, 3 = waterPump2 Paalle, 4 = waterPump2 Pois, 5 tai muu = Sammutetaan ohjelma: "))

    if pumpSwitch == "1":
        print("waterPump1 kytketaan paalle")
        waterPump1.on()
        pumpMode1 = True

    elif pumpSwitch == "2":
        print("waterPump1 kytketaan pois paalta")
        waterPump1.off()
        pumpMode1 = False
        
    elif pumpSwitch == "3":
        print("waterPump2 kytketaan paalle")
        waterPump2.on()
        pumpMode2 = True

    elif pumpSwitch == "4":
        print("waterPump2 kytketaan pois paalta")
        waterPump2.off()
        pumpMode2 = False

### Molemmat sammuttaa ohjelma, jompikumpi voi poista.
    elif pumpSwitch == "5":
        if pumpMode1 == True or pumpMode2 == True:
            print("Sammutetaan ohjelma ja molemmat pumput")
            waterPump1.off()
            waterPump2.off()
            break
        
        elif pumpMode1 == False and pumpMode2 == False:
            waterPump1.off()
            waterPump2.off()
            break
    else:
        break
