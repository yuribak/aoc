f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
with open(f) as fin:
    data = [_.strip().split() for _ in fin]


print(sum((ord(x)-ord('X')+1 + (((ord(x)-ord('X')-ord(a)+ord('A'))%3 + 1)%3)*3) for a, x in data))
print(sum((ord(x)-ord('X'))*3 + (ord(a)-ord('A')+( ord(x)-ord('X')-1))%3 + 1 for a, x in data))