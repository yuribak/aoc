
f="input/6"
with open(f) as fin:
    data = fin.read()

print(min(i for i in range(len(data)) if len(set(data[i-4:i]))==4))
print(min(i for i in range(len(data)) if len(set(data[i-14:i]))==14))
