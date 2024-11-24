#BOJ 1183
import sys
input=sys.stdin.readline

N=int(input())


arr=[]
for _ in range(N):
    A,B=map(int,input().split())
    T=B-A
    arr.append([A,B])

dif=sorted([b-a for a,b in arr])
if N%2==1:
    mid=dif[N//2]
    min_t_c=1
else:
    mid1=dif[N//2-1]
    mid2=dif[N//2]
    min_t_c=mid2-mid1+1

print(min_t_c)