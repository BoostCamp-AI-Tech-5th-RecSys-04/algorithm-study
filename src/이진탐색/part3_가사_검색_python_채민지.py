'''
    Chapter 15.이진탐색문제 : 가사 검색

    접근법 1
        각 단어를 길이에 따라 나눈 후 키워드 별로 매치된 단어 개수 찾기
        froaa <= fro?? <= frozz
        -> 이진 탐색 모듈 bisect

        접두사의 경우 뒤집어서 생각하기
        ????o : oaaaa <= o???? <= ozzzz 

    접근법 2
        문자열 검색
        -> Trie 알고리즘

        <Trie>
        ['frodo','front']를 Trie형태로 바꾸기
        trie = {5: {'f': [2, {'r': [2, {'o': [2, {'d': [1, {'o': [1, {}]}], 'n': [1, {'t': [1, {}]}]}]}]}]}}
        - 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조
        - 루트에서부터 자식들을 따라가면서 생성된 문자열들을 저장
        - 시간복잡도 
            생성시 O(M*L) (L : 제일 긴 문자열의 길이, M : 총 문자열의 수)
            탐색시 O(L)
'''

from bisect import bisect_left,bisect_right

def solution(words, queries):
    answer = []
    
    # 같은 길이의 단어끼리 모으기
    w = [[] for _ in range(10001)]
    reverse_w = [[] for _ in range(10001)]
    for word in words:
        w[len(word)].append(word)
        reverse_w[len(word)].append(word[::-1])
        
    # 정렬
    for i in range(10001):
        w[i].sort()
        reverse_w[i].sort()
            
    for q in queries:
        # 이분 탐색을 통해 범위 구하기
        # froaa <= fro?? <= frozz
        # ????o : oaaaa <= o???? <= ozzzz
        qA = q.replace('?','a')
        qZ = q.replace('?','z')
        
        # ?가 접두사에 있는가? -> 단어를 뒤집어서 범위 구하기
        if q[0] == '?':
            s = bisect_left(reverse_w[len(q)],qA[::-1])
            e = bisect_right(reverse_w[len(q)],qZ[::-1])
            answer.append(e-s)
        # ?가 접미사에 있는가?
        else:
            s = bisect_left(w[len(q)],qA)
            e = bisect_right(w[len(q)],qZ)
            answer.append(e-s)
    
    return answer

#######################################################3
# Trie 사용
def make_trie(words,reverse):
    trie = {}
    # 얕은 복사 이용
    for word in words:
        trie.setdefault(len(word),{})
        next_trie = trie[len(word)]

        # 뒤집기?
        if reverse:
            word = word[::-1]

        for letter in word:
            next_trie.setdefault(letter,[0,{}])
            next_trie[letter][0] += 1
            next_trie = next_trie[letter][1]
    return trie

# 매치하는 문자 수 구하기
def cnt(query,new_query,trie):
    # 글자수가 같은 단어가 없으면 0
    if len(query) not in trie.keys():
        return 0
    cur_trie = trie[len(query)]
    for letter in new_query:
        # letter까지 글자가 매치하지 않는가?
        if letter not in cur_trie.keys():
            return 0
        # 매치한다면 다음 글자 확인
        else:
            cur_trie = cur_trie[letter][1]
    # 글자가 다 매치한다
    return sum(v[0] for v in cur_trie.values())



def solution(words, queries):   
    answer = []
    
    # trie 만들기(접두사를 위해 뒤집은 것도 만들기)
    word_trie = make_trie(words,False)
    reverse_word_trie = make_trie(words,True)        
    
    # 검색키워드 별로 세보자
    for q in queries:
        new_q = q.replace('?','')
        
        # ?가 접두사에 있는가?
        # ????o -> reverse_w에서 o 찾기
        if q[0] == '?':
            c = cnt(q,new_q[::-1],reverse_word_trie)
            answer.append(c)
        # ?가 접미사에 있는가?
        # fro?? -> w에서 fro 찾기
        else:
            c = cnt(q,new_q,word_trie)
            answer.append(c)
            
    return answer