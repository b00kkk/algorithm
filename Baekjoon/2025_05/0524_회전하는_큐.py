# BOJ 1021
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
deq=deque(i for i in range(1,n+1))
r=list(map(int,sys.stdin.readline().split()))
c=0
for i in r:
    if deq[0]==i:
        deq.popleft()
        continue
    if deq.index(i)<=len(deq)//2:
        rot=-1
    else:
        rot=1
    while deq[0]!=i:
        deq.rotate(rot)
        c+=1
    deq.popleft()
print(c)