# BOJ 1110
import sys
input = sys.stdin.readline

N=input().strip()
if len(N)==1:
    N='0'+N
new_n=N[-1]+str(int(N[0])+int(N[-1]))[-1]
cnt=1
while N!=new_n:
    if len(new_n)==1:
        new_n='0'+new_n
    new_n=new_n[-1]+str(int(new_n[0])+int(new_n[-1]))[-1]
    cnt+=1

print(cnt)