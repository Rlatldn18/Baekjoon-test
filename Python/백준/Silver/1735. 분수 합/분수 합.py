import sys
input = sys.stdin.readline

def gcd(result1,result2):
    while result2 != 0:
        result1,result2 = result2, result1%result2
    return result1

a,b  = map(int, input().split())
c,d  = map(int, input().split())

result1 = a*d + b*c
result2 =  b*d

s = (gcd(result1, result2))
print(result1 //s, result2//s)