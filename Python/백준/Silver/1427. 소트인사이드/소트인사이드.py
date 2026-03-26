import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))

n.sort()
print(*n[::-1], sep="")