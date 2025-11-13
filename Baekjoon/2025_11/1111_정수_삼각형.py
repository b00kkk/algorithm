# BOJ 1932
import sys
input = sys.stdin.readline
n=int(input())
triangle=[list(map(int,input().split())) for _ in range(n)]

a=triangle[0]
for h in range(1,n):
    cur=[]
    for w in range(h+1):
        if w==0:
            cur.append(a[0]+triangle[h][0])
        elif w==h:
            cur.append(a[-1]+triangle[h][-1])
        else:
            cur.append(max(a[w-1],a[w])+triangle[h][w])
    a=cur
print(max(a))
