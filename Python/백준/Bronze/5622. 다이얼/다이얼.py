alp = input()

sec = 0

for i in alp:
    if i in "ABC":
        sec += 3
    elif i in "DEF":
        sec += 4
    elif i in "GHI":
        sec += 5
    elif i in "JKL":
        sec += 6
    elif i in "MNO":
        sec += 7
    elif i in "PQRS":
        sec += 8
    elif i in "TUV":
        sec += 9
    elif i in "WXYZ":
        sec += 10

print(sec)