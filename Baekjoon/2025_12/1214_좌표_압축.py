# BOJ 18870
import sys
input=sys.stdin.readline

n=int(input())
x=list(map(int,input().split()))
xx=sorted(set(x))
xxx={xx[i]:i for i in range(len(xx))}
for i in x:
    print(xxx[i],end=" ")