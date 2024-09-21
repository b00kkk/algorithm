#BOJ 2302
import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

dp=[0]*41
arr=[0]*41
dp[1]=1
dp[2]=2
for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]
cnt=0
answer=1

for _ in range(M):
    seat=int(input())
    arr[seat]=1

for i in range(1,N+1):
    if arr[i]==0:
        cnt+=1
    elif cnt:
        answer*=dp[cnt]
        cnt=0
if cnt:
    answer*=dp[cnt]

print(answer)