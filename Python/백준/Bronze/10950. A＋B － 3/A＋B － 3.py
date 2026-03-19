t = int(input())
a1 = []
b1 = []
for  i in range(t):
    a, b = input().split()
    a1.append(a)
    b1.append(b)
     
for  i in range(t):
    print(int(a1[i]) + int(b1[i]))
