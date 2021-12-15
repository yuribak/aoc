fish = open('input').readlines()
fish = list(map(int,fish[0].split(",")))


CACHE={}
def babies(timer, days):
    if timer >= days:
        return 0

    days -= timer
    if days in CACHE:
        return CACHE[days]
    return CACHE.setdefault(days, 1 + babies(7,days) + babies(9,days))

print(sum(babies(f,80) for f in fish) + len(fish))
print(sum(babies(f,256) for f in fish) + len(fish))

