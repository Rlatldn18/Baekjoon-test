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


import sys
input = sys.stdin.readline

result = []
while True:
    n = int(input())
    if n != 0:        
        a = set(eratos(2*n))
        b = set(eratos(n))
        
        result.append(a-b)
        print(len(*result))

        result.clear()
    else:
        break