import sys
from collections import Counter
input = sys.stdin.readline

alplist = []
t, lens = map(int, input().split())

for i in range(t):
    alp = input().strip()
    if len(alp) >= lens:
        alplist.append(alp) 
    
a = Counter(alplist)
#많이 나온 단어 => 길이가 긴 단어 => 사전순
result = sorted(a.keys(), key=lambda x: (-a[x], -len(x), x))

for j in result:
    print(j)