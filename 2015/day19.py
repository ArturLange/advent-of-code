import re
from typing import List


class Molecule:
    def __init__(self, str_: str):
        self.list_ = re.findall(r'[A-Z][a-z]?', str_)

    def __len__(self):
        return len(self.list_)

    def __getitem__(self, key):
        return self.list_[key]

    def __eq__(self, value):
        return self.list_ == value.list_

    def __hash__(self):
        return hash(''.join(self.list_))

    def copy(self):
        return Molecule(''.join(self.list_))

    def replace(self, index: str, replacement):
        del self.list_[index]
        for i in replacement.list_[::-1]:
            self.list_.insert(index, i)

    def __repr__(self):
        return '-'.join(self.list_)


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
    print(all_reactions)
    all_options = set()
    for i in range(len(starting_molecule)):
        if starting_molecule[i] in all_reactions:
            for replacement in all_reactions[starting_molecule[i]]:
                mol = starting_molecule.copy()
                mol.replace(i, replacement)
                all_options.add(mol)
    return len(all_options)


if __name__ == "__main__":
    print(part1())
    # mol = get_molecule('HOH')
    # print(mol)
    # replace_in_molecule(mol, 0, get_molecule('HO'))
    # print(mol)
