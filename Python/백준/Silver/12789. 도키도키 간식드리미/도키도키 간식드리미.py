"""
    ==========================
pop=> 1 2    |    | 5 4 1 3 2  <=num    
    ==========     ===========
              |   |
              | 3 | <= stack
              | 4 |
              | 5 |

num 스택에서 바로 나갈 수 있으면 pop으로 제거 
못나가면 stack에 저장
stack에서 바로 나갈 수 있으면 pop으로 제거 
만약 stack에 아무것도 없다 => Nice
stack에 숫자가 하나라도 존재해 => Sad
"""
def down_list(x):
    stack = []
    n = 1
    
    for num in x:
        #스택이 비어있지 않고 맨 처음이 나갈 차례면 pop
        while stack and stack[-1] == n:
            stack.pop()
            n += 1

        if num == n:
            n += 1         
        else:
            stack.append(num)
    while stack and stack[-1] == n:
        stack.pop()
        n += 1
    return "Nice" if not stack else "Sad"

import sys
input = sys.stdin.readline

t = int(input())

num = list(map(int, input().split()))
print(down_list(num))