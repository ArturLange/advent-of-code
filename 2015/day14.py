class Reindeer:
    def __init__(self, name: str, speed: int, stamina: int, rest_time: int):
        self.name = name
        self.speed = speed
        self.max_stamina = stamina
        self.rest_time = rest_time
        self.distance = 0
        self.stamina = self.max_stamina
        self.current_rest_time = self.rest_time
        self.points = 0

    def fly(self):
        if self.stamina > 0:
            self.stamina -= 1
            self.distance += self.speed
        elif self.current_rest_time > 0:
            self.current_rest_time -= 1
        else:
            self.current_rest_time = self.rest_time
            self.stamina = self.max_stamina
            self.stamina -= 1
            self.distance += self.speed

    def fly_for(self, seconds):
        for i in range(seconds):
            self.fly()

    def __str__(self):
        return f'{self.name}, speed: {self.speed}, stamina: {self.max_stamina}, rest time: {self.rest_time}, distance: {self.distance}'


def part1():
    reindeers = dict()
    with open('day14input') as input_file:
        for line in input_file.readlines():
            parsed_line = line.split()
            reindeers[parsed_line[0]] = Reindeer(
                parsed_line[0],
                int(parsed_line[3]),
                int(parsed_line[6]),
                int(parsed_line[13])
            )
    for reindeer in reindeers.values():
        reindeer.fly_for(2503)

    return max(x.distance for x in reindeers.values())


def part2():
    reindeers = dict()
    with open('day14input') as input_file:
        for line in input_file.readlines():
            parsed_line = line.split()
            reindeers[parsed_line[0]] = Reindeer(
                parsed_line[0],
                int(parsed_line[3]),
                int(parsed_line[6]),
                int(parsed_line[13])
            )
    for i in range(2503):
        for reindeer in reindeers.values():
            reindeer.fly()
        distance = max(x.distance for x in reindeers.values())
        for reindeer in reindeers.values():
            if reindeer.distance == distance:
                reindeer.points += 1

    return max(x.points for x in reindeers.values())


if __name__ == "__main__":
    print(part2())
