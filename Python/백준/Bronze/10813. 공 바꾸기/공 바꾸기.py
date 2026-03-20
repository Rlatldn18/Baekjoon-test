import sys

n,m = map(int, sys.stdin.readline().split())
num = []*n

for x1 in range(1, n+1):
    num.append(x1)


for h in range(m):
    i,j = map(int, sys.stdin.readline().split())
    num[i-1], num[j-1] = num[j-1], num[i-1]

for result in range(n):
    print(num[result], end=" ")