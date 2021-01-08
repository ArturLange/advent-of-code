import re
import numpy as np
from PIL import Image

pattern = re.compile(r'position=<.*?(-?\d*),.*?(-?\d*)> velocity=<.*?(-?\d*),.*?(-?\d*)>')

with open('day10_input') as input_file:
    lines =  input_file.readlines()[:-1]
    points = []
    for line in lines:
        numbers = [
            int(x) for x in
            pattern.search(line).groups()
        ]
        points.append(
            {
                'coords': [numbers[0], numbers[1]],
                'velocity': (numbers[2], numbers[3])
            }
        )


def points_size(points):
    return (
        abs(max([point['coords'][0] for point in points]) - min([point['coords'][0] for point in points])) *
        abs(max([point['coords'][1] for point in points]) - min([point['coords'][1] for point in points]))
    )

def print_points(points, img_num):
    # breakpoint()
    offset = -min((
        min([point['coords'][0] for point in points]), 
        min([point['coords'][1] for point in points])
    ))
    image_name = f"images/img{img_num}.png"
    image_size = (
        max([point['coords'][0] for point in points]) + offset + 1, 
        max([point['coords'][1] for point in points]) + offset + 1
    )
    im = Image.new(mode='1', size=image_size)


    arr = np.full(image_size, False)
    for point in points:
        x, y = point['coords'][0], point['coords'][1]
        # arr[x+offset][y+offset] = True
        im.putpixel((x + offset, y + offset), 1)
    # im = Image.fromarray(arr, mode='1')
    im.save(image_name, quality=100)


def part1(points):
    num = 0
    old_size = points_size(points)
    while True:
        new_size = points_size(points)
        if points_size(points) > old_size:
            num -= 5
            for point in points:
                point['coords'][0] -= 5* point['velocity'][0]
                point['coords'][1] -= 5*point['velocity'][1]
            for _ in range(10):
                print_points(points, num)
                num += 1
                for point in points:
                    point['coords'][0] += point['velocity'][0]
                    point['coords'][1] += point['velocity'][1]
            break
        print(f"Image no. {num} done - size = {old_size}")
        num += 1
        for point in points:
            point['coords'][0] += point['velocity'][0]
            point['coords'][1] += point['velocity'][1]
        old_size = new_size
        



import cProfile as profile
# profile.run("part1(points)")
print(part1(points))
