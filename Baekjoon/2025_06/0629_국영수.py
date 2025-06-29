# BOJ 10825
import sys
input = sys.stdin.readline

N=int(input())
score=[]
for _ in range(N):
    name,k,e,m=input().strip().split()
    score.append((name,int(k),int(e),int(m)))

sorted_score=sorted(score, key=lambda x: (-x[1],x[2],-x[3],x[0]))
for s in sorted_score:
    print(s[0])