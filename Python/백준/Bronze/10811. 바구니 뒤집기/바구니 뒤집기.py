import sys
numline = []

n,m = map(int, sys.stdin.readline().split())

num = list(range(1, n+1))

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    num[i-1:j] = reversed(num[i-1:j])
    
print(*num)