import copy
import numpy as np

from filterpy.kalman import KalmanFilter


class Robot(object):

    def __init__(self, initial_state, control, sensors):
        self.sensors = sensors
        self.initial_state = initial_state
        self.states = []
        self.init_state()

    def init_state(self):
        self.filter = KalmanFilter(
            dim_x=3,
            dim_z=3
        )
        # Initial state
        self.filter.x = self.initial_state
        self.filter.P = np.zeros((3, 3))
        self.filter.B = np.identity(3)
        # State transition
        self.filter.F = np.identity(3)

    def sense(self):
        H, z, R = self.sensors[0].get_measurement(self.filter.x)
        self.filter.update(z, R=R, H=H)

    def move(self, controls):
        self.states.append(copy.deepcopy(self.filter))
        self.filter.predict(u=controls, Q=np.diag([0.05, 0.1, 0.5]))
