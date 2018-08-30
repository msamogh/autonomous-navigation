import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse

from control import RobotControl
from robot import Robot
from sensor import MarkerSensor
from trajectory import Rectangle
from world import Marker


trajectory = Rectangle()
marker = Marker(3, 0)
marker_sensor = MarkerSensor(marker)
control = RobotControl()
robot = Robot(
    initial_state=np.array([
        -Rectangle.WIDTH / 2,
        -Rectangle.HEIGHT / 2,
        math.pi / 2]),
    control=control,
    sensors=[marker_sensor]
)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'bo', animated=True, label='Actual trajectory')
legend = plt.legend()
plt.grid()


def init():
    trajectory.draw(ax)
    marker.draw(ax)
    return ln,

patches = []


def update(t):
    control_vector = control.get_control_vector(t)
    if all([x == 0 for x in control_vector]):
        return patches
    robot.move(control_vector)
    robot.sense()
    xdata = [state.x[0] for state in robot.states]
    ydata = [state.x[1] for state in robot.states]

    state = robot.filter
    variance = Ellipse(xy=state.x[:2],
                       width=state.P[0][0], height=state.P[1][1],
                       angle=state.P[2][2],
                       facecolor='none',
                       edgecolor='g')
    patches.append(variance)
    patches.append(ln)
    ax.add_patch(variance)
    ln.set_data(xdata, ydata)
    return patches

ani = FuncAnimation(fig,
                    update,
                    frames=500,
                    init_func=init,
                    blit=True,
                    interval=50)
plt.show()
