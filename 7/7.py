crabs = list(map(int,open('input').read().strip().split(",")))

print(min(sum(abs(c-x) for c in crabs) for x in range(min(crabs),max(crabs))))
print(int(min(sum((abs(c-x)+1)*(abs(c-x)/2) for c in crabs) for x in range(min(crabs),max(crabs)))))
