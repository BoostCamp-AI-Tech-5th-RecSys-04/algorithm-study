"""
    Chapter 11.그리디 : 볼링공 고르기
    접근법
        볼링공의 조합을 찾는 문제이다
        조합 라이브러리를 사용하면 조합이 반환된다
        두 사람의 무게는 서로 달라야 하므로 조건문을 통해 판별한다
    
    해결법
        리스트 컨프리헨션을 이용해서 조건이 일치할 때마다 임의의 값을 넣어주고
        리스트의 길이를 반환하면 한줄 코딩 할 수 있다
    
"""

from itertools import combinations

## answer
def solution(n: int, m: int, li: list) -> int:
    return len([0 for x, y in list(combinations(li, 2)) if x != y])


### ------------- Test ------------- ###
import random
def test_case():
    n = random.randrange(1, 1001)
    m = random.randrange(1, 11)
    li = []
    for _ in range(n):
        li.append(random.randrange(1, m + 1))
    return n, m, li

def answer(n: int, m: int, data: list) -> int:
    array = [0] * 11
    for x in data:
        array[x] += 1
    result = 0
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n
    return result

if __name__ == "__main__":
    for i in range(10):
        n, m, li = test_case()
        if solution(n, m, li) == answer(n, m, li):
            print('test{} : pass'.format(i + 1))
            continue
        print('test{} : fail'.format(i + 1))