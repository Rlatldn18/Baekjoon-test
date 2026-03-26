import sys
input = sys.stdin.readline

n = int(input())

x = [list(map(int, input().split())) for _ in range(n)]

x.sort()

for i in x:
    print(i[0], i[1])