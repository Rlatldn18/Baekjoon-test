def append(stack, x):
    stack.append(x)
    
def pops(stack):
    if stack:
        print(stack.pop())
    else:
        print(-1)
        
def len_stack(stack):
    print(len(stack))

def empty(stack):
    if stack:
        print(0)
    else:
        print(1)

def upprint(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)
    
import sys
input = sys.stdin.readline

t = int(input())

stack = []

for _ in range(t):
    n = input().split()
    
    if n[0] == "1":
        append(stack, int(n[1]))
    elif n[0] == "2":
        pops(stack)
    elif n[0] == "3":
        len_stack(stack)
    elif n[0] == "4":
        empty(stack)
    elif n[0] == "5":
        upprint(stack)