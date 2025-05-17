#BOJ 7569 토마토
import sys
from collections import deque
input=sys.stdin.readline

M,N,H=map(int,input().split())
tomato=list(list(list(map(int,input().split())) for _ in range(N)) for _ in range(H))

dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]

q = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 1:
                q.append((z, y, x))

while q:
    z,y,x=q.popleft()
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0<=nx<M and 0<=ny<N and 0<=nz<H:
            if tomato[nz][ny][nx]==0:
                tomato[nz][ny][nx] = tomato[z][y][x]+1
                q.append((nz,ny,nx))

day=0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x]==0:
                print(-1)
                sys.exit()
            day=max(day,tomato[z][y][x])

print(day-1)