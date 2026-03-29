def leftappend(queue, b):
    queue.appendleft(b)
    
def rightappend(queue, b):
    queue.append(b)
        
def leftpop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()
    
def rightpop(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
        queue.pop()
        
def lenqueue(queue):
    print(len(queue))
        
def empty(queue):
   if len(queue) == 0:
       print(1)
   else:
       print(0)

def leftprint(queue):
   if len(queue) == 0:
       print(-1)
   else:
       print(queue[0])

def rightprint(queue):
   if len(queue) == 0:
       print(-1)
   else:
       print(queue[-1])

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

t = int(input())

for _ in range(t):
    x = input().split()
    if x[0] == "1":
        leftappend(queue, x[1])
        
    if x[0] == "2":
        rightappend(queue, x[1])
        
    if x[0] == "3":
        leftpop(queue)
        
    if x[0] == "4":
        rightpop(queue)
        
    if x[0] == "5":
        lenqueue(queue)
        
    if x[0] == "6":
        empty(queue)
        
    if x[0] == "7":
        leftprint(queue)
        
    if x[0] == "8":
        rightprint(queue)