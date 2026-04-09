import sys
input = sys.stdin.readline
n = int(input())

stair = [0] * (n+1)
for i in range(1, n+1):
  stair[i] = int(input())
  
if n == 1: 
    print(stair[i])
else:
    dp = [0] * (n+1)
    
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    
    for i in range(3, n+1):
        dp[i] = max(
            # 한칸 건너뛰고 오는 경우 ex)  1 => 3, 2 => 4,  3 => 5
            dp[i-2] + stair[i],
            #연속 2칸을 밟는 경우 ex) 0 => 2 => 3, 1 => 3 => 4
            #3칸 연속 밟는것은 안되므로 i-2는 건너 뜀 
            dp[i-3] + stair[i-1] + stair[i]
        )
    print(dp[n])