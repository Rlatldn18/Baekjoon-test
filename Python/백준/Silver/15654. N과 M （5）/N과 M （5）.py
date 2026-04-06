"""
    N개의 자연수 중에서 M개를 고른 수열
    사전 순으로 증가하는 순서
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False] * n # 같은 숫자 중복 사용 방지

def backtracking(result):
    
    if len(result) == m:
        print(*result)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True # 사용한 것 
            result.append(num[i])
            backtracking(result)
            result.pop()       # 백트래킹
            visited[i] = False # 백트래킹
                
backtracking([])