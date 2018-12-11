import re

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
                'coords': (numbers[0], numbers[1]),
                'velocity': (numbers[2], numbers[3])
            }
        )

def print_points(points, img_num):
    image_name = f"images/img{img_num}.jpg"
    image_size = max([point['coords'][1] for point in points]), max([point['coords'][0] for point in points])
    im = Image.new(mode='1', size=image_size)

    for point in points:
        x, y = point['coords'][1], point['coords'][0]
        im.putpixel((x, y), 1)
    im.save(image_name)


def part1(points):
    num = 0
    while True:
        print_points(points, num)
        input()
        num += 1
        for point in points:
            point['coords'][0] += point['velocity'][0]
            point['coords'][1] += point['velocity'][1]
        




print(part1(points))
