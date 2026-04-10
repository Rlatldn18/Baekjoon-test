"""
    n: 물건 개수, k: 배낭 최대 무게
    w: 물건 무게, v: 물건 가치

    dp[j] = 무게 j까지 담았을 때 얻을 수 있는 최대 가치

    점화식
        dp[j-w] + v : 현재 물건을 넣는 경우
        dp[j]       : 현재 물건을 넣지 않는 경우
        둘 중 최댓값 선택
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)

for i in range(n):
    w, v = map(int, input().split())
    #같은 물건을 여러번 사용하는 것을 방지하기 위해 뒤에서부터 진행
    for j in range(k,w-1,-1):
        # 이전 상태 + 현재 넣을 가치, 물건 안 넣음
        dp[j] = max(dp[j-w] + v, dp[j])
print(dp[k])