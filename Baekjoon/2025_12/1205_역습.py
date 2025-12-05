# BOJ 3976
import sys
input=sys.stdin.readline

c=int(input())
for _ in range(c):
    n,l1,l2,s1,s2=map(int,input().split())
    p1=list(map(int,input().split()))
    d1=list(map(int,input().split()))
    p2=list(map(int,input().split()))
    d2=list(map(int,input().split()))
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1]=l1
    dp[1][1]=l2
    for i in range(2,n+1):
        dp[0][i]=min(dp[1][i-1]+p2[i-2],dp[0][i-1]+d1[i-2])
        dp[1][i]=min(dp[0][i-1]+p1[i-2],dp[1][i-1]+d2[i-2])
    result=min(dp[0][n]+s1,dp[1][n]+s2)
    print(result)