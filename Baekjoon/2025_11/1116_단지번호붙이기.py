# BOJ 2667
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
graph=[]
for _ in range(N):
    m=input().strip()
    arr=[]
    for i in m:
        arr.append(int(i))
    graph.append(arr)

visited=[[0]*N for _ in range(N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=[]

def bfs(i,j):
    queue=deque()
    queue.append([i,j])
    visited[i][j]=1
    size=1
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx]==1 and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    size+=1
                    queue.append([ny,nx])
    return size


for i in range(N):
        for j in range(N):
            if graph[i][j]==1 and visited[i][j]==0:
                result.append(bfs(i,j))

result.sort()
print(len(result))
for i in result:
    print(i)