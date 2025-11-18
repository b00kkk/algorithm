# BOJ 9465
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    dp=[[0]+list(map(int,input().split())) for _ in range(2)]
    for i in range(2,n+1):
        dp[1][i]=dp[1][i]+max(dp[0][i-1],dp[0][i-2])
        dp[0][i]=dp[0][i]+max(dp[1][i-1],dp[1][i-2])

    print(max(dp[1][n],dp[0][n]))