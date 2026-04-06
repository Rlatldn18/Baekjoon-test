"""
    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

def backtracking(result):
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        result.append(num[i])
        backtracking(result)
        result.pop()

backtracking([])