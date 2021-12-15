octo = open('input').readlines()
octo = [list(map(int,_.strip()) )  for _ in octo]

FCOUNTER = 0

def flash(i,j):
    global  FCOUNTER
    FCOUNTER +=1
    flashes = set()
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if not 0 <= x < len(octo) or not 0 <= y < len(octo[x]):
                continue

            octo[x][y] +=1
            if octo[x][y] > 9:
                flashes.add((x,y))
    return flashes


STEPS = 0
while True:
    STEPS += 1
    flashes = set()
    for i in range(len(octo)):
        for j in range(len(octo)):
            octo[i][j] +=1
            if octo[i][j] > 9:
                flashes.add((i,j))

    flashed = set()
    while flashes:
        i,j = flashes.pop()
        if (i,j) in flashed:
            continue

        flashes |= flash(i,j)
        flashed.add((i,j))

    for i in range(len(octo)):
        for j in range(len(octo)):
            if octo[i][j] > 9:
                octo[i][j] = 0

    if STEPS == 100:
        print(FCOUNTER)
    if len(flashed) == 100:
        break

print(STEPS)