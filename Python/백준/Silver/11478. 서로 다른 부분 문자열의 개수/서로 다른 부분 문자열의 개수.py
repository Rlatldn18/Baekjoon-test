import sys
input = sys.stdin.readline

result = set()
n = input().strip()

for i in range(len(n)):
    for j in range(i, len(n)):
        result.add(n[i:j+1])

print(len(result))