import numpy as np
from timeit import default_timer
from random import randint

from scomponent.Color import Color
from scomponent.Camera import Camera
from scomponent.Screen import Screen
from scomponent.Ray import Ray

from sobject.Sphere import Sphere

def main():

    width = 300
    height = 300
    aspect_ratio = float(width / height)

    camera = Camera(x=0, y=0, z=-1)
    screen = Screen(bottom=-1, top=1, left=1 / aspect_ratio, right=-1 / aspect_ratio, width=width, height=height)


    objects = [
        Sphere(origin=np.array([0, 0, 2]), radius=1.0, color=Color(r=0.25, g=0.25, b=1.0)),
        Sphere(origin=np.array([1, 0, 3]), radius=1.0, color=Color(r=0.25, g=1.0, b=0.25)),
        Sphere(origin=np.array([-1, 0, 1]), radius=1.0, color=Color(r=1.0, g=0.25, b=0.25)),
    ]



    print("Working...")
    starting_time = default_timer()
    for i, y in enumerate(np.linspace(screen.bottom, screen.top, screen.height)):

        for j, x in enumerate(np.linspace(screen.left, screen.right, screen.width)):

            pixel = np.array([x, y, 0])
            ray = Ray(origin=camera.position, destination=pixel)

            nearest_object_distance = np.inf
            nearest_object = None

            for obj in objects:
                object_distance = obj.intersects_with_ray(ray)

                if object_distance is None:
                    continue

                if object_distance < nearest_object_distance:
                    nearest_object_distance = object_distance
                    nearest_object = obj

                screen.set_pixel_color(x=i, y=j, color=nearest_object.color)

                intersection_point = ray.origin + ray.direction * nearest_object_distance
                #print(intersection_point)

    end_time = default_timer()
    screen.write_to_file()

    print(f"Done! - Elapsed time: {end_time - starting_time} s")


main()
