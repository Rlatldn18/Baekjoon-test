s = input()

alpha = "abcdefghijklmnopqrstuvwxyz"

for _ in alpha:
    if _ in s:
        print(s.index(_), end=" ")
    else:
        print(-1, end=" ")