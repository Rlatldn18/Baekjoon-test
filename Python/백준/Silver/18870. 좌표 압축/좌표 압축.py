import sys
input = sys.stdin.readline
dic = {}

n = int(input())
x = list(map(int, input().split()))

sort_num = sorted(set(x))

for _ in range(len(sort_num)):
    dic[sort_num[_]] = _

for _ in x:
    print(dic[_], end=" ")