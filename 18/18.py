nums = open('input').readlines()
nums = [eval(_) for _ in nums]

def add_left(x, n):
    if isinstance(n, int):
        return x + n
    return [add_left(x, n[0]), n[1]]


def add_right(x, n):
    if isinstance(n, int):
        return x + n
    return [n[0], add_right(x, n[1])]


def explode(n, l=4):
    if isinstance(n, int):
        return None, n, None
    a, b = n
    if l == 0:
        return a, 0, b
    else:
        al, av, ar = explode(a, l - 1)
        if ar:
            b = add_left(ar, b)
            return al, [av, b], None
        elif a == av:
            bl, bv, br = explode(b, l - 1)
            if bl:
                av = add_right(bl, av)
            return None, [av, bv], br
        return al, [av,b], None


test_cases = [
    ([[[[[9, 8], 1], 2], 3], 4], [[[[0, 9], 2], 3], 4]),
    ([7, [6, [5, [4, [3, 2]]]]], [7, [6, [5, [7, 0]]]]),
    ([[6, [5, [4, [3, 2]]]], 1], [[6, [5, [7, 0]]], 3]),
    ([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]),
    ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],[[3,[2,[8,0]]],[9,[5,[7,0]]]])
]

# for t, e in test_cases:
#     a = explode(t)[1]
#     assert a == e,( a,e)


def split(n):
    if isinstance(n, int):
        if n >= 10:
            # print("split:", n)
            return [n//2,n-n//2]
        return n
    a = split(n[0])
    if a == n[0]:
        return [a,split(n[1])]
    return [a,n[1]]


def reduce(n):
    while True:
        l,m,r = explode(n)
        if m != n:
            n=m
            continue
        p = split(m)
        if p == n:
            break
        n=p
    return n


def add(a, b):
    return reduce([a, b])

def mag(n):
    if isinstance(n,int):
        return n
    return 3*mag(n[0])+2*mag(n[1])

s = nums[0]

for _ in nums[1:]:
    s = add(s,_)
print(mag(s))

from itertools import combinations
print(max(mag(add(a,b)) for a,b in combinations(nums,2)))