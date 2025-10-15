# BOJ 1166
import sys
input=sys.stdin.readline

N,L,W,H=map(int,input().split())

lower=0.0
high=float(min(L,W,H))

for _ in range(100):
    mid=(lower+high)/2.0
    if int(L//mid) * int(W//mid) * int(H//mid) >=N:
        lower=mid
    else:
        high = mid
    
print(lower)