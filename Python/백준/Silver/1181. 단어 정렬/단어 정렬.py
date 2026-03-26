import sys
input = sys.stdin.readline

n = int(input())

x = set(input().strip() for _ in range(n))

x = sorted(x, key = lambda x: (len(x), x))

for i in x:
    print(i)