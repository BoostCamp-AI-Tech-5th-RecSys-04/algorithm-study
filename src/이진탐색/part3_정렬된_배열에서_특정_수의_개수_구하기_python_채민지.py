"""
    Chapter 15.이진탐색문제 : 정렬된 배열에서 특정 수의 개수 구하기

    접근법 1
        시간복잡도 O(logN)으로 설계
        오름차순으로 정렬된 수열에서 특정 수의 개수 구하기(시작위치, 마지막위치을 구하기)
        -> 이진 탐색 

    접근법 2
        이진 탐색 모듈
        -> form bisect import bisect_left, bisect_right

        bisect_left(arr,target)
        (arr내에 target의 시작 인덱스 == 정렬된 arr 내에 target이 들어갈 수 있는 가장 작은 인덱스)
        bisect_right(arr,target)
        (arr내에 target의 마지막 인덱스 + 1 == 정렬된 arr 내에 target이 들어갈 수 있는 가장 큰 인덱스)
"""

import sys
input = sys.stdin.readline

# 원소의 개수, 찾는 수
n, x = map(int,input().split())
# 원소
arr = list(map(int,input().split()))

# x의 시작 인덱스 구하기
# arr : 원소, x : 찾는 값, n : 원소의 총 개수 
def find_start(arr,x,n):
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        # x의 시작점을 찾았는가?
        # 이전 값이 x가 아니면 됨
        if (mid == 0 or arr[mid-1] < x) and arr[mid] == x:
            return mid        
        # 중간값이 x보다 크거나 같은 경우 -> 왼쪽부분을 확인해보자
        if arr[mid] >= x:
            r = mid - 1
        # 중간값이 x보다 작은 경우 -> 오른쪽부분을 확인해보자
        elif arr[mid] < x:
            l = mid + 1
    return -1

# x의 마지막 인덱스 구하기
def find_end(arr,x,n):
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        # x의 끝점을 찾았는가?
        # 이후 값이 x가 아니면 됨
        if (mid == n-1 or arr[mid+1] > x) and arr[mid] == x:
            return mid        
        # 중간값이 x보다 큰 경우 -> 왼쪽부분을 확인해보자
        if arr[mid] > x:
            r = mid - 1
        # 중간값이 x보다 작거나 같은 경우 -> 오른쪽부분을 확인해보자
        elif arr[mid] < x:
            l = mid + 1
    return -1

start_index = find_start(arr,x,n)
# 값이 x인 데이터가 존재하지 않는다면
if start_index == -1:
    print(-1)
else:
    end_index = find_end(arr,x,n)
    print(end_index - start_index + 1)

#####################################################################

from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

# 원소의 개수, 찾는 수
n, x = map(int,input().split())
# 원소
arr = list(map(int,input().split()))

# (x의 시작(오른쪽) 인덱스) 구하기
start_index = bisect_left(arr,x)
# (x의 마지막(왼쪽) 인덱스+1) 구하기
end_index = bisect_right(arr,x)

answer = end_index - start_index
if answer == 0:
    print(-1)
else:
    print(answer)