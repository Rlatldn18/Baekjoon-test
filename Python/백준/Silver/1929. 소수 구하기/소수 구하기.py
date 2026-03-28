"""
    에라토스테네스의 체를 이용하여 소수 찾음
    ==> 소수의 배수는 전부 소수가 아님 // 1은 제외 
    
    n m 사이의 소수를 출력
"""    
import sys
input = sys.stdin.readline

def eratos(x):
    prime = [True] * (x+1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(x**0.5)+1):
        if prime[i]:
            for j in range(i*i, x+1, i):
                prime[j] = False
    return[i for i,v in enumerate(prime) if v]    

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())        

a = set(eratos(m))
b = set(eratos(n))

if prime(n):
    print(n)
    print(*sorted(a - b), sep="\n")
else:
    print(*sorted(a - b), sep="\n")