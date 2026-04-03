"""
    w h == 가로 세로 2차원 배열
    block == 쌓인 높이
    두포인터로 왼쪽 오른쪽 나눔
    왼쪽 블럭이 더 낮으면 물 높이는 왼쪽 기준으로 결정
    오른쪽 블럭이 더 낮으면 물 높이는 오른쪽 기준으로 결정
    왼쪽에서 가장 높은 블럭 - 현재 블럭 == 고인 물 양
    이때 현재블럭이 더 크면 높은 블럭 갱신 => 이땐 물 안 고임
    오른쪽 동일
"""
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
        
left = 0
right = w-1
max_left = 0 # 왼쪽에서의 최대 높이
max_right = 0 # 오른쪽에서의 최대 높이
water = 0 # 총 고인 물의 양

while left < right: 
    #왼쪽이 더 낮을 때 => 왼쪽 기준으로 결정
    if blocks[left] < blocks[right]:
        #현재 왼쪽 블럭이 왼쪽에서의 최대 높이보다 크면 => 빗물 안고임
        if blocks[left] >= max_left:
            #왼쪽에서의 최대 높이 갱신 
            max_left = blocks[left]
        else:
            #최대 높이가 아니면 물 고임으로 물의 양 추가
            #최대 높이 - 현재 높이 = 고인 물의 양
            water += max_left - blocks[left]
        #오른쪽으로 한칸 이동 
        left += 1
    else:
        #위와 같은 방법으로 오른쪽에서 왼쪽으로 
        if blocks[right] >= max_right:
            max_right = blocks[right]
        else:
            water += max_right - blocks[right]
        right -= 1 
        
print(water)