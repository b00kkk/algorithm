# BOJ 7576
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def isFinished():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    return True

def isValid(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append([i, j])

ans = 0
while q:
    q_size = len(q)
    for _ in range(q_size):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny) and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx, ny])
    ans += 1

if not isFinished():
    print(-1)
else:
    print(ans - 1)