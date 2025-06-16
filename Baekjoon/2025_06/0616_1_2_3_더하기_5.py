# BOJ 15990
import sys
input = sys.stdin.readline

T=int(input())
inputs=[int(input()) for _ in range(T)]
max_input=max(inputs)
MOD=1000000009

dp=[[0]*4 for _ in range(max_input+1)]
dp[1][1]=1
dp[2][2]=1
dp[3][1]=1
dp[3][2]=1
dp[3][3]=1

for i in range(4,max_input+1):
    dp[i][1]=(dp[i-1][2]+dp[i-1][3])%MOD
    dp[i][2]=(dp[i-2][1]+dp[i-2][3])%MOD
    dp[i][3]=(dp[i-3][1]+dp[i-3][2])%MOD
for i in inputs:
    print(sum(dp[i])%MOD)