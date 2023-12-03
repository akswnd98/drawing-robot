from motor import *
from path import *
import json
from draw import *

wiringpi.wiringPiSetup()

# test_dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]x

try:
    init_all_output_pins()
    for test_dir in test_dirs:
        for _ in range(2000):
            step_direction(test_dir)
    #with open('./data2.txt', 'r') as f:
        #paths = json.loads(f.read())
        #step_paths = convert_paths_to_step_paths([384, 543.085], paths)
        #drawer = Drawer()
        #drawer.draw(step_paths)
        
except KeyboardInterrupt:
    deinit_all_output_pins()
