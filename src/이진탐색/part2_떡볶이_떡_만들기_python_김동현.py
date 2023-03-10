"""
접근법
    1. 이진 탐색. -> 자를 떡의 길이를 기준으로 이진 탐색 시작 (1 ~ max(떡))
    
고찰
    가장 기본적인 이진탐색 문제였다. 그럴수록, 정답을 구하는 과정에서 left, right 값 실수하지 않도록 주의하자
"""



n,m=map(int,input().split())

rice=list(map(int,input().split()))


left=1
right=max(rice)-1

while(left<=right):
    mid=(left+right)//2

    #자르고 남은 떡의 길이 계산
    rest=0
    for i in rice:
        rest+=(i-mid) if i>mid else 0
    '''
    자른 떡의 길이가 남은 떡의 길이와 같게 되었을 때, 
    right는 조건을 만족하지 않게 되므로 1칸 앞인 left가 답.
    '''
    if(rest<m):
        right=mid-1
    else:
        left=mid+1

print(right)