#BOJ 15666
import sys
from itertools import product
input=sys.stdin.readline

N,M=map(int,input().split())
arr=sorted(list(map(int,input().split())))

nHr = set(p for p in product(arr, repeat=M) if all(p[i] <= p[i+1] for i in range(M-1)))
nHr=sorted(nHr)

for i in nHr:
    print(' '.join(map(str,i)))