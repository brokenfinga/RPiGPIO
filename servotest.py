import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

l = GPIO.PWM(13,50)
r = GPIO.PWM(15,50)

l.start(7.5)
r.start(7.5)

try:

	while True:
		l.ChangeDutyCycle(7.5)
		r.ChangeDutyCycle(7.5)
		time.sleep(1)

		l.ChangeDutyCycle(12.5)
		r.ChangeDutyCycle(12.5)
		time.sleep(1)

		l.ChangeDutyCycle(2.5)
		r.ChangeDutyCycle(2.5)
		time.sleep(1)


except KeyboardInterrupt:
	l.stop()	
	r.stop()
	GPIO.cleanup()

