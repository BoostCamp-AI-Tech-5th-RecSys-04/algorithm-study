
"""
접근법

    1. 이진 탐색. ->  수열과 같은 시퀀스 데이터에서 특정 조건을 만족하는 값을 찾는 것은 대표적인 이진 탐색 문제이다. 이를 살짝 응용해 두 번 탐색하도록 한 문제이다.


    
고찰
    이진 탐색 과정에서 =의 유무를 달리하여 연속으로 만족하는 구간의 시작 점과 끝 점을 구하여 해결했다.
    
    어떤 조건을 만족하는 구간을 찾기 위해, 시작 점과 끝 점을 각각 이진 탐색으로 구해서 해결할 수 있다는 논리를 알게 되었다.
    

"""

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
