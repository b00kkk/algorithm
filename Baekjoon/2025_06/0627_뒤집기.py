# BOJ 1439
import sys
input = sys.stdin.readline

S=input().strip()
cnt_0=0
cnt_1=0

if S[0]=='0':
    cnt_0+=1
else:
    cnt_1+=1

for i in range(1,len(S)):
    if S[i]!=S[i-1]:
        if S[i]=='0':
            cnt_0+=1
        else:
            cnt_1+=1
print(min(cnt_0,cnt_1))