heights = open('input').readlines()
heights = [list(map(int, _.strip())) for _ in heights]

def _min(i, j):
    return min(
        [
            (x, y)
            for x, y in [(i, j), (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if 0 <= x < len(heights) and 0 <= y < len(heights[x])
        ],
        key=lambda xy: heights[xy[0]][xy[1]]
    )

def flow(i,j):
    while _min(i,j) != (i,j):
        i,j = _min(i,j)
    return i,j


def fill(x,y):
    unvisited = {(x, y)}
    visited = set()
    filled = set()
    while unvisited:
        i, j = unvisited.pop()
        filled.add((i, j))
        visited.add((i, j))
        for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (a, b) in visited: continue
            if (a, b) in unvisited: continue
            if 0 <= a < len(heights) and 0 <= b < len(heights[0]) and 9 > heights[a][b]:
                if heights[a][b] >= heights[i][j]:
                    unvisited.add((a, b))
            else:
                visited.add((a, b))

    return filled

coords = set((x,y) for x in range(len(heights)) for y in range(len(heights[x])))

basins = {}
while coords:
    i,j = coords.pop()
    # print(i,j)
    if heights[i][j] == 9: continue
    root = flow(i,j)
    basins[root] = fill(*root)
    coords -= basins[root]

from math import prod
print(sum(1+heights[x][y] for x,y in basins.keys()))
print(prod(sorted(map(len, basins.values()))[-3:]))
