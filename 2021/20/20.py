_algo, imagestr = open('input').read().split("\n\n")
_algo = [0 if _ == '.' else 1 for _ in _algo]
image = set()
for i, row in enumerate(imagestr.split('\n')):
    for j, s in enumerate(row):
        if s == '#': image.add((i, j))

print(_algo)
print(len(image), sorted(image))


def square(i, j):
    for _i in range(-1, 2):
        for _j in range(-1, 2):
            yield (i + _i, j + _j)


CACHE = {}


def pixel(i, j, step):
    # print(i,j,step)
    if step == 0:
        return int((i, j) in image)

    if (i, j, step) not in CACHE:
        CACHE[(i, j, step)] = _algo[int(''.join(map(str, (pixel(*_, step - 1) for _ in square(i, j)))), 2)]

    return CACHE[(i, j, step)]


mn = min(_[0] for _ in image), min(_[1] for _ in image)
mx = max(_[0] for _ in image), max(_[1] for _ in image)

STEPS = 50

from tqdm import tqdm

#margins
# l= 35
# r = 60
# t = 55
# b = 40

l, r, t, b = 35,60,55,40

# s = sum(tqdm(
#     pixel(i, j, STEPS)
#     for i in range(mn[0] - t, mx[0] + b)
#     for j in range(mn[1] - l, mx[1] + r))
#
# )

for step in range(STEPS+1):
    # if step % 100: continue
    for i in range(mn[0] - t , mx[0] + b):
        for j in range(mn[1] - l, mx[1] + r):
            print('.#'[pixel(i,j,step)], end='')
        print()
    print()
    print()
