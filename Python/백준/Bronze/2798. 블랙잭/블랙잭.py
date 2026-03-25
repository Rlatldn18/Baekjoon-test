"""
    첫째 줄에 카드의 개수 n
    n개의 수를 3개만 더했을 때 m보다 작은 경우의 수를
    출력 
"""
import sys
input = sys.stdin.readline 
n, m = map(int, input().split())
card_num = list(map(int, input().split()))

card_max= 0 
# n개의 카드중 3개만 고름 
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = card_num[i]+ card_num[j] + card_num[k]
            #조건 3개의 합이 m보다 작아야되는데 
            # 그중 가장 최대
            if sum <= m:
                card_max = max(card_max, sum)
print(card_max)