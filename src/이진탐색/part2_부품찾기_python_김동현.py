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
    

