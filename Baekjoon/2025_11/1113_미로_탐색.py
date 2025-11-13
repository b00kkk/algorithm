# BOJ 2178
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().strip())))

def bfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if maze[nx][ny]==1:
                    maze[nx][ny]=maze[x][y]+1
                    queue.append((nx,ny))
    return maze[-1][-1]
print(bfs(0,0))