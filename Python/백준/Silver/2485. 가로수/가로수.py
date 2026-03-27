"""
    최대공약수 구하는 방법 
    def gcd(result1,result2):
    while result2 != 0:
        result1,result2 = result2, result1%result2
    return result1
"""

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

t = int(input())

tree = [int(input()) for _ in range(t)]

distance = []
for i in range(1,t):
    distance.append(tree[i] - tree[i-1])

g = 0
for d in distance:
    g = gcd(g,d)

result = 0
for j in distance:
    result += (j // g) -1

print(result)