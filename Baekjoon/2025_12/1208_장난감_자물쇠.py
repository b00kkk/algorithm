# BOJ 32373
import sys
input=sys.stdin.readline

N,k=map(int,input().split())
A=list(map(int,input().split()))

S=sorted(A)
possible=True

for r in range(k):
    orig=[]
    targ=[]

    i=r
    while i<N:
        orig.append(A[i])
        targ.append(S[i])
        i+=k

    orig.sort()
    targ.sort()

    if orig!=targ:
        possible=False
        break

print('Yes' if possible else "No")