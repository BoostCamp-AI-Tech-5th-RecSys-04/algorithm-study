"""
    Chapter 15.이진탐색 : 가사 검색

    https://school.programmers.co.kr/learn/courses/30/lessons/60060

    접근법
    1. 내 마음대로 알고리즘
        1 - words를 정렬합니다.
        2 - quries에서 하나씩 꺼내서 검사를 진행
            2 - 1 start,end를 모두 찾아서 갯수 확인 | 첫 알파벳 기준으로 정렬된 words
            2 - 2 start,end를 모두 찾아서 갯수 확인 | 맨 뒤 알파벳 기준으로 정렬된 words
        3. 출력 반환
    
    2. 정답 알고리즘
        1 - words를 글자수를 key로 갖는 dict로 변환 -> 끝에서부터 탐색을 찾을 경우도 있기 때문에 words를 뒤집은 글자도 dict 생성
        2 - 두 dict의 values를 모두 알파벳 순으로 정렬
        3 - 쿼리에서 하나씩 꺼내서 검사를 진행 ?를 a와 z로 변경한 후 그 사이의 단어를 탐색하여 start,end 값을 확인 후 갯수 확인
        4. 3의 과정을 모든 쿼리를 수행 할 때 까지 반복
    
    고찰
    접근법을 세우며 코드를 고민해보았지만 20분내에 답이 나오지 않아 정답 알고리즘을 참고 하였습니다.
    bisect 라이브러리를 손으로 구현 할 수 있는 것이 좋다고 생각하였지만 count_by_value() 함수를 구현함에 있어서 
    binary_search_left or right를 구현하는 것은 시간 관계상 혹은 시험 당일 떠오르지 않는 상황들이 있을 수 있다고 생각하였습니다.
    
    그렇기에 bisect 함수를 이진 탐색을 진행할 때에는 필수적으로 사용하는 법을 외워야 할 것 같아져서 연습을 진행하였습니다.
    
    또한 정답 알고리즘은 훨씬 더 클린한 자료구조들을 잘 사용하였지만 처음 생각한 알고리즘은 흐름만을 생각하다보니 자료구조를 어떻게 사용할지 고민하지 못해서 좋지 못한 결과들을 도출했습니다.
    
    하지만 큰 그림에는 접근하는 방식이 비슷하다고 생각하여 이후에 다시 풀어볼 경우 해결 할 수 있다고 생각하였습니다.

"""
from collections import defaultdict
from bisect import bisect_left, bisect_right


def count_by_value(array, left_value, right_value):
    return bisect_right(array, right_value) - bisect_left(array, left_value)


def solution(words, queries):
    answer = []

    # 1 - words를 글자수를 key로 갖는 dict로 변환 -> 끝에서부터 탐색을 찾을 경우도 있기 때문에 words를 뒤집은 글자도 dict 생성
    words_len_dict = defaultdict(list)
    reverse_words_len_dict = defaultdict(list)

    for word in words:
        words_len_dict[len(word)].append(word)
        reverse_words_len_dict[len(word)].append(word[::-1])

    # 2 - 두 dict의 values를 모두 알파벳 순으로 정렬
    for key in words_len_dict.keys():
        words_len_dict[key].sort()
        reverse_words_len_dict[key].sort()

    # 3 - 쿼리에서 하나씩 꺼내서 검사를 진행 ?를 a와 z로 변경한 후 그 사이의 단어를 탐색하여 start,end 값을 확인 후 갯수 확인
    for query in queries:
        length = len(query)
        left_query, right_query = query.replace("?", "a"), query.replace(
            "?", "z"
        )
        if query[0] == "?":
            left_query, right_query = left_query[::-1], right_query[::-1]
            answer.append(
                count_by_value(
                    reverse_words_len_dict[length], left_query, right_query
                )
            )
        else:
            answer.append(
                count_by_value(words_len_dict[length], left_query, right_query)
            )

    return answer
