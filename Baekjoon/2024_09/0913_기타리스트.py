#BOJ 1495
import sys
input=sys.stdin.readline

N,S,M=map(int,input().split())
V=[0]+list(map(int,input().split()))

dp=[[0 for i in range(M+1)] for j in range(N+1)]
dp[0][S]=True

for i in range(1,N+1):
    for j in range(M+1):
        if dp[i-1][j]==0:
            continue
        if j+V[i]<=M:
            dp[i][j+V[i]]=True
        if j-V[i]>=0:
            dp[i][j-V[i]]=True

c=-1
for i in range(M,-1,-1):
    if dp[N][i]==1:
        c=i
        print(c)
        break
if c==-1:
    print(-1)