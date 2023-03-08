"""
    Chapter 7.이진탐색 : 떡볶이 떡 만들기

    파라메트릭 서치 (Parametric Search)

    접근법
    1. 이진탐색 - 재귀 (딱 맞게 떨어지지 않을 때 처리법을 모르겠음) : 실패
    2. 이진탐색 - 반복문 (마지막에 기억해둔 memo를 반환하여 '적어도'의 조건을 지킴)
    
    고찰
    재귀로 구현하던 문제는 책에도 까다롭다고 언급되었는데 어떤식으로 구현 할 수 있을지도 궁금합니다.

"""
import sys

input = sys.stdin.readline


def tteok_check(array, height):
    total_sum = sum([x - height for x in array if x - height > 0])
    return total_sum


# 1 재귀
# def binary_tteok_search_recursive(array, target, start, end):
#     """
#     재귀함수
#     """
#     mid = (start + end) // 2
#     sum_of_tteok = tteok_check(array, mid)
#     if sum_of_tteok == target:
#         return mid
#     elif sum_of_tteok > target:
#         binary_tteok_search_recursive(array, target, mid + 1, end)
#     else:
#         binary_tteok_search_recursive(array, target, start, mid - 1)


# 2 반복문
def binary_tteok_search_iter(array, target, start, end):
    """
    반복문
    """
    while start <= end:
        mid = (start + end) // 2
        sum_of_tteok = tteok_check(array, mid)
        if sum_of_tteok == target:
            return mid
        elif sum_of_tteok > target:
            start = mid + 1
        else:
            memo = mid
            end = mid - 1
    return memo


N, M = map(int, input().split())
array = list(map(int, input().split()))

# 떡을 자를 때 준비된 모든 떡을 사용할 경우 H == 0
# 떡의 길이가 1 이상 주어지기 때문에 H는 최대 길이-1 최대이다.
start, end = 0, max(array) - 1

# H = binary_tteok_search_recursive(array, M, start, end)
H = binary_tteok_search_iter(array, M, start, end)
print(H)

"""
4 6
19 15 10 17
"""
"""
15
"""
