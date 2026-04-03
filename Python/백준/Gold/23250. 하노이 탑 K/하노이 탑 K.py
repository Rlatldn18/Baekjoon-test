"""
    << >> 비트시프트연산자 
    a >> n == a % 2**n 
    a << n == a * 2**n
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def hanoi(n, start, end, mid, k):
    if n == 1:
        print(start, end)
        return

    left = (1 << (n - 1)) - 1  # 왼쪽 subtree 크기
        
    if k <= left:
        hanoi(n - 1, start, mid, end, k)

    elif k == left + 1:
        print(start, end)

    else:
        hanoi(n - 1, mid, end, start, k - left - 1)

hanoi(n, 1, 3, 2, k)