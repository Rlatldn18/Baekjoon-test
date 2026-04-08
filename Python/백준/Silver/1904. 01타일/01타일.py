"""
    0, 1타일에서 00, 1 타일로 바뀐 2진 수열 만들기
    n=1 1
    n=2 2
    n=3 3 
    n=5 5
    n=6 8 => 피보나치 수열과 같음
"""
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
dp[1] = 1

if n >= 2:
    dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
print(dp[n])
