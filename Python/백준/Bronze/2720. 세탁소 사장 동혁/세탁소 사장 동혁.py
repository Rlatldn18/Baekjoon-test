import sys
input = sys.stdin.readline

t = int(input())

C_cnt = []

for _ in range(t):
    c = int(input())
    
    C_cnt.append(c // 25)
    c = c%25
    C_cnt.append(c // 10)
    c = c%10
    C_cnt.append(c // 5)
    c = c%5
    C_cnt.append(c // 1)
    c = c%1
    
    print(*C_cnt)
    C_cnt.clear()