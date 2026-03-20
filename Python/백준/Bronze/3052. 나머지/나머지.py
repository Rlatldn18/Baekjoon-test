import sys

renum = set()

for i in range(10):
    num1 = int(sys.stdin.readline())
    renum.add(num1%42)
print(len(renum))