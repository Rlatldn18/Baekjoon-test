"""
    ( or [ 면 stack에 추가   
    ) or ] 면 stack에 제거
    이때 스택의 맨 위에 (인데 ]가 나오면 no 
    스택의 맨 위에 [인데 )가 나오면 no
    
    (가 안나왔는데 )가 나왔다=> no
    [가 안나왔는데 ]가 나왔다=> no
    
    입력에 () [] 둘 다 없어도 yes ex) Help 입력 => yes
    "."이 나오면 그만 나오기 전까진 계속 // " ."은 yes로 나와야됨 
"""
def vps_check(x):
    stack = []
    
    for i in x:
        if i == "(" or i == "[":
            stack.append(i)
            
        elif i == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
        
        elif i == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
            
    if not stack:
        return "yes"
    else:
        return "no"

import sys
input = sys.stdin.readline


while True:
    check = input().rstrip()
    
    if check == ".":
        break
    
    print(vps_check(check))