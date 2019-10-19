import RPi.GPIO as GPIO
from gpiozero import LED
import time

red = LED(23)

# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17

def callback(MoistureSensor1):  
	if GPIO.input(MoistureSensor1):
                print("LED on")
                red.on()
	else:
                print("LED off")
                red.off()

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
MoistureSensor1 = 17
# Set the GPIO pin to an input
GPIO.setup(MoistureSensor1, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(MoistureSensor1, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(MoistureSensor1, callback)

# This is an infinte loop to keep our script running
while True:
	# This line simply tells our script to wait 0.1 of a second, this is so the script doesnt hog all of the CPU
	#time.sleep(0.1)
	time.sleep(1)

