# BOJ 20365
import sys
input=sys.stdin.readline

N=int(input())
color=input().strip()

cntB,cntR=0,0

if color[0]=='B':
    cntB+=1
else:
    cntR+=1

for i in range(1,N):
    if color[i]!=color[i-1]:
        if color[i]=='B':
            cntB+=1
        else:
            cntR+=1

print(min(cntB,cntR)+1)