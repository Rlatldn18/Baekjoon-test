import sys
input = sys.stdin.readline

def cantor(n):
    if n == 1:
        return '-'
    
    cantor_div = cantor(n // 3)
    
    cantor_u = cantor_div + " "*(n // 3) + cantor_div
    return cantor_u
    
while True:
    try:
        n = int(input())
        print(cantor(3**n))
    except:
        break