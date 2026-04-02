"""
    순서X => 조합
    종료조건 : 전 값과 현재값에 숫자가 더 작은 값 갱신
    
    과정
        1. 사람 선택하여 팀1 완성하면 팀2에 나머지 다 넣음 
            L>이때 team1이 완성 될 때까지 재귀로 사람 뽑음 
        2. 팀1,팀2의 능력치의 합 구함   
        3. 팀간 능력치 차이를 구함
        4. 이전 능력치 차이와 현재 능력치 차이 확인하여 작은값 갱신 
        5. 추가했던 사람 제거
        6. 위 내용 반복하여 팀 능력치 차이의 최소를 구함
    
    시간 복잡도 : O(nCn/2)
"""

import sys
input = sys.stdin.readline

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

min_value = 1000000000

def teammatch(start, team1):
    global min_value
    
    if len(team1) == n//2:
        #팀1에 선택되지 않은 사람 모두 팀2에 넣기
        team2 = [i for i in range(n) if i not in team1]
        
        team1sum = 0
        team2sum = 0
        
        #팀1 능력치 계산
        for i in range(len(team1)):
            for j in range(i+1, len(team1)):
                a,b = team1[i], team1[j]
                team1sum += stat[a][b] + stat[b][a]
        #팀2 능력치 계산 
        for i in range(len(team2)):
            for j in range(i+1, len(team2)):
                a,b = team2[i], team2[j]
                team2sum += stat[a][b] + stat[b][a]

        min_value = min(min_value, abs(team1sum-team2sum))
        return
    # team1에 n//2명이 될 때까지 재귀
    for i in range(start, n):
        team1.append(i)
        teammatch(i+1, team1)
        team1.pop()

teammatch(0, [])
print(int(min_value))