"""
1 2 3 4 5 6 7
3칸씩
1 2 3 4 5 6 7  
1 2 4 5 6 7 1 2
4 5 6 7 1 2
4 5 7 1 2 4 5
7 1 2 4 5
7 1 4 5 7 1
4 5 7 1
4 5 1 4 5
1 4 5
1 4 1 4
1 4 4
1 4 1 4
"""
def josephus(x, kill):
    result = []
    while x:
        for _ in range(kill-1):
            x.append(x.popleft())
        
        result.append(x.popleft())
    print("<" + ", ".join(map(str, result)) + ">")

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

num, kill = map(int, input().split())

for _ in range(1, num+1):
    queue.append(_)

josephus(queue, kill)