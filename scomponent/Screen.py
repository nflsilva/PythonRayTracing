import numpy as np
import matplotlib.pyplot as plt

class Screen:

    def __init__(self, left, right, top, bottom, width, height):

        self.width = width
        self.height = height

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

        self.image = np.zeros((height, width, 3))

    def set_pixel_color(self, x, y, color):
        self.image[x, y] = (color.r, color.g, color.b)


    def write_to_file(self):
        plt.imsave("output.png", self.image)
