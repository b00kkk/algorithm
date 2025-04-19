# Programmers 43162
from collections import deque

def solution(n, computers):
    visited=[0]*n
    def bfs(start):
        queue=deque([start])
        visited[start]=1
        while queue:
            x=queue.popleft()
            for i in range(n):
                if computers[x][i]==1 and visited[i]==0:
                    visited[i]=1
                    queue.append(i)
    count=0
    for i in range(n):
        if visited[i]==0:
            bfs(i)
            count+=1
    return count