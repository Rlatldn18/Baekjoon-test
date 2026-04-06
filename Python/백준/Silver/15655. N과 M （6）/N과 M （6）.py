import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

def backtracking (start, result):
    
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n):
        result.append(num[i])
        backtracking(i+1, result)
        result.pop()

                
backtracking(0, [])