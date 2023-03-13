'''
    Chapter 11. 볼링공 고르기

    접근법 1
        각 무게별로 볼링공이 몇 개씩 있는지 세기 -> Counter
        무게가 i인 볼을 선택할 때 나오는 경우의 수 합하기 (i=1,...,M-1)

        A가 무게가 i인 볼을 선택할 때 나오는 경우의 수 (B는 A보다 무거운 볼을 선택한다고 가정) 
        (무게가 i인 볼)*(무게가 i+1인 볼) + ... +(무게가 i인 볼)*(무게가 M인 볼)
        == (무게가 i인 볼)*(무게가 i+1인 볼 + ... + 무게가 M인 볼)
'''

# ------------------ 사용 메모리 측정 ----------------------- #
import psutil
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")
# -------------------------------------------------------- #

from collections import Counter
import sys
input = sys.stdin.readline

# 볼링공의 개수, 공의 최대 무게
N,M = map(int,input().split())
# 볼링공의 무게
ball = list(map(int,input().split()))

# 각각 무게 개수 세기
cnt = Counter(ball)
answer = 0
# 무게가 M인 볼링공을 고르는 경우 0
for i in range(1,M):
    N -= cnt[i]
    answer += cnt[i]*N

print(answer)
memory_usage('1')
# [1] memory usage:   16.68359 MB
# [1] memory usage:   16.62500 MB