
"""
접근법

    1. 이진 탐색.

    -> words를 정렬하여 조건을 만족하는 가사의 구간을 찾을 수 있다. (이를 위해, 가사의 길이로 분류를 해서 정렬한다.)
    -> 조건을 만족하는 가사의 구간은 ? 자리에 각각 a를 넣고, z를 넣었을 때 그 사이의 구간이다. 
     
    ex) fr???이라면, fraaa ~ frzzz 사이의 구간.
    
    -> 두 위치를 각각 이진 탐색으로 찾는다. -> 정렬된 배열에서 특정 수의 개수 구하기 문제 응용
    -> 인덱스의 위치를 이진 탐색으로 알아내서 빼주면 답.


고찰

    이 문제는 이진 탐색이라고 유형을 알았기 때문에 비교적 빨리 풀 수 있었다.
    몰랐으면, 사전으로 접근했다가 풀었어도 시간 초과가 났을 가능성이 있다.

    그리고 정렬된 배열에서 특정 수의 개수 구하기 문제에서 두 점을 이진 탐색으로 각각 구하는 방법이 떠올라서 해결 논리는 빠르게 잡았다.

"""



#이진 탐색 수행 함수
def b_s(words,standard, r):
    w=words
    s=standard.replace('?', r)
    
    #인덱스를 기준으로 이진 탐색.
    left=0
    right=len(w)-1
    
    while(left<=right):
        
        mid=(left+right)//2
        
        #문제 조건을 만족하는 인덱스 위치 찾기.
        if(w[mid]>=s):
            right=mid-1
        else:
            left=mid+1
        
    return right
            
def solution(words, queries):
    answer = []

    #문자를 길이 별로 담기 위한 리스트 
    arr=[[] for _ in range(10001)]
    r_arr=[[] for _ in range(10001)]
    
    #문자 그대로 담는 리스트 하나, 문자 역순으로 담는 리스트 하나
    for i in words:
        arr[len(i)].append(i)
        r_arr[len(i)].append(i[::-1])
    
    #이진 탐색을 위한 정렬
    for i in range(10001):
        if(arr[i]):
            arr[i].sort()
        if(r_arr[i]):
            r_arr[i].sort()
    
    for i in queries:
        
        #양 끝이 ? 라면 전체가 ? 인것. -> i의 길이의 word의 개수를 담음
        if(i.startswith('?') and i.endswith('?')):
            answer.append(len(arr[len(i)]))
        
        #?로 시작한다면, 역순으로 바꾸고 -> 이진 탐색으로 개수 구함 -> ex) ????o라면, aaaao ~ zzzzo  내의 개수를 구한다는 발상
        elif(i.startswith('?')):
            answer.append(b_s(r_arr[len(i)], i[::-1], 'z') - b_s(r_arr[len(i)], i[::-1], 'a')) # (o로 시작하는 가장 큰 인덱스 + 1) - (o로 시작하는 가장 작은 인덱스) 
        
        #?로 끝난다면, -> 이진 탐색으로 개수 구함 -> ex) fr???라면, fraaa ~ frzzz  내의 개수를 구한다는 발상 (fr로 시작하는 가장 큰 인덱스 + 1) - (fr로 시작하는 가장 작은 인덱스)
        elif(i.endswith('?')):
            answer.append(b_s(arr[len(i)], i, 'z') - b_s(arr[len(i)], i, 'a'))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
