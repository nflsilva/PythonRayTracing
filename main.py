import numpy as np
from timeit import default_timer
from random import randint

from scomponent.Color import Color
from scomponent.Camera import Camera
from scomponent.Screen import Screen
from scomponent.Ray import Ray
from scomponent.Light import Light

from sobject.Sphere import Sphere


def find_nearest_object_to_ray(scene_objects, ray):

    nearest_object_distance = np.inf
    nearest_object = None

    for obj in scene_objects:
        object_distance = obj.intersects_with_ray(ray)

        if object_distance is None:
            continue

        if object_distance < nearest_object_distance:
            nearest_object_distance = object_distance
            nearest_object = obj

    return nearest_object_distance, nearest_object



def main():

    width = 300
    height = 300
    aspect_ratio = float(width / height)

    camera = Camera(x=0, y=0, z=-1)
    screen = Screen(bottom=-1, top=1, left=1 / aspect_ratio, right=-1 / aspect_ratio, width=width, height=height)

    light = Light(x=0, y=5, z=2, color=Color(r=1.0, g=1.0, b=1.0))

    scene_objects = [
        Sphere(origin=np.array([0, 0, 2]), radius=1.0, color=Color(r=0.25, g=0.25, b=1.0)),
        #phere(origin=np.array([1, 0, 3]), radius=1.0, color=Color(r=0.25, g=1.0, b=0.25)),
        #Sphere(origin=np.array([-1, 0, 1]), radius=1.0, color=Color(r=1.0, g=0.25, b=0.25)),
    ]



    print("Working...")
    starting_time = default_timer()
    for i, y in enumerate(np.linspace(screen.bottom, screen.top, screen.height)):

        for j, x in enumerate(np.linspace(screen.left, screen.right, screen.width)):

            pixel = np.array([x, y, 0])
            ray = Ray(origin=camera.position, destination=pixel)

            nearest_obj_distance, nearest_obj = find_nearest_object_to_ray(scene_objects, ray)

            if nearest_obj is None:
                continue

            intersection_point = ray.origin + nearest_obj_distance * ray.direction
            intersection_normal = nearest_obj.get_intersection_normal(ray, intersection_point)
            shifted_nearest_obj_intersection_point = intersection_point + 1e-10 * intersection_normal

            light_ray = Ray(origin=shifted_nearest_obj_intersection_point, destination=light.position)
            light_ray_intersection_distance, _ = find_nearest_object_to_ray(scene_objects, light_ray)
            intersection_to_light_distance = np.linalg.norm(light.position - intersection_point)
            is_shadowed = light_ray_intersection_distance < intersection_to_light_distance

            if is_shadowed:
                continue

            screen.set_pixel_color(x=i, y=j, color=nearest_obj.color)

            #print(intersection_point)

    end_time = default_timer()
    screen.write_to_file()

    print(f"Done! - Elapsed time: {end_time - starting_time} s")


main()
