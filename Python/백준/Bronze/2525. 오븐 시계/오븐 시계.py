a,b = map(int, input().split())
c = int(input())

c_h=c//60 
c_m=c%60 

a += c_h
b += c_m

if b >= 60:
    a += b//60 
    b = b%60 
    if a >= 24:
        a -=24
        print(a,b)
    else:
        print(a,b)
else:
    if a>= 24:
        a -= 24
        print(a,b)
    else:
        print(a,b)