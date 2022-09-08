import RPi.GPIO as GPIO
from time import sleep

def setup(config):
    global relay_pin, toggled_time
    relay_pin = int(config['RELAY_PIN'])
    toggled_time = int(config['TOGGLED_TIME'])
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin, GPIO.OUT)

def toggle_door():
    global relay_pin, toggled_time
    try:
        GPIO.output(relay_pin, GPIO.HIGH)
        sleep(toggled_time)
        GPIO.output(relay_pin, GPIO.LOW)
    except:
        GPIO.cleanup()
        return False
    GPIO.cleanup()
    return True
