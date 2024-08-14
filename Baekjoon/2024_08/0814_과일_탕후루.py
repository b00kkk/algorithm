#BOJ 30804
import sys
input=sys.stdin.readline
N=int(input())
S=list(map(int,input().split()))

left,right=0,0
count=[0]*10
count[S[0]]+=1
temp=[0]*10
temp[S[0]]=1
kind=sum(temp)

answer=1

while True:
    if kind<=2:
        answer=max(answer,sum(count))
        right+=1
        if right==N:
            break
        count[S[right]]+=1
        temp[S[right]]=1
        kind=sum(temp)
    else:
        count[S[left]]-=1
        if count[S[left]]==0:
            temp[S[left]]=0
        kind=sum(temp)
        left+=1
print(answer)