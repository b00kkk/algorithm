# BOJ 1012
import sys
 
t = int(input())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    board = []
    visited = []
    vegetable = []
    worm_num = 0
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for _ in range(m):
        board.append([0] * n)
        visited.append([0] * n)

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        vegetable.append([x, y])
        board[x][y] = 1

    for i, j in vegetable:

        if visited[i][j] == 1:
            continue

        visited[i][j] = 1
        queue = []
        queue.append([i, j])
        while queue:
            cur_x, cur_y = queue.pop()
            for jumpx, jumpy in dir:
                next_x = cur_x + jumpx
                next_y = cur_y + jumpy
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                    continue
                if board[next_x][next_y] == 1 and visited[next_x][next_y] != 1:
                    visited[next_x][next_y] = 1
                    queue.append([next_x, next_y])
        worm_num += 1
    print(worm_num)