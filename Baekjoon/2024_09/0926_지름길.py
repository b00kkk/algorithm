#BOJ 1446
import sys
input = sys.stdin.readline

N,D=map(int,input().split())
route=[]
for _ in range(N):
    s,e,r=map(int,input().split())
    if r<e-s:
        route.append([s,e,r])

route.sort()

dp=[i for i in range(D+1)]
for s,e,r in route:
    for i in range(1,D+1):
        if e==i:
            dp[i]=min(dp[i],dp[s]+r)
        else:
            dp[i]=min(dp[i],dp[i-1]+1)
print(dp[D])