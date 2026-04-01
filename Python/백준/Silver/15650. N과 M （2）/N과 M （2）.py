"""
    N과 M (1)에서 오름차순 정렬 추가
    => 조합 (순서 X)   

    백트레킹 과정 
        1. 1~n 까지 숫자중 numlist 안에 있는지 확인
        2. 숫자 선택 이후 m조건이 안 맞으면 반복
        3. m조건에 맞으면 출력 이후 리스트 뒤 숫자 제거
        4. numlist[0]의 숫자가 오를 수록
           start에 1더해줌으로서 조합 성립 // 오름차순 유지
        5. 모든 경우가 탐색 될 때 까지 위 반복
    
    시간 복잡도 : O(nCm) = 조합과 같음 
"""
def backtracking(start, numlist):
    #numlist안에 인덱스가 m개가 있을 경우 출력
    if len(numlist)==m:
            print(*numlist)
            return
        
    #모든 경우 탐색 start부터 시작 => 오름차순 유지
    for i in range(start, n+1): 
        numlist.append(i) #선택
        #조합에서 1,2 == 2,1 // 시작부분 +1해서 중복 방지
        #1,2,3,4,5 => 2,3,4,5 => 3,4,5 => 4,5 재귀
        backtracking(i+1, numlist)   
        numlist.pop() # 되돌리기 

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
backtracking(1, []) #1부터 시작하여 n까지 // 빈 리스트 생성
