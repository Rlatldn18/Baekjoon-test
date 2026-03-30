from itertools import combinations
import sys
input = sys.stdin.readline
li=[]
comb = []
n, k = map(int, input().split())

for i in range(1, n+1):
    li.append(i)

comb = list(combinations(li, k))
print(len(comb))