'''
    Chapter 15.이진탐색문제 : 공유기 설치
    접근법 1
        가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
        탐색 범위가 큰 상황
        -> 이진 탐색
        가능한 크게 설치이므로 이전 mid 기록해두기
        
'''

import sys
input = sys.stdin.readline

# 집의 개수, 공유기의 개수
N, C = map(int,input().split())
# 집의 좌표
home = sorted([int(input()) for i in range(N)])

# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 설치
# 공유기 사이 최소거리, 최대거리
s = 1
e = home[-1] - home[0]

answer = 0
while s <= e:
    mid = (s+e)//2
    # 거리를 mid로 했을 때 설치할 수 있는 공유기 수
    cnt = 1

    # 현재 설치된 공유기 위치
    current = home[0]
    for i in range(1,N):
        # 공유기 사이 거리가 mid보다 크거나 같다면 거기 설치
        if home[i] - current >= mid:
            current = home[i]
            cnt += 1

    # 현재 거리에서 설치가 많이 되어있다면
    # -> 거리를 넓히자
    if cnt >= C:
        s = mid +1
        # 거리 저장
        answer = mid
    # 현재 거리에 설치가 적게 되어있다면 더 설치해야하니깐 
    # -> 거리를 좁히자
    else:
        e = mid -1

print(answer)