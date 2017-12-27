import RPi.GPIO as GPIO
import dht11
import time
import datetime

def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(100.0 / 1000.0)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(100.0 / 1000.0)
        return


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using GPIO 14 , PIN = 08
# led signal using GPIO 17, PIN = 11
instance = dht11.DHT11(pin=14)
GPIO.setup(17, GPIO.OUT)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
        blink(17)
    time.sleep(1)
