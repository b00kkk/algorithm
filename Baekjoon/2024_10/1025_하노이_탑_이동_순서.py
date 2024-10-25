#BOJ 11729
import sys
input=sys.stdin.readline

N=int(input())

m=[]

def hanoi(N,A,B):
    if N==1:
        m.append((A,B))
        return
    hanoi(N-1,A,6-A-B)
    m.append((A,B))
    hanoi(N-1,6-A-B,B)

hanoi(N,1,3)
print(len(m))
for i in m:
    print(*i)