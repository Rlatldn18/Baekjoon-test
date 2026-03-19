import sys

n, m = map(int, sys.stdin.readline().split())
n1 = [0]*n

for x in range (m):
    i,j,k = map(int, sys.stdin.readline().split())
    for y in range(i, j+1):
        n1[y-1] = k

for z in range (n):
    print(n1[z], end=" ")