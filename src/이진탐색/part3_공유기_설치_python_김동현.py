
N,C=map(int,input().split())

home=[]

for _ in range(N):
    home.append(int(input()))

home.sort()

#나올 수 있는 거리들을 기준으로 이진 탐색 시작.

left=1 #최소 거리
right=home[N-1]-home[0] #최대 거리

while(left<=right):
    
    mid=(left+right)//2
     
    remain=C-1 #남은 공유기의 개수
    start=home[0] #집 사이 마다의 거리를 재기 위함

    #mid로 지정된 최대 거리 보다 작은 거리면 공유기를 설치할 수 있음
    for i in home[1:]:
        
        
        if(i-start>=mid): #mid로 지정된 최대 거리보다 작으면서 가장 큰 거리를 가지는 집에 공유기 설치
            start=i
            remain-=1 #남은 공유기 개수 빼기.

    if(remain<=0): #남아있는 공유기가 없다면, 최대 거리를 늘려보기.
        left=mid+1
    else: #남아 있는 공유기가 있다면, 최대 거리 줄이기.
        right=mid-1
    print(left, right)

#남아 있는 공유기가 있도록 하는 거리 중에서 최대 값을 반환.
print(right)