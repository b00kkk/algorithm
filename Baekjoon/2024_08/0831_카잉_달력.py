#BOJ 6064
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    M,N,x,y=map(int,input().split())
    c=x
    while True:
        if c>M*N:
            print(-1)
            break
        if (c-x)%M==0 and (c-y)%N==0:
            print(c)
            break
        c+=M