"""
    규칙 : n이 주어지면 4*n-3 크기의 정사각형이 들어감
    n=3이면 9 9 크기 안에 5 5크기 안에 1 
    안에 들어간다 할때 어디부터? => 2,2 좌표부터 
    기저조건 => n=1이면 별 찍기
    
    과정
        1. n입력 받기
        2. 4 * n - 3 크기의 리스트 만들기
        3. 테두리에 별찍기 
        4. 재귀하여 안 패턴 찍어야함
        5. 이때 별이 시작하는 부분이 2,2 좌표
        6. 위 반복 이때 n=1일때 별 찍고 출력
        
    시간복잡도 : O(n**2)
"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())

def starPattern(n):
    if n == 1:
        return ["*"]
    
    size = 4 * n - 3
    #size 크기의 빈 2차원 리스트 만듦
    result = [[' ' for _ in range(size)] for _ in range(size)]
    # 테두리만 * 찍기
    for i in range(size):
        for j in range(size):
            #순서대로 맨 위 줄 or 맨 아래 줄 or 맨 완쪽 줄 or 맨 오른쪽 줄
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                result[i][j] = "*"
    #테두리 안쪽 구현하기 위해 재귀
    inner = starPattern(n-1)
    
    #안쪽은 2,2 부터 inner 패턴 재귀
    for i in range(len(inner)):
        for j in range(len(inner)):
            result[i+2][j+2] = inner[i][j]
        
    #리스트를 문자열로 변환하여 출력              
    return ["".join(row) for row in result]
    
print("\n".join(starPattern(n)))