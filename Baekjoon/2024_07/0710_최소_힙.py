#BOJ 1927
import sys
import heapq

heap=[]
n=int(sys.stdin.readline())
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)