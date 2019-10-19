import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.LOW)
GPIO.setup(23,GPIO.IN)
while True:
	try:
		if GPIO.input(23):
			print("No light")
			time.sleep(1.0)
		else:
			print("Light")
			time.sleep(1.0)
	except KeyboardInterrupt:
		pass
