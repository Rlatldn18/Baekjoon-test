"""
    ( 면 stack에 추가   
    ) 면 stack에 제거
    (가 안나왔는데 )가 나왔다=> NO
    스택이 비어있으면 YES
    스택에 하나라도 있으면 NO
"""
def vps_check(x):
    stack = []
    
    for i in x:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return "NO"
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    check = input().strip()
    print(vps_check(check))