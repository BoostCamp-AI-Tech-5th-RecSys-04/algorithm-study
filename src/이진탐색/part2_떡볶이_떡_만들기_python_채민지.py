"""
    Chapter 7.이진탐색 : 떡볶이 떡 만들기

    접근법 1
        탐색 범위가 큰 상황
        -> 이진 탐색

        '적어도' M만큼의 떡을 얻기 위해 이전 mid를 기억해두기
"""

import sys
input = sys.stdin.readline

# 떡의 개수, 요청한 떡의 길이
N, M = map(int,input().split())
# 떡의 개별 높이
arr = list(map(int,input().split()))

s = 0
# 가장 긴 떡을 기준으로 
e = max(arr)-1

answer = 0
while s <= e:
    mid = (s+e)//2
    # 잘린 떡의 총 합
    x = sum([i-mid for i in arr if i-mid > 0])

    # 떡의 양이 부족한가? -> 더 자르자 -> 높이를 낮추자
    if x < M:
        e = mid - 1
    # 떡의 양이 충분한가? -> 덜 잘라보자 -> 높이를 높인다.
    elif x > M:
        answer = mid
        s = mid + 1
        
print(answer)