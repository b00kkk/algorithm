# BOJ 1712
import sys
input = sys.stdin.readline

A,B,C=map(int,input().split())

i=0
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)