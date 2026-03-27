import sys
input = sys.stdin.readline
str1= []
str2= []
count=0
t1, t2= map(int, input().split())

for _ in range(t1):
    str1.append(input().rsplit())
for _ in range(t2):
    str2.append(input().rsplit())

for i in str2:
    if i in str1:
        count += 1
print(count)