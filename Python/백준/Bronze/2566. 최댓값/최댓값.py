import sys

input = sys.stdin.readline

arr1 = [list(map(int, input().split())) for _ in range(9)]

max = -1
pos = 0, 0

for i in range(9):
    for j in range(9):
        if arr1[i][j] > max:
            max = arr1[i][j]
            pos = i+1,j+1

print(max)
print(*pos)