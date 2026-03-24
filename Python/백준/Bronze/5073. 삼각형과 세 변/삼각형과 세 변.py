import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    max_num = max(a,b,c)
    
    if a != 0 or a != 0 or a != 0:  
        if max_num >= a+b:
            print("Invalid")
            
        else:   
            if a == b == c:
                print("Equilateral")
            elif a==b or a==c or b==c :
                print("Isosceles")
            elif a != b != c:
                print("Scalene")
    else:
        break