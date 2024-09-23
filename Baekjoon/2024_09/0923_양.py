#BOJ 3184
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

o, v = 0, 0

def bfs(x, y):
    global o, v
    queue = deque()
    queue.append((x, y))
    o_area = 0
    v_area = 0
    
    if graph[x][y] == 'o':
        o_area = 1
    elif graph[x][y] == 'v':
        v_area = 1

    graph[x][y] = '#'

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '#':
                    continue
                if graph[nx][ny] == 'v':
                    v_area += 1
                    graph[nx][ny] = '#'
                    queue.append((nx, ny))
                elif graph[nx][ny] == 'o':
                    o_area += 1
                    graph[nx][ny] = '#'
                    queue.append((nx, ny))
                elif graph[nx][ny] == '.':
                    graph[nx][ny] = '#'
                    queue.append((nx, ny))

    if v_area >= o_area:
        o_area = 0
    else:
        v_area = 0

    o += o_area
    v += v_area

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            bfs(i, j)

print(o, v)
