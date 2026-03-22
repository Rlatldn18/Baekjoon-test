import sys
input = sys.stdin.readline

n,b = map(int, input().split())

dic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
    
while n > 0:
    result = dic[n%b] + result
    n //= b
        
print(result)