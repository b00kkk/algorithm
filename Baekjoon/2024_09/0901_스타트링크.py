#BOJ 5014
import sys
from collections import deque
input=sys.stdin.readline

#F:전체층, S:현재층, G:스타트링크위치
F,S,G,U,D=map(int,input().split())

dx=[U,-D]
visited=[0]*(F+1)

def bfs():
    queue=deque()
    queue.append(S)
    visited[S]=True
    while queue:
        x=queue.popleft()
        for i in range(2):
            nx=x+dx[i]
            if 1<=nx<=F and visited[nx]==0:
                visited[nx]=visited[x]+1
                queue.append(nx)
                if nx==G:
                    print(max(visited)-1)
                    return
    print('use the stairs')

if S==G:
    print(0)
else:
    bfs()