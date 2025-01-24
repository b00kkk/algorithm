#BOJ 2573
import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[]
for _ in range(N):
    arr=list(map(int,input().split()))
    graph.append(arr)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visited[i][j]=1
    while queue:
        x,y=queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<=N and 0<=ny<=M and visited[nx][ny]==0:
                if graph[nx][ny]==0 and graph[x][y]>0:
                    graph[x][y]-=1
                elif graph[nx][ny]>0:
                    visited[nx][ny]=1
                    queue.append((nx,ny))
    return 1

result=0
while True:
    c=0
    visited=[[0]*(M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]>0 and visited[i][j]==0:
                c+=bfs(i,j)
    if c>1:
        break
    result+=1

    if c==0:
        result=0
        break
print(result)