#BOJ 18352
import sys
from collections import deque
input=sys.stdin.readline

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
dist=[-1]*(N+1)
dist[X]=0
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)


queue=deque()
queue.append(X)

while queue:
    x=queue.popleft()
    for i in graph[x]:
        if dist[i]==-1:
            dist[i]=dist[x]+1
            queue.append(i)


for i in range(N+1):
    if dist[i]==K:
        print(i)
if K not in dist:
    print(-1)