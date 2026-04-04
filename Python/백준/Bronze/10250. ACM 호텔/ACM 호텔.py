import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    H, W, N = map(int, input().split())

    floor = N % H if N % H != 0 else H
    room = N // H + (1 if N % H != 0 else 0)

    print(f"{floor}{room:02d}")