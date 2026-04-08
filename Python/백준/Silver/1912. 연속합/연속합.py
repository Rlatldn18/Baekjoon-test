"""
    배열 처음값 = arrN 의 처음값
    더한 값이랑 현재값 중 더 큰 것을 저장
    저장해둔 리스트의 최대 출력
"""
import sys
input = sys.stdin.readline
n = int(input())
arrN = list(map(int, input().split()))

arr_max = [0] * n
arr_max[0] = arrN[0]

for i in range(1, n):
    arr_max[i] = max(arrN[i], arr_max[i-1] + arrN[i])
    
print(max(arr_max))
