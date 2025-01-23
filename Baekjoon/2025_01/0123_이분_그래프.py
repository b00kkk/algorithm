#BOJ 1707
import sys
from collections import deque
input = sys.stdin.readline

K=int(input())

def bfs(n):
    queue=deque()
    queue.append(n)
    visited[n]=1
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if visited[i]==0:
                visited[i]=-visited[x]
                queue.append(i)
            elif visited[i]==visited[x]:
                return False
    return True


for _ in range(K):
    V,E=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    visited=[0]*(V+1)
    for _ in range(E):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,V+1):
        if visited[i]==0:
            result=bfs(i)
            if not result:
                break
    print('YES' if result else 'NO')