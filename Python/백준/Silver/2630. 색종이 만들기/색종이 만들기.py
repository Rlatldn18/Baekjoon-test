"""
   n = 한 변의 길이 n은 최대 128 || 2**k (1 <= k <= 7)
   n * n 크기의 종이 
   하얀색 색종이와 파란색 색종이의 개수 출력 
"""
import sys
input = sys.stdin.readline
n = int(input()) 
p = [list(map(int, input().split()))for _ in range(n)] 

blue = 0
white = 0

def papers(n, x, y):
   global blue, white
   color = p[x][y]
   
   for i in range(x, x + n):
      for j in range(y, y + n):
         if p[i][j] != color: # 색 다르면 크기 나누고 4등분 재귀
            half = n // 2
            papers(half, x, y)
            papers(half, x, y + half)
            papers(half, x + half, y)
            papers(half, x + half, y + half)
            return
         
   if color == 1: # 영역이 모두 1일 때 
      blue += 1
   else: # 영역이 모두 0일 때
      white += 1
   
papers(n,0,0)
print(white)
print(blue)