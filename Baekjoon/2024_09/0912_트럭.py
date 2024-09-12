#BOJ 13335
import sys
from collections import deque
input=sys.stdin.readline
n,w,L=map(int,input().split())
a=deque(map(int,input().split()))
second=0
bridge=[0]*w

while bridge:
    second+=1
    bridge.pop(0)
    if a:
        if sum(bridge)+a[0]<=L:
            bridge.append(a.popleft())
        else:
            bridge.append(0)
print(second)