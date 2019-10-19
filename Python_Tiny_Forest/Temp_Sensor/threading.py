import threading
import time
import RPi.GPIO as GPIO
import signal
import sys
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

#setup GPIO
# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#MoistureSensor1 = 15
#Pump1 = 3
#Pump2 = 2
#Temp1 = 4

# Temperature Sensor on GPIO 4 laitettu /boot/config.txt kautta

#GPIO.setup(MoistureSensor1, GPIO.IN)
#GPIO.setup(Temp1, GPIO.IN)

#GPIO.setup(Pump1, GPIO.OUT)
#GPIO.setup(Pump2, GPIO.OUT)


class sensor:

    def __init__ (self):
        self.key = True


#    def thread_moisture(self,asd):
#      while self.key:
#          time.sleep(0.5)
#
#          print("Checking moisture")
#
 #         time.sleep(0.5)
  #        if GPIO.input(MoistureSensor1) == 1:
   #           print("Dry")
    #          GPIO.output(Pump1, GPIO.HIGH)
     #         GPIO.output(Pump2, GPIO.HIGH)
      #        time.sleep(0.25)

       #   else:
#              print("Wet")
 #             GPIO.output(Pump1, GPIO.LOW)
  #            GPIO.output(Pump2, GPIO.LOW)
   #           time.sleep(0.25)

    #      time.sleep(0.5)

    #  if not self.key:
     #     GPIO.output(Pump1, GPIO.LOW)
      #    GPIO.output(Pump2, GPIO.LOW)

    sensor = W1ThermSensor()

    def thread_temp(self,asd):
        while self.key:
            temperature = sensor.get_temperature()
            if temperature > 32:
                print("The temperature is HIGH AT %s celsius" % temperature)
                time.sleep(5)

            elif temperature < 20:
                print("The temperature is LOW AT %s celsius" % temperature)
                time.sleep(5)
            else:
                print("The temperature is fuckang amazing!" % temperature)
                time.sleep(5)


if __name__ == "__main__":
    
    waterpump_sensor = sensor()
    #begin = threading.Thread(target=waterpump_sensor.thread_moisture, args=(1,))

    begin2 = threading.Thread(target=waterpump_sensor.thread_temp, args=(1,))
    
    #begin.start()
    begin2.start()
    print("main method print")


def sig_handler(sig, frame):


  waterpump_sensor.key = False
  sys.exit(0)


signals = ['SIGINT', 'SIGTERM', 'SIGTSTP', 'SIGTTIN', 'SIGTTOU']

for i in signals: 
    signal.signal(getattr(signal, i), sig_handler)


signal.pause()
