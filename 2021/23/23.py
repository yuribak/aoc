steps = open('input').readlines()

# room, pos (0=bottom), hallway (0=left): distance

DIST = {
    (0, 0): 3,
    (0, 1): 2,
    (0, 2): 2,
    (0, 3): 4,
    (0, 4): 6,
    (0, 5): 8,
    (0, 6): 9,
    (1, 0): 5,
    (1, 1): 4,
    (1, 2): 2,
    (1, 3): 2,
    (1, 4): 4,
    (1, 5): 6,
    (1, 6): 7,
    (2, 0): 7,
    (2, 1): 6,
    (2, 2): 4,
    (2, 3): 2,
    (2, 4): 2,
    (2, 5): 4,
    (2, 6): 5,
    (3, 0): 9,
    (3, 1): 8,
    (3, 2): 6,
    (3, 3): 4,
    (3, 4): 2,
    (3, 5): 2,
    (3, 6): 3,
}

DIST = {(r, f, h): d + (3 - f) for f in range(4) for (r, h), d in DIST.items()}


def cost(a, s, t):
    return [1, 10, 100, 1000][a] * DIST[s + (t,)]


from copy import deepcopy

CACHE = {}


# 1726882 / 1729810
# 346907 / 346907
BRANCHES = 0
def move(rooms, hallway, moved, indent='', cutoff=2 ** 100):
    global BRANCHES
    BRANCHES += 1
    _id = (tuple(tuple(_) for _ in rooms), tuple(hallway), tuple(moved))
    if cutoff < 0:
        return 2 ** 100, []
    # print(indent, rooms,hallway,moved)
    if _id not in CACHE:

        moves = []
        if all(len(rooms[r]) == 4 and all(_ % 4 == r for _ in rooms[r]) for r in range(len(rooms))):
            CACHE[_id] = 0, []
        else:
            mincost = 2 ** 100
            minmove = None

            for h in range(len(hallway)):

                if hallway[h] is not None:
                    a = hallway[h] % 4
                    if all(_ % 4 == a for _ in rooms[a]) and all(hallway[_] is None for _ in PATH[(a, h)]):
                        moves.append(('h', hallway[h], h, a))

            for r in range(len(rooms)):
                if rooms[r] and not moved[rooms[r][-1]]:
                    for h in range(len(hallway)):
                        if hallway[h] is None and all(hallway[_] is None for _ in PATH[(r, h)]):
                            moves.append(('r', rooms[r][-1], r, h))
            for t, *m in moves:
                _r = deepcopy(rooms)
                _h = list(hallway)
                _m = list(moved)
                if t == 'h':
                    a, h, r = m
                    _r[r].append(_h[h])
                    _h[h] = None
                    e = cost(a % 4, (r, len(_r[r]) - 1), h)
                else:
                    a, r, h = m
                    _h[h] = _r[r].pop()
                    _m[_h[h]] = 1
                    e = cost(a % 4, (r, len(_r[r])), h)

                co = cutoff-mincost if cutoff < 2**100 and mincost < 2**100 else cutoff if cutoff < 2**100 else mincost if mincost < 2*100 else cutoff

                me, mm = move(_r, _h, _m, indent=indent + '     ', cutoff=co)
                if me + e < mincost:
                    mincost = e + me
                    minmove = [(t,) + tuple(m) + (e,)] + mm


            CACHE[_id] = mincost, minmove
    return CACHE[_id]


#############
# ...........#
###C#D#D#A###
# #B#A#B#C#
# #########

H = [0, 1, 2, 3, 4, 5, 6]
# (room,hallway): [path]
PATH = {
    (0, 0): [1],
    (0, 1): [],
    (0, 2): [],
    (0, 3): [2],
    (0, 4): [2, 3],
    (0, 5): [2, 3, 4],
    (0, 6): [2, 3, 4, 5],

    (1, 0): [2, 1],
    (1, 1): [2],
    (1, 2): [],
    (1, 3): [],
    (1, 4): [3],
    (1, 5): [3, 4],
    (1, 6): [3, 4, 5],

    (2, 0): [3, 2, 1],
    (2, 1): [3, 2],
    (2, 2): [3],
    (2, 3): [],
    (2, 4): [],
    (2, 5): [4],
    (2, 6): [4, 5],

    (3, 0): [4, 3, 2, 1],
    (3, 1): [4, 3, 2],
    (3, 2): [4, 3],
    (3, 3): [4],
    (3, 4): [],
    (3, 5): [],
    (3, 6): [5],

}

rooms = [
    [1, 11, 15, 2],
    [0, 9, 10, 3],
    [5, 8, 13, 7],
    [6, 14, 12, 4],
]

#############
# ...........#
###B#C#B#D###
# A#D#C#A#
#########

# rooms = [
#     [0, 1],
#     [3, 2],
#     [6, 5],
#     [4, 7],
# ]

# rooms = [
#     [0, 11, 15, 1],
#     [3, 9, 10, 2],
#     [6, 8, 13, 5],
#     [4, 14, 12, 7],
# ]

moved = [0] * 16
hallway = [None] * 7

e, path = move(rooms, hallway, moved)
print(e)

for m, a, s, t, e in path:
    print(
        f'Ampo {"ABCD"[a % 4]} from {"Hallway" if m == "h" else "Room"}{s} to {"Hallway" if m == "r" else "Room"}{t} = {e}')
