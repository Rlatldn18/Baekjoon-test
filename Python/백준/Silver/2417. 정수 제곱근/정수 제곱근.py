import sys
import math
input = sys.stdin.readline

num = int(input())
result = math.isqrt(num)

if result**2 != num:
    result += 1
print(result)