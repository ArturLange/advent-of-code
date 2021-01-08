import re

string = 'set a 4'

rx = re.compile(r'set (?P<sound>[a-z]) (?P<value>-?[a-z0-9]+)')

# for _ in range(10000000):
#     if rx.fullmatch(string):
#         match = rx.fullmatch(string)
#         sound = match.group('sound')
#         value = match.group('value')

for _ in range(10000000):
    if string.startswith('set'):
        list_ = string.split(' ')
        sound = list_[1]
        value = list_[2]
