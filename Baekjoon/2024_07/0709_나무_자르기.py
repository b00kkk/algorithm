#BOJ 2805
import sys

n,m=map(int,sys.stdin.readline().split())
h=list(map(int,sys.stdin.readline().split()))
start,end=1,max(h)
while start<=end:
    tree=0
    mid=(start+end)//2
    for i in h:
        if i>mid:
            tree+=i-mid
    if tree<m:
        end=mid-1
    else:
        start=mid+1
print(end)