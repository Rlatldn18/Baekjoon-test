year = int(input())
leaf = 0

if (year % 4) == 0:
    if (year % 100) != 0 or (year % 400) == 0:
        leaf = 1
    else:
        leaf = 0
else:
    leaf = 0
print(leaf)