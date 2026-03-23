import sys
input = sys.stdin.readline
list1 = [] #약수 구할때 쓸 것
list2 = [] # n의 약수만 여기다가 저장

n, k = map(int, input().split())

for _ in range(1, n+1): # n일 때 1~n까지 저장
    list1.append(_)

for _ in range(len(list1)):
    if n % int(list1[_]) == 0:
        list2.append(n // int(list1[_]))
        
list2 = sorted(list2)

if k <= len(list2):
    print(list2[k-1])
else:
    print(0)