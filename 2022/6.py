
f = "2022/input/" + __file__.split('/')[-1].split('.')[0]
with open(f) as fin:
    data = fin.read()

print(min(i for i in range(len(data)) if len(set(data[i-4:i]))==4))
print(min(i for i in range(len(data)) if len(set(data[i-14:i]))==14))
