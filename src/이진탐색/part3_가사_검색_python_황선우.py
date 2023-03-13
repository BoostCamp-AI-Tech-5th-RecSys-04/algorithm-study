'''
    chapter 15. 가사 검색
    
    접근법
    1. 각 쿼리 별로 매치되는 단어 개수를 찾아야 하므로 queries를 for문에 돌려야 할 것
    2. 탐색할 단어 중 쿼리와 길이가 같은것부터 추출하기 --> 이 방법이 비효율적인 것 같아 다른 방법을 알아봤으나 책의 코드에서도 이 부분을 그대로 구현하였음을 확인
    3. 탐색은 시간초과를 발생시키지 않기 위해 이진탐색을 사용해야 하는데, ?부분을 a와 z로 바꾸어 쿼리의 범위를 만들어야 함.
    
    고찰: 실전에서 만났다면 절대 이진탐색을 떠올릴 수 없었을 문제인 것 같다. 이진탐색을 통해서 푸는 것을 아는 상태에서 만났는데도 풀지 못해 교재의 코드를 거의 그대로 쳐서 구현했다. 빠른 탐색이란 문제가 주어졌다면 사전 또는 문자를 봤을 때도 이진탐색을 떠올려야겠다.
    
''' 
from bisect import bisect_left, bisect_right #이진탐색 알고리즘을 구현한 모듈이 있음. 왼쪽 인덱스 구하는 모듈, 오른쪽 인덱스 구하는 모듈

def count_by_range(a, left_value, right_value): 
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)] #단어 길이는 10000개 이하까지 가능
rarray = [[] for _ in range(10001)] #접미사의 경우 뒤집어서 보는것이 좋으므로 단어의 문자들을 거꾸로 넣은 배열도 필요

def solution(words, queries):
    
    answer = []
    
    #단어 길이에 따라 리스트에 분류해줌
    for word in words: 
        array[len(word)].append(word) 
        rarray[len(word)].append(word[::-1])
    
    #단어 길이에 따라 분류된 단어들을 사전순 오름차순 정렬
    for i in range(10001): 
        array[i].sort()
        rarray[i].sort()
    
    #쿼리와 길이가 같은 단어 중 쿼리를 포함하는 단어 개수 세기
    for query in queries:
        if query[0] == '?': #접두사에 쿼리가 있는 경우
            res = count_by_range(rarray[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
        else:
            res = count_by_range(array[len(query)], query.replace('?','a'),query.replace('?','z'))
        answer.append(res)
    return answer