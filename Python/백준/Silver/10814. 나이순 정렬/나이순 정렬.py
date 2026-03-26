import sys
input = sys.stdin.readline

n = int(input())

x = [list(map(str, input().split())) for _ in range(n)]

x.sort(key= lambda x : int(x[0]))

for i in x:
    print(*i)