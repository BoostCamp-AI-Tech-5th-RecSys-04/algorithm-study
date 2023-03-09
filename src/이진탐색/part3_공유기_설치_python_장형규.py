"""
    Chapter 15.이진탐색 : 공유기 설치
    접근법
        첫번째 집에 공유기를 설치한다고 가정한 후에 인접한 두 공유기 거리를 크게 설치한다.
        가장 큰 값을 찾아야 하므로 gap을 result에 저장해 둔다
    
    접근법 2
        count가 n을 넘어가면 무의미 하기 때문에 중간에 멈추고 최대 gap을 저장한다.
"""
import sys

def solution(n: int, c: int, li: list) -> int:
    li.sort() # 정렬 수행

    start = 1 # 최소 거리
    end = li[-1] - li[0] # 최대 거리
    result = 0
    while(start <= end):
        gap = start + (end - start) // 2 # 가장 인접한 두 공유기 사이의 거리를 의미
        value = li[0]
        count = 1 # 첫째 집에 공유기 설치 가정하기 때문에 1로 초기화
        # 현재의 gap 값을 이용해 공유기를 설치하기
        for i in range(1, n): # 순차 처리
            if li[i] >= value + gap:
                value = li[i]
                count += 1
            if count == c: # c를 넘어가면 의미가 없기 때문에 값이 커질때를 생각해서 for 종료
                start = gap + 1
                result = max(result, gap) # 최적의 결과를 저장
                break
        if count < c:
            end = gap - 1
    return result

if __name__ == "__main__":
    n = 5
    c = 3
    li = [1, 2, 8, 4, 9]
    print(solution(n, c, li))

    input = sys.stdin.readline
    n, c = list(map(int, input().split(' ')))
    li = [int(input()) for _ in range(n)]
    print(solution(n, c, li))