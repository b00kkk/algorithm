# BOJ 2606
import sys
input=sys.stdin.readline

def dfs(M):
    global ans
    for start in range(V):
        visited[M]=True
        if graph[M][start]==True and visited[start]==False:
            ans+=1
            dfs(start)

V = int(input())
N = int(input())
ans = 0

graph = [[False]*(V) for _ in range(V)]
visited = [False]*(V)

for i in range(N):
    a,b = map(int,input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True
dfs(0)
print(ans)
