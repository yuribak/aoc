import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH) and puzzle.input_data:
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)
    
def wins(t, d):
    return len([h for h in range(1,t) if ((t-h) * h )> d])


def solve_a(data):
    times, dists = data.split('\n')
    times = list(map(int,times.split(':')[1].strip().split()))
    dists = list(map(int,dists.split(':')[1].strip().split()))
        
    s = 1
    for t,d in zip(times,dists):
        s *= wins(t,d)

    return s

def solve_b(data):
    times, dists = data.split('\n')
    times = int(''.join(times.split(':')[1].strip().split()))
    dists = int(''.join(dists.split(':')[1].strip().split()))
    
    return wins(times, dists)


data = puzzle
# data = puzzle.examples[0]


a = solve_a(data.input_data)
b = solve_b(data.input_data)
print(a)
print(b)


puzzle.answer_a = a
puzzle.answer_b = b

