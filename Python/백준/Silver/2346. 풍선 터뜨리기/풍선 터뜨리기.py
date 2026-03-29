def balloon(t, kill):
     # (풍선 번호, 이동값) 형태로 deque 생성
    dq = deque((i+1, kill[i]) for i in range(t))
    result = [] # 터진 풍선 번호 저장
    
    while dq: #풍선 터뜨리기
        idx, move = dq.popleft()
        result.append(idx) 
        
        if not dq:
            break
        
        if move > 0:
            #양수일때 왼쪽으로 이동
            dq.rotate(-(move-1))
        else:
            # 음수는 오른쪽 이동
            dq.rotate(-move)
    return result
        
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

t = int(input())
arr = list(map(int, input().split()))
print(*balloon(t, arr))