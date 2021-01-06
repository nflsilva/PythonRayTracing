import numpy as np


def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis


def normalize(vector):
    return vector / np.linalg.norm(vector)
