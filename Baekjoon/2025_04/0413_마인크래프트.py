#BOJ 18111
import sys
input=sys.stdin.readline

N,M,B=map(int,input().split())
ground=[list(map(int,input().split())) for _ in range(N)]

max_floor=0
for i in range(N):
    max_floor=max(max_floor,max(ground[i]))

min_floor=0
for i in range(N):
    min_floor=min(min_floor,min(ground[i]))

arr=[sys.maxsize,0]

for v in range(min_floor, max_floor+1):
    up=0
    down=0
    time=0
    for i in range(N):
        for j in range(M):
            diff=ground[i][j]-v
            if diff>0:
                down+=diff
            else:
                up-=diff
    if down+B>=up:
        time=down*2+up
        if arr[0]>=time:
            arr[0]=time
            arr[1]=v

print(*arr)