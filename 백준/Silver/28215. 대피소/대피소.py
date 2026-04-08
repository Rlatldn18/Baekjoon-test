"""
    n = 집 k = 대피소 || n은 최대 50 k는 최대 3 
    x,y = 집 좌표 위치 || 좌표 최대 100000 100000
    두 집사이의 거리 = |x1 - x2| + |y1 - y2| 
        1. 좌표 지정
        2. 대피소 집 정해주고 
        각 집의 거리 확인
        최대 갱신 최소 갱신   
        
"""
import sys
from itertools import combinations 
input = sys.stdin.readline
result = float("inf")
n, k = map(int, input().split())
house = [tuple(map(int, input().split())) for _ in range(n)]
for comb in combinations(house, k):
    worst = 0
    for x, y in house:
        best = min(abs(x - a) + abs(y - b) for a,b in comb) 
        worst = max(worst, best)
    result = min(result, worst)
print(result)