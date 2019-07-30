import re
from itertools import product
from pprint import pprint
from typing import List

MOL_RX = re.compile(r'[A-Z][a-z]?')


class Molecule:
    __slots__ = ['list_', 'str']

    def __init__(self, str_: str, list_=None):
        if list_ is None:
            self.list_ = MOL_RX.findall(str_)
        else:
            self.list_ = list_
        self.str = str_

    def __len__(self):
        return len(self.list_)

    def __getitem__(self, key):
        return self.list_[key]

    def __eq__(self, value):
        return self.list_ == value.list_

    def __hash__(self):
        return hash(self.str)

    def copy(self):
        return Molecule(self.str, self.list_)

    def count(self, x):
        return self.list_.count(x)

    def replace(self, index, replacement):
        del self.list_[index]
        for i in replacement.list_[::-1]:
            self.list_.insert(index, i)
        self.str = ''.join(self.list_)

    def is_reaction_valid(self, index, replacement):
        if index >= len(self.list_) or replacement[0] != self.list_[index]:
            return False
        else:
            return True

    def __repr__(self):
        return self.str


def part1():
    all_reactions = dict()
    with open('day19input') as input_file:
        lines = input_file.read().splitlines()
    reactions = lines[:-2]
    starting_molecule = Molecule(lines[-1])
    for reaction in reactions:
        reagents = reaction.split(' => ')
        if reagents[0] not in all_reactions:
            all_reactions[reagents[0]] = [Molecule(reagents[1])]
        else:
            all_reactions[reagents[0]].append(Molecule(reagents[1]))
    all_options = set()
    for i in range(len(starting_molecule)):
        if starting_molecule[i] in all_reactions:
            for replacement in all_reactions[starting_molecule[i]]:
                mol = starting_molecule.copy()
                mol.replace(i, replacement)
                all_options.add(mol)
    return len(all_options)


def part2():
    # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju?utm_source=share&utm_medium=web2x
    all_reactions = []
    with open('day19input') as input_file:
        lines = input_file.read().splitlines()
    reactions = lines[:-2]
    end_molecule = Molecule(lines[-1])

    end_molecule_len = len(end_molecule)
    return end_molecule_len - (end_molecule.count('Rn') + end_molecule.count('Ar')) - 2 * end_molecule.count('Y') - 1


if __name__ == "__main__":
    print(part1())
    print(part2())
