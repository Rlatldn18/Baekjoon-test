import sys

input = sys.stdin.readline

li = [1, 2, 3, 4, 5, 6, 7, 8]

num = list(map(int,input().split()))

if li == num:
    print("ascending")
elif li == num[::-1]:
    print("descending") 
else:
    print("mixed")