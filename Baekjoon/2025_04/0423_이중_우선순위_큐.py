# BOJ 7662
import sys
from heapq import heappush, heappop
from collections import defaultdict
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    k=int(input())
    min_Q=[]
    max_Q=[]
    count = defaultdict(int)  
    size=0

    for _ in range(k):
        s,n=input().split()
        n=int(n)
        if s=='I':
            heappush(min_Q,n)
            heappush(max_Q,-n)
            count[n]+=1
            size+=1
        else:
            if size!=0:
                if n==1:
                    while max_Q and count[-max_Q[0]]==0:
                        heappop(max_Q)
                    val= -heappop(max_Q)
                    count[val]-=1
                else:
                    while min_Q and count[min_Q[0]]==0:
                        heappop(min_Q)
                    val= heappop(min_Q)
                    count[val]-=1
                size-=1


    while min_Q and count[min_Q[0]] == 0:
        heappop(min_Q)
    while max_Q and count[-max_Q[0]] == 0:
        heappop(max_Q)

    if size > 0:
        print(-max_Q[0], min_Q[0])
    else:
        print("EMPTY")