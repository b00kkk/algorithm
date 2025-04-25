# BOJ 10026
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())

color = [list(input().strip()) for _ in range(N)]

queue=deque()
dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited=[[0]*N for _ in range(N)]

def bfs(a,b):
    queue.append((a,b))
    visited[a][b]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and color[nx][ny]==color[x][y] and visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx,ny))

cnt1=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            bfs(i,j)
            cnt1+=1

cnt2=0
for i in range(N):
    for j in range(N):
        if color[i][j]=='G':
            color[i][j]='R'

visited=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            bfs(i,j)
            cnt2+=1

print(cnt1,cnt2)