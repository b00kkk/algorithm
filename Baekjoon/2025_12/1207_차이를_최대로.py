import sys
from itertools import permutations
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
r=[]
for i in permutations(a,n):
    s=0
    for j in range(0,n-1):
        s+=abs(i[j]-i[j+1])
    r.append(s)
print(max(r))