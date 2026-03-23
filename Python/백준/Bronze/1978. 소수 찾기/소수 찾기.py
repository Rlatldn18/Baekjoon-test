import sys
input = sys.stdin.readline

a1= []
PrimeNum = []

n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    
    for j in range(1, x[i]+1):
        if x[i] % j == 0:
            a1.append(j)
    PrimeNum.append(len(a1))
    a1.clear()    

print(PrimeNum.count(2))