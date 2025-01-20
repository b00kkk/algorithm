#BOJ 1260
N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]  
for i in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (N + 1)


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, N + 1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)


def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, N + 1):
            if graph[v][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)