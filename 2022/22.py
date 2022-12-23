import re
f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    smap, pathstr = fin.read().split("\n\n")
    map = smap.split('\n')
    path = []
    while pathstr:
        diststr, dir = re.match(r"^(\d+)([LR])?",pathstr).groups()
        pathstr = pathstr[len(diststr)+1:]
        path.append((int(diststr),dir))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

# start on top / left most '.'
i,j = (0,map[0].index('.'))
# start facing right
D = (0,1)

def show(i,j):
    r = list(map[i])
    r[j] = 'X'
    return ''.join(r)

def neg(a):
    return tuple(-1*_ for _ in a)

dname = dict(zip([(0,1),(1,0),(0,-1),(-1,0)],'RDLU'))

for dist,dir in path:
    # print((i,j),dname[D],dist,dir)
    for _ in range(dist):
        ni,nj = add((i,j),D)

        if not (0 <= ni < len(map)) or not (0 <= nj < len(map[ni])) or map[ni][nj] == ' ':
            # edge of map, look back to find wrap-around re-entry
            nd = neg(D)
            nnij = add((ni,nj),nd)
            while  (0 <= nnij[0] < len(map)) and (0 <= nnij[1] < len(map[nnij[0]])) and map[nnij[0]][nnij[1]] != ' ':
                ni,nj = nnij
                nnij = add((ni,nj),nd)
            if map[ni][nj] == '#':
                # wrap around is blocked
                 break
            # found wrap around
            i,j = ni,nj
            continue
        elif map[ni][nj] == '.':
            i,j = ni,nj
            continue
        elif map[ni][nj] == '#':
            break
            
    if dir == 'R':
        D = (D[1],-D[0])
    elif dir=='L':
        D = (-D[1], D[0])
    else:
        break

dscore = [(0,1),(1,0),(0,-1),(-1,0)].index(D)
print(1000*(i+1)+4*(j+1)+dscore)