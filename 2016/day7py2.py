inp = open('day7input').read().split('\n')

def hasabba(ph):
    if len(ph) < 4:
        return False
    for i in range(len(ph) - 4):
        if ph[i:i+4] == ph[i:i+4][::-1]:
            return True
    return False

count = 0
for item in inp:
    b = []
    o = []
    while '[' in item:
        o.append(item[:item.find('[')])
        item = item[item.find('[') + 1:]
        b.append(item[:item.find(']')])
        item = item[item.find(']') + 1:]
    if len(item) != 0:
        o.append(item)
    good = False
    for aa in o:
        if hasabba(aa):
            good = True
    for aa in b:
        if hasabba(aa):
            good = False
    if good:
        count += 1
print(count)
