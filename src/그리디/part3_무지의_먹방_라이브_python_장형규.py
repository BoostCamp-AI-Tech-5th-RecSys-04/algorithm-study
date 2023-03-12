"""
    Chapter 11.그리디 : 무지의 먹방 라이브
    https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3#
    접근법
    배열에 값과 인덱스를 담아야 할 필요가 있다
    값 배열, 인덱스 배열을 따로 만들어서 하기에는 효율이 떨어진다
    (val, index)개념의 리스트가 필요하다.
    heapq나 PriorityQueue에는 첫째 값을 기준으로 정렬하면서 다른 값을 뒤에 넣을 수 있다.

    해결법
    이진 탐색의 떡볶이 떡 만들기 문제의 이진 탐색을 사용하지 않는 접근법과 비슷하다.
    작은 값부터 제거해가며 len을 곱해 가면서 차이를 누적시키면 된다.
    그 후에 남은 값으로 마지막 인덱스를 계산하면 된다.
"""

import heapq
def solution(food_times: list, k: int) -> int:
    # 총 음식의 개수가 k보다 같거나 작으면 계산할 필요 없음
    if sum(food_times) <= k:
        return -1
    
    # (val(값), index)로 val 크기를 기준으로 정렬하면서, index값을 저장해둠
    que = []
    for i, val in enumerate(food_times):
        heapq.heappush(que, (val, i + 1))
    
    eat_time = 0 # 누적 시간
    point = 0  # 이전 value

    while eat_time + ((que[0][0] - point) * len(que)) <= k:
        value = heapq.heappop(que)[0]
        # (현재 값 - 이전값) + (que의 길이 + 1(앞에서 pop을 했기 때문에 1 더한다) )
        eat_time += (value - point) * (len(que) + 1)
        point = value

    # 남은 인덱스 정렬, 값 출력
    result = sorted([heapq.heappop(que)[1] for _ in range(len(que))])
    return result[(k - eat_time) % len(result)]

"""
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.03ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.3MB)
테스트 20 〉	통과 (0.00ms, 10.4MB)
테스트 21 〉	통과 (0.16ms, 10.2MB)
테스트 22 〉	통과 (0.23ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (1.10ms, 10.3MB)
테스트 25 〉	통과 (1.59ms, 10.3MB)
테스트 26 〉	통과 (3.41ms, 10.4MB)
테스트 27 〉	통과 (3.26ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.2MB)
테스트 29 〉	통과 (0.02ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.4MB)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.04ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (437.84ms, 40MB)
테스트 2 〉	통과 (279.13ms, 40.8MB)
테스트 3 〉	통과 (411.95ms, 39.3MB)
테스트 4 〉	통과 (406.63ms, 39.3MB)
테스트 5 〉	통과 (361.03ms, 40.1MB)
테스트 6 〉	통과 (365.49ms, 40.2MB)
테스트 7 〉	통과 (405.37ms, 39.6MB)
테스트 8 〉	통과 (409.38ms, 40.5MB)
"""