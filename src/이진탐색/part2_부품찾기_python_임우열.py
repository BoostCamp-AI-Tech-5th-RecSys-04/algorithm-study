"""
    Chapter 7.이진탐색 : 부품찾기

    접근법
    1. python in 연산을 사용한 탐색
    2. 이진탐색

    고찰
    In 연산에서 일어나는 탐색은 무슨 탐색인지 효율은 어떤지 궁금해졌습니다.
    
"""
import sys
import time

input = sys.stdin.readline

# 입력값
N = int(input().rstrip())
num_list = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
target_list = list(map(int, input().rstrip().split()))

########################################################################

# 1 Python in 연산을 사용한 탐색
st1 = time.time()
num_set = set(num_list)
# num_set = list(num_list)
for target in target_list:
    if target in num_set:
        print("yes", end=" ")
    else:
        print("no", end=" ")
ed1 = time.time()
print(f"\n#1 걸린시간 : {ed1-st1}s")

########################################################################

# 2 이진탐색
def binary_search(array: list, target, start, end):
    """
    반복문
    """
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None


st2 = time.time()
sorted_num_list = sorted(num_list)
for target in target_list:
    if binary_search(sorted_num_list, target, 0, N - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
ed2 = time.time()
print(f"\n#2 걸린시간 : {ed2-st2}s")

########################################################################


"""
5
8 3 7 9 2
3
5 7 9
"""
"""
no yes yes
"""
