# BOJ 2512
import sys
input=sys.stdin.readline

n=int(input())
asset=list(map(int, input().split()))
m=int(input())

def solve():
    start=0
    end=max(asset)
    ans=0
    while start<=end:
        mid=(start+end)//2
        total=0
        for i in asset:
            total+=min(i,mid)
        if total<=m:
            start=mid+1
            ans=mid
        else:
            end=mid-1
    return ans
print(solve())