import os

import aocd
import math

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)


def parse(data):
    directions, nodes = data.split('\n\n')
    ns = {}
    for line in nodes.split('\n'):
        node, left_right = line.split(' = ')
        left, right = left_right[1:-1].split(', ')
        ns[node]= (left, right)
    return directions, ns


def solve_a(data):
    directions, nodes = parse(data)
    i = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = nodes[node][0 if directions[i%len(directions)] == 'L' else 1]
        i+=1
    return i


def solve_b(data):
    directions, nodes = parse(data)
    i = 0
    ns = [n for n in nodes if n.endswith('A')]
    counts = [0 for _ in range(len(ns))]
    while any(ns):
        ns = [nodes[n][0 if directions[i%len(directions)] == 'L' else 1] if n is not None else None for n in ns]
        for j in range(len(ns)):
            if ns[j] and ns[j].endswith('Z'):
                ns[j] = None
                counts[j] = i+1 # mother f****r
        i+=1

    lcm = counts[0]
    for c in counts:
        lcm = math.lcm(c, lcm)
    return lcm

answer_a = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


answer_b = solve_b(puzzle.input_data)
print(answer_b)