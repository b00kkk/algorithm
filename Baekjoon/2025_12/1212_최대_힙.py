# BOJ 11279
import sys
import heapq

n=int(sys.stdin.readline())
max_heap=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x>0:
        heapq.heappush(max_heap,-x)
    elif x==0:
        if max_heap:
            print(-heapq.heappop(max_heap))       
        else:
            print(0)