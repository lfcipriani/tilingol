import RPi.GPIO as GPIO
import time

class JingueBells:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)

    def shake(self, iterations, speed):
        self.pwm.start(19)
        time.sleep(speed)
        for n in range(iterations):
            pwm.ChangeDutyCycle(16)
            time.sleep(speed)
            pwm.ChangeDutyCycle(19)
            time.sleep(speed)
        pwm.stop()

    def __del__(self):
        GPIO.cleanup()

