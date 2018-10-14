import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)

try:
	while True:
		GPIO.output(20,1)
		sleep(30)
		GPIO.output(20,0)
		sleep(30)

except KeyboardInterrupt:
	GPIO.cleanup()
