# BOJ 1074

import sys
n,r,c=map(int,sys.stdin.readline().split())
def increase(n,r,c):
    if n==0:
        return 0
    return 2*(r%2)+(c%2)+4*(increase(n-1,r//2,c//2))

print(increase(n,r,c))