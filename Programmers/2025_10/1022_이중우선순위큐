# Programmers 42628
import heapq

def solution(operations):
    heap=[]
    for i in operations:
        a,b=i.split()
        b=int(b)
        if a=='I':
            heapq.heappush(heap,b)
        else:
            if heap:
                if b==1:
                    mx = max(heap)
                    heap.remove(mx)   
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)
    if heap:   
        answer= [max(heap), heap[0]]
    else:
        answer=[0,0]
    return answer