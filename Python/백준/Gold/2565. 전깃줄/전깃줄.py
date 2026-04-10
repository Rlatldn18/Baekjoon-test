import sys
input = sys.stdin.readline
n = int(input())

elct = []
elect_end = []
for i in range(n):
    line = list(map(int, input().split()))
    elct.append(line)
elct.sort()

dp = [1] * n

for i in range(n):
    for j in range(i):
        if elct[j][1] < elct[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))