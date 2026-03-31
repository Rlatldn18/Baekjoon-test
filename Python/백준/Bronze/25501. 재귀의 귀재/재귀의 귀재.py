def recursion(s, left, right, cnt):
    cnt += 1
    if left >= right:
        return 1, cnt
    elif s[left] != s[right]:
        return 0, cnt
    else:
        return recursion(s, left+1, right-1, cnt)

def Palindrome(s):
    return recursion(s, 0, len(s)-1, cnt)


import sys
input = sys.stdin.readline
cnt = 0
t = int(input())

for i in range(t):
    pal = input().strip()
    print(*Palindrome(pal))