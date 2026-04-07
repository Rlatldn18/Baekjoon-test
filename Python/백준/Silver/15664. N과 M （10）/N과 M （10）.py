"""
    N개의 자연수 중에서 M개를 고른 수열
    고른 수열은 비내림차순이어야 한다
    중복되는 수열을 여러 번 출력하면 안됨
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * n

def backtracking(start, result):
    if len(result) == m:
        print(*result)
        return

    prev = -1
    
    for i in range(start, len(num)):
        if not visited[i] and num[i] != prev:
            visited[i] = True
            result.append(num[i])
            prev = num[i] 
            backtracking(i, result)
            result.pop()
            visited[i] = False

backtracking(0, [])