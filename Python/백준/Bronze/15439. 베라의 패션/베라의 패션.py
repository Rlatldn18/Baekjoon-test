"""
    상의2벌 하의2벌일때 서로 다른 색상 조합
    순서 없음 => 조합
    조합 => n(n-1)
"""
import sys
input = sys.stdin.readline
t = int(input())

print(t*(t-1))