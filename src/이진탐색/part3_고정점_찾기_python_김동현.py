
n=int(input())

arr=list(map(int,input().split()))

#인덱스를 탐색 기준으로 설정
left=0
right=len(arr)-1

answer=0
flag=False


while(left<=right):
    mid=(left+right)//2

    #인덱스와 인덱스에 해당하는 값을 비교
    if(mid>arr[mid]):
        left=mid+1
    elif(mid<arr[mid]):
        right=mid-1
    else: #같은 것이 존재하면 답으로 선정
        flag=True
        answer=mid
        break

if(flag): #같은 것이 있다면
    print(answer)
else: #같은 것이 없다면
    print(-1)