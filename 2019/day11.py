from arturlib.vectors import GridCrawler, SparseGrid, Vector
from arturlib.intcode import IntcodeExecution

with open('inputs/day11') as input_file:
    task_input = [int(x) for x in input_file.readline().split(',')]


def part1(input_):
    execution = IntcodeExecution(input_, [])
    grid = SparseGrid(0, [1])
    grid_walker = GridCrawler(Vector((0, 0)))
    painted = set()

    while not execution.done:
        input_value = grid[tuple(grid_walker.location)]
        if not execution.inputs:
            execution.inputs.append(input_value)
        while len(execution.outputs) < 2:
            if execution.done:
                return len(painted)
            execution.process()
        grid[tuple(grid_walker.location)] = execution.outputs.popleft()
        painted.add(tuple(grid_walker.location))
        turn_dir = execution.outputs.popleft()
        if turn_dir == 0:
            grid_walker.turn_left()
        else:
            grid_walker.turn_right()
        grid_walker.go_ahead()
    return len(painted)


def get_grid(input_):
    execution = IntcodeExecution(input_, [])
    grid = SparseGrid(0, [1])
    grid[(0, 0)] = 1
    grid_walker = GridCrawler(Vector((0, 0)))

    while not execution.done:
        input_value = grid[tuple(grid_walker.location)]
        if not execution.inputs:
            execution.inputs.append(input_value)
        while len(execution.outputs) < 2:
            if execution.done:
                return grid
            execution.process()
        grid[tuple(grid_walker.location)] = execution.outputs.popleft()
        turn_dir = execution.outputs.popleft()
        if turn_dir == 0:
            grid_walker.turn_left()
        else:
            grid_walker.turn_right()
        grid_walker.go_ahead()
    return grid


def part2(input_):
    grid = get_grid(input_)
    for j in reversed(range(-6, 3)):
        for i in range(-6, 43):
            value = '#' if grid[(i, j)] else '.'
            print(value, end='')
        print()


if __name__ == '__main__':
    # test()
    # import cProfile as profile
    # profile.run('print(part1(task_input))')
    print(part2(task_input))
