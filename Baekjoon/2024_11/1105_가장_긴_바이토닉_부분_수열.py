#BOJ 11054
import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

dp1=[1]*N
dp2=[1]*N
for i in range(1,N):
    for j in range(i):
        if A[i]>A[j]:
            dp1[i]=max(dp1[i],dp1[j]+1)

A2=A[::-1]
for i in range(1,N):
    for j in range(i):
        if A2[i]>A2[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)

dp2.reverse()
dp=[0]*N
for i in range(N):
    dp[i]=dp1[i]+dp2[i]

print(max(dp)-1)