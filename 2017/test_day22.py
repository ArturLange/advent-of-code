import unittest
from pprint import pprint

from day22 import Grid, enlarge_map, GridImproved


class TestDay22(unittest.TestCase):
    def test_bursts(self):
        map_ = [
            ['.', '.', '#'],
            ['#', '.', '.'],
            ['.', '.', '.']
        ]
        map_ = enlarge_map(map_, 6)
        grid = Grid(map_)
        print(grid.virus_position)
        for _ in range(70):
            grid.burst()
        pprint([''.join(row) for row in grid.map])
        print(grid.infected_count)

    def test_bursts_v2(self):
        map_ = [
            ['.', '.', '#'],
            ['#', '.', '.'],
            ['.', '.', '.']
        ]
        map_ = enlarge_map(map_, 6)
        grid = GridImproved(map_)
        for _ in range(100):
            grid.burst()
        print(grid.infected_count)


if __name__ == '__main__':
    unittest.main()
