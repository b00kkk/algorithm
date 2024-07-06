#BOJ 9095
import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    
    if n>=4:
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        dp[2]=4
        for j in range(4,n+1):
            dp[j-1]=dp[j-2]+dp[j-3]+dp[j-4]
    else:
        dp=[1,2,4]
    print(dp[n-1])