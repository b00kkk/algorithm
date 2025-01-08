#BOJ 2785
import sys
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))
L.sort()

ring=0
if N<3:
    ring=1
else:
    while len(L)>=2:
        if L[0]<=0:
            L.pop(0)
        else:
            L[0]-=1
            L[-2]+=L[-1]
            L.pop()
            ring+=1
print(ring)