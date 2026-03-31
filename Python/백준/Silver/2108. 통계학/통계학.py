import sys
from collections import Counter
input = sys.stdin.readline

numlist = []
t = int(input())

for i in range(t):
    num = int(input())
    numlist.append(num)
    
numlist.sort() 

print(round(sum(numlist)/t)) #산술평균
print(numlist[int(t//2)]) #중앙값

a = Counter(numlist).most_common() 

if t == 1: #최빈값
    print(num)
else:
    if a[0][1] == a[1][1]:
        print(a[1][0])
    else:
        print(a[0][0])
        
print(max(numlist)-min(numlist)) #범위