import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nper = set()
mper = set()

for _ in range(n):
    nper.add(input().strip())    
     
for _ in range(m):
    mper.add(input().strip())
    
result = list(sorted(nper & mper))

print(len(result))
for i in range(len(result)):
    print(result[i], sep="\n")