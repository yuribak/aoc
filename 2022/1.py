f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
with open(f) as  fin:
    cals = list(map(str.split, fin.read().split("\n\n")))
    cals = [sum(map(int,_)) for _ in cals]
    

print(max(cals))
print(sum(sorted(cals)[-3:]))
