# BOJ 30022
import sys
input=sys.stdin.readline

N,A,B=map(int,input().split())

charge=[]
sum_q=0

for _ in range(N):
    p,q=map(int,input().split())
    charge.append((p,q,p-q))
    sum_q+=q

charge.sort(key=lambda x:x[2])

ans=sum_q+sum(x[2] for x in charge[:A])
print(ans)