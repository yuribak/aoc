with open("2023/input/1") as fin:
    lines = fin.readlines()

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for c in "0123456789":
    digits[c] = c


calibration = 0
for line in lines:
    s = ""

    for i in range(len(line)):
        for d in digits:
            if line[i:].startswith(d):
                s += digits[d]
                break
        if len(s):
            break

    rline = line[::-1]
    for i in range(len(rline)):
        for d in digits:
            if rline[i:].startswith(d[::-1]):
                s += digits[d]
                break
        if len(s) == 2:
            break

    # print(line, s)
    calibration += int(s)

print(calibration)
