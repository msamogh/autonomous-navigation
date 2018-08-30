import matplotlib.patches as patches


class Rectangle(object):

    MARGIN = 5
    WIDTH = 10
    HEIGHT = 5

    @property
    def perimeter(self):
        return 2 * (Rectangle.WIDTH + Rectangle.HEIGHT)

    def draw(self, ax):
        ax.set_xlim(-Rectangle.WIDTH / 2 - Rectangle.MARGIN, Rectangle.WIDTH / 2 + Rectangle.MARGIN)
        ax.set_ylim(-Rectangle.WIDTH / 2 - Rectangle.MARGIN, Rectangle.WIDTH / 2 + Rectangle.MARGIN)
        ax.legend()
        rect = patches.Rectangle(
            (-Rectangle.WIDTH / 2, -Rectangle.HEIGHT / 2),
            Rectangle.WIDTH, Rectangle.HEIGHT,
            linewidth=1,
            label='Ideal trajectory',
            edgecolor='r',
            facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)
