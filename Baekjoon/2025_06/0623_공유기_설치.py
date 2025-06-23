# BOJ 2110
import sys
input = sys.stdin.readline

N,C=map(int,input().split())
modem=[]

for _ in range(N):
    x=int(input())
    modem.append(x)

modem.sort()

start,end=1,modem[-1]-modem[0]
result=0

while start<=end:
    mid=(start+end)//2
    cnt=1
    last=modem[0]
    
    for i in range(1,N):
        if modem[i]-last>=mid:
            cnt+=1
            last=modem[i]

    if cnt>=C:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)