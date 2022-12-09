with open(f'input/1') as  fin:
    cals = list(map(str.split, fin.read().split("\n\n")))
    cals = [sum(map(int,_)) for _ in cals]
    

print(max(cals))
print(sum(sorted(cals)[-3:]))
