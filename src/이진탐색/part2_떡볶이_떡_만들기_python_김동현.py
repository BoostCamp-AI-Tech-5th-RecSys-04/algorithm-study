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
    if(rest<=m):
        right=mid-1
    else:
        left=mid+1

print(left)