"""
    Chapter 7.이진탐색 : 부품찾기

    접근법 1
        탐색 범위가 큰 상황
        -> 이진 탐색

        함수가 아닌 flag를 사용
        (flag가 True로 바뀌면 부품이 존재 / False이면 부품이 존재X)
    
    접근법 2
        부품이 있는지 없는지 유무만 체크
        -> in 연산자
"""

import sys
input = sys.stdin.readline

# 전체 부품 수
N = int(input())
# 전체 부품
all_num = list(map(int,input().split()))
# 이진 탐색을 위해 정렬
all_num.sort()

# 손님이 원하는 부품 수
M = int(input())
# 손님이 원하는 부품 번호
want_num = list(map(int,input().split()))

# 손님이 원하는 부품 있는지 하나씩 확인
for n in want_num:
    flag = False
    s = 0
    e = N-1
    while s <= e:
        mid = (s+e)//2
        # 찾았다?
        if all_num[mid] == n:
            flag = True
            break
        # 작아? -> 왼쪽확인
        elif all_num[mid] > n:
            e = mid -1
        # 커? -> 오른쪽 확인
        elif all_num[mid] < n:
            s = mid  + 1
    # 찾았다?
    if flag:
        print('yes',end=' ')
    else:
        print('no',end=' ')

######################################################

import sys
input = sys.stdin.readline

# 전체 부품 수
N = int(input())
# 전체 부품 - 중복 제거
all_num = set(list(map(int,input().split())))

# 손님이 원하는 부품 수
M = int(input())
# 손님이 원하는 부품 번호
want_num = list(map(int,input().split()))

for n in want_num:
    # 부품이 있는가?
    if n in all_num:
        print('yes',end=' ')
    # 부품이 없는가?
    else:
        print('no',end=' ')