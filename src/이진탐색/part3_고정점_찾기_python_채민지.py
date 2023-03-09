'''
    Chapter 15.이진탐색문제 : 고정점 찾기

    접근법 1
        시간복잡도 O(logN)으로 설계
        오름차순으로 정렬된 수열에서 특정 수의 개수 구하기(시작위치, 마지막위치을 구하기)
        -> 이진 탐색 
'''

import sys
input = sys.stdin.readline

# 원소의 개수
N = int(input())
# 원소
arr = list(map(int,input().split()))

s = 0
e = N-1
flag = False
while s <= e:
    mid = (s+e)//2
    # 고정점인가?
    if arr[mid] == mid:
        flag = True
        break
    # 값이 인덱스보다 작은가? -> 오른쪽 확인
    if arr[mid] < mid:
        s = mid + 1
    # 값이 인덱스보다 큰가? -> 왼쪽 확인
    elif arr[mid] > mid:
        e = mid - 1

# 고정점이 있는가?
if flag:
    print(mid)
else:
    print(-1)