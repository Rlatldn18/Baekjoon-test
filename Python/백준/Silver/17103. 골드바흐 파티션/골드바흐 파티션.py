def eratos(x):
    prime = [True] * (x+1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(x**0.5)+1):
        if prime[i]:
            for j in range(i*i, x+1, i):
                prime[j] = False
    return prime 

import sys
input = sys.stdin.readline

t = int(input())
max = 1000000
prime = eratos(max)

for _ in range(t):
    num = int(input())
    
    cnt = 0
    for k in range(2, num//2+1):
        if prime[k] and prime[num-k]:
            cnt +=1
    print(cnt)