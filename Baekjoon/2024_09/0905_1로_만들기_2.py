#BOJ 12852
import sys
input=sys.stdin.readline

N=int(input())
dp=[0]*(N+1)
result={1:[1]}
for i in range(2,N+1):
    dp[i]=dp[i-1]+1
    if i%3==0:
        if dp[i]>=dp[i//3]+1:
            dp[i]=dp[i//3]+1
            result[i]=result[i//3].copy()
            result[i].append(i)
    if i%2==0:
        if dp[i]>=dp[i//2]+1:
            dp[i]=dp[i//2]+1
            result[i]=result[i//2].copy()
            result[i].append(i)
    if i not in result:
        result[i]=result[i-1].copy()
        result[i].append(i)
print(dp[N])
print(*result[N][::-1])