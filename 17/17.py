tx, ty = open('input').read().split(":")[1].strip().split(",")
xmin, xmax = tx = tuple(map(int, tx.split("=")[1].split("..")))
ymin, ymax = ty = tuple(map(int, ty.split("=")[1].split("..")))

vxmin = 0
_xmin = xmin
while _xmin-vxmin > 0:
    _xmin -= vxmin
    vxmin +=1

target = {(x, y) for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)}

MAXY = 0
vs = set()

for vy in range(ymin, abs(ymin) + 1):
    for vx in range(vxmin,xmax + 1):
        if (vx, vy) in vs:
            continue
        path = [(0,0)]
        _vx, _vy = vx, vy
        while path[-1][1] >= ymin:
            path.append((path[-1][0]+ _vx, path[-1][1] + _vy))
            _vy -= 1
            if _vx > 0:
                _vx -=1

            if path[-1] in target:
                vs.add((vx, vy))
                MAXY = max(MAXY, max(_[1] for _ in path))
                break
            # print((vx,vy),len(path),path)
            # for i in range(max([_[1] for _ in path]+[ymax]),ymin-1,-1):
            #     for j in range(0,xmax):
            #         print('#' if (j,i) in path else 'T' if (j,i) in target else ' ', end='')
            #     print()
            # print('-'*40)
print(MAXY)
print(len(vs))
