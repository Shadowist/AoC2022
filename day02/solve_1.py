# Globals
SCORING = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

RESULTS = {
    'A X': 0,
    'A Y': 1,
    'A Z': -1,

    'B X': -1,
    'B Y': 0,
    'B Z': 1,

    'C X': 1,
    'C Y': -1,
    'C Z': 0
}

# Data ingesting
data = []
# file = "day02/test.txt"
file = "day02/input.txt"
with open(file, 'r') as f:
    for line in f.readlines():
        data.append(line.strip())

# Solution
opponent = 0
player = 0
for entry in data:
    o, p = entry.split(' ')
    if RESULTS[entry] == -1:
        opponent += SCORING[o] + 6
        player += SCORING[p]
    elif RESULTS[entry] == 1:
        opponent += SCORING[o]
        player += SCORING[p] + 6
    else:
        opponent += SCORING[o] + 3
        player += SCORING[p] + 3

print(f'Opponent: {opponent}')
print(f'Player: {player}')
