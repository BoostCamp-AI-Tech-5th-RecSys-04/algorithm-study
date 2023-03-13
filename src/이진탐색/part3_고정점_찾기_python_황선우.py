'''
    접근법: 이진탐색
    1. 오름차순 정렬이 된 상태
    2. 시간복잡도 O(logN)
    3. 정렬된 상태 + 고정점 최대 한개 존재 --> 이진탐색 기본 코드로 알고리즘 작성 가능
'''
import sys 
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

#시작 인덱스와 마지막 인덱스 초기화
start = 0 #원소개수는 무조건 1개 이상
end = n-1

#고정점 -1로 초기화
result = -1

while start<=end:
    mid = (start+end)//2
    if mid == array[mid]:
        result = mid
        break

    # 중간값의 인덱스가 중간값보다 클 때 -> 더 큰 인덱스에는 고정점이 존재할 수 없음
    elif mid<array[mid]: 
        end = mid - 1

    # 중간값의 인덱스가 중간값보다 클 때 -> 더 작은 인덱스에는 고정점이 존재할 수 없음
    else:
        start = mid + 1

print(result)