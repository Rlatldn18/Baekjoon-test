"""
    포켓몬 개수 n, 찾을 포켓몬 m(이름 또는 번호)
    영어를 번호로
    번호를 영어로 
    
    딕셔너리 1 : 포켓몬1번
    딕셔너리 포켓몬1번 : 1
    포켓몬을 받으면 => 숫자로
    숫자를 받으면 => 포켓몬으로 바꾸고 출력
"""
import sys
input = sys.stdin.readline
poketmon_dic = {}

n, m = map(int, input().split())

for _ in range(1, n+1):
    poketmon = input().strip()
    poketmon_dic[poketmon] = _
    poketmon_dic[str(_)] = poketmon

for _ in range(m):
   poketmon_find = input().strip()
   print(poketmon_dic[poketmon_find])