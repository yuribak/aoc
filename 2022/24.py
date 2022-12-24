f = "2022/input/" + __file__.split("/")[-1].split(".")[0]


MOVES = DOWN, RIGHT, LEFT, UP = [(1,0),(0,1),(0,-1),(-1,0)]
DIRECTIONS = dict(zip('v><^',MOVES))
LEFT_RIGHT = (LEFT, RIGHT)
UP_DOWN = (UP, DOWN)

storms=[]
with open(f) as fin:
    map = fin.read().split("\n")
    H = len(map)-2
    W = len(map[0])-2
    for i, row in enumerate(map[1:-1]):
        for j, v in enumerate(row[1:-1]):
            if v == '.':
                continue
            storms.append((i,j,DIRECTIONS[v]))

START, END = (-1,0), (H,W-1)

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

cache = {}
def safe(m, i,j, storms):
    key = (m%(H*W),i,j)
    if key not in cache:
        cache[key] = _safe(m,i,j,storms)
    return cache[key]

def _safe(m,i,j,storms):
    if (i,j) in ((-1,0), (H,W-1)): return True
    if not (0<= i < H and 0 <= j < W): return False
    for si,sj, d in storms:
        if d in LEFT_RIGHT:
            if i!=si: continue
            if (sj+m*d[1])%W == j: return False

        elif d in UP_DOWN:
            if j != sj: continue
            if (si+m*d[0])%H == i: return False
    return True


    
import bisect


def find(storms, start=START, end=END, m=0):
    
    q = [(m,start)]
    seen = set(q)
    MIN = float('inf')
    while q:
        
        m, pos = q.pop(0)

        if pos == end:            
            print(len(seen), len(q), m)
            MIN = min(m,MIN)
        
        if m + abs(end[0]-pos[0]) + abs(end[1]-pos[1]) >= MIN:
            continue


        for move in [(0,0)] + MOVES:
            new_pos = add(pos, move)
            if not safe(m+1, *new_pos, storms):
                continue

            if ((m+1)%(H*W), new_pos) not in seen:
                bisect.insort_left(q,(m+1,new_pos), key=lambda _:  m + abs(end[0]-_[1][0]) + abs(end[1]-_[1][1]))
                seen.add(((m+1)%(H*W), new_pos))
    return MIN

m = find(storms)
m = find(storms, start=END, end=START,m=m)
m = find(storms, m=m)
print(m)