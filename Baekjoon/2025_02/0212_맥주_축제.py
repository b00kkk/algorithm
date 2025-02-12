#BOJ 17503
import sys
import heapq
input=sys.stdin.readline

N,M,K=map(int,input().split())
beer=[]
for _ in range(K):
    v,c=map(int,input().split())
    beer.append([v,c])

beer.sort(key=lambda x:x[1])

def solution():
    pick=[]
    p=0

    for b in beer:
        heapq.heappush(pick,b)
        p+=b[0]
        if len(pick)>=N:
            if p>=M:
                return b[1]
            else:
                p -= heapq.heappop(pick)[0]
    return -1

print(solution())