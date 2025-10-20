# BOJ 3085
import sys
input=sys.stdin.readline

N=int(input())
board=list(list() for _ in range(N))

for i in range(N):
    candy=input().strip()
    for c in candy:
        board[i].append(c)

def max_line(line):
    best = cur =1
    for k in range(1, len(line)):
        if line[k] == line[k-1]:
            cur+=1
        else:
            cur=1
        if cur > best:
            best=cur
    return best

def check_row(r):
    return max_line(board[r])

def check_col(c):
    col=[board[r][c] for r in range(N)]
    return max_line(col)

ans=1
for i in range(N):
    ans=max(ans,check_row(i))
for j in range(N):
    ans=max(ans,check_col(j))

for i in range(N):
    for j in range(N-1):
        if board[i][j]==board[i][j+1]:
            continue
        board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
        ans=max(ans,check_row(i),check_col(j), check_col(j+1))
        board[i][j],board[i][j+1]=board[i][j+1],board[i][j]



for i in range(N-1):
    for j in range(N):
        if board[i][j]==board[i+1][j]:
            continue
        board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
        ans=max(ans,check_row(i),check_row(i+1), check_col(j))
        board[i][j],board[i+1][j]=board[i+1][j],board[i][j]

print(ans)