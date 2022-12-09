from heapq import heappush, heappop

risk = open('input').readlines()
risk = [list(map(int, _.strip())) for _ in risk]


def inc(x, n=1):
    for _ in range(n):
        x = x % 9 + 1
    return x


def astar(m):
    minpaths = {(x, y): len(m) ** 2 + 1 for x in range(len(m)) for y in range(len(m[x]))}
    target = (len(m) - 1, len(m[0]) - 1)

    def h(x, y):
        return target[0] - x + target[1] - y

    s = [(0 + h(0, 0), ((0, 0),))]  # list[(cost, path)]
    while s:
        cost, path = heappop(s)
        if path[-1] == target:
            break
        x, y = path[-1]

        for xd, yd in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            xn, yn = nn = x + xd, y + yd

            if not (0 <= xn < len(m) and 0 <= yn < len(m[x])): continue
            if nn in path: continue

            ncost = cost - h(x, y) + m[xn][yn] + h(xn, yn)
            if ncost >= minpaths[nn]: continue

            minpaths[nn] = ncost
            heappush(s, (ncost, path + (nn,)))
    return path


path = astar(risk)
print(sum(risk[x][y] for x, y in path[1:]))

bigrisk = []
for row in risk:
    bigrisk.append([inc(_, i) for i in range(5) for _ in row])

for i in range(4 * len(risk)):
    bigrisk.append([inc(_) for _ in bigrisk[len(bigrisk) - len(risk)]])

# import time
# start = time.time()
bigpath = astar(bigrisk)  # 17.976665496826172 secs
# print(time.time()-start)
print(sum(bigrisk[x][y] for x, y in bigpath[1:]))

# for x in range(len(bigrisk)):
#     for y in range(len(bigrisk[x])):
#         print("\033[94m#\033[0m" if (x,y) in bigpath else "X" if (x%len(risk),y%(len(risk[0]))) in path else " ", end='')
#     print()
