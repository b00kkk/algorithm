#BOJ 2470
import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
arr.sort()
max_size=sys.maxsize
a,b=0,N-1
while a<b:
    c=arr[a]+arr[b]
    if abs(c)<max_size:
        max_size=abs(c)
        result=[a,b]
    if c<0:
        a+=1
    else:
        b-=1

print(arr[result[0]],arr[result[1]])
