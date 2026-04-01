"""
    백트레킹 : 모든 경우 탐색 
               L> 답이 될 가능성이 없으면 중간에 되돌아감(버림) 
               

    순열 만들기 순서 O
    n과 m 
    n= (1 ~ n)까지의 숫자 // m = 묶을 개수
    
    백트레킹 과정 
        1. 1~n 까지 숫자중 numlist 안에 있는지 확인
        2. 없으면 값 추가 numlist 안에 인덱스가 m개가 되면 출력 후
        3. 오른쪽 인덱스 꺼내기 
        4. 모든 경우가 탐색될 때까지 위 반복
    
    시간 복잡도 : O(nPm) = 순열과 같음 
"""
def backtracking(numlist):
    #numlist안에 인덱스가 m개가 있을 경우 출력
    if len(numlist)==m:
        print(*numlist)
        return
    #모든 경우 탐색 
    for i in range(1, n+1): 
        if i not in numlist: #이미 사용한 숫자 제외(중복 제거)
            numlist.append(i) #선택
            backtracking(numlist) # 재귀
            numlist.pop() # 되돌리기 

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
backtracking([]) #빈 리스트 만들기 numlist = []