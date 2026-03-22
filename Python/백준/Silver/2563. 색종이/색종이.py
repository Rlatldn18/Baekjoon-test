import sys
input = sys.stdin.readline

# 100*100 크기의 도화지 생성 한칸에 0
paper = [[0]*100 for _ in range(100)]

#색종이 개수
n = int(input())

# n개의 좌표 설정 :: 색종이 왼쪽 아래 모서리
for _ in range(n):
    x,y= map(int, input().split()) 
    #도화지에 10*10 크기의 색종이 만큼의 영역 칠하기 0 => 1
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1
            
# 100 * 100 도화지 중 1로 칠해진 값만 다 더하기
sum_paper = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            sum_paper += 1
print(sum_paper)