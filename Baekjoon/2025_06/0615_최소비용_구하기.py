# BOJ 1916
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N=int(input())
M=int(input())

graph=defaultdict(list)
for _ in range(M):
    s,e,c=map(int,input().split())
    graph[s].append((e,c))

start,end=map(int,input().split())

distance=[sys.maxsize]*(N+1)

def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0
    while queue:
        dist,now=heapq.heappop(queue)
        if distance[now]<dist:
            continue
        for neighbor,cost in graph[now]:
            new_cost=dist+cost
            if new_cost < distance[neighbor]:
                distance[neighbor]=new_cost
                heapq.heappush(queue, (new_cost, neighbor))

dijkstra(start)
print(distance[end])