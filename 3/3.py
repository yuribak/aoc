report = open('input').readlines()


def bit_mod(report, pos):
    return int(sum(int(r[pos]) for r in report) >= len(report)/2)


gamma = [str(bit_mod(report,_)) for _ in range(len(report[0])-1)]
epsilon = [str(1-bit_mod(report,_)) for _ in range(len(report[0])-1)]


gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)

print(gamma, epsilon, gamma*epsilon)

oxy = set(report)
i=0
while len(oxy) > 1:
    b = str(bit_mod(oxy,i))
    oxy = set(_ for _ in oxy if _[i] == b)
    i+=1

oxy = int(oxy.pop(),2)



co2 = set(report)
i=0
while len(co2) > 1:
    b = str(1-bit_mod(co2,i))
    co2 = set(_ for _ in co2 if _[i] == b)
    i+=1

co2 = int(co2.pop(),2)
print(oxy*co2)


