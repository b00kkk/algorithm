#BOJ 12865
import sys
input=sys.stdin.readline

N,K=map(int,input().split())

bag=[[0,0]]

for _ in range(N):
    W,V=map(int,input().split())
    bag.append([W,V])

dp=[[0]*(K+1)for _ in range(N+1)]

for i in range(N+1):
    weight,value=bag[i]
    for j in range(K+1):
        if weight>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)

print(dp[N][K])