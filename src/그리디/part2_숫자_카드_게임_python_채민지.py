'''
    Chapter 3. 그리디 : 숫자 카드 게임

    접근법 1 
        각 행의 가장 작은 수 중 가장 큰 수!
        각 행의 가장 작은 수를 r_min(list)에 저장 -> r_min 중 가장 큰 수 출력

'''

# ------------------ 사용 메모리 측정 ----------------------- #
import psutil
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")
# -------------------------------------------------------- #

import sys
input = sys.stdin.readline

# 행, 열
N,M = map(int,input().split())

# 각 행에서 가장 작은 수
r_min = []

for i in range(N):
    # i번째 행
    r = list(map(int,input().split()))
    # i번째 행에서 가장 작은 수
    r_min.append(min(r))

# 각 행에서 가장 작은 수 중 가장 큰 수
print(max(r_min))
memory_usage('1')
# [1] memory usage:   16.61719 MB
# [1] memory usage:   16.61328 MB