# BOJ 1300
import sys
input = sys.stdin.readline

N=int(input())
k=int(input())

start,end=1,k

while start<end:
    mid=(start+end)//2
    cnt=0

    for i in range(1,N+1):
        cnt+=min(mid//i,N)

    if cnt<k:
        start=mid+1
    else:
        end=mid

print(start)