"""
    길이가 a,b,c의 막대기가 있음
    길이는 맘대로 줄일 수 있음
    3개의 막대기로 삼각형을 만들 수 있어야한다
    가장 긴 변 < 나머지 두 변
    max_num < a+b
    삼각형의 둘레는 최대값으로
    무조건 둘레가 최대값이 되는 조건을 만족시키면 
    구할 수 있다?
      1+1  max_num < a+b 
      두개의 값이 같으면 다른 한 값도 무조건 같아야함
      나머지 두 변 더한거에서 -1
      57 
"""
import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
a = sorted(a) 

if a[2] < a[0] + a[1]:
    print(sum(a))
else:
    print((a[0]+a[1])*2-1)