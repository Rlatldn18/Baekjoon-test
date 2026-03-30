import sys
input = sys.stdin.readline
t = int(input())
check = set()
cnt = 0

for i in range(t):
    gomgom = input().strip()

    if gomgom == "ENTER":
        check.clear()
    else:
        if gomgom not in check:
            check.add(gomgom)
            cnt += 1
print(cnt)