import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

lst = [input().strip() for _ in range(n)]

visited = [False] * n
result_set = set() 

def backtracking(result):
    if len(result) == k:
        number = ''.join(result) # 문자열 합치기
        result_set.add(number) # 중복 제거
        return
    
    for i in range(n): # start 제거 (순열)
        if not visited[i]:
            visited[i] = True
            result.append(lst[i])
            backtracking(result)
            result.pop()
            visited[i] = False

backtracking([])

print(len(result_set))