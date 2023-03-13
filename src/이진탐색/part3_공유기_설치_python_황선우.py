'''
    chapter 15. 공유기 설치

    접근법: 파라매트릭 서치 이진탐색
    1. 공유기 간 최소 간격을 최대로 하는 문제
    2. 공유기 간의 최소 간격을 자체를 탐색해야 한다.
    3. 정확한 간격을 요구하는 것이 아닌 "최대" 간격을 요구하는 것이므로 파라매트릭 서치이다.

    고찰: 문제가 본질적으로 요구하는 답이 무엇인지 볼 것
    <풀지 못했을 때 접근법>
    1. 공유기 간 최소 간격을 최대로 하는 문제
    2. 최소거리를 최대화하는 경우의 수에는 [첫 좌표, ... ,마지막 좌표]가 무조건 포함될 것
    ==>
    <왜 풀지 못했을까?>
    이 문제는 공유기를 설치하는 좌표가 아닌 "최소 거리"를 타겟으로 이진탐색을 해야하는 문제였다.
    집 좌표가 10억에서 1까지 입력될 수 있으므로 탐색 범위가 매우 넓어서 이진탐색을 사용해야 하는 것은 분명했지만,
    1) 배열로 주어지는 값이 좌표라서
    2) 거리를 탐색 타겟으로 두는게 익숙하지 않아 
    풀기 어려웠다.

'''
import sys 
input = sys.stdin.readline

#전체 집 개수(2개 이상), 공유기 개수(2개 이상)
n,c = map(int,input().split())

#집 좌표 배열
array = []
for _ in range(n):
    array.append(int(input()))

#이진탐색을 위한 오름차순 정렬
array.sort() 
print(array)
'''
#탐색범위 시작점, 종료점 초기화 ==> 좌표 기준 알고리즘일 때 사용
start = 0
end = n-1
'''

start = 1 #가능한 최소 거리: 1
end = array[-1] - array[0] #가능한 최대 거리: 시작~끝 사이의 거리 초기화
result = 0 #답 초기화

while start <= end:

    mid = (start+end)//2 # mid를 최소거리 후보로 선정.
    latest = array[0] #시작점에 공유기 설치
    count = 1 #공유기를 설치한 집 수 초기화(시작 집 무조건 포함.)


    for house in array:
        #print(house)

        if house-latest >= mid: # mid 거리 이상으로 띄어 놓고 공유기 설치
            #print(house, latest, mid)
            latest = house
            count += 1


    #if count ==c: # "최대"거리를 찾는 것이므로, 조건에 적합하다고 최적의 해를 보장할 순 없다
    if count >=c:
        start = mid + 1 #탐색범위의 하한선을 높임
        result = mid # 이 이상 간격을 넓게 할 수 있는 경우가 없다면 현재 mid가 최적해가 됨.

    else:
        end = mid - 1 #탐색범위의 상한선을 낮춤

print(result)