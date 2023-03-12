"""
    Chapter 15.이진탐색 : 공유기 설치

    https://www.acmicpc.net/problem/2110
    
    접근법
    1. 이진탐색 - 반복문
        - 이진탐색의 대상 : 거리
        - 현재 선정된 거리로 몇개의 공유기가 설치 가능한가?
        - C개와 일치하면 탐색완료
    
    - 다음의 문제 풀이는 블로그를 참고 하였습니다. - https://my-coding-notes.tistory.com/119

    고찰
    이진탐색을 떠올릴 수 없었을 것 같은 문제였습니다.
    또한 무엇을 조건으로 탐색을 진행해야할지 막막하였으나 피어세션때 의견을 나누어 일단 가능한 모든 조건을 생각해보고 대입해보며 풀이를 진행할 수 있었습니다.
    하나의 가정에서 나온 다른 가정들로 문제의 흐름을 계획하고 코드로 구현했습니다.
    아직 많은 문제들을 풀며 노하우를 길러야 할 것 같다고 생각했습니다.
"""

import sys

input = sys.stdin.readline


def binary_search(array, start, end):
    result = 0
    while start <= end:
        # 이진탐색을 위한 mid 값 선정
        mid = (start + end) // 2

        # mid 좌표에 공유기 1개 설치
        count, last_router = 1, array[0]

        # 현재 선정된 거리로 몇개의 공유기가 설치 가능한가?
        for i in range(1, N):
            if array[i] - last_router >= mid:
                count += 1
                last_router = array[i]

        # 설치된 갯수가 C개와 같거나 크다면 -> 갯수가 더 크다는 것은 최소 C개는 설치가 가능하다는 뜻
        if C <= count:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


# 입력 데이터 처리
N, C = map(int, input().split())
ary = []
for _ in range(N):
    ary.append(int(input()))

# 집 주소 정렬
ary.sort()

# 최대 간격과 최소 간격
start, end = 0, ary[-1] - ary[0]

# 이진탐색 결과 출력
print(binary_search(ary, start, end))
