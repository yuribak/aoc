directions = open('input').readlines()

x = 0
y = 0
for dir in directions:
    # print(dir)
    d,v = dir.split()
    v = int(v)
    match d:
        case 'forward':
            x+=v
        case 'up':
            y-=v
        case 'down':
            y+=v
print(x * y)



x = 0
y = 0
aim = 0
for dir in directions:
    # print(dir)
    d,v = dir.split()
    v = int(v)
    match d:
        case 'forward':
            x+=v
            y+=aim*v
        case 'up':
            aim-=v
        case 'down':
            aim+=v
print(x * y)






