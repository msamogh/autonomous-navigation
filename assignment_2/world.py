import math
import numpy as np

import matplotlib.patches as patches


class Marker(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intensity_at(self, x, y):
        return np.array([abs(self.x - x), abs(self.y - y)])

    def draw(self, ax):
        circle = patches.Circle((self.x, self.y), 0.1, linewidth=1, color='g')
        ax.add_patch(circle)
