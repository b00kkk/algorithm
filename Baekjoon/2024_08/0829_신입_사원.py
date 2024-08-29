#BOJ 1946
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    score=[]
    N=int(input())
    for _ in range(N):
        a,b=map(int,input().split())
        score.append([a,b])

    score.sort()
    a1=score[0][1]
    c=1

    for i in range(1,N):
        if score[i][1]<a1:
            c+=1
            a1=score[i][1]
    print(c)