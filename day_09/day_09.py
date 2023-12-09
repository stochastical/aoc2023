## Part 1

with open("input.txt") as f:
    history = [list(map(int, line.strip().split())) for line in f]
history

extraps: [int] = []
for hist in history:
    extrap = hist[-1]
    differences = [y - x for x, y in zip(hist, hist[1::])]
    while any(differences):
        extrap += differences[-1]
        differences = [y - x for x, y in zip(differences, differences[1::])]
    extraps.append(extrap)

sum(extraps)

## Part 2
import functools

extraps: [int] = []
for hist in history:
    difference = [y - x for x, y in zip(hist, hist[1::])]
    differences = [hist, difference]
    while any(difference):
        difference = [y - x for x, y in zip(difference, difference[1::])]
        differences.append(difference)

    sequence: [int] = [diff[0] for diff in reversed(differences)]
    extrap = functools.reduce(
        lambda acc, next_val: next_val - acc, sequence[1:], sequence[0]
    )

    # Or, without a fold:
    # extrap = 0
    # for _, next in zip(sequence, sequence[1:]):
    #     extrap = next - extrap

    extraps.append(extrap)
sum(extraps)
