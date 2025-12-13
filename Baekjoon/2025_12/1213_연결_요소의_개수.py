# BOJ 11724
import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
c=0
for i in range(1,n+1):
    if visited[i]:
        continue
    que=deque([i])
    visited[i]=True #방문
    while que:
        node=que.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next]=True
                que.append(next)
    c+=1
print(c)