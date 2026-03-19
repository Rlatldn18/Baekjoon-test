import sys

t = int(sys.stdin.readline())
c=0
for i in range(t):
    c += 1
    a,b = map(int, sys.stdin.readline().split())
    print("Case #{}:".format(c), a+b)