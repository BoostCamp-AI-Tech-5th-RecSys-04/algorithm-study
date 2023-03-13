'''
    Chapter 7.이진탐색 : 부품찾기

    접근법1: 데이터에 O(1)시간만에 접근할 수 있는 set in 활용

    1. 개수와 상관없이 종류의 존재 여부만을 묻는 문제.
    2. 가게에 있는 부품 종류를 set에 담으면 O(1)만에 손님이 요구하는 부품의 존재 여부를 알 수 있음
'''

n = int(input()) #가게 부품종류 개수
dlist = set(map(int,input().split())) #가게의 모든 부품을 입력받고 중복 제거

m = int(input()) #손님 요청 부품종류 개수
for i in list(map(int,input().split())): #손님이 요구하는 부품을 입력 받고, set에 존재하는가 여부 확인
  if i in dlist: #O(1)
    print('yes', end=' ')
  else:
    print('no', end=' ')


'''
    접근법2: 재귀함수로 구현한 이진탐색

    1. 실전에서 set을 사용하는 방법을 생각하지 못했을 경우
    2. 손님이 요구하는 부품을 찾으려면 그때그때 가게 부품을 모두 순회해야함
    3. 효율적인 탐색방법인 이진탐색 활용해야 할 것
    4. 요구한 모든 부품에 대하여 반복되는 과정이므로 재귀로 구현해봄
'''
#시간 복잡도: O(NlogN) + O(M) * O(logN)

def bin_search(target, array, start, end): # 이진탐색 함수: O(logN)
  mid = (start+end)//2
  if start > end: #찾을 수 없을 경우 바로 반환
    return "no"
  if array[mid] == target: #찾는 경우 바로 반환
    return "yes"
  elif array[mid] > target: #요청한 부품 번호가 탐색범위 중간값보다 작을 경우
    end = mid-1
  else: #요청한 부품 번호가 탐색범위 중간값보다 클 경우
    start = mid+1 
  return bin_search(target, array, start, end)


n = int(input())
market = list(map(int,input().split()))
market.sort() #이진탐색을 위한 정렬: O(NlogN)
m = int(input())
client = list(map(int,input().split()))


for c in client: #이진탐색 함수 루프문: O(M)
  print(bin_search(c, market, 0, n-1), end=' ')