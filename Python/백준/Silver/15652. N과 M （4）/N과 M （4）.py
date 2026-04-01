"""
    N과 M (1)에서 중복 허용 + 비오름차순 정렬
    => 조합 (순서 X) + 중복 허용   

    백트레킹 과정 
        1. 1~n 까지 숫자중 numlist 안에 있는지 확인
        2. 숫자 선택 이후 m조건이 안 맞으면 반복 (중복 허용)
        3. m조건에 맞으면 출력 이후 리스트 뒤 숫자 제거
        4. 조합 성립 + 중복 허용 // 비오름차순 유지
        5. 모든 경우가 탐색 될 때 까지 위 반복
    
    시간 복잡도 : O(n**m) => n개씩 m번 선택 
"""
def backtracking(start, numlist):
    #numlist안에 인덱스가 m개가 있을 경우 출력
    if len(numlist)==m:
        print(*numlist)
        return
        
    #모든 경우 탐색 // 조합 => 오름차순 자동 정렬
    for i in range(start, n+1): 
        #N과 M (1)에서 중복 조건 제거 => 중복 허용됨 
        numlist.append(i) #선택
        # 현재 선택한 값보다 작은 값 제외
        #n=5 : 1,2,3,4,5 => 2,3,4,5 => 3,4,5 => 4,5 (중복 가능)
        backtracking(i, numlist) 
        numlist.pop() # 되돌리기 

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
backtracking(1, []) #1부터 시작하여 n까지 // 빈 리스트 생성