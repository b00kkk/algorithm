# BOJ 1699
import sys
input=sys.stdin.readline

n=int(input())

def c(n):
    dp=[sys.maxsize]*(n+1)
    dp[0]=0

    for i in range(1,n+1):
        j=1
        while j**2<=i:
            dp[i]=min(dp[i],dp[i-j*j]+1)
            j+=1
    return dp[n]

print(c(n))