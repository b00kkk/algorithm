# BOJ 28183
import sys

input=sys.stdin.readline

N,R=map(int,input().split())

s=0

for i in range(1,int((N-R)**0.5)+1):
    if (N-R)%i==0:
        if i>R:
            s+=i
        if (N-R)//i !=i and (N-R)//i >R:
            s+=(N-R)//i

print(s)