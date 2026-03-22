import sys
input = sys.stdin.readline

arr = [input().strip() for _ in range(5)]
max_len = max(len(row) for row in arr)

for j in range(max_len):
    for i in range(5):
        if len(arr[i]) > j:
            print(arr[i][j].strip(), end="")
