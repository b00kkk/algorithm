#BOJ 2583
import sys
from collections import deque
input=sys.stdin.readline

M,N,K=map(int,input().split())
graph=[[0]*M for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(K):
    ldx,ldy,rux,ruy=map(int,input().split())
    for i in range(ldx,rux):
        for j in range(ldy,ruy):
            graph[i][j]=1

def bfs(a,b):
    queue.append((a,b))
    graph[a][b]=1
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                queue.append((nx,ny))
                graph[nx][ny]+=1
                cnt+=1
    return cnt

num=0
queue=deque()
result=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            num+=1
            result.append(bfs(i,j))
result.sort()
print(num)
print(*result)