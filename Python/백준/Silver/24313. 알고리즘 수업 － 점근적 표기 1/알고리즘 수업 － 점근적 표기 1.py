x, y = map(int, input().split())
c = int(input())
o = int(input())

if (x*o+y) <= (c*o) and x <= c:
    print(1)
else:
    print(0)