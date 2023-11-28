import numpy as np
from motor import *
from path import *

class Drawer:
    cur_pos = np.array([0, 0], dtype=np.int32)

    def move_to_target (self, target_pos):
        while self.cur_pos[0] != target_pos[0] or self.cur_pos[1] != target_pos[1]:
            direction = find_direction(self.cur_pos, target_pos)
            if check_overflow(self.cur_pos, direction):
                return;
            step_direction(direction)
            self.cur_pos += np.array(direction, dtype=np.int32)

    def draw (self, step_paths):
        for step_path in step_paths:
            self.move_to_target(np.array(step_path[0], dtype=np.int32))
            for pos in step_path[1: ]:
                self.move_to_target(np.array(pos, dtype=np.int32))
