import sys
input = sys.stdin.readline

avr = 0
mid = 0
num = []
for _ in range(5):
    n = int(input())
    num.append(n)

num.sort()
avr = sum(num) // 5 
print(avr)
print(num[2])