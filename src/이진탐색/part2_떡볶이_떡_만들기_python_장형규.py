"""
    Chapter 7.이진탐색 : 떡볶이 떡 만들기

    접근법 [이진 탐색으로 접근을 한다면]
        이진 탐색은 배열 내부의 데이터가 정렬되어 있어야 사용할 수 있는 알고리즘이다
        떡볶이 떡 문제는 정렬 순서의 영향을 받지 않는 문제이다
        이진 탐색의 개념을 변형해서 푸는 문제지만
        [1 <= N <= 1000000, 1 <= M <= 2000000000]의 범위를 가지고 있지 때문에
        시간이 급격하게 증가할 수 있다.
    
    접근법 [동적계획법으로 접근해 보자]
        적은 범위에서는 sort() 과정이 포함되어 있어 이진 탐색 접근보다는 느릴수 있지만
        범위가 커질수록 유리해진다
        while 반복문은 항상 N회 반복 이하로 정답을 리턴한다
        장점 : 조건문이 1개로 시간을 줄일 수 있다
              각 길이 리스트를 생성하고 sum(list) 연산하는 과정이 생략된다
        단점 : li는 중복 값이 제거되어 메모리가 사용 메모리가 줄어들지만
              Counter 개체를 생성함으로 메모리가 조금 더 필요하다
"""

import time
from collections import Counter

# DP로 접근
def solution(M: int, N: int, li: list) -> int:
    li_cnt = Counter(li)
    li = list(set(li)) # 중복 값을 제거하기 위해 set으로 변환 후 리스트로 
    li.append(0)
    li.sort()
    tteok_gage = 0 # 1칸당 증가하는 떡의 양
    total_tteok = 0 # 손님에게 줄 떡의 길이

    while True:
        tallest_tteok = li.pop()
        tteok_gage += li_cnt[tallest_tteok]
        plus_tteok = (tallest_tteok - li[-1]) * tteok_gage
        total_tteok += plus_tteok

        if total_tteok >= N:
            break
    answer = li.pop() + (total_tteok - N) // tteok_gage
    return answer

# 이코테 정답
def answer(n: int, m: int, array: list) -> int:
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(array)

    # 이진 탐색 수행 (반복적)
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            # 잘랐을 때의 떡볶이 양 계산
            if x > mid:
                total += x - mid
        # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
        if total < m:
            end = mid - 1
        # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1
    return result

if __name__ == '__main__':
    ## Test_Case
    tc = [[1, 1, [1]],
          [1, 0, [1]],
          [1, 1, [1, 1, 1]],
          [2, 11000, [10000, 2225]],
          [5, 6, [1, 2, 3, 4, 5]],
          [7, 5678,[1234, 2345, 3456, 4567, 5678, 6789, 7890]],
          [7, 34567,[12345, 23456, 34567, 45678, 56789, 67890, 78901]],
          [14, 569, [12345, 23456, 34567, 45678, 56789, 67890, 78901,
                     12345, 23456, 34567, 45678, 56789, 67890, 78901]],
          [70, 30280, [1345, 3456, 3467, 4678, 5689, 6780, 7891,
                     1446, 4456, 3567, 8578, 4789, 7810, 2901,
                     2547, 2756, 3457, 4578, 6589, 6290, 4901,
                     1268, 3426, 3467, 4478, 5729, 6780, 3901,
                     5749, 3356, 2467, 5678, 5639, 7290, 1901,
                     6840, 1256, 6467, 8578, 1789, 3890, 8901,
                     8941, 6456, 5567, 1578, 7689, 5290, 7101,
                     9042, 3356, 9567, 5678, 5679, 3490, 4901,
                     5143, 2456, 1456, 4678, 6789, 1890, 7901,
                     6344, 8343, 2467, 2678, 2789, 2890, 7201,]]

    ]
    for i, test_list in enumerate(tc):
        print('----- {}번째 Test_Case -----'.format(i + 1))
        print('동적계획법 - answer :',end = ' ')
        start_time = time.time() # 측정 시작
        print(solution(test_list[0], test_list[1], test_list[2]))
        end_time = time.time() # 측정 종료
        print("time:", end_time - start_time) # 수행 시간 출력

        print('이진  분할 - answer :', end = ' ')
        start_time = time.time() # 측정 시작
        print(answer(test_list[0], test_list[1], test_list[2]))
        end_time = time.time() # 측정 종료
        print("time:", end_time - start_time) # 수행 시간 출력
        print('')


"""
----- 1번째 Test_Case -----
동적계획법 - answer : 0
time: 1.5020370483398438e-05
이진  분할 - answer : 0
time: 2.86102294921875e-06

----- 2번째 Test_Case -----
동적계획법 - answer : 1
time: 3.814697265625e-06
이진  분할 - answer : 1
time: 2.1457672119140625e-06

----- 3번째 Test_Case -----
동적계획법 - answer : 0
time: 3.0994415283203125e-06
이진  분할 - answer : 0
time: 3.0994415283203125e-06

----- 4번째 Test_Case -----
동적계획법 - answer : 612
time: 3.0994415283203125e-06
이진  분할 - answer : 612
time: 5.0067901611328125e-06

----- 5번째 Test_Case -----
동적계획법 - answer : 2
time: 4.291534423828125e-06
이진  분할 - answer : 2
time: 1.9073486328125e-06

----- 6번째 Test_Case -----
동적계획법 - answer : 4893
time: 4.76837158203125e-06
이진  분할 - answer : 4893
time: 5.7220458984375e-06

----- 7번째 Test_Case -----
동적계획법 - answer : 56337
time: 4.0531158447265625e-06
이진  분할 - answer : 56337
time: 6.9141387939453125e-06

----- 8번째 Test_Case -----
동적계획법 - answer : 78616
time: 3.0994415283203125e-06
이진  분할 - answer : 78616
time: 9.059906005859375e-06

----- 9번째 Test_Case -----
동적계획법 - answer : 6256
time: 1.3828277587890625e-05
이진  분할 - answer : 6256
time: 2.9802322387695312e-05
"""