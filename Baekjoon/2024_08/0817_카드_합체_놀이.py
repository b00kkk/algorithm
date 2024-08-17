#BOJ 15903
import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))

card=0

for i in range(m):
    a.sort()
    a[0]=a[1]=a[0]+a[1]
print(sum(a))