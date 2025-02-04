#BOJ 1051
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
square=[input().strip() for _ in range(N)]

c=min(N,M)
result=1
while c>0:
    
    for i in range(N-c+1):
        for j in range(M-c+1):
            if square[i][j]==square[i][j+c-1]==square[i+c-1][j]==square[i+c-1][j+c-1]:
                result=c*c
    if result>1:
        break            
    c-=1



print(result)
