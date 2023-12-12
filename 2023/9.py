import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)


def parse(data):
    return [list(map(int,line.split())) for line in data.split('\n')]


def next(D):
    if not D:
        return 0
    return D[0][-1]+next(D[1:])

def prev(D):
    if not D:
        return 0
    return D[0][0]-prev(D[1:])

def solve_a(data, f=next):
    histories = parse(data)
    s = 0
    for h in histories:
        diffs = [b-a for a,b in zip(h[:-1],h[1:])]
        D = [h]
        while any(diffs):
            D.append(diffs)
            diffs = [b-a for a,b in zip(diffs[:-1],diffs[1:])]

        d = f(D)
        s += d
    return s

def solve_b(data):
    return solve_a(data, f=prev)

answer_a = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


answer_b = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b