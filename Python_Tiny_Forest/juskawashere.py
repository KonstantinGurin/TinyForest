#!/usr/bin/python
#
#  TinyForest Garden System
#
#  Python back-end for sensor data
#
#  Copyright (c) 2019, Kasviloordit
#

import RPi.GPIO as GPIO
import signal
import sys
import re
import threading
import time
import datetime
import json

GPIO.setmode(GPIO.BCM)

# Suppress GPIO warnings
GPIO.setwarnings(False)

####################

# TODO: add support to the following sensors
# - acidity sensor (pH)
# - temperature sensor
# - light sensor
# - support for multiple plant profiles (JSON?)
#   - remove/generalize hardcoded/duplicate variable definitions from this code

####################

# GPIO pin mapping + directions
# Ref: https://pinout.xyz
pin = {
  'pump_1':     '2 out',
  'pump_2':     '3 out',
  'moisture_1': '15 in'

#  'acid_1': 'XX in',
#  'temp_1': 'XX in',

#  'lightdetect_1': 'XX in',
#  'lightbulb_1':   'XX out'
}

####################

class sensor(object):

  def __init__ (self, high_time, time_step, max_high_time):

    self.high_out  = False
    self.low_out   = False
    self.run       = True
    self.high_time = high_time

    # Time step between while loop rounds, in seconds
    self.time_step = time_step

    # Maximum time the sensor can be active, in seconds
    self.max_high_time = max_high_time

  ##########
  def powercontrol(self, datavalue, trigger_pin, trigger_min, trigger_max, pin, pindef):

    def msg_header():
      return str(datetime.datetime.now()) + " - " + pindef

    # Set trigger value of a new variable pump_powerthread
    # Used when the Python process is interrupted
    while self.run:
      if datavalue == "pindata":
        arg = GPIO.input(trigger_pin)
      else:
        arg = int(datavalue)

      # Use sleep to avoid incorrect outputs
      time.sleep(self.time_step)

      if arg <= trigger_min:
        GPIO.output(pin,GPIO.HIGH)
        self.low_out = False

        self.high_time = self.high_time + self.time_step

        if not self.high_out:
          print(msg_header(), "ON (GPIO pin: " + str(pin) + ")")
          self.high_out = True

      if arg >= trigger_max or self.high_time >= self.max_high_time:
        GPIO.output(pin,GPIO.LOW)
        self.high_out = False

        if not self.low_out:
          if self.high_time != 0:
            print(msg_header(), "active time: " + str(round(self.high_time,2)) + " seconds")
            self.high_time = 0

          print(msg_header(), "OFF (GPIO pin: " + str(pin) + ")")
          self.low_out = True

    if not self.run:
      GPIO.output(pin,GPIO.LOW)

  ##########
  # TODO file data value parser for temperature, light and acidity sensors
  #def fileparser():

####################

# Extract pin numbers from pin dictionary key values to a temporary dictionary pin_tmp
pin_tmp = {}
for key,value in pin.items():
  value = int(''.join(filter(str.isdigit,value)))
  pin_tmp[key] = int(value)

# Set pin directions properly according to pin dictionary key values
for key,value in pin_tmp.items():
  if re.search(r'out',pin[key]):
    GPIO.setup(value,GPIO.OUT, initial=GPIO.LOW)
  elif re.search(r'in',pin[key]):
    GPIO.setup(value,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  else:
    raise ValueError("Pin direction not defined for " + key)
    sys.exit(1)

# Since pin directions are known, replace original pin dict with pin_tmp with properly
# extracted pin numbers for further use.
pin = pin_tmp
del pin_tmp

####################

# TODO change condition "== 0" to "== 1" and vice versa
waterpump_power          = sensor(0, 0.25, 5)
waterpump_powerthread    = threading.Thread(
  target=waterpump_power.powercontrol,
  args=(
    'pindata',           # data value. Use pindata to read 1/0 GPIO value. For more sophisticated checks, use a defined integer value
    pin['moisture_1'],   # trigger sensor
    0, 1,                # trigger sensor values: min, max
    pin['pump_1'],       # target sensor
    'Water pump (1)',    # target sensor friendly name
  )
)

#nutrientpump_power       = sensor(0, 0.25, 5)
#nutrientpump_powerthread = threading.Thread(
#  target=nutrientpump_power.powercontrol,
#  args=(
#    XX,
#    pin['acid_1'],
#    XX,XX,
#    pin['pump_2'],
#    'Nutrient pump (1)',
#  )
#)
#
#lightsensor_power        = sensor(0, 2, 240)
#lightsensor_powerthread  = threading.Thread(
#  target=lightsensor_power.powercontrol,
#  args=(
#    XX,
#    pin['lightdetect_1'],
#    XX,XX,
#    pin['lightbulb_1'],
#    'UV light (1)',
#  )
#)

####################
# Linux process signal handler function

def sig_handler(sig, frame):

  # Terminate child threads
  waterpump_power.run    = False
#  nutrientpump_power.run = False
#  lightsensor_power.run  = False
  sys.exit(0)

####################
# Linux process signal handlers
# Covers KeyboardInterrupt as well
# See: 'man 7 signal' for additional signals


#FIX PLZ. Keyboardinterrupt -> pump stays on
signals = ['SIGINT', 'SIGTERM', 'SIGTSTP', 'SIGTTIN', 'SIGTTOU']

for i in signals:
  signal.signal(getattr(signal, i), sig_handler)

####################

# ONLY FOR TEMPORARY TESTING PURPOSES

if re.search(r'[y|Y]',input("Run test? [Y/n] ")):

  while True:

    test_input = int(input("Insert value 0-5: "))

    if test_input == 0:
      GPIO.output(pin['pump_1'], GPIO.HIGH)

    elif test_input == 1:
      GPIO.output(pin['pump_2'], GPIO.HIGH)

    elif test_input == 2:
      GPIO.output(pin['pump_1'], GPIO.HIGH)
      GPIO.output(pin['pump_2'], GPIO.HIGH)

    elif test_input == 3:
      GPIO.output(pin['pump_1'], GPIO.LOW)

    elif test_input == 4:
      GPIO.output(pin['pump_2'], GPIO.LOW)

    elif test_input == 5:
      GPIO.output(pin['pump_1'], GPIO.LOW)
      GPIO.output(pin['pump_2'], GPIO.LOW)
      sys.exit(0)

    else:
      print("Value must be between 0-5")

##########

else:
  waterpump_powerthread.start()
#  nutrientpump_powerthread.start()
#  lightsensor_powerthread.start()

####################

signal.pause()

#haista paska
