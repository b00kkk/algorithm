#BOJ 4963
import sys
from collections import deque
input=sys.stdin.readline

dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,1,-1,1,-1]

def bfs(x,y):
    land[y][x]=0
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<w and 0<=ny<h and land[ny][nx]==1:
                land[ny][nx]=0
                queue.append((nx,ny))

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    land=[]
    cnt=0
    for _ in range(h):
        m=list(map(int,input().split()))
        land.append(m)
    for y in range(h):
        for x in range(w):
            if land[y][x]==1:
                cnt+=1
                bfs(x,y)
    print(cnt)