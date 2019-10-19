def callback(MoistureSensor1):
    #if GPIO.input(MoistureSensor1):
    if GPIO.gpio_function(15) == GPIO.HIGH:
        print("MoistureSensor on")
        GPIO.output(Pump1, GPIO.HIGH)
        GPIO.output(Pump2, GPIO.HIGH)
        time.sleep(0.25)
    else:
        print("MoistureSensor off")
        GPIO.output(Pump1, GPIO.LOW)
        GPIO.output(Pump2, GPIO.LOW)
        time.sleep(0.25)

def main():
    pump_and_moisture = input("Switch pump and moisture sensor on? ")
    if pump_and_moisture == "yes":
        callback()
    else:
        print("nope")
    
# Runs main() function first!
if __name__ == "__main__":
    import RPi.GPIO as GPIO
    import time

    GPIO.setwarnings(False)

    # Set our GPIO numbering to BCM
    GPIO.setmode(GPIO.BCM)

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
    GPIO.add_event_detect(MoistureSensor1, GPIO.BOTH, bouncetime=300)
    # This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
    GPIO.add_event_callback(MoistureSensor1, callback)

    # This is an infinte loop to keep our script running
    while True:
        time.sleep(1)

    main()
