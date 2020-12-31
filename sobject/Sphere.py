import numpy as np
from sobject.SceneObject import SceneObject


class Sphere(SceneObject):

    def __init__(self, origin, radius, color):
        self.origin = origin
        self.radius = radius
        self.color = color

    def intersects_with_ray(self, ray):

        b = 2 * np.dot(ray.direction, ray.origin - self.origin)
        c = np.linalg.norm(ray.origin - self.origin) ** 2 - self.radius ** 2
        delta = b ** 2 - 4 * c

        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)

        return None
