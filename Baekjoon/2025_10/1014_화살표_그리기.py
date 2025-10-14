# BOJ 15970
import sys
input = sys.stdin.readline

N=int(input())
arr=[list() for _ in range(N)]

for _ in range(N):
    x,y=map(int,input().split())
    arr[y-1].append(x)

l=0
for a in arr:
    a.sort()
    if len(a)==2:
        l+=(a[1]-a[0])*2
    elif len(a)>2:
        l+=a[1]-a[0]
        l+=a[-1]-a[-2]
        for i in range(1,len(a)-1):
            l+=min(a[i+1]-a[i], a[i]-a[i-1])

print(l)