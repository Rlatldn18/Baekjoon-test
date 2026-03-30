"""
    양수 A가 N의 진짜 약수 조건
    1. N이 A의 배수
    2. A가 1 그리고 N이 아니여야 함
    출력할 N은 진짜 약수이므로 위 조건 다 만족
    
    따라서 입력할 수는 
    1과 N을 제외한 가장 작은 A와 가장 큰 A를 곱한 것이 N
    ex) 16의 약수 1 2 4 8 16
    a = 2 4 8 N = 16
    
    입력 
    첫번째 줄 N의 약수의 개수 
    두번째 줄 약수가 주어짐 
    출력 => N
    
"""
import sys
input = sys.stdin.readline

t = int(input())

a = list(map(int, input().split()))
print(max(a)*min(a))
