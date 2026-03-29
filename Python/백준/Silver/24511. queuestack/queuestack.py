"""
0은 큐 1은 스택
0 1 1 0
1 2 3 4

2 4 7을 넣을꺼임

      q  s s q
초기값 1 2 3 4 에 2넣음
첫번째 2,1에서 그냥 pop=> 1나옴
두번째 2 1에서 pop=> 1나옴 후 삭제
세번째 3 1에서 pop => 1나옴 후 삭제 
네번째 1,4에서 pop => 4나옴 
따라서 2의 리턴 값 == 4

첫번째 원소 삽입 후 [2,2,3,1] 에 4넣음
첫번째 4,2 에서 pop=> 2나옴
두번째 2 2에서 pop=> 2나옴 후 삭제
세번째 3 2에서 pop => 2나옴 후 삭제 
네번째 2,1에서 pop => 1나옴
따라서 4의 리턴 값 == 1
두번째 원소 삽입 후 [4,2,3,2]
...
7의 리턴값 == 2
"""
def queeustack(t,case_1,case_2,case_3,case_4):
    dep = deque()
    result = []
    
    for i in range(t):  
        if case_1[i] == 0:
            dep.appendleft(case_2[i])
    
    for j in case_4:
        dep.append(j)
        result.append(dep.popleft())
        
    return print(*result)
    
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
case_1 = list(map(int, input().split())) # 0: 큐, 1: 스택
case_2 = list(map(int, input().split())) # 초기 값
case_3 = int(input())
case_4 = list(map(int, input().split())) # 넣을 값

queeustack(t,case_1,case_2,case_3,case_4)