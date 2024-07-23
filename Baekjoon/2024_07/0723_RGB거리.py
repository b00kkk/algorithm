#BOJ 1149
import sys
input = sys.stdin.readline
n=int(input())
total=[[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    r,g,b=map(int,input().split())
    total[i][0]=min(total[i-1][1],total[i-1][2])+r
    total[i][1]=min(total[i-1][0],total[i-1][2])+g
    total[i][2]=min(total[i-1][0],total[i-1][1])+b

print(min(total[n][0],total[n][1],total[n][2]))