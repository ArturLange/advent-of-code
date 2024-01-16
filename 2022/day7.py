import string
import itertools
import re
from collections import deque
from copy import deepcopy
from pathlib import PurePosixPath as Path
from typing import Iterable
import operator

with open('inputs/day7.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())


CD_RE = re.compile(r'^\$ (cd)(\s[a-z.\/]+)$')
LS_RE = re.compile(r'^\$\sls')
DIR_RE = re.compile(r'^dir (\w*)$')
FILE_RE = re.compile(r'^(\d+) ([a-z.]+)')

TOTAL_DISK_SPACE = 70_000_000
DISK_SPACE_NEEDED = 30_000_000

def count_dir_size(directory: int|dict) -> int:
    if isinstance(directory, int):
        return directory
    elif isinstance(directory, dict):
        return sum(count_dir_size(val) for val in directory.values())
    
def count_directories(commands: Iterable[str]) -> dict[Path, int]:
    directories: dict = {
        '/': {}
    }
    pwd = Path('/')
    def get_directory(dirs: Path) -> dict:
        current_dir = directories
        for val in dirs.parts:
            if not current_dir.get(val):
                current_dir[val] = {}
            current_dir = current_dir[val]
        return current_dir
    
    current_dir = get_directory(pwd)
    for command in commands:
        if command.startswith('$'):
            if match := CD_RE.match(command):
                argument : str = match.groups()[1].strip()
                if argument == '/':
                    pwd = Path('/')
                    current_dir = get_directory(pwd)
                elif argument == '..':
                    pwd = pwd.parent
                    current_dir = get_directory(pwd)
                else:
                    pwd /= argument
                    current_dir = get_directory(pwd)
            elif match := LS_RE.match(command):
                pass
        else:
            if match := DIR_RE.match(command):
                dir_name = match.groups()[0]
                if not current_dir.get(dir_name):
                    current_dir[dir_name] = {}
            elif match := FILE_RE.match(command):
                size = int(match.groups()[0])
                filename = match.groups()[1]
                if not current_dir.get(filename):
                    current_dir[filename] = size
    sizes = {}
    def calculate_sizes(sizes: dict[str, int], directory, directory_path):
        if isinstance(directory, dict):
            sizes[directory_path] = count_dir_size(directory)
            for name, dir_ in directory.items():
                calculate_sizes(sizes, dir_, directory_path / name)
    calculate_sizes(sizes, directories['/'], Path('/'))
    return sizes

def solve1(commands: Iterable[str]) -> int:
    sizes = count_directories(commands)
    return sum(b for b in sizes.values() if b <= 100000)
    
def solve2(commands: Iterable[str]) -> int:
    sizes = count_directories(commands)
    root_size = sizes[Path('/')]
    need_to_free_size = DISK_SPACE_NEEDED - (TOTAL_DISK_SPACE - root_size)
    deletion_candidates = ((path_, size) for path_, size in sizes.items() if size >= need_to_free_size)
    deletion_candidates = sorted(deletion_candidates, key=operator.itemgetter(1))
    return deletion_candidates[0][1]

## Test 1
test_cases_1 = (
    ([
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k',
], 95437),
)

for value, expected_result in test_cases_1:
    assert solve1(value) == expected_result

## Part 1

print(solve1(lines))

## Test 2

test_cases_2 = (
    ([
    '$ cd /',
    '$ ls',
    'dir a',
    '14848514 b.txt',
    '8504156 c.dat',
    'dir d',
    '$ cd a',
    '$ ls',
    'dir e',
    '29116 f',
    '2557 g',
    '62596 h.lst',
    '$ cd e',
    '$ ls',
    '584 i',
    '$ cd ..',
    '$ cd ..',
    '$ cd d',
    '$ ls',
    '4060174 j',
    '8033020 d.log',
    '5626152 d.ext',
    '7214296 k',
], 24933642),
)

for value, expected_result in test_cases_2:
    assert solve2(value) == expected_result

## Part 2

print(solve2(lines))