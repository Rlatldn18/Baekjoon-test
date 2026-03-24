"""
    2부터 ~ 무한으로 커지는 수 만큼 나누는데
    몫이 0이 아니면 다음 수로 가고 다시 반복
    나눌 때 마다 I 출력
"""

import sys
input = sys.stdin.readline

n = int(input())
list1 = []
if n == 1:
    pass
else:
    i=2
    while i <= n:
        while n % i ==0:
            print(i)
            n//= i
        i += 1