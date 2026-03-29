def card_re (x):
    while True:
        if len(x) != 1:
            x.popleft()
            x.append(x[0])
            x.popleft()
        else:
            print(x[0])
            break
        
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

num = int(input())

for _ in range(1,num+1):
    queue.append(_)
    
card_re(queue)