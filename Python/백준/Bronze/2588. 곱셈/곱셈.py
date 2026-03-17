a = int(input())
b = input()
a4 = a * int(b)

for i in range(2, -1, -1): 
    a1 = a * int(b[i])
    print(a1, sep="\n")

print (a4)