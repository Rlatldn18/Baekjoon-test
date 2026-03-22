import sys
input = sys.stdin.readline

n = int(input())

a1 = 2
for _ in range(n):
    a1 = (a1*2)-1
    
print(a1**2)    