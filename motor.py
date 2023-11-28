import wiringpi
from time import sleep

right_dir_pin = 24
right_out_pin = 25
left_dir_pin = 27
left_out_pin = 28

output_pins = [left_dir_pin, left_out_pin, right_dir_pin, right_out_pin]

time_step = 1 / 2000

def init_output_pin (pin):
    wiringpi.pinMode(pin, wiringpi.OUTPUT)

def init_all_output_pins ():
    for pin in output_pins:
        init_output_pin(pin)

def step_motors (left, left_dir, right, right_dir):
    wiringpi.digitalWrite(left_dir_pin, left_dir)
    wiringpi.digitalWrite(right_dir_pin, right_dir)
    wiringpi.digitalWrite(left_out_pin, left)
    wiringpi.digitalWrite(right_out_pin, right)
    sleep(time_step / 2)
    wiringpi.digitalWrite(left_out_pin, wiringpi.LOW)
    wiringpi.digitalWrite(right_out_pin, wiringpi.LOW)
    sleep(time_step / 2)

def convert_direction_to_motor (delta):
    if delta[0] == 0 and delta[1] == 1:
        return [[wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH]]
        #return [1, 1]
    elif delta[0] == 1 and delta[1] == 0:
        return [[wiringpi.HIGH, wiringpi.LOW, wiringpi.HIGH, wiringpi.HIGH]]
        #return [-1, 1]
    elif delta[0] == 0 and delta[1] == -1:
        return [[wiringpi.HIGH, wiringpi.LOW, wiringpi.HIGH, wiringpi.LOW]]
        #return [-1, -1]
    elif delta[0] == -1 and delta[1] == 0:
        return [[wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH, wiringpi.LOW]]
        #return [1, -1]
    elif delta[0] == 1 and delta[1] == 1:
        return [[wiringpi.LOW, wiringpi.LOW, wiringpi.HIGH, wiringpi.HIGH]] * 2
        #return [0, 2]
    elif delta[0] == -1 and delta[1] == -1:
        return [[wiringpi.LOW, wiringpi.LOW, wiringpi.HIGH, wiringpi.LOW]] * 2
        #return [0, -2]
    elif delta[0] == 1 and delta[1] == -1:
        return [[wiringpi.HIGH, wiringpi.LOW, wiringpi.LOW, wiringpi.LOW]] * 2
        #return [-2, 0]
    elif delta[0] == -1 and delta[1] == 1:
        return [[wiringpi.HIGH, wiringpi.HIGH, wiringpi.LOW, wiringpi.LOW]] * 2
        #return [2, 0]
    
def step_direction (delta):
    motor = convert_direction_to_motor(delta)
    for args in motor:
        step_motors(*args)

def test_horizontal (test_steps):
    for _ in range(test_steps):
        step_motors(wiringpi.HIGH, wiringpi.LOW, wiringpi.HIGH, wiringpi.HIGH)

    for _ in range(test_steps):
        step_motors(wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH, wiringpi.LOW)

def test_vertical (test_steps):
    for _ in range(test_steps):
        step_motors(wiringpi.HIGH, wiringpi.LOW, wiringpi.HIGH, wiringpi.LOW)

    for _ in range(test_steps):
        step_motors(wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH)

def test_diagonal(test_steps):
    for left, right in [[wiringpi.LOW, wiringpi.HIGH], [wiringpi.HIGH, wiringpi.LOW]]:
        for _ in range(test_steps):
            step_motors(left, wiringpi.HIGH, right, wiringpi.HIGH)

        for _ in range(test_steps):
            step_motors(left, wiringpi.LOW, right, wiringpi.LOW)

def deinit_output_pin (pin):
    wiringpi.digitalWrite(pin, wiringpi.LOW)
    wiringpi.pinMode(pin, wiringpi.INPUT)

def deinit_all_output_pins ():
    for pin in output_pins:
        deinit_output_pin(pin)
