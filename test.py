from path import *
from servo import *
from motor import *
import wiringpi

wiringpi.wiringPiSetup()

try:
    init_all_output_pins()
except KeyboardInterrupt:
    deinit_all_output_pins()

#for _ in range(1000):
#    step_motors(wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH, wiringpi.HIGH)
#for _ in range(1000):
#    step_motors(wiringpi.HIGH, wiringpi.LOW, wiringpi.HIGH, wiringpi.LOW)
for _ in range(1000):
    step_direction([1, 0])

for _ in range(1000):
    step_direction([-1, 0])

