"""
m n 각각 숫자를 입력 받음 이때 m < n
m n 사이 숫자 중 소수의 합과 소수 중 최솟값을 출력

m n 사이에 소수를 찾아 다 리스트에 정리

리스트 모두 더함
가장 왼쪽에 있는게 최소
이때 m n 사이에 소수가 없으면 -1 출력
range(m, n) 써야될 것 같음
"""
import sys
input = sys.stdin.readline
PrimeNum = []

m = int(input())
n = int(input())

for i in range(m, n+1):
    if i > 1:
        cnt = 0
        for j in range(2, i):
            if  i%j == 0:
                cnt += 1
                break
        if cnt == 0:
            PrimeNum.append(i)

if len(PrimeNum) == 0:
    print(-1)
    
else:
    print(sum(PrimeNum))
    print(PrimeNum[0])