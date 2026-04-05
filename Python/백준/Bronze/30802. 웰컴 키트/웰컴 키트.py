import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

tshirt = sum((i + t - 1) // t for i in size)

print(tshirt)
print(n // p, n % p)