"""
    LCS = 최장 공통 부분 수열
    순서 유지 
    1. 두 문자열을 동시에 어디까지 봤는지 확인해야함 => 2차원 배열 생성
    2. 공통으로 있는 부분 + 1 없으면 이전 값 중 큰 값 선택
    3. dp의 마지막 값 출력
    
          A C B D
        0 0 0 0 0
    A   0 1 1 1 1
    B   0 1 1 2 2
    C   0 1 2 2 2
    D   0 1 2 2 3
"""
import sys
input = sys.stdin.readline
str1 = list(input().rstrip())
str2 = list(input().rstrip())

dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,  len(str1)+1):
    for j in range(1,  len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[len(str1)][len(str2)])