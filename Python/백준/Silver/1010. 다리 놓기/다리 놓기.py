"""
    조합 mCn 사용 
    파스칼 삼각형(dp)에 의하여 
    mCn = (m-1)C(n-1) + (m-1)Cn 
    ==> dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
"""
def brigedp (m,n):
    # 행(가로)는 n만큼 열(세로)은 m만큼 2차원 배열 만들기
    #파스칼 삼각형(dp) 쓰기 위함
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    #n이 0일때와 n m이 같을 때 무조건 1
    for i in range(m+1):
        dp[i][0] = 1
        if i <= n:
            dp[i][i] = 1
    
    #파스칼 삼각형(dp) 점화식을 이용해 값 도출하기
    for i in range(2, m+1):
        for j in range(1, min(i, n)+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[m][n] 
        
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(brigedp(m,n))