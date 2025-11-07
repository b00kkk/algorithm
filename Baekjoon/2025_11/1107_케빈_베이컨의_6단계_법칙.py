# BOJ 1389
import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(a,b):
    queue=deque()
    queue.append(graph[a])
    path=0
    while queue:
        path+=1
        for _ in range(len(queue)):
            edges=queue.popleft()
            for edge in edges:
                if not visit[edge]:
                    visit[edge]=True
                    if edge==b:
                        return path
                    else:
                        queue.append(graph[edge])

answer=[]
for i in range(n):
    temp=0
    for j in range(n):
        if i==j:
            continue
        else:
            visit=[False]*n
            temp+=bfs(i,j)
    answer.append(temp)

minimum=min(answer)
for i in range(n):
    if answer[i]==minimum:
        print(i+1)
        break