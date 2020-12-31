import numpy as np


def normalize(vector):
    return vector / np.linalg.norm(vector)


class Ray:

    def __init__(self, origin, destination):
        self.origin = origin
        self.direction = normalize(destination - origin)
