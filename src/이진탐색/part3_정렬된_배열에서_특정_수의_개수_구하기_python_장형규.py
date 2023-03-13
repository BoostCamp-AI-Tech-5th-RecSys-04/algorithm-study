"""
    Chapter 15.이진탐색 : 정렬된 배열에서 특정 수의 개수 구하기
    
    해결법
        O(logN)이기 때문에 이진 탐색 알고리즘 변형이 필요한것 같지만
        그냥 bisect쓰면 되는 문제
        bisect는 최대한 왼쪽 마지막에 들어 갈수 있는 값, 최대한 오른쪽 마지막에
        들어갈 수 있는 값을 O(logN)의 복잡도로 반환하기 때문에
        그냥 사용하면 된다.
"""

import sys
import bisect

def solution(target, li):
    # 오른쪽에 배치 가능한 최대 인덱스 값
    right = bisect.bisect_right(li, target)
    # 왼쪽에 배치 가능한 최대 인덱스 값
    left = bisect.bisect_left(li, target)
    count = right - left
    # 값이 없으면 오른쪽 끝이나 왼쪽끝이 같은 값이 리턴되므로 0이 되면 -1을 리턴한다
    if count == 0:
        return -1
    return count

if __name__ == "__main__":
    test_case = [[7, 2, [1, 1, 2, 2, 2, 2, 3]],
                 [7, 4, [1, 1, 2, 2, 2, 2, 3]]]
    
    for tc in test_case:
        print(solution(tc[1], tc[2]))
    
    input = sys.stdin.readline
    N, x = map(int, input().split())
    a = list(map(int, input().split()))