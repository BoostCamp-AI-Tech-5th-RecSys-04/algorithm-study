
"""
접근법
    1. 완전 탐색: 조합을 사용하여 모든 경우의 수 탐색.
    
고찰
    이 문제를 보자마자 combinations가 생각났다. 5가지 중에 2가지를 뽑는 모든 경우의 수를
    조사하면, 답이 나올 것이라 생각했다. 
    N의 범위도 1000이기 때문에, 최대 개수 1000 C 2 = 499500 으로, 반복의 횟수도 그렇게 많지 않다.
"""

import itertools

n,m=map(int,input().split())
k=list(map(int,input().split()))

#조합 구하기
a=list(itertools.combinations(k,2))

answer=0

for x,y in a:
    #두 볼링공의 무게가 다를 때만 카운트
    if(x!=y):
        answer+=1

print(answer)

