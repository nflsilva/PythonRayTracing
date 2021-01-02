from utils import normalize


class Ray:

    def __init__(self, origin, destination):
        self.origin = origin
        self.direction = normalize(destination - origin)
