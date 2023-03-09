"""
    Chapter 15.이진탐색 : 고정점 찾기

    접근법
        정렬되어 있고 O(logN)으로 알고리즘을 설계 해야한다 -> 이진 탐색법
    해결법
        기본적인 이진 탐색 정렬 알고리즘에 타겟을 인덱스 값으로 변경하면 된다

"""
import sys

def solution(N, li):
    left = 0
    right = N - 1
    while left <= right:
        mid = left + (right - left) // 2
        # 중간값이 인덱스 값과 일치 한 경우 mid리턴
        if li[mid] == mid:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        if li[mid] > mid:
            right = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    test_case = [[5, [-15, -6, 1, 3, 7]], # answer : 3
                 [7, [-15, -4, 2, 8, 9, 13, 15]], # answer : 2
                 [7, [-15, -4, 3, 8, 9, 13, 15]]] # answer : -1
    for tc in test_case:
        print(solution(tc[0] ,tc[1]))
    
    input = sys.stdin.readline
    
    N = int(input())
    a = list(map(int, input().split()))
    print(solution(N, a))
