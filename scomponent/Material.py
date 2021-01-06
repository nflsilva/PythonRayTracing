

class Material:

    def __init__(self, ambient, diffuse, specular, shininess=None, reflection=0.0):

        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.reflection = reflection

