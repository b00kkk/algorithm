#BOJ 11663
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

def start_idx(dot,start):
    a,b=0,N-1
    while a<=b:
        c=(a+b)//2
        if dot[c]<start:
            a=c+1
        else:
            b=c-1
    return a

def end_idx(dot,end):
    a,b=0,N-1
    while a<=b:
        c=(a+b)//2
        if dot[c]<=end:
            a=c+1
        else:
            b=c-1
    return a

dot=list(map(int,input().split()))
dot.sort()
for _ in range(M):
    start,end=map(int,input().split())
    cnt=end_idx(dot,end)-start_idx(dot,start)
    print(cnt)
