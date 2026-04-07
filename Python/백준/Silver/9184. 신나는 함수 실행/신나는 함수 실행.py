"""
    재귀 사용시 시간복잡도 : O(2**n 이상) 
    중복 호출 때문에 20들어가면 시간 초과 발생함
    
    dp 사용시 시간복잡도 : O(21**3) => O(1) 
    가능한 상태가 21*21*21으로 주어짐
    
    문제에서 a, b, c ≤ 20으로 제한되어 있어
    상수로 볼 수 있으므로 O(1)처럼 동작함 
"""
import sys
input = sys.stdin.readline
rept = True
#충분히 큰 값으로 a b c 3차원 배열 만들기
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    # 하나라도 0이면 1 반환 
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # a b c중 하나라도 20을 초과하면 20으로 통일
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    # 이미 계산한 값이면 반환 DP
    if dp[a][b][c]:
        return dp[a][b][c]
    # 조건 점화식
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else: 
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    # dp에 저장되있는 값 반환
    return dp[a][b][c]

while rept:
    a,b,c = map(int, input().split())
    
    if a == -1 and b == -1 and c == -1:
        rept = False
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")