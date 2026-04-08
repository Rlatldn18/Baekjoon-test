import sys
input = sys.stdin.readline
t = int(input())


for i in range(t):
    n = int(input())
    
    if n <= 5:
        base = [0, 1, 1, 1, 2, 2]
        print(base[n])
        continue
    
    p = [0]*(n+1)
    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2
    p[5] = 2
        
    for j in range(6, n+1):
        p[j] = p[j-1] + p[j-5]
    print(p[n])
