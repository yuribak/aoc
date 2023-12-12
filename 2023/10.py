import os

import aocd

day = int(os.path.basename(__file__[:-3]))
year = int(os.path.basename(os.path.dirname(__file__)))
INPUT_PATH = f"./{year}/input/{day}"

puzzle = aocd.models.Puzzle(year=year, day=day)

if not os.path.exists(INPUT_PATH):
    with open(INPUT_PATH,'w') as fout:
        fout.write(puzzle.input_data)


directions = {
    '|':((-1,0),(1,0)),
    '-': ((0,-1),(0,1)),
    'F':((1,0),(0,1)),
    '7':((1,0),(0,-1)),
    'L':((-1,0),(0,1)),
    'J':((-1,0),(0,-1)),
    '.': tuple(),
    # 'S': tuple()
}


def parse(data):
    start = None
    for i,line in enumerate(data.split('\n')):
        for j,c in enumerate(line):
            if c == 'S':
                start = (i,j)
    return start, [list(line.strip()) for line in data.split('\n')]
        

def solve(data):
    start, pipes = parse(data)
    ROWS = len(pipes)
    COLS = len(pipes[0])

    def safe(i,j):        
        return 0 <= i < ROWS  and 0 <= j < COLS
    
    def add(a,b):
        return tuple(x+y for x,y in zip(a,b))

    def nbs(coords):
        i,j = coords
        return [(i+x,j+y) for x,y in [(-1,0),(1,0),(0,-1),(0,1)]]
    
    def dirs(coord):
        i,j=coord
        return [add(coord, d) for d in directions[pipes[i][j]]]

    def flood(start, loop, f=nbs):
        visited = set()
        dists = {}
        q = start
        boundary = False
        while q:
            (i,j),d = q.pop(0)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            dists[(i,j)] = d

            for n in f((i,j)):
                if not safe(*n):
                    boundary = True
                    continue
                if n in visited or n in loop:
                    continue
                q.append((n,d+1))
        return visited, dists, boundary


    q = []
    for ni,nj in nbs(start):
        if any(add((ni,nj),d)==start for d in directions.get(pipes[ni][nj],[])):
            q.append(((ni,nj),1))

    start_ds = tuple(tuple(a-b for a,b in zip(nbr, start)) for nbr,_ in q)
    for symbol, ds in directions.items():
        if start_ds == ds or start_ds == ds[::-1]:
            pipes[start[0]][start[1]] = symbol
            break

    
    loop, dists, _ = flood(q, set() ,dirs)

    max_dist = max(dists.values())

    def is_in_loop(i,j,loop):
        ci = 0
        left = right = 0
        i+=1
        while i < ROWS:
            if (i,j) in loop:
                c = pipes[i][j]
                if c == '-':
                    ci+=1
                elif c == '7':
                    left = True
                elif c == 'J':
                    if right:
                        ci+=1
                        right = False
                    left=False
                elif c == 'F':
                    right = True
                elif c == 'L':
                    if left:
                        ci +=1
                        left = False
                    right = False                
            i+=1

        return ci%2==1

    in_loop, outside_loop = set(), set()


    for i in range(ROWS):
        for j in range(COLS):
            if (i,j) in loop: continue
            if (i,j) in in_loop: continue
            if (i,j) in outside_loop: continue
            s, dists, boundary = flood(start=[((i,j),0)], loop=loop)

            if boundary or not is_in_loop(i,j,loop):
                outside_loop |= s
            else:
                in_loop |= s


    return max_dist, len(in_loop)


answer_a, answer_b = solve(puzzle.input_data)
print(answer_a)
print(answer_b)