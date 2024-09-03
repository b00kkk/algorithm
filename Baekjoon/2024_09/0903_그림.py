#BOJ 1926
import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
c=0
size=0

def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    size=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append((nx,ny))
                size+=1
    return size

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            size=max(size,bfs(i,j))
            c+=1

print(c)
print(size)