"""
    하노이의 탑 최소 이동 횟수 => (2**n)-1
    n = 원판의 개수
    n = 3이면 1 2 3 3이 가장 큰 원판이라 할때
    1 2를 mid에다 옮기고 
    3을 3번째 장대에 옮기고
    1 2를 3으로 옮겨줘야함
    1=>3 1=>2 3=>2 1=>3 2=>1 2=>3 1=>3
"""
def hanoi(n, start, end, mid):
    #원판이 1개면 바로 3으로 이동
    if n == 1:
        print (start, end)
        return
    
    #큰 원판을 옮기기 위해 위에 것을 중간에 옮김
    hanoi(n-1,start,mid,end) 
    #가장 큰 원판 => 3으로 이동
    print(start,end)
    #중간에 옮긴것을 3으로 이동
    hanoi(n-1, mid,end,start)
    
import sys
input = sys.stdin.readline

n = int(input())
print((2**n)-1)
hanoi(n,1,3,2)
