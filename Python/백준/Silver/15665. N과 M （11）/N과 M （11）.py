"""
    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.
    중복되는 수열을 여러 번 출력하면 안됨
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

def backtracking(result):
    if len(result) == m:
        print(*result)
        return

    prev = -1 
    for i in range(n):
        if num[i] != prev:
            result.append(num[i])
            prev = num[i] 
            backtracking(result)
            result.pop()

backtracking([])