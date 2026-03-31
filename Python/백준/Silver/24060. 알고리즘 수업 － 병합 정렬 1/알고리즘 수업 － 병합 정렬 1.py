"""
1. 분할 (Divide)
주어진 배열을 두 개의 하위 배열로 나눈다. 
이 과정을 배열의 길이가 1이 될 때까지 반복

2. 정복 (Conquer)
분할된 배열들이 길이가 1인 상태가 되면, 
이 배열은 이미 정렬된 상태로 간주됨

3. 병합 (Merge)
정렬된 두 개의 배열을 합쳐서 하나의 정렬된 배열로 만듦
이 과정에서 두 배열의 요소를 비교하여 작은 값을 먼저 결과 배열에 추가
"""
# num 하나씩 나누는 방법 (분할)
def merge_sort(arr):
    if len(arr) <= 1: #num이 모두 분할될 때 스탑
        return arr

    mid = (len(arr)+1)//2 #가운데 찾기
    left = merge_sort(arr[:mid]) #가운데 기준 왼쪽 분할
    right =  merge_sort(arr[mid:]) #가운데 기준 오른쪽 분할
    
    return merge(left, right) #모두 나눠질 때 까지 반복(재귀)
        
def merge(left, right): #병합
    mergelist = [] # 정렬 결과 저장
    l = r = 0 #왼쪽 오른쪽 포인터 설정
    
    while l < len(left) and r < len(right): #왼쪽 오른쪽 병합
        if left[l] > right[r]: #오른쪽이 왼쪽보다 크면
            mergelist.append(right[r]) #오른쪽 값 리스트 추가
            q.append(right[r]) # q리스트에 추가
            r += 1 
        else: #위랑 반대일 때
            mergelist.append(left[l])
            q.append(left[l])
            l += 1
            
    while l < len(left): #왼쪽애 남은 값 처리
        mergelist.append(left[l])
        q.append(left[l])
        l += 1
        
    while r < len(right): #오른쪽에 남은 값 처리
        mergelist.append(right[r])
        q.append(right[r])
        r += 1
        
    return mergelist

import sys
input = sys.stdin.readline
a, k = map(int, input().split())
num = list(map(int, input().split()))

q = [] #병합 과정 저장 리스트

merge_sort(num) #병랍 정렬 실행
if len(q) >= k: #k번째 저장 값 출력
    print(q[k-1])
else: #저장 횟수가 k보다 작으면 -1
    print(-1)