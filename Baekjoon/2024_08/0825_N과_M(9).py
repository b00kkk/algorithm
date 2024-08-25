#BOJ 15663
import sys
from itertools import permutations
input=sys.stdin.readline

N,M=map(int,input().split())
num=list(map(int,input().split()))
c=set(permutations(num,M))
result=[]
for i in c:
    i=[x for x in i]
    result.append(i)
result.sort()
for r in result:
    print(*r)