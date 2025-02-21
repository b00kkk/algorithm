# BOJ 1351
import sys
input = sys.stdin.readline

N,P,Q=map(int,input().split())

dp={}
dp[0]=1
def solution(N):
    if N in dp:
        return dp[N]
    else:
        dp[N]=solution(N//P)+solution(N//Q)
        return dp[N]

print(solution(N))