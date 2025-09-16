# BOJ 1966
from collections import deque
import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    q=deque(list(map(int,sys.stdin.readline().split())))
    idx=deque(list(range(n)))
    c=0
    while q:
        if q[0]==max(q):
            c+=1
            q.popleft()
            if idx.popleft()==m:
                print(c)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
            