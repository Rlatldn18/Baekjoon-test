"""
    a+b+c = 180 and a = b = c   Equilateral
    a+b+c = 180 and 
    a == b or b == c or c == a Isosceles
    a+b+c = 180 and a != b != c Scalene
    a+b+c != ERROR
    
"""
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b == c:
        print("Equilateral")
    elif a==b or b==c or a==c :
        print("Isosceles")
    else:
        print("Scalene") 
else:
    print("Error")