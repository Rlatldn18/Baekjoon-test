import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

def Big_num (lst):
    result = ""
    
    lst_str  = [str(i) for i in lst] 
    #1000000000 이하여서 10 곱함 
    # ex) 3 30 => 3333333333, 3030303030303030303030 
    lst_str.sort(key=lambda c : c*10, reverse=True)
    result = str(int("".join(lst_str)))
    
    return result

print(Big_num(lst))