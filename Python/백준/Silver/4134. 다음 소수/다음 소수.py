"""
    소수 찾는 알고리즘 
    def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
"""    
import sys
input = sys.stdin.readline

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next(n):
    a = n
    while not prime(a):
        a += 1
    return a

t = int(input())

for _ in range(t):
    num = int(input())
    print(next(num))