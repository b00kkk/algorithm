# BOJ 10844
import sys
input = sys.stdin.readline
n=int(input())
c=[0]+[1]*9

for _ in range(1,n):
    c=[sum(c[j] for j in (x+1,x-1) if 0<=j<10) for x in range(10)]
print(sum(c)%1000000000)