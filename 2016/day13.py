from typing import Iterable
import functools
import collections
import random


FAVORITE_NUMBER = 1362

Coords = tuple[int, int]

START_COORDS = (1, 1)
END_COORDS = (31, 39)


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, position: Coords = None, parent=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"Node <{self.position[0]}, {self.position[1]}> (f:{self.f}, g:{self.g}, h:{self.h})"


@functools.lru_cache
def is_wall(coords: Coords, favorite_number: int) -> bool:
    x, y = coords
    number = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    counter = collections.Counter(bin(number)[2:])
    return counter["1"] % 2 == 1


def is_path(coords: Coords, favorite_number: int) -> bool:
    return not is_wall(coords, favorite_number)


@functools.lru_cache
def is_coords_valid(coords: Coords, favorite_number: int) -> bool:
    return not any((
        coords[0] < 0 or coords[1] < 0, 
        is_wall(coords, favorite_number)
        ))


def find_path_a_star(start: Coords, end: Coords, favorite_number: int):
    open_list: list[Node] = []
    closed_list: list[Node] = []

    start_node = Node(start)
    end_node = Node(end)

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate children
        children: list[Node] = []
        for new_position in ((0, -1), (0, 1), (-1, 0), (1, 0)):  # Adjacent squares
            # Get node position
            node_position: Coords = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1],
            )

            # Make sure walkable terrain
            if not is_coords_valid(node_position, favorite_number):
                continue

            # Create new node
            new_node = Node(position=node_position, parent=current_node)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(
                child.position[1] - end_node.position[1]
            )
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def find_close_locations(start_coords, favorite_number, limit):
    distances = {
        start_coords: 0
    }
    

def part1(start_coords, end_coords, favorite_number) -> int:
    shortest_path = find_path_a_star(start_coords, end_coords, favorite_number)
    print(shortest_path)
    return len(shortest_path) - 1

def part2(start_coords, favorite_number) -> int:
    # checked = 0
    # potential_locations: set[Coords] = {(1,1)}
    # checked_locations: set[Coords] = {(1,1)}
    # for x in range(52):
    #     for y in range(52):
    #         if is_coords_valid((x, y), favorite_number) and (x - start_coords[0] + y - start_coords[1]) <= 50:
    #             potential_locations.add((x, y))
    # for location in potential_locations:
    #     checked += 1
    #     if location not in checked_locations:
    #         shortest_path = find_path_a_star(start_coords, location, favorite_number)
    #         if shortest_path is not None and len(shortest_path) - 1 <= 50:
    #             checked_locations |= set(shortest_path)
    # return checked_locations
    pass


TEST_CASES_1 = [((7, 4), 11)]


def test_1():
    for coords, steps in TEST_CASES_1:
        assert (
            part1(start_coords=(1, 1), end_coords=coords, favorite_number=10) == steps
        )


if __name__ == "__main__":
    test_1()
    # test_2()
    print(part1(START_COORDS, END_COORDS, FAVORITE_NUMBER))
    # test_coords = (11, 11)
    # while is_wall(test_coords, FAVORITE_NUMBER):
    #     test_coords = random.randint(10, 15), random.randint(10, 15)
    # print(test_coords)
    # len(find_path_a_star(START_COORDS, test_coords, FAVORITE_NUMBER))
    print(part2(START_COORDS, FAVORITE_NUMBER))
