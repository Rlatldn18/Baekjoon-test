import sys
input = sys.stdin.readline
PrimeNum = []

m = int(input())
n = int(input())

for i in range(m, n+1):
    if i > 1:
        cnt = 0
        for j in range(2, i):
            if  i%j == 0:
                cnt += 1
                break
        if cnt == 0:
            PrimeNum.append(i)

if len(PrimeNum) == 0:
    print(-1)
    
else:
    print(sum(PrimeNum))
    print(PrimeNum[0])