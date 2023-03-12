"""
    Chapter 15.이진탐색 : 정렬된 배열에서 특정 수의 개수 구하기


    접근법
    1. list.count() 내장 함수를 통한 결과값 출력
    2. 이진탐색 - 반복문
        - 탐색하고자 하는 수의 처음과 끝자리를 탐색한다.
    
    고찰
    책의 풀이를 살펴보니 31/43번째 줄의 조건에 mid가 처음이거나 끝일 때에 대한 조건이 추가로 존재하는데 해당 부분을 생각하지 못하고 코드를 작성했던 것이 아쉬웠습니다.
    조건을 생각할 때 경계값 분석을 하는 습관을 더 늘려야 할 것 같습니다.
"""

import sys

input = sys.stdin.readline

N, x = map(int, input().split())
ary = list(map(int, input().split()))

##################################################################

# 1. count()
cnt = ary.count(x)
print(cnt if cnt else "-1")

##################################################################

# 2. 이진탐색
def binary_search_start_idx(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or array[mid - 1] < target) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def binary_search_end_idx(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if (mid == N - 1 or array[mid + 1] > target) and array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


start_idx = binary_search_start_idx(ary, x, 0, N - 1)
end_idx = binary_search_end_idx(ary, x, 0, N - 1)

print(start_idx, end_idx)

if start_idx or end_idx:
    if start_idx == end_idx:
        print(1)
    else:
        print(end_idx - start_idx + 1)
else:
    print(-1)

##################################################################

"""
7 2
1 1 2 2 2 2 3
"""
# 4

"""
7 1
1 1 2 2 2 2 3
"""
# 2

"""
7 3
1 1 2 2 2 2 3
"""
# 1

"""
7 4
1 1 2 2 2 2 3
"""
# -1
