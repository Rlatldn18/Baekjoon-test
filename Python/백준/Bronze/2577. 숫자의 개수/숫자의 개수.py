import sys
from collections import Counter
input = sys.stdin.readline

num1 = int(input())
num2 = int(input())
num3 = int(input())

muti = str(num1*num2*num3)
result = Counter(muti) 
for i in range(10):
    print(result[str(i)])