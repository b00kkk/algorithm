#BOJ 2559
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
lst=list(map(int,input().split()))
c=sum(lst[:K])
m=c
for i in range(K,N):
    c+=lst[i]-lst[i-K]
    m=max(m,c)
print(m)