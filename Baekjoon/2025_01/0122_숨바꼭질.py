#BOJ 1697
import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())
visited=[0]*(100001)
queue=deque()

def bfs(N):
    queue.append([N,0])
    while queue:
        x,c=queue.popleft()
        if x==K:
            return c
        if 0<=x+1<=100000 and visited[x+1]==0:
            visited[x+1]=1
            queue.append([x+1,c+1])
        if 0<=x-1<=100000 and visited[x-1]==0:
            visited[x-1]=1
            queue.append([x-1,c+1])
        if 0<=x*2<=100000 and visited[x*2]==0:
            visited[2*x]=1
            queue.append([2*x,c+1])
        
print(bfs(N))