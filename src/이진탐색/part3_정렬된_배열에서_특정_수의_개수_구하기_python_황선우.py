'''
    chapter 15. 그리디: 정렬된 배열에서 특정 수의 개수 구하기

    접근법: 이진탐색
    1. 배열이 오름차순으로 이미 정렬된 상태(정렬된 상태를 이용해야 함)
    2. o(logN)으로 탐색을 하기 위해서는 이진탐색을 활용해야 함
    3. x의 시작 지점과 끝지점을 각각 이진탐색으로 찾아 두 지점 빼주기

'''
def binary_search(array,start,end,target,left=True):
    length = len(array) - 1
    if left: #left가 True일 경우 시작점 찾기
        while start<=end:
            mid = (start+end)//2
            if array[mid] == x and (mid==0 or array[mid-1] < x): #배열 자체 시작점일 경우 고려
                return mid
            elif array[mid] >=x:
                end = mid-1
            else:
                start = mid+1
    else:
        while start<=end:
            mid = (start+end)//2
            if array[mid] == x and (mid==length or array[mid+1] > x): #배열 자체 끝점일 경우 고려
                return mid
            elif array[mid] <=x:
                start = mid+1
            else:
                end = mid-1
    return -1


import sys
input = sys.stdin.readline

n,x = map(int,input().split()) #원소 개수, 등장횟수를 세어야 하는 원소
array = list(map(int,input().split()))

#시작 인덱스와 끝 인덱스 설정
start = 0
end = n-1

left = binary_search(array,start,end,x) #시작점 찾기
right = binary_search(array,start,end,x,False) #끝점 찾기

if left!=-1:
    print(right-left+1)
else:
  print(left)