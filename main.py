import numpy as np
from timeit import default_timer
from utils import normalize
from random import randint

from scomponent.Color import Color
from scomponent.Camera import Camera
from scomponent.Screen import Screen
from scomponent.Ray import Ray
from scomponent.Light import Light
from scomponent.Material import Material

from sobject.Sphere import Sphere
from sobject.Triangle import Triangle


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

    image_size_divider = 1
    image_width = int(1920 / image_size_divider)
    image_height = int(1080 / image_size_divider)
    aspect_ratio = float(image_width) / image_height

    camera = Camera(x=0, y=0, z=-1.5)
    screen = Screen(bottom=-1 / aspect_ratio, top=1 / aspect_ratio, left=-1, right=1, width=image_width, height=image_height)

    scene_lights = [

        Light(x=-1.5, y=0.5, z=0,
              material=Material(ambient=Color(.1, .1, .1),
                                diffuse=Color(.7, .7, .7),
                                specular=Color(1.0, 1.0, 1.0))),

        Light(x=0, y=0.75, z=0,
              material=Material(ambient=Color(.1, .1, .1),
                                diffuse=Color(.2, .2, .2),
                                specular=Color(0.5, 0.5, 0.5)))

    ]

    floor_material = Material(ambient=Color(.1, .1, .1),
                              diffuse=Color(.7, .7, .7),
                              specular=Color(1.0, 1.0, 1.0),
                              shininess=100)

    scene_objects = [

        Triangle(point0=np.array([-1.0, -0.5, 0]),
                 point1=np.array([1.0, -0.5, 0]),
                 point2=np.array([-5.0, -0.5, 7.5]),
                 material=floor_material),

        Triangle(point0=np.array([-5.0, 5.0, 7.5]),
                 point1=np.array([-5.0, -0.5, 7.5]),
                 point2=np.array([1.0, -0.5, 0]),
                 material=floor_material),

        Sphere(origin=np.array([-0.5, 0, 0.5]),
               radius=0.25,
               material=Material(ambient=Color(.2, .0, .0),
                                 diffuse=Color(.7, .0, .0),
                                 specular=Color(1, 1, 1),
                                 shininess=1000)),

        Sphere(origin=np.array([-1.0, -0.5 + 0.075, 1.0]),
               radius=0.075,
               material=Material(ambient=Color(.0, .1, .0),
                                 diffuse=Color(.0, .7, .0),
                                 specular=Color(1, 1, 1),
                                 shininess=75)),

    ]

    scene_objects = scene_objects[0:4]
    scene_lights = scene_lights[0:1]

    print("Working...")
    starting_time = default_timer()

    for i, y in enumerate(np.linspace(screen.top, screen.bottom, screen.height)):

        for j, x in enumerate(np.linspace(screen.left, screen.right, screen.width)):

            pixel = np.array([x, y, 0])
            ray = Ray(origin=camera.position, destination=pixel)

            nearest_obj_distance, nearest_obj = find_nearest_object_to_ray(scene_objects, ray)

            if nearest_obj is None:
                continue

            intersection_point = ray.origin + nearest_obj_distance * ray.direction
            intersection_normal = nearest_obj.get_intersection_normal(ray, intersection_point)
            shifted_nearest_obj_intersection_point = intersection_point + 1e-10 * intersection_normal

            # RGB
            illumination = np.zeros((3))
            for light in scene_lights:

                light_ray = Ray(origin=shifted_nearest_obj_intersection_point, destination=light.position)
                light_ray_intersection_distance, _ = find_nearest_object_to_ray(scene_objects, light_ray)
                intersection_to_light_distance = np.linalg.norm(light.position - intersection_point)
                is_shadowed = light_ray_intersection_distance < intersection_to_light_distance

                #print(str(light_ray_intersection_distance) + " - " + str(intersection_to_light_distance))

                if is_shadowed:
                    continue

                # ambient
                illumination += nearest_obj.material.ambient * light.material.ambient

                # diffuse
                illumination += nearest_obj.material.diffuse * light.material.diffuse * np.dot(light_ray.direction, intersection_normal)

                # specular
                intersection_to_camera = normalize(camera.position - intersection_point)
                H = normalize(light_ray.direction + intersection_to_camera)
                illumination += nearest_obj.material.specular * light.material.specular * np.dot(intersection_normal, H) ** (nearest_obj.material.shininess / 4)

            illumination = np.clip(illumination, 0, 1)

            screen.set_pixel_color(x=j, y=i, color=Color(illumination[0], illumination[1], illumination[2]))



            #print(intersection_point)

    end_time = default_timer()
    screen.write_to_file()

    print(f"Done! - Elapsed time: {end_time - starting_time} s")


main()
