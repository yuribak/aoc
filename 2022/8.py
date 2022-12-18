from operator import mul, or_

f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
with open(f) as fin:
    data = [list(map(int, _.strip())) for _ in fin]


def scan(data, fscore, fagg1, fagg2):

    rows = []
    cols = []

    for row in data:
        l = fscore(row)
        r = fscore(row[::-1])[::-1]
        rows.append([fagg1(*_) for _ in zip(l,r)])

    for col in [*zip(*data)]:
        t = fscore(col)
        b = fscore(col[::-1])[::-1]
        cols.append([fagg1(*_) for _ in zip(t,b)])

    result = [[False] * len(data[0]) for _ in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] = fagg1(rows[i][j], cols[j][i])

    return fagg2(_ for __ in result for _ in __)


def visible(vec):
    m = -1
    vs = [False] * len(vec)
    for i, v in enumerate(vec):
        if v > m:
            m = v
            vs[i] = True
    return vs


def vscores(vec):

    blocks = {}
    score = [0] * len(vec)
    for i in range(1, len(vec)):
        if vec[i - 1] >= vec[i]:
            blocks[i] = i - 1
            score[i] = 1
        else:
            j = blocks.get(i - 1)
            while j is not None and vec[j] < vec[i]:
                j = blocks.get(j)
            blocks[i] = j
            score[i] = i - (0 if j is None else j)
    return score

print(scan(data, visible, or_, sum))
print(scan(data, vscores, mul, max))
