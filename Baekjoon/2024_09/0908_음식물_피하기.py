#BOJ 1743
import sys
from collections import deque
input=sys.stdin.readline

N,M,K=map(int,input().split())
graph=[[0]*(M) for _ in range(N)]
visited=[[0]*(M) for _ in range(N)]

for _ in range(K):
    r,c=map(int,input().split())
    graph[r-1][c-1]=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=1
    count=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny]=1
                count+=1
    return count

size=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            size=max(size,bfs(i,j))
print(size)