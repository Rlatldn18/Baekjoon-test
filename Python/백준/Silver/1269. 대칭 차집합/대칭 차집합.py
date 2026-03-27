import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nper = set(map(int, input().split()))
mper = set(map(int, input().split()))
print(len(nper ^ mper)) 