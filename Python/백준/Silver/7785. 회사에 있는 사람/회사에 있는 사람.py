import sys
input = sys.stdin.readline

list1 = set()

t = int(input())

for _ in range(t):
    name, check = input().split()
    
    if check == "enter":
        list1.add(name)
    else:
        list1.remove(name)
        
result = sorted(list1, reverse=True)

for name in result:
    print(name)