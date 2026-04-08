"""
    거리는 선분으로 나타냄
    1번 부터 n번까지 순서대로 있음
    빨강 초록 파랑 중 하나의 색으로 칠해야함
    조건
        1 : 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
        2 : N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
        3 : i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, 
            i+1번 집의 색과 같지 않아야 한다.
    이때 모든 집을 칠하는 비용의 최솟값 출력
    
    1. 초기값 r,g,b의 처음 비용
    2. 두번째 집 부터 이전 집에서 같은 색 제외 
                  다른 색 2개 중 최소 + 현재 비용을 저장
    3. 마지막 3개의 비용 중 최솟값 출력  
"""
import sys
input = sys.stdin.readline
n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]

r,g,b = 0,1,2
dp = [[0] * 3 for _ in range(n)]
dp[0] = [house[0][r], house[0][g], house[0][b]]

for i in range(1, n):
    dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + house[i][r]
    dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + house[i][g]
    dp[i][b] = min(dp[i-1][g], dp[i-1][r]) + house[i][b]

print(min(dp[n-1]))
