'''
    분헤합이란: 자연수 n이 주어졌을 때 n을 이루는 각 자리수의 합
    생성자 M : 자연수 M의 분해합이 N이면 M은 N의 생성자 
    Ex) 245 256 ==> 245+2+4+5 == 256 이므로 245는 생성자
    256은 245에 의해 생성되었기 때문 
    
    출력 : 자연수 n의 가장 작은 생성자를 출력 (n=분해합)
    생성자가 없거나 여러개인 경우?
    생성자가 없다 == x + 각 자리수 합 =1 이나와야되는데 나오는값 X
    생성자가 여러개 == x + 각자리수 합 = 분해합 일때 
    x= 91,101 이면 같은 분해합이 나옴 
'''
import sys
input = sys.stdin.readline
n = int(input())

for i in range(1, n+1):
    gsum = i

    for j in str(i):
        gsum += int(j)

    if gsum == n:
        print(i)
        break
else:
    print(0)  