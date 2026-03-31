"""
    recursion 재귀 : 함수 내부에서 자기 자신을 다시 호출하여 문제 해결 
"""
def fac (n):
    if n == 0:
        return 1
    return fac(n-1) * n        

import sys
input = sys.stdin.readline
num = int(input())

print(fac(num))