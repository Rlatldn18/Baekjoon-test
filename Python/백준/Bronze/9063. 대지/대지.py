import sys
input = sys.stdin.readline
listx = []
listy = []

n = int(input())

for _ in range(n):
    x, y = list(map(int, input().split()))
    listx.append(x)
    listy.append(y)

w = max(listx) - min(listx)
h = max(listy) - min(listy)
print(w*h)