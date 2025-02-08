#BOJ 2615
import sys
from collections import deque
input=sys.stdin.readline

omok=[list(map(int,input().split())) for _ in range(19)]

dx=[1,0,1,-1]
dy=[0,1,1,1]

def bfs(color,a,b):
    for i in range(4):
        queue=deque([(a,b)])
        visited=[[0]*19 for _ in range(19)]
        check=1
        while queue:
            x,y=queue.popleft()
            visited[x][y]=1
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<19 and 0<=ny<19 and omok[nx][ny]==color and visited[nx][ny]==0:
                check+=1
                visited[nx][ny]=1
                queue.append([nx,ny])
                if check==5:
                    if 0<=a-dx[i]<19 and 0<=b-dy[i]<19 and omok[a-dx[i]][b-dy[i]]==color:
                        break
                    if 0<=nx+dx[i]<19 and 0<=ny+dy[i]<19 and omok[nx+dx[i]][ny+dy[i]]==color:
                        break
                    print(color)
                    print(a+1,b+1)
                    sys.exit(0)

for i in range(19):
    for j in range(19):
        if omok[i][j]!=0:
            bfs(omok[i][j],i,j)
print(0)
