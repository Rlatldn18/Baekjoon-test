"""
시간 제한 0.5 배열 다 돌면 시간 터질 듯
2**N X 2**N인 2차원 배열을 Z모양으로 탐색

     01 23
0    00|00
1    00|00
     =====
2    00|00
3    00|00  => 2 3 1이면  r = 3 c = 1 값 출력

사분면으로 나누고 지나간 만큼 더해주는 방식
2사분면에서 1사분면으로 이동할때 2**(2n-2) 만큼 더하기 
1 => 3 | 2 * 2**2n-2 ////  3 => 4 | 3 * 2**2n-2  

이후 (r, c)를 해당 사분면 기준으로 좌표를 줄이고,
같은 과정을 재귀적으로 반복
"""
import sys
input = sys.stdin.readline
n, r, c = map(int, input().split()) 

def zPattern(n, r, c):
    if n == 0:
        return 0    
    
    half = 2**(n-1)
    
    if r < half and c < half: # 왼쪽 위 2사분면
        return zPattern(n-1, r, c)
    
    elif r < half and c >= half: # 오른쪽 위 1시븐면
        return half * half + zPattern(n-1, r, c - half)

    elif r >= half and c < half: # 왼쪽 아래 3사분면
        return 2 * half * half + zPattern(n-1, r - half, c)
    
    else: # 오른쪽 아래 4사분면
        return 3 * half * half + zPattern(n-1, r - half, c - half)
    
print(zPattern(n, r, c))