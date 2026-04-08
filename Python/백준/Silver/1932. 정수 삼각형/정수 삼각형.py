"""
    위에서 부터 아래로 내려오면서 누적합 저장 
    
    삼각형에서 다음 값을 전값이랑 더한 걸 dp에 저장
    이때 왼쪽 오른쪽 max 비교 해서 큰 값을 갱신  
    마지막 줄 오면 마지막 리스트 안 max값 출력
    
    시간,공간 복잡도 : O(n**2)
"""
import sys
input = sys.stdin.readline
n = int(input())

dp = [list(map(int, input().split())) for _ in range(n)]    

for i in range(1, n):
    for j in range(i + 1): 
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
# print(dp)
print(max(dp[n-1]))