import numpy as np
from utils import normalize

from sobject.SceneObject import SceneObject


class Sphere(SceneObject):

    def __init__(self, origin, radius, material):
        self.origin = origin
        self.radius = radius
        self.material = material

    def intersects_with_ray(self, ray):

        b = 2 * np.dot(ray.direction, ray.origin - self.origin)
        c = np.linalg.norm(ray.origin - self.origin) ** 2 - self.radius ** 2
        delta = b ** 2 - 4 * c

        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                object_distance = min(t1, t2)
                return object_distance

        return None

    def get_intersection_normal(self, ray, intersection_point):
        intersection_normal = normalize(intersection_point - self.origin)
        return intersection_normal
