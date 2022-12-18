from itertools import cycle

f = "2022/input/" + __file__.split('/')[-1].split('.')[0]

with open(f) as fin:
    _jets = fin.read()



_rocks = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")
_rocks = [[_.strip() for _ in r.split('\n')] for r in _rocks]
__rocks = []
for rock in _rocks:
    r = []
    h = 0
    w = 0
    for y,row in enumerate(rock[::-1]):
        for x,val in enumerate(row):
            if val !='.':
                r.append((x,y))
                h = max(h,y)
                w = max(w,x)
    __rocks.append((tuple(r),h,w))


rocks = cycle(__rocks)
jets = cycle(_jets)

W = 7



def move(x,y,rock,h,w,buff: set, xm, ym):
    if x +w+xm >= W or x +xm < 0 or y+ym < 0:
        return x,y
    for xd,yd in rock:
        if y+yd+ym<0 or x+xd+xm<0 or x+xd+xm >= W or (x+xd+xm,y+yd+ym) in buff:
            return x,y
    return x+xm,y+ym



def rocks(i):
    return __rocks[i%len(__rocks)]

def jets(i):
    return _jets[i%len(_jets)]



# N=1000000000000
N=10000
BP=N+1



def cycle_detection(i, j, heights, ctx):

    mxt = max(heights)
    anchor = heights[0]
    skyline = tuple([_-anchor for _ in heights])

    if not any(skyline):

        flat_i = ctx.get('flat_i',0)
        flat_j = ctx.get('flat_j',0)
        flat_height = ctx.get('flat_height', -1)
        flats = ctx.get('flats',[])
        flat_cycle = ctx.get('flat_cycle',set())

        flats.append((i,i-flat_i,mxt,mxt-flat_height,j,j-flat_j))
        if (i-flat_i,mxt-flat_height,j-flat_j) not in flat_cycle:
            flat_cycle.add((i-flat_i,mxt-flat_height,j-flat_j))
        else:
            raise StopIteration
        ctx['flat_i'] = i
        ctx['flat_j'] = j
        ctx['flat_height'] = mxt
        ctx['flats'] = flats
        ctx['flat_cycle'] = flat_cycle





def tetris(start=0,end=N,j=0, f=None):

    buff = set()
    ctx = {}
    HEIGHTS = [-1]*W
    i = start-1
    while True:
        i+=1
        if end and i >= end:
            break
        rock,h,w = rocks(i)
        x = 2
        y = max(HEIGHTS)+3+1

        while True:
            jet = jets(j)
            j+=1
            xm = 1 if jet == '>' else -1
            x,y = move(x,y,rock,h,w,buff,xm,0)
            nx,ny = move(x,y,rock,h,w,buff,0,-1)        
            if ny==y:
                buff.update([(x+xd,y+yd) for xd,yd in rock])
                for xd,yd in rock:
                    if y+yd > HEIGHTS[x+xd]:
                        HEIGHTS[x+xd] = y+yd
                
                if f:
                    try:
                        f(i, j, HEIGHTS, ctx)
                    except StopIteration:
                        return ctx
                break
            x,y=nx,ny
        if i >= BP:
            print(HEIGHTS)
    return max(HEIGHTS)+1



flats = tetris(end=None, f=cycle_detection)['flats']

cycle_start = None
cycle_start_height = None
for flat in flats:
    if (flat[1],flat[3]) == (flats[-1][1],flats[-1][3]):
        cycle_start, cycle_start_height, cycle_j_start = (flat[0],flat[2],flat[4])
        break

cycle_length = flats[-1][0]-cycle_start
cycle_gain = flats[-1][2]-cycle_start_height
cycle_j_gain = flats[-1][4] - cycle_j_start
cycles_count = ((N-cycle_start)//cycle_length)


tail= max(N-cycle_start,0)%cycle_length
tail_height = tetris(N-tail+1,N,cycle_j_start + cycle_j_gain*cycles_count)

cycles_height = cycles_count*cycle_gain if cycle_start+cycle_length <= N else 0

print(cycle_start_height + cycles_height + tail_height+1)



# 1525872442870 too low
# 1526744186037 wrong
# 1526744186042 JUST RIGHT!!
# 1526744186057 too high
# 1526744186058 too high
# 