with open('day7_input') as input_file:
    lines = [(line.split()[1], line.split()[7]) for line in input_file.readlines()]

test_lines = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]
test_lines = [(line.split()[1], line.split()[7]) for line in test_lines]


class Worker:
    def __init__(self, number):
        self.number = number
        self.letter = ''
        self.time_left = 0

    @property
    def ready(self) -> bool:
        return len(self.letter) == 0

    def add(self, letter):
        self.letter = letter
        self.time_left = ord(letter) - 4
    
    def work(self):
        self.time_left -= 1
        if self.time_left == 0:
            letter = self.letter
            self.letter = ''
            return letter

    def __str__(self):
        if not self.ready:
            return f'Worker {self.number} working on letter {self.letter}, {self.time_left} seconds left' 
        return f'Worker {self.number} idle'

def part1(lines):
    instructions = list(lines)
    done = []
    all_letters = set()
    for x in instructions:
        all_letters.add(x[0])
        all_letters.add(x[1])
    print(all_letters)

    ready = list(sorted(filter(
            lambda x: x not in [y[1] for y in instructions] and x not in done, 
            all_letters)))
    while ready:
        done.append(ready[0])
        for index in reversed(range(len(instructions))):
            if instructions[index][0] in done:
                instructions.pop(index)
        ready = list(sorted(filter(
            lambda x: x not in [y[1] for y in instructions] and x not in done, 
            all_letters)))
    return(''.join(done))


def part2(lines):
    timer = 0
    instructions = list(lines)
    done = []
    all_letters = set()
    for x in instructions:
        all_letters.add(x[0])
        all_letters.add(x[1])
    print(all_letters)

    ready = list(sorted(filter(
            lambda x: x not in [y[1] for y in instructions] and x not in done, 
            all_letters)))

    workers = [
        Worker(i) for i in range(5)
    ]

    while len(all_letters) != len(done):
        for worker in workers:
            if ready and worker.ready:
                worker.add(ready.pop(0))
        print([str(worker) for worker in workers])
        done.extend(list(filter(
            lambda x: x is not None,
            [worker.work() for worker in workers]
        )))
        for index in reversed(range(len(instructions))):
            if instructions[index][0] in done:
                instructions.pop(index)
        worker_letters = [worker.letter for worker in workers]
        ready = list(sorted(filter(
            lambda x: x not in [y[1] for y in instructions] and x not in done and x not in worker_letters, 
            all_letters)))
        timer += 1
        print(ready)
    
    return done, timer

print(part2(lines))
# print(part2(test_lines))
