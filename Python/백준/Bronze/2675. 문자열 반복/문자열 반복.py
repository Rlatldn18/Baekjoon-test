t = int(input())

for _ in range(t):
    count,s = input().split()
    for x in range(len(s)):
        print(int(count)*s[x], end='')
    print()