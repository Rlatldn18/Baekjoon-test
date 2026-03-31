def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)       

import sys
input = sys.stdin.readline
num = int(input())
if num == 0:
    print(0)
else:
    for i in range(1, num+1):
        result = Fibonacci(i)
    print(result)