
"""
접근법

    1. 이진 탐색. ->  인덱스를 기준으로 이진 탐색, 배열의 실제 값과 인덱스를 비교하여 탐색한다는 논리.

    


고찰
    문제를 읽었을 때, 이진 탐색 문제이고, left, right로 둘 수 있는 것이 인덱스 밖에 없기 때문에 index라고 머리에 박고 논리를 펼쳤다.
    그래서 로직을 빠르게 알아낼 수 있었던 것 같다.
    

"""


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