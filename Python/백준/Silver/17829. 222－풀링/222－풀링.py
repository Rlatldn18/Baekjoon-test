"""
    N이 주어짐 N*N크기의 정사각형을 2*2크기로 나눔
    2*2 상자 안에서의 두번째로 큰 값을 저장
    다시 N//2 크기의 정사각형을 만들어서 값을 넣음 
    
    과정
        1. n과 n*n정사각형 입력
        2. 2*2크기로 나눔
        3. 나눈 크기 2*2 크기 안에 2번째로 큰 값 찾아서 리스트에 저장
        4. 저장된 리스트를 다시 N//2 크기 상자안에 넣기 
        5. 위 반복하여 1이 되면 출력
        
    시간복잡도 : O(n**2)
    정렬하고 => 2번째 값 넣기?
"""
import sys
input = sys.stdin.readline

n = int(input())
boxs = [list(map(int, input().split())) for _ in range(n)]

def pooling (x, y):
    # 2*2 빈박스에 값 넣기  
    nums = [
        boxs[x][y],
        boxs[x][y+1],
        boxs[x+1][y],
        boxs[x+1][y+1],
    ]
    # 오름차순 정렬 후 2번째로 큰 값 리턴
    nums.sort()
    return nums[2]
    
def division(x, y, size):
    # 박스의 크기가 2*2이면 pooling 실행
    if size == 2:
        return pooling(x, y)
    
    half = size // 2 #4등분 
    # 4등분을 반복 이때 박스크기가 2*2면 if문 실행
    results = [
        division(x, y, half), 
        division(x, y+half, half),
        division(x+half, y, half),
        division(x+half, y+half, half)
    ]
    # 오름차순 정렬 후 2번째로 큰 값 리턴
    results.sort()
    return results[2]
# 전체 배열 분할 하여 값 출력
print(division(0,0, n))