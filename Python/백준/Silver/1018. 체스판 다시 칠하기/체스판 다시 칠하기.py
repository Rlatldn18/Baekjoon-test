'''
    M N의 2차원 배열
    W B가 교차되거나 동일하게 나옴 ex) WBWBWBWWWBBB
    N M의 사각형 안에 8 8의 정사각형을 넣을 때
    다시 칠해야 하는 최소 개수를 구해야함

    구조
    체스판의 최대 크기 == 64칸
    8 8 체스판을 왼쪽 위(1,1)에서부터 (N M)까지 반복 
    1,1 1,2 1,3 ...
    2,1 2,2 2,2 ...
    
    반복할 때 마다 8 8박스안에서 바꿔야되는 경우를 구함
    1,1 부터 8,8 까지 반복 
    B 교체 횟수 저장
    W 교체 횟수 저장
    
    짝수칸 일 때
        시작이 W 이면 B를 W로 바꿈 바꾸면 B를 +1씩 더해줌 = 칠하는 것
        시작이 B 이면 W를 B로 바꿈 바꾸면 W를 +1씩 더해줌 = 칠하는 것
    홀수칸 일 때 짝수랑 반대 색 배치 해줘야함
        시작이 W 이면 B를 W로 바꿈 바꾸면 W를 +1씩 더해줌 == 칠하는 것
        시작이 B 이면 W를 B로 바꿈 바꾸면 B를 +1씩 더해줌 == 칠하는 것
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

cb = [input().strip() for _ in range(n)]
# print(cb)
cb_max = 64

for i in range(n-7):
    for j in range(m-7): #왼쪽부터 8 8이되는 경우 다 세보기
        w_s = 0 # 흰색 시작할 때 다시 칠해야 되는 개수
        b_s = 0 # 검은색 시작할 때 다시 칠해야 되는 개수
        
        for q in range(8):
            for k in range(8):
                if (q+k)%2 == 0: #체스판이 짝수 칸일 때
                    if cb[q+i][k+j] != "W":
                        w_s += 1
                    if cb[q+i][k+j] != "B":
                        b_s += 1
                else: #홀수 칸일 때
                    if cb[q+i][k+j] != "B":
                        w_s += 1
                    if cb[q+i][k+j] != "W":
                        b_s += 1
        cb_max = min(cb_max, w_s, b_s)
print(cb_max)