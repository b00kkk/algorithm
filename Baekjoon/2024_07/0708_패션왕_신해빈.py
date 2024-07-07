#BOJ 9375
import sys

t=int(sys.stdin.readline())
for i in range(t):
    dic={}
    n=int(sys.stdin.readline())
    for j in range(n):
        a,b=map(str,sys.stdin.readline().rstrip().split())
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=2
    c=1
    for j in dic:
        c*=dic[j]
    print(c-1)