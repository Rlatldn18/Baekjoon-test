"""
    앞에 온 연사자부터 차례대로 계산
    
    과정
        1. 연산자가 차례대로 + -  * // 의 사용 개수가 주어짐
        2. 연산자 리스트에서 0이 아니면 연산
        3. 0이면 다음으로
        4. 연산자리스트 안 모든 숫자가 사용되면 이전 최대 최소와 현재 값 비교
        5. 재귀가 끝났으면 연산자 복구(백트래킹)
        6. 위 내용을 반복
            L>전 값보다 현재 값이 더 높으면 현재 값 갱신
            L>전 값이 현재 값보다 더 높으면 전 값 유지
            => 최소도 동일
    
    시간 복잡도 : O(4**n)
"""

import sys
input = sys.stdin.readline

#num의 개수 
nCnt = int(input())
# nCnt로 이루어진 수열안 숫자 입력
num = list(map(int, input().split()))
#연산자 개수 입력 : 왼쪽부터 + - * //  
oper = list(map(int, input().split()))

# 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 
# 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 문제에 주어짐
max_value = -1000000000
min_value = 1000000000

def operator(idx, value): #
    global max_value, min_value
    
    if idx == nCnt:
        # max이면 스탑
        max_value = max(max_value, value)
        # min이면 스탑
        min_value = min(min_value, value)
        return

    # oper에서 숫자가 있으면 연산자 실행하고 -1, 0이면 다음
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
        
            if i == 0: # +
                operator(idx+1, value+num[idx])
            
            elif i == 1: # -
                operator(idx+1, value-num[idx])
            
            elif i == 2: # *
                operator(idx+1, value*num[idx])
                
            elif i == 3: # //
                if value < 0:
                    operator(idx+1, -(-value//num[idx]))
                else:
                    operator(idx+1, value//num[idx])

            oper[i] += 1 # 연산자 되돌리기

operator(1, num[0])
print(max_value)
print(min_value)