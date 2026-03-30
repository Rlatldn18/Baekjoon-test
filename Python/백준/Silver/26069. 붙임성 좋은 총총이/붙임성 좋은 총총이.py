import sys
input = sys.stdin.readline
dance = set(["ChongChong"])
t = int(input())

for i in range(t):
    per = input().split()
    
    if per[0] in dance or per[1] in dance:
        dance.add(per[0])
        dance.add(per[1])

print(len(dance))