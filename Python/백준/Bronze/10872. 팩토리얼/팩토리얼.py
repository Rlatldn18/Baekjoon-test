import sys
input = sys.stdin.readline
t = int(input())
result = 1

if t == 0:
    print(1)
else:
    for i in range(1, t+1):
        result *= i
    print(result)