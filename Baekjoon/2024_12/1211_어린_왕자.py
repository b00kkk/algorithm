#BOJ 1004
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    c=[]
    for _ in range(n):
        c.append(list(map(int,input().split())))

    cnt=0
    for cx,cy,r in c:
        d1=(cx-x1)**2+(cy-y1)**2
        d2=(cx-x2)**2+(cy-y2)**2
        if d1<r**2 and d2>r**2:
            cnt+=1
        elif d2<r**2 and d1>r**2:
            cnt+=1
    print(cnt)