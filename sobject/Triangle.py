import numpy as np
from utils import normalize

from sobject.SceneObject import SceneObject


class Triangle(SceneObject):

    def __init__(self, point0, point1, point2, material):
        self.point0 = point0
        self.point1 = point1
        self.point2 = point2
        self.material = material

        edge02 = point2 - point0
        self.edge01 = point1 - point0
        self.edge12 = point2 - point1
        self.edge20 = point0 - point2



        self.normal = normalize(np.cross(edge02, self.edge01))
        #self.normal = normalize(np.cross(self.edge01, edge02))

        #print(self.normal)
        self.origin = -np.dot(self.normal, self.point0)

    def intersects_with_ray(self, ray):

        numerator = np.dot(self.normal, ray.origin) + self.origin
        denominator = np.dot(self.normal, ray.direction)

        object_distance = -(numerator / denominator)


        if object_distance > 0:


            intersection_point = ray.direction * object_distance + ray.origin

            vp0 = intersection_point - self.point0
            c = np.cross(self.edge01, vp0)
            if np.dot(c, self.normal) > 0:
                return None

            vp1 = intersection_point - self.point1
            c = np.cross(self.edge12, vp1)
            if np.dot(c, self.normal) > 0:
                return None

            vp2 = intersection_point - self.point2
            c = np.cross(self.edge20, vp2)
            if np.dot(c, self.normal) > 0:
                return None

            return object_distance

        return None

    def get_intersection_normal(self, ray, intersection_point):
        return self.normal

