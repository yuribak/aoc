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
    return [list(_) for _ in data.split('\n')]


def south(data):
    # loads = [0]*len(data[0])
    round_rocks = [0]*len(data[0])
    for load,row in enumerate(data):
        for i,obj in enumerate(row):
            match obj:
                case '.': continue
                case 'O': 
                    round_rocks[i] += 1
                    row[i] = '.'
                case '#':
                    for j in range(load-round_rocks[i],load):
                        data[j][i] = 'O'
                    round_rocks[i] = 0        
    
    for i,obj in enumerate(row):
        if round_rocks[i]:
            for j in range(load+1-round_rocks[i],load+1):
                data[j][i] = 'O'
    return data



def calc_south_load(data):
    LOAD =0 
    for load,row in enumerate(data):
        for i,obj in enumerate(row):            
            if data[load][i] == 'O':
                LOAD += load+1
    return LOAD

def north(data):
    d = south(data[::-1])
    return d[::-1]


def transpose_west(data):
    return [[row[i] for row in data] for i in range(len(data[0])-1,-1,-1)]

def transpose_east(data):
    return [[row[i] for row in data][::-1] for i in range(len(data[0]))]

def west(data):
    d = south(transpose_west(data))
    return transpose_east(d)

def east(data):
    d = south(transpose_east(data))
    return transpose_west(d)


def show(data, title=''):
    print(f'--{title}--')
    for row in data:
        print(' '.join(row))
    print('')

def solve_a(data):    
    data = parse(data)
    data = north(data)
    return calc_south_load(data[::-1]), data

cache = {}

def loop(data,n):
    for _ in range(n):
        for f in [north, west, south, east]:
            data = f(data)
        s = ''.join(''.join(row) for row in data)
        if s in cache:
            return data, cache[s], _
        cache[s] = _
    return data, None, n

def solve_b(data):
    data = parse(data)
    
    data, start, end = loop(data, 1000000000)
    cache.clear()
    remainder = (1000000000-1-end)%(end-start) 
    if remainder > 0:
        data, start, end = loop(data, remainder)
    return calc_south_load(data[::-1]), data



answer_a_example, data = solve_a(puzzle.examples[0].input_data)
# show(data)
print(answer_a_example, puzzle.examples[0].answer_a, str(answer_a_example) == puzzle.examples[0].answer_a)

answer_a, data = solve_a(puzzle.input_data)
print(answer_a)
puzzle.answer_a = answer_a


answer_b_example, data = solve_b(puzzle.examples[0].input_data)
# show(data, "answer b")
print(answer_b_example, puzzle.examples[0].answer_b, answer_b_example == puzzle.examples[0].answer_b)

answer_b, data = solve_b(puzzle.input_data)
print(answer_b)
puzzle.answer_b = answer_b
