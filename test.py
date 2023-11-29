from path import *
from servo import *

#print(convert_paths_to_step_paths([300, 600], [[[32, 100], [43, 20]]]))
#print(find_direction(np.array([1, 1]), np.array([3, 3])))
#print(find_direction(np.array([3, 3]), np.array([3, 3])))
#print(find_direction(np.array([1, 1]), np.array([1, 2])))
#print(find_direction(np.array([1, 1]), np.array([2, 3])))
#print(find_direction(np.array([1, 1]), np.array([-2, 3])))


servo = Servo(12)
servo.down_pen()
