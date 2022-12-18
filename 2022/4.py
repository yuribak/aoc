f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
print(sum((lambda a,b,c,d:(a>=c)and(b<=d)or(c>=a)and(d<=b))(*list(map(int,[_ for p in l.split(",")for _ in p.split("-")])))for l in open(f)))
print(sum((lambda a,b,c,d:(b>=c)and(a<=d))(*list(map(int,[_ for p in l.split(",")for _ in p.split("-")])))for l in open(f)))