from itertools import islice

with open('inputs/day2.txt') as input_file:
    lines = tuple(line.strip() for line in input_file.readlines())

SCORES_CHOICES = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissors
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissors
}

SCORES_RESULTS = {
    'WIN': 6,
    'DRAW': 3, 
    'LOSE': 0
}

WHO_BEATS_WHO = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

RESULT_CHOICES = {
    'Z': 'WIN',
    'Y': 'DRAW', 
    'X': 'LOSE'
}

## Part 1

score_sum = 0
for line in lines:
    enemy_choice, my_choice = line.split(' ')
    if WHO_BEATS_WHO[enemy_choice] == my_choice:
        result = 'LOSE'
    elif WHO_BEATS_WHO[my_choice] == enemy_choice:
        result = 'WIN'
    else:
        result = 'DRAW'
    score = SCORES_RESULTS[result] + SCORES_CHOICES[my_choice]
    score_sum += score

print(score_sum)

## Part 2

score_sum = 0
for line in lines:
    enemy_choice, my_choice = line.split(' ')
    if RESULT_CHOICES[my_choice] == 'WIN':
        score = (SCORES_CHOICES[enemy_choice] - 1 + 1) % 3 + 1
    elif RESULT_CHOICES[my_choice] == 'DRAW':
        score = (SCORES_CHOICES[enemy_choice] - 1) % 3 + 1
    elif RESULT_CHOICES[my_choice] == 'LOSE':
        score = (SCORES_CHOICES[enemy_choice] - 1 - 1) % 3 + 1

    score += SCORES_RESULTS[RESULT_CHOICES[my_choice]]
    score_sum += score
    
print(score_sum)