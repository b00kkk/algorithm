# BOJ 14235
import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    a=list(map(int,input().split()))
    if a[0]!=0:
        arr.extend(a[1:])
        arr.sort()
    else:
        if arr:
            print(arr.pop())
        else:
            print(-1)