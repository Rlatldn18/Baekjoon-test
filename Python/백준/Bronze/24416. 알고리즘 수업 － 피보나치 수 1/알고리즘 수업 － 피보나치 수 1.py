import sys
input = sys.stdin.readline

num = int(input())

def fibonacci(n): # dp로 피보나치 구하기 
    
    f = [0] * (num+1)
    f[1] = f[2] = 1
    
    for i in range(3, num+1):
        f[i] = f[i-1] + f[i-2]
        
    return f[n]
print(fibonacci(num), num-2)

# 일반 재귀로 피보나치 구하기
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#        return fib(n-1) + fib(n-2)