f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

# Schar = 'E'
# E = 0
Schar='S'
Echar='E'
E = 26 

S = None
with open(f) as fin:
    data = [_.strip() for _ in fin]
    ndata = [[(ord(_.lower())-ord('a') if _!= Echar else 26) if _ != Schar else 0 for _ in row] for row in data ]
    for i,row in enumerate(data):
        if Schar in row:
            S = i,row.index(Schar)

# for row in ndata: print(row)

def bfs():

    q = [(S,0,[])]
    seen = set()
    Q = set()
    Q.add(S)


    def nbrs(i,j):
        result = []
        for x,y in ((i,j+1),(i,j-1),(i+1,j),(i-1,j)):
            if not (0 <= x < len(ndata) and 0 <= y < len(ndata[0])):
                continue
            if (x,y) in seen:
                continue
            if (x,y) in Q:
                continue
            result.append((x,y))

        return sorted(result, key=lambda _: ndata[_[0]][_[1]], reverse=True)

    m = -1
    mp=[]

    while q:
        (i,j),d,path = q.pop(0)
        # print(len(q), d)
        seen.add((i,j))
        ns = nbrs(i,j)
        for x,y in ns:
            if ndata[x][y] <= ndata[i][j]+1:
            # if ndata[i][j]-1 <= ndata[x][y]:
                p = path+[(x,y)]
                m = max(m,ndata[x][y])
                mp=p
                # p=None
                if ndata[x][y] == E:
                    return path
                q.append(((x,y),d+1,p))
                Q.add((x,y))
    return mp


def encode(i,j,_,path=None):

    if path and (i,j) in path[:-1]:

        # x,y = p[k+1]
        # if x > i:
        #     return 'v'
        # elif x < i:
        #     return '^'
        # elif y > j:
        #     return '>'
        # elif j > y:
        #     return '<'
        return chr(ndata[i][j]+ord('a')).upper()
    # elif (i,j) in visited:
    #     return chr(_+ord('a'))
    

    if (i,j) == S:
        return 'S'

    # return chr(_+ord('a'))    
    return '.'
        


    



p = bfs()

# for i,row in enumerate(ndata):
    # print(''.join([encode(i,j,_,p) for j,_ in enumerate(row)]))

# print(p)
print(len(p)+1)


