import RPi.GPIO as GPIO
import time

SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 3

SERVO_UP_DUTY = 5
SERVO_DOWN_DUTY = 3

class Servo:
    def __init__ (self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.pin = pin

    def rotate_servo (self, duty):
        self.pwm.ChangeDutyCycle(duty)
        pass

    def up_pen (self):
        self.rotate_servo(SERVO_UP_DUTY)
        pass

    def down_pen (self):
        self.rotate_servo(SERVO_DOWN_DUTY)
        pass

    def end_servo (self):
        self.pwm.stop()
        GPIO.cleanup(self.pin)
        pass
