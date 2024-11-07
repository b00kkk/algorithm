#BOJ 9251
import sys
input=sys.stdin.readline

s1=' '+input().strip()
s2=' '+input().strip()

N1=len(s1)
N2=len(s2)

dp=[[0]*(N2) for _ in range(N1)]

for i in range(1,N1):
    for j in range(1,N2):
        if s1[i]==s2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[N1-1][N2-1])