#BOJ 21736
import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[]
for i in range(N):
    info=list(input().strip())
    graph.append(info)
    for j in range(M):
        if info[j]=='I':
            doyeon=[i,j]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

visited=[[False]*M for _ in range(N)]
c=0
q=deque()
x,y=doyeon
visited[x][y]=True
q.append(doyeon)

while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==False and graph[nx][ny]!='X':
                visited[nx][ny]=True
                q.append((nx,ny))
                if graph[nx][ny]=='P':
                    c+=1

if c==0:
    print('TT')
else:
    print(c)