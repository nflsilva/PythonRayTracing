from utils import normalize


class Ray:

    def __init__(self, origin, destination):
        self.reflections = 0
        self.reflection_value = 1
        self.origin = origin
        self.direction = normalize(destination - origin)
