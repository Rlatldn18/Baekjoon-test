import sys
input = sys.stdin.readline
lens = int(input())
l = list(map(str, input().strip()))
m = 1234567891
result = 0

for i, c in enumerate(l):
    value = ord(c) - 96
    result += value * (31 ** i)

result = result % m
print(result)