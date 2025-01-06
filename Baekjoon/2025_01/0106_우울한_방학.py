#BOJ 17392
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
H=list(map(int,input().split()))

S=sum(H)+N
result=0

if S<M:
    l=M-S
    q=l//(N+1)
    r=l%(N+1)

    for i in range(1,q+1):
        result+=i**2*(N+1)
    result+=(q+1)**2*r
print(result)