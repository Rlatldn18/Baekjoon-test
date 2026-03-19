import sys
n = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(list1.count(v))