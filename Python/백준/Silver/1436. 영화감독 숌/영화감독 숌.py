'''
    6이 적어도 3번 들어가는 n번째 숫자 출력
    ex) n=2면 1666 n=4면 3666 n=11이면 6661 n=101이면 16661
    그러면 n이 늘어날 수록
    n의 첫번째 자리 + 666 + n의 두번째 자리부터 마지막 자리-1
'''

import sys
input = sys.stdin.readline
num = 0
cnt = 0

n = int(input())
while True:
    if cnt != n:
        num += 1
        if "666" in str(num):
            cnt += 1
    else:
        print(num)
        break