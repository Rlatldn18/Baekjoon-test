import sys
input = sys.stdin.readline

n = int(input())

cb = [None]*n
vs = [False]*n
cnt = 0        

def check(x): # 놓을 수 
    # 퀸을 a개 둬야하는것
    for i in range(x):
        #같은 줄이거나 대선 줄에 있을 때는 안됨
        if cb[x] == cb[i] or abs(cb[x]-cb[i]) == abs(x-i):
            return False
        
    return True

def queenPlace(x):
    global cnt
    
    if x == n:
        cnt += 1
        return

    for i in range(n):
        if vs[i]:
            continue
        
        cb[x] = i
        
        if check(x):
            vs[i] = True
            queenPlace(x+1)
            vs[i] = False
            
queenPlace(0)       
print(cnt)