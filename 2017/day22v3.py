import sys
from collections import defaultdict

part_b = 'b' in sys.argv
data = open('inputs/day22', 'r').read().strip().split('\n')

grid = defaultdict(int)

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3
MODULUS = 4
ADD_AMOUNT = 2 - part_b

pos = (0, 0)
direction = (-1, 0)
lefts = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
rights = {lefts[k]: k for k in lefts}

grid_height = len(data)
grid_width = len(data[0])
for row in xrange(grid_height):
    for col in xrange(grid_width):
        grid[(row-grid_height/2, col-grid_width/2)
             ] = int(data[row][col] == '#') * 2

c = 0
BURSTS = 10000000 if part_b else 10000
for burst in xrange(BURSTS):
    if grid[pos] == CLEAN:
        direction = lefts[direction]
        if not part_b:
            c += 1
    elif grid[pos] == WEAKENED:
        c += 1
    elif grid[pos] == INFECTED:
        direction = rights[direction]
    else:
        direction = rights[rights[direction]]
    grid[pos] = (grid[pos] + ADD_AMOUNT) % MODULUS
    pos = (pos[0] + direction[0], pos[1] + direction[1])
print c
