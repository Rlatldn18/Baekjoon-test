"""
    3번 먼저 사면 손해인 경우
    중간이 크면 3번으로 살 때 손해임
    이땐 2번으로 중간 처리
"""
import sys
input = sys.stdin.readline

factory = int(input())
rmvalues = list(map(int, input().split()))
rmvalues += [0, 0] # 범위 초과 방지 
 
cost = 0

for i in range(factory):
    
    # 다음 공장이 다다음 공장보다 많으면 
    # 3묶음 손해 2묶음 먼저 처리
    if rmvalues[i+1] > rmvalues[i+2]:
        # i 와 i+1에서 2개 묶음으로 살 수 있는 최대 개수 
        # 이때 i+1를 i+2와 맞춰줘야함 
        t = min(rmvalues[i], rmvalues[i+1] - rmvalues[i+2])
        # 구매
        rmvalues[i] -= t
        rmvalues[i+1] -= t
        cost += 5 * t
    
    # 3묶음으로 구매 할 수 있는 최대 개수
    t = min(rmvalues[i], rmvalues[i+1], rmvalues[i+2])
    rmvalues[i] -= t; rmvalues[i+1] -= t; rmvalues[i+2] -= t
    cost += 7 * t

    #남은 것 중 2묶음으로 구매 할 수 있는 개수
    t = min(rmvalues[i], rmvalues[i+1])
    rmvalues[i] -= t; rmvalues[i+1] -= t
    cost += 5 * t
    
    # 남은 쩌리들 구매 
    cost += 3 * rmvalues[i]

print(cost)