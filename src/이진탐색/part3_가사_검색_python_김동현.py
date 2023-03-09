
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
