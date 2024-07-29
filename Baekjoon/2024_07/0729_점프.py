#BOJ 1890
import sys
input = sys.stdin.readline
n=int(input())
jump=[]
for i in range(n):
    jump.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]
x,y=0,0
start=jump[x][y]

if x+start<n:
    dp[x+start][y]=1
if y+start<n:
    dp[x][y+start]=1

for i in range(n):
    for j in range(n):
        if dp[i][j]:
            start=jump[i][j]
            c=dp[i][j]
            if start==0:
                continue
            if i+start<n:
                dp[i+start][j]+=c
            if j+start<n:
                dp[i][j+start]+=c
print(dp[n-1][n-1])