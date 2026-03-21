n = int(input())

for i in range(1 , n*2):
    if n > i:
        print(" "*(n-i)+ "*"*(i*2-1))

    elif n == i:
        print("*"*(n*2-1))
    
    elif n < i:
        print(" "*(i-n)+ "*"*((2*n-i)*2-1))