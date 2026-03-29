import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

def push(queue, b):
    queue.append(b)
    
def pop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()
        
def size(queue):
    print(len(queue))
    
def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)
        
def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        
def back(queue):
   if len(queue) == 0:
       print(-1)
   else:
       print(queue[-1])

t = int(input())

for _ in range(t):
    x = input().split()
    if x[0] == "push":
        push(queue, x[1])
        
    if x[0] == "pop":
        pop(queue)
        
    if x[0] == "size":
        size(queue)
        
    if x[0] == "empty":
        empty(queue)
        
    if x[0] == "front":
        front(queue)
        
    if x[0] == "back":
        back(queue)