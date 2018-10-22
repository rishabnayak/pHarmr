import RPi.GPIO as GPIO

# Import standard python modules
import time

# import Adafruit Blinka
import digitalio
import board

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = 'fa8007a47db04ca29386bdcca2f0c203'
ADAFRUIT_IO_USERNAME = 'pHarmr'

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('light')
except RequestError: # create a digital feed
    feed = Feed(name="light")
    digital = aio.create_feed(feed)

# led set up
led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT



try:
	while True:
            data = aio.receive(digital.key)
            print(data)
            if data.value == 'toggle':
                print('received <- ON\n')
                GPIO.output(20,1)
                time.sleep(30)
                print('Grow light on\n')

            elif data.value == '0':
                print('received <- OFF\n')
                GPIO.output(20,1)
                sleep(30)



except KeyboardInterrupt:

	GPIO.output(20,0)
	GPIO.cleanup()
while True:
    data = aio.receive(digital.key)
    print(data)
    if data.value == 'toggle':
        print('received <- ON\n')
        GPIO.output(20,1)
        time.sleep(30)
        print('Grow light on\n')

    elif data.value == '0':
        print('received <- OFF\n')

    # set the LED to the feed value
    led.value = data.value
    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)
