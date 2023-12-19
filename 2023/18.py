import os

import aocd
from collections import defaultdict

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def mul(a,n):
    return tuple(x*n for x in a)
   
DIRS = dict(zip('UDLR',[UP,DOWN,LEFT,RIGHT]))
def parse(data):
    data = [row.split() for row in data.split('\n')]
    data = [(DIRS[d],int(x), c[1:-1]) for d,x,c in data]
    return data

DIRS_B = dict(zip('3120',[UP,DOWN,LEFT,RIGHT]))

def parse_b(data):
    data = [row.split() for row in data.split('\n')]
    data = [(DIRS[d],int(x), c[2:-1]) for d,x,c in data]
    data = [(DIRS_B[c[-1]],int(c[:5],16),None) for doesnt,matter,c in data]

    return data

def solve_a(data, parse=parse):
    data = parse(data)

    start = (0,0)
    pos = start
    trench = defaultdict(lambda : defaultdict(list))
    mxi = 0
    mni = float('inf')
    for direction, distance, color in data:
        i,j = pos
        if direction in {UP, DOWN}:            
            ni = add(pos,mul(direction,distance))[0]
            trench[(min(i,ni), max(i,ni))][j] = direction            
        else:
            ni, nj = add(pos,direction)
            nj = max(nj,add(pos,mul(direction,distance))[1]-1)
            trench[(i,i)][nj] = direction
        pos = add(pos,mul(direction,distance))
        mxi = max(mxi,pos[0])
        mni = min(mni,pos[0])

    lagoon = 0
    keys = sorted(trench)
    print(mni,mxi)
    for i in range(mni, mxi+1):
        if i%1000000 == 0:
            print((i-mni)/(mxi-mni))
        itrench = {}
        for a,b in keys:
            if a <= i <= b:
                itrench.update(trench[(a,b)].items())
            if a > i:
                break
        if not itrench:
            continue
        j = 0
        
        last_j, last_d = None, None

        row = sorted(itrench)

        while j < len(row):
            last_j, last_d = j, itrench[row[j]]
            while j < len(row) -1 and itrench[row[j+1]] in {last_d, LEFT, RIGHT}:
                j += 1
            while j < len(row) -1 and itrench[row[j+1]] != last_d:
                j += 1
        
            lagoon += row[j]-row[last_j] + 1
            
            j+=1

    return lagoon

def solve_b(data):
    return solve_a(data, parse=parse_b)

# answer_a_example = solve_a(puzzle.examples[0].input_data)
# print(answer_a_example, puzzle.examples[0].answer_a, str(answer_a_example) == puzzle.examples[0].answer_a)

# answer_a = solve_a(puzzle.input_data)
# print(answer_a)
# puzzle.answer_a = answer_a


# answer_b_example = solve_b(puzzle.examples[0].input_data)
# print(answer_b_example, puzzle.examples[0].answer_b, str(answer_b_example) == puzzle.examples[0].answer_b)

answer_b = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b