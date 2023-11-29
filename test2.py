from motor import *

wiringpi.wiringPiSetup()
init_all_output_pins()

for _ in range(1000):
    step_direction([1, 0])

for _ in range(1000):
    step_direction([-1, 0])
