"""
    n은 3의 거듭제곱
    k는 n=3**k => k = log3(n) 
    크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)*(N/3) 
    정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
    => n=27이면 9*9크기의 정사각형을 크기 9의 패턴으로 둘러싼 형태
"""

def starPattern(n):
    if n == 1:
        return["*"]
    
    star = starPattern(n//3)
    result = []
    for ln in star:
        result.append(ln * 3)
    for ln in star:
        result.append(ln + " " * (n//3) + ln)
    for ln in star:
        result.append(ln * 3)
    return result
    
import sys
input = sys.stdin.readline

n = int(input().rstrip())
print('\n'.join(starPattern(n)))