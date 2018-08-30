import numpy as np


class MarkerSensor(object):

    def __init__(self, marker):
        self.name = 'marker_sensor'
        self.marker = marker

    def get_measurement(self, state):
        observation_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        noise = np.diag([1, 1, 0.1])
        distances = np.array([
            abs(state[0] - self.marker.x),
            abs(state[1] - self.marker.y)
        ])
        distance = np.linalg.norm(distances)
        if distance < 3:
            noise = np.diag([5 * distances[0] + 1, 10 * distances[1] + 1, 0.01])
            print(noise)
            return (observation_matrix, np.matmul(observation_matrix, state), noise)
        return (None, None, noise)
