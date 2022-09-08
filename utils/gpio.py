import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

def setup(config):
    global relay_pin, toggled_time
    relay_pin = int(config['RELAY_PIN'])
    toggled_time = int(config['TOGGLED_TIME'])
    GPIO.setup(relay_pin, GPIO.OUT)

def toggle_door():
    global relay_pin, toggled_time
    GPIO.output(relay_pin, GPIO.HIGH)
    sleep(toggled_time)
    GPIO.output(relay_pin, GPIO.LOW)
    GPIO.cleanup()
    return True
