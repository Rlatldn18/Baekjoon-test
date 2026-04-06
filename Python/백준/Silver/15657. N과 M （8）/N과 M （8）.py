"""
    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.
    고른 수열은 비내림차순이어야 한다.
    길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 
    비내림차순이라고 한다.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

def backtracking(start, result):
    if len(result) == m:
        print(*result)
        return

    for i in range(start, n):
        result.append(num[i])
        backtracking(i, result)
        result.pop()

backtracking(0, [])