import math

## Part 1
with open("input.txt") as f:
    times = list(map(int, f.readline().removeprefix("Time:").strip().split()))
    distances = list(map(int, f.readline().removeprefix("Distance:").strip().split()))

races = dict(zip(times, distances))
races

def number_of_wins(races: dict[int, int]) -> int:
    num_wins: [int] = []
    for boost, distance_record in races.items():
        wins = 0
        for s in range(boost + 1):
            distance: int = (boost - s) * s
            if distance > distance_record:
                wins += 1
        num_wins.append(wins)
    return math.prod(num_wins)

print(number_of_wins(races))

## Part 2

with open("input.txt") as f:
    times = int("".join(f.readline().removeprefix("Time:").split()))
    distances = int("".join(f.readline().removeprefix("Distance:").split()))

races: dict[int, int] = {times: distances}
races

print(number_of_wins(races))
