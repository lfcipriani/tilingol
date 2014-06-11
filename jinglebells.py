import RPi.GPIO as GPIO
import time
import sys

class JingleBells:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def shake(self, iterations, speed):
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(19)
        time.sleep(speed)
        for n in range(iterations):
            self.pwm.ChangeDutyCycle(16)
            time.sleep(speed)
            self.pwm.ChangeDutyCycle(19)
            time.sleep(speed)
        self.pwm.stop()

    #def __del__(self):
    #    GPIO.cleanup()

if __name__ == '__main__':
    jb = JingleBells(18)
    jb.shake(int(sys.argv[1]), float(sys.argv[2]))

