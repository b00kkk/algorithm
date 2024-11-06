#BOJ 2565
import sys
input=sys.stdin.readline

N=int(input())
line=[]
for _ in range(N):
    A,B=map(int,input().split())
    line.append([A,B])

line.sort()

dp=[1]*N
for i in range(1,N):
    for j in range(i):
        if line[i][1]>line[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))