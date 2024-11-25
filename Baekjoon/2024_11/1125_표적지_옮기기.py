#BOJ 23973
import sys
input=sys.stdin.readline

def score(x, y):
    if x == 0 or x == 18 or y == 0 or y == 18:
        return 1
    elif x == 1 or x == 17 or y == 1 or y == 17:
        return 2
    elif x == 2 or x == 16 or y == 2 or y == 16:
        return 3
    elif x == 3 or x == 15 or y == 3 or y == 15:
        return 4
    elif x == 4 or x == 14 or y == 4 or y == 14:
        return 5
    elif x == 5 or x == 13 or y == 5 or y == 13:
        return 6
    elif x == 6 or x == 12 or y == 6 or y == 12:
        return 7
    elif x == 7 or x == 11 or y == 7 or y == 11:
        return 8
    elif x == 8 or x == 10 or y == 8 or y == 10:
        return 9
    return 10

def starting(x, y, n, m, board):
    cnt = [0] * 11
    for i in range(19):
        inx = x - 9 + i
        for j in range(19):
            iny = y - 9 + j
            if inx < 0 or inx >= n or iny < 0 or iny >= m:
                continue
            if board[inx][iny] == '1':
                number = score(i, j)
                cnt[number] += 1
                if cnt[number] >= 2:
                    return False
    for i in range(1, 11):
        if cnt[i] < 1:
            return False
    return True

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

c=0
for i in range(n):
    for j in range(m):
        if board[i][j] == '1' and starting(i, j, n, m, board):
            c=1
            a,b=i,j

if c==0:
    print(-1)
else:
    print(a,b)