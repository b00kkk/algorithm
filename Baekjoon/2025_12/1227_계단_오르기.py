import sys
input=sys.stdin.readline

s=int(input())
dp=[0]*s
stair=[]
for i in range(s):
    p=int(input())
    stair.append(p)
dp[0]=stair[0]
if s>=2:
    dp[1]=max(stair[1],stair[0]+stair[1])
if s>=3:
    dp[2]=max(stair[1]+stair[2],stair[0]+stair[2])
    for i in range(3,s):
        dp[i]=max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
print(dp[s-1])