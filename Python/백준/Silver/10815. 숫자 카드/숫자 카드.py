import sys
input = sys.stdin.readline

t1 = int(input())
m1 = set(map(int, input().split()))

t2 = int(input())
m2 = list(map(int, input().split()))

for i in m2:
    if i in m1:
        print(1, end=" ")
    else:
        print(0, end=" ")