#BOJ 16194
import sys
input=sys.stdin.readline

N=int(input())
P=[0]+list(map(int,input().split()))
dp=[P[1]*i for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+P[j])
print(dp[-1])