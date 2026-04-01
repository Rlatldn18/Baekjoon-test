"""
    N과 M (1)에서 중복 허용
    => 순열 (순서 O) + 중복 허용   

    백트레킹 과정 
        1. 1~n 까지 숫자중 numlist 안에 있는지 확인
        2. 숫자 선택 이후 m조건이 안 맞으면 반복 (중복 허용)
        3. m조건에 맞으면 출력 이후 리스트 뒤 숫자 제거
        4. 모든 경우가 탐색 될 때 까지 위 반복
    
    시간 복잡도 : O(n**m) => n개씩 m번 선택 
"""
def backtracking(numlist):
    #numlist안에 인덱스가 m개가 있을 경우 출력
    if len(numlist)==m:
            print(*numlist)
            return
        
    #모든 경우 탐색
    for i in range(1, n+1): 
        #N과 M (1)에서 중복 조건 제거 => 중복 허용됨 
        numlist.append(i) #선택
        backtracking(numlist) # 재귀
        numlist.pop() # 되돌리기 

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
backtracking([]) # 빈 리스트 생성 numlist = []
