import sys
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == -1: # -1입력시 종료 
        break
    list1=[]
    
    for i in range(1,n): #약수 찾기
        if n%i ==0:
            list1.append(i) # 약수면 리스트에 추가 이때 n은 안 넣음 
    
    # 약수의 합이 n과 같으면 완전수
    if sum(list1) == n: #완전수일때
        print(f"{n} =", end=" ")
        
        # 약수 출력
        for i in range(len(list1)): 
            if i == len(list1)-1: #약수의 마지막일 때 6(1 2 3 중 3)
                print(list1[i])
            else: #약수의 마지막이 아닐 때 6의(1 2 3중 1 2)
                print(list1[i], "+", end=" ")     
    else: 
        #완전수 X
        print(f"{n} is NOT perfect.")