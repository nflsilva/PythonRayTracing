import numpy as np


class Color:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, other):
        return np.array([self.r * other.r, self.g * other.g, self.b * other.b])
