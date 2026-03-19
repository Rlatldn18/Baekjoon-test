import sys
a1=[]
for  i in range(9):
    n = int(sys.stdin.readline())
    a1.append(n)

print(max(a1))
print(a1.index(max(a1))+1)