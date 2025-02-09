#BOJ 15686
import sys
from itertools import combinations
input=sys.stdin.readline

N,M=map(int,input().split())
city=[list(map(int, input().split())) for _ in range(N)]
houses=[]
chickens=[]

for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            houses.append((i, j))
        elif city[i][j]==2:
            chickens.append((i, j))

def chicken_distance(selected_chickens):
    total=0
    for dx,dy in houses:
        min_distance=float('inf')
        for nx,ny in selected_chickens:
            distance=abs(dx-nx)+abs(dy-ny)
            min_distance=min(min_distance,distance)
        total+=min_distance
    return total

# 모든 치킨집 조합 중 최소 치킨 거리 계산
min_chicken_distance=float('inf')

for selected_chickens in combinations(chickens,M):
    min_chicken_distance=min(min_chicken_distance,chicken_distance(selected_chickens))

print(min_chicken_distance)