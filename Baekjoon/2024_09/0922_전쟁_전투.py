#BOJ 1303
import sys
from collections import deque
input=sys.stdin.readline

M,N=map(int,input().split())

graph=[]
for _ in range(N):
    cloth=list(input().strip())
    graph.append(cloth)

visited=[[0]*M for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(a,b,k):
    queue=deque()
    queue.append((a,b))
    visited[a][b]=1
    c=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==k and visited[nx][ny]==0:
                visited[nx][ny]=1
                c+=1
                queue.append((nx,ny))
    return c

b,w=0,0
for i in range(N):
    for j in range(M):
        if visited[i][j]==0 and graph[i][j]=='B':
            b+=bfs(i,j,graph[i][j])**2
        elif visited[i][j]==0 and graph[i][j]=='W':
            w+=bfs(i,j,graph[i][j])**2
print(w,b)