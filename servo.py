import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 100)

p.start(19)

time.sleep(2)
while 1:
        p.ChangeDutyCycle(16)
        time.sleep(0.1)
        p.ChangeDutyCycle(19)
        time.sleep(0.1)
 
p.stop()

GPIO.cleanup()
