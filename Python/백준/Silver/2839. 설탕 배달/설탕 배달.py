'''
    설탕 n킬로그램이 있음
    각각 3kg 5kg를 담을 수 있는 봉투가 존재 
    n킬로그램을 전부 담아야함 못담으면 -1
    담을때 더 적게 봉투를 써야함 
    
    설탕 n킬로그램을 3 5kg로 나눌 때 가장 작은 봉투의 개수 출력
'''

import sys
input = sys.stdin.readline
cnt = 0

n = int(input())

while n >= 0:
    
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1
    
else:
    print(-1)