"""
    t = 실행 횟수
    뒤집었을 때 문자가 같으면 = 0
    왼쪽부터 한 글자씩 지우면서 펠린드롭인지 확인
    ex coimmoc => oimmoc cimmoc commoc 만약 펠린드롭이면
    1출력
    다 검사했는데 팰린드롬이 아니면 2
"""
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().strip()
    
    if string == string[::-1]:
        print(0)
        continue
    
    result = 2
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1 
            
        else:
            # 왼쪽 제거
            del_word_left = string[left+1:right+1]
            if del_word_left == del_word_left[::-1]:
                result = 1
                break
            
            # 오른쪽 제거
            del_word_right = string[left:right]
            if del_word_right == del_word_right[::-1]:
                result = 1
                break
            
            break
    
    print(result)