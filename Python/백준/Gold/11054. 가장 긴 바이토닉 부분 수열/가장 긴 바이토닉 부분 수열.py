import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

dp_up = [1]*n
# 증가하는 배열
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)
#감소하는 배열 
dp_down = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if lst[i] > lst[j]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)
#증가 + 감소 - 1 
result = 0
for i in range(n):
    result = max(result, dp_up[i] + dp_down[i] - 1)

print(result)