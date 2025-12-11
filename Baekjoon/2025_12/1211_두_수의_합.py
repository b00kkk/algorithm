# BOJ 3273
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
x=int(input())
arr.sort()
cnt=0

a=0
b=n-1
while a!=b:
    s=arr[a]+arr[b]
    if s==x:
        cnt+=1
        a+=1
    elif s<x:
        a+=1
    else:
        b-=1

print(cnt)