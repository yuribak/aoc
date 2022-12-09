
with open('input/2') as fin:
    data = [_.strip().split() for _ in fin]


# (me - op)% 3 == {0: draw, 1: win, 2: lose}

# s,t=0,0
# for a, x in data:
#     a = ord(a)-ord('A')
#     x = ord(x)-ord('X')
#     s += x+1 + (((x-a)%3 + 1)%3)*3
#     t += x*3 + (a+(x-1))%3+1
# print(s,t)

print(sum((ord(x)-ord('X')+1 + (((ord(x)-ord('X')-ord(a)+ord('A'))%3 + 1)%3)*3) for a, x in data))
print(sum((ord(x)-ord('X'))*3 + (ord(a)-ord('A')+( ord(x)-ord('X')-1))%3 + 1 for a, x in data))