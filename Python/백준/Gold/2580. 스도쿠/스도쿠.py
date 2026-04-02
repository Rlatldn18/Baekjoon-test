"""
    9*9크기의 정사각형 안에
        1. 스도쿠 가로 세로줄 1~9 중복 X
        2. 3*3크기의 정사각형 안에도 1~9 중복X
    
    과정
        1. 0,0부터 칸의 숫자가 0인지 확인 하여 따로 저장
        2. 리스트의 처음 0부터 1~9까지 넣음 
        3. 넣을 수 있으면 넣고 다음 칸 실행
        4. 반복하다 넣을 수 없으면 되돌리고 다시 확인
        5. empty의 리스트가 없어질 때까지 반복
        6. empty안에 0이 모두 없어지면 출력
        =========================================== 
    시간 초과
        is_possibleNum 함수를 너무 많이 호출 => 시간초과 뜸
        
    개선
        1. 가능 여부 함수를 제거 후 => O(1) 방식으로 확인      
         => visited 적용
        2. 숫자가 이미 존재하면 True 빈칸이면 False
        3. 0인 곳에 숫자가 들어가면 True
        4. 백트래킹중 안되면 다시 False 와 0으로 되돌리기
        5. 위 반복 후 empty리스트 안 인덱스 없으면 출력
        
        시간 복잡도: 최악: O(9**k) k는 빈칸의 개수        
        그러나 가지치기 떄문에 훨씬 빨라짐 
        
        visited 없으면 시간복잡도 => O(9**k*27)
        visited 있으면 시간복잡도 => O(3**k)
        가능 여부 호출X => 배열 접근으로 O(1)
"""
# 숫자가 행, 열, 3*3 중 같은 숫자가 있는지 체크 
# def is_possibleNum(row, col, num):
#     for i in range(9): #같은 행 체크
#         if sudoku[row][i] == num:
#             return False
        
#     for i in range(9): #같은 열 체크
#         if sudoku[i][col] == num:
#             return False
        
#     sudoku_row = (row // 3) * 3
#     sudoku_col = (col // 3) * 3
        
#     for i in range(sudoku_row,sudoku_row+3): #3*3 같은지 체크
#         for j in range(sudoku_col, sudoku_col+3):
#             if sudoku[i][j] == num:
#                 return False
#     return True

def backtrack(idx):
    #empty 리스트에 0이 모두 없어지면 종료
    if idx == len(empty):
        for rows in sudoku:
            print(*rows)
        sys.exit()
    
    r, c = empty[idx] #빈칸의 좌표 r c 저장
    b = (r // 3) * 3 + (c // 3) #현재 좌표가 속한 박스 번호 계산
    
    for num in range(1, 10):
        # 넣을 수 있는지 확인 => r행,c열,b박스에 num이 있는지 확인
        if not row[r][num] and not col[c][num] and not boxs[b][num]: 
            sudoku[r][c] = num #넣을 수 있으면 넣기
            row[r][num] = True  # r행에 num 사용 
            col[c][num] = True  # c열에 num 사용
            boxs[b][num] = True # b박스에 num 사용
            backtrack(idx+1) # 다음 0으로 이동 
            
            sudoku[r][c] = 0 #안되면 다시 0으로 되돌리기
            row[r][num] = False  # 사용 제거 
            col[c][num] = False
            boxs[b][num] = False
            
import sys
input = sys.stdin.readline

# 스도쿠 만들기
sudoku = [list(map(int, input().split())) for _ in range(9)]

row = [[False]*10 for _ in range(9)] #각 행에서 숫자 사용 여부 확인
col = [[False]*10 for _ in range(9)] #각 열에서 숫자 사용 여부 확인
boxs = [[False]*10 for _ in range(9)] #각 박스에서 숫자 사용 여부 확인

# 스도쿠의 빈 칸 리스트에 저장  
empty = []
for i in range(9):
    for j in range(9):
        num = sudoku[i][j] 
        if num == 0: #빈칸이면 empty에 넣음
            empty.append((i, j))
        else: #숫자가 이미 있으면 True 표시
            row[i][num] = True
            col[j][num] = True
            #해당 숫자가 속한 박스에 True 표시
            boxs[(i // 3) * 3 + (j // 3)][num] = True

# empty 첫번째 0부터 실핼  
backtrack(0)
