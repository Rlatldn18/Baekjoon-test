""" 
    5 5
    5 7
    7 5
    7 7
    평행한 직사각형을 만들기 위해선 무조건 같은 축에 있어야함
    == 같은 축에 같은 수가 2개 있어야한다
    조건으로 풀기에는 경우의 수가 너무 많음
    2차원 배열로 만들고 x y 값만 따로 모아서 
    같은 수가 2개 있는지 확인 1개 있는것만 모아서 출력 
"""
import sys
input = sys.stdin.readline
listx = []
listy = []

for i in range(3):
    x,y = list(map(int, input().split()))
    listx.append(x)
    listy.append(y)

for x in listx:
    if listx.count(x) == 1:
        result_x = x

for y in listy:
    if listy.count(y) == 1:
        result_y = y
print(result_x, result_y)