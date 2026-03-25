'''
    입력은 a b c d e f를 받아야함

    연립일차방정식     
    ax + by = c
    dx + ey = f
    이때 x y의 해는 무조건 1개
    즉 기울기의 부호가 다름
    ae != db
'''
import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(f"{x} {y}")