import sys
input = sys.stdin.readline

#현재 줄 번호
line = 1
#현재 줄까지의 마지막 번호
total = 1

x = int(input())

#x가 속한 줄 찾는것
# total = 1 - 3 - 6 - 10 - ...
while total < x:
    line += 1       #다음 줄로 이동
    total += line   #총 몇 개의 배열이있는지
    
#현재 줄은 찾은 상태 
#현재 줄에서 몇 번째인지 찾기
#현재 줄의 시작 번호 = total - line + 1
idx = x - (total - line)

#분자 / 분모 결정 
#짝수 줄일때 홀수 줄일때 나눠짐
if line % 2 == 0:   #짝수 줄일 때
    up = idx
    down = line - idx + 1

else:               #홀수 줄일 때
    up = line - idx + 1
    down = idx
    
print(f"{up}/{down}")