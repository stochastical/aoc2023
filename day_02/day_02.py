import regex as re

with open('input.txt') as f:
    games = f.readlines()

## Part 1
COLOUR_MAXES = {'red': 12, 'green': 13, 'blue': 14}

ans = 0
for index, game in enumerate(games, start=1):
    possible = True
    for colour, max_val in COLOUR_MAXES.items():
        if any(i > max_val for i in map(int, re.findall(f'(\d+) {colour}', game))):
            possible = False
            break
    if possible:
        ans += index
ans

## Part 2
power = 0
for game in games:
    product = 1
    for colour in COLOUR_MAXES:
        product *= max(map(int, re.findall(f'(\d+) {colour}', game)))
    power += product
power
