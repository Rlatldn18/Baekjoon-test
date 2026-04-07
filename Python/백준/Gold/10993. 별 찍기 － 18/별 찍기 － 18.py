"""
   2**n => 10개면 가능  
"""
import sys
input = sys.stdin.readline
n = int(input())

h = 2**n - 1
w = 2**(n+1)-3
arr = [[" "]* w for _ in range(h)]

def starPattern(num, start_x, start_y, tri):
   if num == 1:
      arr[start_x][start_y] = "*"
      return 
      
   height = 2**num - 1
   width = 2**(num+1)-3
   
   if tri: # 짝수
      #대각선 \/
      for i in range(height): # x
         arr[start_x - i][start_y + i] = "*"
         arr[start_x - i][start_y + width - 1 - i] = '*'
      #바닥 ㅡ
      for i in range(width):
         arr[start_x][start_y + i] = '*'
         
      starPattern(num-1, start_x - height//2, start_y + width//4 + 1, not tri)
       
   else: # 홀수
      #대각선 /\
      for i in range(height):
         arr[start_x + i][start_y + i] = '*'
         arr[start_x + i][start_y + width - 1 - i] = '*'
      #바닥 _
      for i in range(width):
         arr[start_x][start_y + i] = '*'
      
      starPattern(num-1, start_x + height//2, start_y + width//4 + 1, not tri)
         
if n % 2 == 1: # n이 홀수 일때랑 짝수일때 달라짐
    starPattern(n, h-1, 0, True)
else:
    starPattern(n, 0, 0, False)

for rows in arr:
   print("".join(rows).rstrip())