import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(0)

#while 1:
    print("vai")
    for dc in range(0, 101, 5):
        p.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(0.1)
    print("volta")
    for dc in range(100, -1, -5):
        p.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(0.1)
 
p.stop()

GPIO.cleanup()