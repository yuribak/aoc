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
    data = [row.split() for row in data.split('\n')]
    data = [(springs, tuple(map(int,damaged.split(',')))) for springs, damaged in data]
    return data

def parse_b(data):
    data = [row.split() for row in data.split('\n')]
    data = [('?'.join([springs]*5), tuple(map(int,damaged.split(',')))*5) for springs, damaged in data]
    return data


def take(string, substring):
    if not len(substring) <= len(string):
        return None
    for actual, expected in zip(string, substring):
        if not (actual == expected or actual == '?'):
            return None
    return string[len(substring):]


CACHE={}
def solve(springs, damaged):
    if not damaged:
        return '#' not in springs
    if not springs:
        return 0
    
    if (springs, damaged) in CACHE:
        return CACHE[(springs, damaged)]
    
    si =0
    while si < len(springs) and springs[si] == '.':
        si+=1
    if not springs[si:]:
        return 0
    
    r = 0
    s = take(springs[si:], '#'*damaged[0]+('.' if len(damaged)>1 else ''))
    if s is not None:
        r =  solve(s, damaged[1:])
    if springs[si] == '?':
        r += solve(springs[si+1:], damaged)
    CACHE[((springs, damaged))] = r
    return r
    

def solve_a(data, parse=parse):
    data = parse(data)
    return sum(solve(springs, damaged) for springs, damaged in data)

def solve_b(data):
    return solve_a(data, parse=parse_b)
    

# answer_a = solve_a(puzzle.input_data)
# print(answer_a)
# puzzle.answer_a = answer_a


answer_b = solve_b(puzzle.input_data)
print(answer_b)
# puzzle.answer_b = answer_b