import os

import aocd

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


def cw(d):
    return (d[1],-d[0])

def ccw(d):
    return (-d[1],d[0])

def straight(d):
    return d

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def parse(data):
    return [list(map(int,row)) for row in data.split('\n')]



def show(data, prevs=None):
    prevs = prevs or []
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            print('*' if (i,j) in prevs else c, end='')
        print()
    print()

import heapq        

def solve_a(data, min_straight=-1, max_straight=3):
    data = parse(data)

    ROWS = len(data)
    COLS  = len(data[0])

    def dist(i,j):
        return ROWS - 1 - i + COLS - 1 - j

    def safe(i, j):
        return 0 <= i < ROWS and 0 <= j < COLS

    start = (0,0)
    # pos, direction, heat_loss, moves
    q = []
    heapq.heappush(q, (dist(*start), start,DOWN, 0,0))
    heapq.heappush(q, (dist(*start), start, RIGHT, 0,0))
    visited = {}
    min_heat_loss = float('inf')
    min_path = []
    plen=0
    prevs = {
        (start, DOWN, 0): [],
        (start, RIGHT, 0): []
    }
    while q:
        d, pos, direction, heat_loss, moves = heapq.heappop(q)        
        
        key = tuple([pos,direction,moves])
        
        if key in visited and visited[key] <= heat_loss:
            continue
        visited[key] = heat_loss

        prev = prevs[key]

        if len(prev) > plen:
                plen = len(prev)
                print(len(visited), len(q), plen, heat_loss, dist(*pos), d)

        if pos == (ROWS-1, COLS-1):
            return heat_loss
        # add turns
        turns = [] 
        if moves > min_straight:
            turns.extend([cw,ccw])
        if moves < max_straight:
            turns.append(straight)
        
        for turn in turns:
            new_direction = turn(direction)
            new_position = add(pos, new_direction)
            if not safe(*new_position): continue
            if new_position in prev: continue
            new_heat_loss = heat_loss + data[new_position[0]][new_position[1]]
            new_moves = moves+1 if new_direction == direction else 1

            heapq.heappush(q,(new_heat_loss + dist(*new_position), new_position, new_direction, new_heat_loss, new_moves))
            prevs[(new_position, new_direction, new_moves)] = prev + [pos]
        


    show(data, min_path)
    return min_heat_loss
        
def solve_b(data):
    return solve_a(data=data, min_straight=3, max_straight=10)

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