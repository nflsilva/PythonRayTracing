import numpy as np


class Light:

    def __init__(self, x, y, z, color):

        self.position = np.array([x, y, z])
        self.color = color
