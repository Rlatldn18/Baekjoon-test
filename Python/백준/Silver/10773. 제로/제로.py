"""
    숫자 입력 => 스택에 숫자 추가
    0입력 => 가장 최근에 받은 숫자 제거
    결과 =>  남은 숫자 합 
"""
    
import sys
input = sys.stdin.readline

stack = []
t = int(input())

for _ in range(t):
    num = int(input())
    
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))       