# BOJ 25682
# PyPy3로 실행

import sys
input=sys.stdin.readline

N,M,K=map(int,input().split())

board=[]

for _ in range(N):
    board.append(input().strip())

def check(start):
    dp=[[0]*(M+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2==0:
                v=(board[i][j]!=start)
            else:
                v=(board[i][j]==start)
            dp[i+1][j+1]=dp[i][j+1]+dp[i+1][j]-dp[i][j]+v

    count=N*M
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            count=min(count,dp[i+K-1][j+K-1]-dp[i+K-1][j-1]-dp[i-1][j+K-1]+dp[i-1][j-1])
    return count

print(min(check('B'),check('W')))