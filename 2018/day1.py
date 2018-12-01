sum_ = 0
with open('day1_input') as input_file:
    for line in input_file.readlines():
        sum_ += int(line)

print(sum_)
