from collections import Counter
from typing import List, Tuple, Union


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
        self.positions: Union[List[Tuple[int, int, int]], None] = []
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
            self.positions[i] = add_coords(
                self.positions[i],
                self.velocities[i]
            ) if self.positions[i] is not None else None

    def calculate_distances(self):
        for i in range(len(self.positions)):
            if self.positions[i] is not None:
                self.distances.append(get_distance_from_zero(self.positions[i]))
        min_distance = min(self.distances)
        for i in range(len(self.positions)):
            if self.distances[i] == min_distance:
                return i

    def check_collisions(self):
        counter = Counter(self.positions)
        positions_to_delete = []
        for position in counter:
            if counter[position] > 1:
                positions_to_delete.append(position)
        for i in range(len(self.positions)):
            if self.positions[i] in positions_to_delete:
                self.positions[i] = None


if __name__ == '__main__':
    with open('inputs/day20', 'r') as input_file:
        particles_data = [x.replace('\n', '') for x in input_file.readlines()]
        par_state = ParticleState(particles_data)
        par_state.initialize_positions()
        for _ in range(1000):
            par_state.tick()
        print(par_state.calculate_distances())

        par_state = ParticleState(particles_data)
        par_state.initialize_positions()
        for _ in range(1000):
            par_state.tick()
            par_state.check_collisions()
        print(len([position for position in par_state.positions if position is not None]))
