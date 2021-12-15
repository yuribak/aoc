coords, instructions = open('input').read().split("\n\n")

coords = set(tuple(map(int, _.strip().split(","))) for _ in coords.strip().split("\n"))
instructions = instructions.strip().split("\n")

for _, inst in enumerate(instructions):
    axis, v = inst.split()[2].split("=")
    v = int(v)
    if axis == 'y':
        coords = set((x, y) if y <= v else (x, v - (y - v)) for (x, y) in coords)
    else:
        coords = set((x, y) if x <= v else (v - (x - v), y) for (x, y) in coords)
    if _ == 0:
        print(len(coords))

for i in range(10):
    for j in range(40):
        print("#" if (j,i) in coords else " ", end="")
    print()
