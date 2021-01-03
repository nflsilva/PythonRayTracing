import numpy as np


class Light:

    def __init__(self, x, y, z, material):

        self.position = np.array([x, y, z])
        self.material = material
