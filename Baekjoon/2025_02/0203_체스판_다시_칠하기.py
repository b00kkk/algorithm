#BOJ 1018
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
board=[input().strip() for _ in range(N)]


c=sys.maxsize
for a in range(N-7):
    for b in range(M-7):
        k1=0
        k2=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if board[i][j]!='W':
                        k1+=1
                    elif board[i][j]!='B':
                        k2+=1
                else:
                    if board[i][j]!='B':
                        k1+=1
                    elif board[i][j]!='W':
                        k2+=1
        c=min(k1,k2,c)

print(c)