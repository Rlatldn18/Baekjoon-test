import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    a = int(input())
    num.append(a)

num.sort()

print(*num, sep="\n")