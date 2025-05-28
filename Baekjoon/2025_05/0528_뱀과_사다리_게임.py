# BOJ 16928
import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())

move={}
for _ in range(N):
    x,y=map(int,input().split())
    move[x]=y

for _ in range(M):
    u,v=map(int,input().split())
    move[u]=v

visited=[0]*101
queue=deque()
queue.append((1,0))
visited[1]=1

while queue:
    now,cnt=queue.popleft()

    if now==100:
        print(cnt)
        break

    for dice in range(1,7):
        next_pos=now+dice
        if next_pos>100:
            continue

        if next_pos in move:
            next_pos=move[next_pos]

        if not visited[next_pos]:
            visited[next_pos]=1
            queue.append((next_pos,cnt+1))