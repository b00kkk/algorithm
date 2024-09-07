#BOJ 1080
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
A=[]
B=[]
for _ in range(N):
    a=input().strip()
    lst =[int(i) for i in a] 
    A.append(lst)
for _ in range(N):
    b=input().strip()
    lst =[int(i) for i in b] 
    B.append(lst)

def convert(i,j):
    for k in range(i,i+3):
        for l in range(j,j+3):
            A[k][l]=1-A[k][l]

count=0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            convert(i,j)
            count+=1

if A!=B:
    print(-1)
else:
    print(count)