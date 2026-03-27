import sys
from collections import Counter
input = sys.stdin.readline

t1 = int(input())
m1 = list(map(int, input().split()))

t2 = int(input())
m2 = list(map(int, input().split()))

count = Counter(m1)
for _ in m2:
    print(count[_], end=" ")