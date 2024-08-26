#BOJ 7562
import sys
from collections import deque
input=sys.stdin.readline

dx=[2,2,1,1,-1,-1,-2,-2]
dy=[1,-1,2,-2,2,-2,1,-1]

def bfs(sx,sy,ex,ey):
    if sx==ex and sy==ey:
        return print(0)
    queue=deque()
    queue.append((sx,sy))
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return print(graph[ex][ey])

T=int(input())

for _ in range(T):
    l=int(input())
    graph=[[0]*l for _ in range(l)]
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())
    bfs(sx,sy,ex,ey)