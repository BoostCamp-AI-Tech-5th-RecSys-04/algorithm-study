"""
    Chapter 7.이진탐색 : 부품찾기

    접근법
    이진탐색 파이썬 내장모듈을 이용
    
    고찰
    코테 환경에서는 bisect모듈이 사용이 된다면 시간 절약을 위해서 활용하는 것이 좋겠지만
    개념은 확실하게 숙지하는 것이 중요하다고 생각한다

    bisect_left(a, x)란?
    정렬된 a에 x를 삽입할 위치를 리턴해준다. x가 a에 이미 있으면 기존 항목의 앞 (왼쪽)의 위치를 반환한다.
    이진 탐색을 통해 들어갈 인덱스를 반환하기 때문에 target이 해당 인덱스의 값과 같은 지 확인하고
    기준 list의 범위를 넘어가지 않도록 확인하는 조건문이 동시에 필요하다. 
"""
# ------------------ 사용 메모리 측정 ----------------------- #
import psutil
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")
# -------------------------------------------------------- #

import sys
import bisect

def search_bool(nums: list[int], target: int) -> bool:
    index = bisect.bisect_left(nums, target) # target이 들어가야할 인덱스 저장

    if index < len(nums) and nums[index] == target:
        return True
    else:
        return False
    
def solution(N: int, M: int, N_list: list, M_list: list):
    sorted_N_list= sorted(N_list)
    for M_value in M_list:
        if search_bool(sorted_N_list, M_value): # bool로 반환하기 때문에 조건문에 바로 사용
            print('yes', end = ' ')
            continue # yes를 출력 했으면 그냥 아래 no는 생략하고 반복 계속
        print('no', end = ' ')


if __name__ == "__main__":
    input = sys.stdin.readline

    # 입력값
    N = int(input().rstrip())
    N_list = list(map(int, input().rstrip().split()))

    M = int(input().rstrip())
    M_list = list(map(int, input().rstrip().split()))
    solution(N, M, N_list, M_list)
    memory_usage('1') # 메모리값 출력
