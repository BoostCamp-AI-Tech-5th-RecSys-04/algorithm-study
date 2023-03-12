"""
    Chapter 15.이진탐색 : 고정점 찾기


    접근법
    1. 이진탐색 - 반복문
    
    고찰
    이진탐색의 조건문의 형태를 변경함에 따라 새로운 문제를 풀 수 있다는 것을 알 수 있었습니다.
"""

import sys

input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(binary_search(ary, 0, N - 1))

"""
5
-15 -6 1 3 7
"""
# 3

"""
7
-15 -4 2 8 9 13 15
"""
# 2

"""
7
-15 -4 3 8 9 13 15
"""
# -1
