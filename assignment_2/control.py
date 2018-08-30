import math
import numpy as np

from trajectory import Rectangle


VELOCITY = 0.3
TURNS = [Rectangle.HEIGHT,
         Rectangle.HEIGHT + Rectangle.WIDTH,
         2 * Rectangle.HEIGHT + Rectangle.WIDTH,
         2 * (Rectangle.HEIGHT + Rectangle.WIDTH)]


class RobotControl(object):

    def __init__(self):
        self.vel_ang = 0
        self.vel_x = 0
        self.vel_y = VELOCITY
        self._theta = math.pi / 2

    def get_control_vector(self, t):
        if t > (TURNS[-1] / VELOCITY):
            return np.zeros(3)
        for turn in TURNS:
            if t == int(turn / VELOCITY):
                self.vel_ang = -math.pi / 2
                self._theta += self.vel_ang
            else:
                self.vel_ang = 0

        self.vel_x = VELOCITY * math.cos(self._theta)
        self.vel_y = VELOCITY * math.sin(self._theta)

        control = np.array([
            self.vel_x,
            self.vel_y,
            self.vel_ang
        ])
        return control
