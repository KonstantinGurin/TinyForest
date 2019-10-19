import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

Pump1 = 3
Pump2 = 2

GPIO.setup(Pump1, GPIO.OUT)
GPIO.setup(Pump2, GPIO.OUT)

def pump_switch():
    pump_loop = True

    while pump_loop:
        pumpSwitch = str(input("1 = Pump1 Paalle, 2 = Pump1 Pois, 3 = Pump2 Paalle, 4 = Pump2 Pois, 5 tai muu = Sammutetaan ohjelma: "))

        if pumpSwitch == "1":
            print("Pump1 kytketaan paalle")
            GPIO.output(Pump1, GPIO.HIGH)

        elif pumpSwitch == "2":
            print("Pump1 kytketaan pois paalta")
            GPIO.output(Pump1, GPIO.LOW)

        elif pumpSwitch == "3":
            print("Pump2 kytketaan paalle")
            GPIO.output(Pump2, GPIO.HIGH)

        elif pumpSwitch == "4":
            print("Pump2 kytketaan pois paalta")
            GPIO.output(Pump2, GPIO.LOW)

        elif pumpSwitch == "5":
            pump_loop = False
            GPIO.output(Pump1, GPIO.LOW)
            GPIO.output(Pump2, GPIO.LOW)
            break

pump_switch()
