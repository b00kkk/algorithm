# BOJ 2075
import sys
from heapq import heappush, heappop
input=sys.stdin.readline

N=int(input())

heap = []
for i in range(N):
    for num in map(int, input().split()):
        heappush(heap, num)
        if len(heap) > N:
            heappop(heap)
print(heap[0])