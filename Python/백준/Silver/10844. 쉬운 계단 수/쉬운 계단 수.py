"""
    2차원배열로 풀어야할듯
     행 => 1~9까지
     열 자리수 
     현재 길이에서 마지막 숫자에 따라 계단 수가 되는 수의 개수 갱신
     이떄 계단 수가 가능한 수의 개수 입력 => n=4이면 3번쨰 행의 모든 값의 합 => 답 
"""
import sys
input = sys.stdin.readline
n = int(input())

dp = [[0] * 10 for _ in range(n)]

# 초기값
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n-1]) % (10 ** 9))