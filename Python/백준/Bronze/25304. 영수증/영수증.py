X = int(input())
N = int(input())
a1 = []
b1 = []
sum = 0
for  i in range(N):
    a, b = input().split()
    a1.append(a)
    b1.append(b)

for  i in range(N):
    sum += int(a1[i]) * int(b1[i])
    
if X == sum:
    print("Yes")
else:
    print("No")