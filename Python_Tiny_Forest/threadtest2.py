import threading
import time
import RPi.GPIO as GPIO
import signal
import sys

#setup GPIO
# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# Define the GPIO pin that we have our digital output from our sensor connected to
MoistureSensor1 = 15
Pump1 = 3
Pump2 = 2

# Set the GPIO pin to an input
# Kosteusmittari
GPIO.setup(MoistureSensor1, GPIO.IN)
# Pumput saadetty output:ina
GPIO.setup(Pump1, GPIO.OUT)
GPIO.setup(Pump2, GPIO.OUT)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
#GPIO.add_event_detect(MoistureSensor1, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
#GPIO.add_event_callback(MoistureSensor1, callback)



class sensor:
    
    def __init__ (self):
        self.key = True


    def thread_moisture(self,asd):
      while self.key:
          time.sleep(0.5)

          print("Checking moisture")

          time.sleep(0.5)
          if GPIO.input(MoistureSensor1) == 1:
              print("Dry")
              GPIO.output(Pump1, GPIO.HIGH)
              GPIO.output(Pump2, GPIO.HIGH)
              time.sleep(0.25)

          else:
              print("Wet")
              GPIO.output(Pump1, GPIO.LOW)
              GPIO.output(Pump2, GPIO.LOW)
              time.sleep(0.25)

          time.sleep(0.5)

      if not self.key:
          GPIO.output(Pump1, GPIO.LOW)
          GPIO.output(Pump2, GPIO.LOW)


if __name__ == "__main__":
    
    waterpump_sensor = sensor()
    begin = threading.Thread(target=waterpump_sensor.thread_moisture, args=(1,))

    #begin2 = threading.Thread(target=thread_temp, args=(1,))
    
    begin.start()
    #begin2.start()
    print("main method print")







def sig_handler(sig, frame):

  # TODO move threading to the main process file
  # Terminate child threads
  waterpump_sensor.key = False
  sys.exit(0)

####################
# Linux process signal handlers
# Covers KeyboardInterrupt as well
# See: 'man 7 signal' for additional signals

signals = ['SIGINT', 'SIGTERM', 'SIGTSTP', 'SIGTTIN', 'SIGTTOU']

for i in signals: 
    signal.signal(getattr(signal, i), sig_handler)


signal.pause()

