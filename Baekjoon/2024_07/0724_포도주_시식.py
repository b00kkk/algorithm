#BOJ 2156
import sys
input = sys.stdin.readline
n=int(input())
grape=[]
for i in range(n):
    grape.append(int(input()))
def solution():
    dp=[0]*n
    dp[0]=grape[0]
    if n==1:
        return grape[0]
    dp[1]=grape[0]+grape[1]
    if n==2:
        return dp[1]
    dp[2]=max(dp[1],grape[0]+grape[2],grape[1]+grape[2])
    if n==3:
        return dp[2]
    for k in range(3,n):
        dp[k]=max(dp[k-2]+grape[k],dp[k-3]+grape[k]+grape[k-1],dp[k-1])
    return max(dp)
print(solution())