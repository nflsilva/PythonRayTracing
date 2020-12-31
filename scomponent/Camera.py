import numpy as np


class Camera:

    def __init__(self, x, y, z):
        self.position = np.array([x, y, z])
