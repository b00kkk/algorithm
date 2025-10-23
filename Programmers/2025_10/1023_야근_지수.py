# Programmers 12927
import heapq

def solution(n, works):
    answer=0
    if n>=sum(works):
        return answer
    heap=[]
    for i in works:
        heapq.heappush(heap, -i)
    for _ in range(n):
        heapq.heappush(heap,heapq.heappop(heap)+1)
    answer=sum(i**2 for i in heap)
    return answer