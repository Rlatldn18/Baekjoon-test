import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 기본: 1 빼기
    dp[i] = dp[i - 1] + 1

    # 2로 나눠질 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나눠질 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
