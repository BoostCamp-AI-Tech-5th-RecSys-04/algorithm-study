"""
    Chapter 11.그리디 : 볼링공 고르기

    접근법
    1. 리스트에 들어있는 원소들을 하나씩 꺼내서 본인을 제외한 리스트에서 본인과 중복되지 않는 볼링공의 갯수를 세고 더하기

    고찰
    하나의 원소들을 제외하면서 남은 리스트의 값들과 비교하는 형식을 사용하면 효율적이라고 생각했지만 
    문제 조건에 볼링공 무게가 최대 10까지 제한이 되어있어서 다음의 조건에 대해서 조금 더 생각해보았다면
    B가 선택하는 경우의 수와 곱하는 식을 생각 할 수 있었을 것 같아서 아쉬웠다.


"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
ary = list(map(int, input().split()))

#################################################

count_1, count_2 = 0, 0

for _ in range(N - 1):
    target = ary.pop()

    # 1 Target과 중복되지 않는지 순차탐색
    for a in ary:
        if a != target:
            count_1 += 1

    # 2 갯수만 세서 연산하기
    if target not in ary:
        count_2 += len(ary)
    else:
        count_2 += len(ary) - ary.count(target)


print(f"Count #1 : {count_1}")
print(f"Count #2 : {count_2}")


#################################################

# 정답 풀이
weights = [0] * 11

for x in ary:
    weights[x] += 1

result = 0

# 1부터 M까지의 각 무게에 대하여 처리
for i in range(1, M + 1):
    N -= weights[i]
    result += weights[i] * N  # B가 선택하는 경우의 수와 곱하기

print(f"Result : {result}")

#################################################
