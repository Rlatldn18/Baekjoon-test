n = int(input())

for z in range(1, n+1):
    print(" "*(n-z) + "*"*(z*2-1))

for z in range(n-1, 0, -1):
    print(" "*(n-z) + "*"*(z*2-1))