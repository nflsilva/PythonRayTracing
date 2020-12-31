import numpy as np
from timeit import default_timer
from random import randint

from Camera import Camera
from Screen import Screen
from Ray import Ray

def main():

    width = int(1920 / 2)
    height = int(1080 / 2)
    aspect_ratio = float(width / height)

    screen = Screen(bottom=-1, top=1, left=1 / aspect_ratio, right=-1 / aspect_ratio, width=width, height=height)

    starting_time = default_timer()

    for i, y in enumerate(np.linspace(screen.bottom, screen.top, screen.height)):
        for j, x in enumerate(np.linspace(screen.left, screen.right, screen.width)):


            # white noise
            color = randint(0, 1)
            screen.set_pixel_rgb(x=i, y=j, r=color, g=color, b=color)

    end_time = default_timer()
    screen.write_to_file()

    print(f"Done! - Elapsed time: {end_time - starting_time} s")


main()
