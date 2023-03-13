'''
    Chapter 3. 그리디 : 1이 될 때까지

    접근법 1
        N이 1이 될 때까지 반복 -> 횟수를 정할 수 없으므로 while문
        K로 나누어 떨어지면 K로 나누고 아니면 1빼기
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

N, K = map(int, input().split())
cnt = 0
while N != 1:
    cnt += 1
    # N이 K로 나누어떨어지면 나누기
    if N%K == 0:
        N /= K
    # 아니면 1을 뺀다
    else:
        N -= 1

print(cnt)
memory_usage('1')
# [1] memory usage:   16.60938 MB