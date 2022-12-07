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
    'A X': 'Z',
    'A Y': 'X',
    'A Z': 'Y',

    'B X': 'X',
    'B Y': 'Y',
    'B Z': 'Z',

    'C X': 'Y',
    'C Y': 'Z',
    'C Z': 'X'
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
    o, r = entry.split(' ')  # TODO: lol get rid of single letter vars
    p = RESULTS[entry]

    if r == 'X':
        opponent += SCORING[o] + 6
        player += SCORING[p]
    elif r == 'Z':
        opponent += SCORING[o]
        player += SCORING[p] + 6
    else:
        opponent += SCORING[o] + 3
        player += SCORING[p] + 3

print(f'Opponent: {opponent}')
print(f'Player: {player}')
