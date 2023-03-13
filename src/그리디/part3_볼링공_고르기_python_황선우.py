'''
    chapter 11. 그리디: 볼링공 고르기

    접근법: 계수정렬을 사용한 그리디
    1. a,b는 서로 무게가 다른 볼링공을 들기만 하면 되며, 무게가 같아도 다 다른 공으로 취급.
    2. 무게별 볼링공의 개수만 알면 경우의 수를 구할 수 있을 것.
    3. 계수정렬을 사용하면 N, M의 크기에 상관없이 시간복잡도 O(1), 11번의 연산 안에 문제 풀이가 가능할 것이라 판단
'''
#접근법
import sys

input = sys.stdin.readline

#볼링공 개수 N, 공의 최대 무게 M 입력받기
n, m = map(int, input().split())

#공의 최대 무게 M의 입력 범위: 1≤M≤10 ==> 계수정렬을 사용해도 될 작은 범위
#무게 별 공의 개수를 담는 리스트 초기화
ball = [0] * 11 #0~10

total = n # 앞으로 고려해야 할 공 개수 초기화
result = 0 # 출력값 초기화

#공 무게가 입력되면 ball리스트에 해당 무게 인덱스의 값 +1
for i in map(int,input().split()):
    ball[i] += 1

for b in ball: 
    total -= b # 앞으로 고려해야할 공 개수 - 현재 인덱스(무게)의 공 개수
    result += b * total # 현재 인덱스의 공 개수b * 앞으로 고려해야 할 공 개수
    #print(i,b,total,result) #작동 과정 확인

print(result)
