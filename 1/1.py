depths = list(map(int, open('input').readlines()))

print(sum(depths[i] > depths[i - 1] for i in range(1, len(depths))))
print(sum(depths[i] > depths[i - 3] for i in range(3, len(depths))))
