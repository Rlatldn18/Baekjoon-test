import sys
input = sys.stdin.readline

num = int(input()) 

grid = [[" "] * (num*2-1) for _ in range(num)]

def starpattern(n, start_i, start_j):
    if n == 3:
        grid[start_i][start_j] = "*"
        grid[start_i+1][start_j-1] = "*"
        grid[start_i+1][start_j+1] = "*"
        for k in range(-2, 3):
            grid[start_i+2][start_j+k] = "*"
        return

    half = n // 2
    starpattern(half, start_i, start_j)
    starpattern(half, start_i + half, start_j - half)
    starpattern(half, start_i + half, start_j + half)
    return

starpattern(num, 0, num-1)

for row in grid:
    print("".join(row))
