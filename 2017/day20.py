from typing import List, Tuple


def add_coords(coords1, coords2):
    return (
        coords1[0] + coords2[0],
        coords1[1] + coords2[1],
        coords1[2] + coords2[2],
    )


def get_distance_from_zero(coords):
    return abs(coords[0]) + abs(coords[1]) + abs(coords[2])


class ParticleState:
    def __init__(self, particles_data: List[str]):
        self.particles_data = particles_data
        self.positions: List[Tuple[int, int, int]] = []
        self.velocities: List[Tuple[int, int, int]] = []
        self.accelerations: List[Tuple[int, int, int]] = []
        self.distances: List[int] = []

    def initialize_positions(self):
        for particle in self.particles_data:
            parameters = particle.split(', ')
            self.positions.append(tuple((int(pos) for pos in parameters[0][3:-1].split(','))))
            self.velocities.append(tuple((int(pos) for pos in parameters[1][3:-1].split(','))))
            self.accelerations.append(tuple((int(pos) for pos in parameters[2][3:-1].split(','))))

    def tick(self):
        for i in range(len(self.positions)):
            self.velocities[i] = add_coords(self.velocities[i], self.accelerations[i])
            self.positions[i] = add_coords(self.positions[i], self.velocities[i])

    def calculate_distances(self):
        for i in range(len(self.positions)):
            self.distances.append(get_distance_from_zero(self.positions[i]))
        min_distance = min(self.distances)
        for i in range(len(self.positions)):
            if self.distances[i] == min_distance:
                return i


if __name__ == '__main__':
    with open('inputs/day20', 'r') as input_file:
        par_state = ParticleState([x.replace('\n', '') for x in input_file.readlines()])
        par_state.initialize_positions()
        print(par_state.positions)
        print(par_state.velocities)
        print(par_state.accelerations)
        for _ in range(1000):
            par_state.tick()
        print(par_state.calculate_distances())

