'''
    Chapter 3. 그리디 : 큰 수의 법칙

    접근법 1
        (가장 큰 수를 K번 더하고 두번째 큰 수 1번 더하기)를 for문을 이용하여 반복하기
        
    접근법 2
        (가장 큰 수를 K번 더하고 두번째 큰 수 1번 더하기)를 반복 -> 반복 주기 (K+1)
        가장 큰수를 더할 횟수 구하기 == (M-cnt)
            
        두번째 큰 수 더할 횟수 == cnt
            1사이클에 1번
            cnt = M//(K+1)

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

# 배열의 크기, 숫자가 더해지는 횟수, 반복 가능 수
N,M,K = map(int,input().split())

# 배열
arr = list(map(int,input().split()))
arr.sort(reverse=True)

# 정답
answer = 0

# 특정 인덱스 연속 횟수
k = 0
for i in range(M):
    k += 1
    # K번 같은 수를 더했는가?
    if k == K:
        # 2번째 큰 수 더하기 + k 초기화
        answer += arr[1]
        k = 0
    # 아니라면
    else:
        # 가장 큰 수 더하기
        answer += arr[0]

print(answer)
memory_usage('1') # 메모리값 출력
# [1] memory usage:   16.54297 MB


##############################################
# 배열의 크기, 숫자가 더해지는 횟수, 반복 가능 수
N,M,K = map(int,input().split())

# 배열
arr = list(map(int,input().split()))
arr.sort(reverse=True)

# 가장 큰 수
f = arr[0]
# 두번째로 큰 수
s = arr[1]

# 두번째로 큰 수 더한 횟수
cnt = M//(K+1)
answer = f*(M-cnt) + s*cnt
print(answer)
memory_usage('1')
# [1] memory usage:   16.57422 MB