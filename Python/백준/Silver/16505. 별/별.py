"""
    **
    *  => 이 반복됨 만약 4*4 크기이면 2*2 크기로 분할 후
          왼쪽 위 오른쪽 위 왼쪽 아래에 * 찍으면 됨
            
    시간복잡도 : O(4**n) => (2**n-1)*(2**n-1)
"""
import sys
input = sys.stdin.readline

num = int(input()) 

def starpattern(n):
    if n == 0:
        return ["*"]
    
    # 이전 단계의 별 패턴을 가져옴
    prev = starpattern(n-1)
    size = 2**n
    half = 2**(n-1)
    star = [[' ']*size for _ in range(size)]
    
    for i in range(half):
        for j in range(half):
            char = prev[i][j]
            # 왼쪽 위에 별 찍기 
            star[i][j] = char
            # 오른쪽 위에 별 찍기 
            star[i][j + half] = char
            # 왼쪽 아래에 별 찍기
            star[i + half][j] = char

    return ["".join(row) for row in star]

result = starpattern(num)
print("\n".join([row.rstrip() for row in result]))