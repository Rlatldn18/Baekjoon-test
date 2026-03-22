import sys
input = sys.stdin.readline

a1 = 1
posmax = 1
n = int(input())

while posmax < n:
    posmax += 6*a1
    a1 += 1
print(a1)