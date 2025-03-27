#BOJ 3190
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apple = set()
for _ in range(K):
    x, y = map(int, input().split())
    apple.add((x, y)) 

L = int(input())
snake = {}
for _ in range(L):
    X, C = input().split()
    snake[int(X)] = C


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  

queue = deque()
queue.append((1, 1))
cnt = 0
x, y = 1, 1 

while True:
    cnt += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if not (1 <= nx <= N and 1 <= ny <= N) or (nx, ny) in queue:
        break

    queue.append((nx, ny))

    if (nx, ny) in apple:
        apple.remove((nx, ny)) 
    else:
        queue.popleft()  
    if cnt in snake:
        if snake[cnt] == 'L':
            direction = (direction - 1) % 4
        else:  
            direction = (direction + 1) % 4

    x, y = nx, ny

print(cnt)
