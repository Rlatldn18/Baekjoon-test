"""
    가로 4*n -3 세로 4*n-1 크기의 빈 리스트 만들기
    맨 위쪽       오른쪽=> 왼쪽     4n-4 만큼
    맨 왼쪽 벽    위    => 아래     4n-2 만큼
    맨 아래       왼쪽  => 오른쪽   4n-4 만큼
    맨 오른쪽 벽  이래   => 위      4n-4 만큼
"""
import sys
input = sys.stdin.readline
num = int(input().rstrip())
result = [[' '] * (4*num -3) for _ in range(4*num-1)]

def starPattern(n,x,y):
    if n == 1:
        result[x][y]="*"
        result[x+1][y]="*"
        result[x+2][y]="*"
        return
    
    #맨 위 오 => 왼
    for _ in range(4*n-4):
        result[x][y] = "*"
        y -= 1
    #맨 왼쪽 위 => 이래
    for _ in range(4*n-2):
        result[x][y] = "*"
        x += 1
    #맨 아래 왼 => 오
    for _ in range(4*n-4):
        result[x][y] = "*"
        y += 1
    #맨 오른쪽 아래 => 위
    for _ in range(4*n-4):
        result[x][y] = "*"
        x -= 1
    #이어주기
    result[x][y]="*"
    result[x][y-1]="*"
    starPattern(n-1, x, y-2)
    
    
    return ["".join(rows).rstrip() for rows in result]
    
if num == 1:
    print("*")
else:
    print("\n".join(starPattern(num,0,4*num-4)))