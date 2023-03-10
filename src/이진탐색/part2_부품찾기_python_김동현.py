
"""
접근법
    1. 이진 탐색. -> 원하는 부품이 존재하는지 반복해서 알아내야하고, 많은 수의 부품을 조사해야함. 따라서, 이진 탐색을 해야 시간초과가 나지 않음.
    
고찰
    기본적인 이진 탐색 문제이다. 이진 탐색을 계속 수행해야 하기 때문에 다른 곳에서 시간 초과가 나지 않도록 주의 하자 (flag 사용)
"""

n=int(input())
part=list(map(int,input().split()))
M=int(input())
sel=list(map(int,input().split()))

#이진 탐색을 위한 정렬. 
part.sort()
for i in sel:

    #인덱스를 양 끝 값으로 설정
    left=0
    right=len(part)-1
    
    #원하는 부품이 있다면 True,  없으면 False
    flag=False

    while(left<=right):
        mid=(left+right)//2
        if(part[mid]<i):
            left=mid+1
        elif(part[mid]>i):
            right=mid-1
        else:
            #같으면 원하는 부품이 있는 것이므로 True
            flag=True
            break
    
    if(flag):
        print('yes')
    else:
        print('no')
    

