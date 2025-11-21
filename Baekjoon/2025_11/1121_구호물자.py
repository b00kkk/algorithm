# BOJ 11581
import sys
input=sys.stdin.readline
def func():
    n=int(input())
    dp=[[0]*n for _ in range(n)]
    for i in range(n-1):
        m=int(input())
        arr=list(map(int,input().split()))
        for j in range(m):
            dp[i][arr[j]-1]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j]=True
    for i in range(n):
        if dp[i][i] and dp[0][i]:
            return "CYCLE"
    return 'NO CYCLE'    
print(func())