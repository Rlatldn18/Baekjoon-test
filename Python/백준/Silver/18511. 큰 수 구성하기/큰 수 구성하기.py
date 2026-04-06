import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arrk = list(input().split())

n = int(n)
result = 0
def maxNum(num):
   global result
   
   # n 이하
   if num != "" and int(num) > n:
      return
   # 최대값 갱신
   if num != "":
      result = max(result, int(num))
   #문자열로 수 붙이기
   for i in arrk: 
      maxNum(num + i)

maxNum("")  
print(result)