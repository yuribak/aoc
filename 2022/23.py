import re

f = "2022/input/" + __file__.split("/")[-1].split(".")[0]

with open(f) as fin:
    map = fin.read().split("\n")

elves = set()
for i, row in enumerate(map):
    for j, v in enumerate(row):
        if v == "#":
            elves.add((i, j))


compass = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j]
dir_names = dict(zip(["NW", "N", "NE", "W", "E", "SW", "S", "SE"], compass))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def lonely(e, elves):
    for _ in compass:
        if add(e, _) in elves:
            return False
    return True


def option_maker(directions, target):
    def f(e, elves):
        for d in directions:
            if add(e, dir_names[d]) in elves:
                return None
        return add(e, dir_names[target])

    return f


opt_n = option_maker(["N", "NE", "NW"], "N")
opt_s = option_maker(["S", "SE", "SW"], "S")
opt_w = option_maker(["W", "NW", "SW"], "W")
opt_e = option_maker(["E", "NE", "SE"], "E")

options = [opt_n, opt_s, opt_w, opt_e]

from collections import defaultdict


def round(elves, options):
    props = defaultdict(list)
    for e in elves:
        if lonely(e, elves):
            continue
        for opt in options:           
            if target := opt(e, elves):
                props[target].append(e)
                break
    moves = 0
    for target, es in props.items():
        if len(es) == 1:
            moves += 1
            elves.remove(es[0])
            elves.add(target)
    options.append(options.pop(0))
    return moves


def empties(elves):
    s = e = float("-inf")
    n = w = float("inf")
    for el in elves:
        n = min(n, el[0])
        s = max(s, el[0])
        w = min(w, el[1])
        e = max(e, el[1])

    # for i in range(s - n + 1):
    #     for j in range(e - w + 1):
    #         if (i + n, j + w) in elves:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print()
    return (s - n + 1) * (e - w + 1) - len(elves)


ROUNDS = 10
for _ in range(ROUNDS):
    round(elves, options)

print(empties(elves))

while round(elves, options):
    _ += 1

print(_ + 2)
