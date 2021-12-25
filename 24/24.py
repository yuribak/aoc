import re

with open('input') as fin:
    inps = fin.readlines()

params = []
with open('input') as fin:
    inps = fin.read()
    s = "mul x 0\nadd x z\nmod x 26\ndiv z (\d\d?)\nadd x (-?\d\d?)\neql x w\neql x 0\nmul y 0\nadd y 25\nmul y x\nadd y 1\nmul z y\nmul y 0\nadd y w\nadd y (\d\d?)\nmul y x\nadd z y"
    for _ in re.findall(s, inps):
        params.append(tuple(map(int, _)))


def f(inp):
    x = y = z = 0

    for n, p in zip(inp, params):
        w = n
        a, b, c = p
        x = z % 26 + b
        z //= a
        x = int(x != w)
        z *= (25 * x + 1)
        z += (w + c) * x
        # print(w, x, y, z, '-', z % 26)
    return w, x, y, z


stack = []
n = [0] * 14
m = [0] * 14

for i, (a, b, c) in enumerate(params):
    if a == 1:
        stack.append((i, a, b, c))
    else:
        j, _a, _b_, _c = stack.pop()
        if abs(b) < _c:
            n[i] = 9
            n[j] = abs(b) + 9 - _c

            m[j] = 1
            m[i] = _c - abs(b) + 1
        else:
            n[j] = 9
            n[i] = _c + 9 - abs(b)

            m[j] = abs(b) - _c + 1
            m[i] = 1

assert f(n)[-1] == 0
print(''.join(map(str, n)))

assert f(m)[-1] == 0
print(''.join(map(str, m)))
