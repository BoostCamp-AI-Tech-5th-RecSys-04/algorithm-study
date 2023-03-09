n,x=map(int,input().split())
arr=list(map(int,input().split()))

#x가 나오는 처음 위치를 찾기 위한 변수
L_left=0
L_right=len(arr)-1

#x가 나오는 마지막 위치를 찾기 위한 변수
R_left=0
R_right=len(arr)-1


while(L_left<=L_right):
    mid=(L_left+L_right)//2

    if(arr[mid]<x): # = 를 제거하면, 처음 x가 나오는 위치의 인덱스를 얻을 수 있음
        L_left=mid+1
    else:
        L_right=mid-1

while(R_left<=R_right):
    mid=(R_left+R_right)//2

    if(arr[mid]<=x): # =를 추가하면, 마지막 x가 나오는 위치의 다음 인덱스를 얻을 수 있음
        R_left=mid+1
    else:
        R_right=mid-1


if((R_right==-1 and L_right==-1) or (R_left==len(arr) and L_left==len(arr))): #수열 범위 밖이면
    print(-1)
else: 
    print(R_left - L_left) #마지막 나오는 위치의 다음 인덱스 - 처음 나오는 위치의 인덱스
