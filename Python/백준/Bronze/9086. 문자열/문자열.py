import sys
t = int(sys.stdin.readline())

for _ in range(t):
    s = list(map(str, sys.stdin.readline()))
    print(s[0] + s[-2])