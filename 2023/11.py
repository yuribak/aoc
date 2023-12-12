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
    data = data.split('\n')
    galaxies = set()
    empty_rows = set(range(len(data)))
    empty_cols = set(range(len(data[0])))
    for i,row in enumerate(data):
        for j,c in enumerate(row):
            if c == '#':
                galaxies.add((i,j))
                if i in empty_rows: empty_rows.remove(i)
                if j in empty_cols: empty_cols.remove(j)
    return list(galaxies), empty_rows, empty_cols

def solve_a(data,N=2):
    galaxies, empty_rows, empty_cols = parse(data)


    def dist(a,b):
        d = abs(a[0]-b[0]) + abs(a[1]-b[1])
        mni, mxi = min(a[0],b[0]),max(a[0],b[0])
        d += len([r for r in empty_rows if mni < r < mxi])*(N-1)
        mnj, mxj = min(a[1],b[1]),max(a[1],b[1])
        d += len([c for c in empty_cols if mnj < c < mxj])*(N-1)
        return d

    D = 0
    for i in range(len(galaxies)):
        for j in range(i,len(galaxies)):
            D += dist(galaxies[i],galaxies[j])

    return D

def solve_b(data):
    return solve_a(data, N=1000000)


answer_a = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


answer_b = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b