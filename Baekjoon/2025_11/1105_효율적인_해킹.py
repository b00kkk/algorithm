# BOJ 1325
# PyPy3

import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[B].append(A)

def bfs(i):
    queue=deque([i])
    visited[i]=1
    c=1
    while queue:
        x=queue.popleft()
        for nx in graph[x]:
            if visited[nx]==0:
                c+=1
                visited[nx]=1
                queue.append(nx)
    return c

num=0
result=[0]*(N+1)
for i in range(1,N+1):
    visited=[0]*(N+1)
    result[i]=bfs(i)
num=max(result)

for i in range(N+1):
    if result[i]==num:
        print(i, end=" ")