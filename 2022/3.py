f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
# 253
# print((lambda p,f:(sum(p([_ for _ in s[:len(s)//2]if _ in s[len(s)//2:]][0])for s in f),sum(p([_ for _ in f[i]if _ in f[i+1]and _ in f[i+2]][0])for i in range(0,len(f),3))))(lambda c:(ord(c)-96)if'a'<=c else(ord(c)-38),[l[:-1]for l in open('input/3')]))

# 134
print(sum((lambda c:(ord(c)-96)if'a'<=c else(ord(c)-38))([_ for _ in s[:len(s)//2]if _ in s[len(s)//2:]][0])for s in open(f)))
# 182
print([sum((lambda c:(ord(c)-96)if'a'<=c else(ord(c)-38))([_ for _ in e[i]if _ in e[i+1]and _ in e[i+2]][0])for i in range(0,len(e),3))for e in[[l[:-1]for l in open(f)]]][0])