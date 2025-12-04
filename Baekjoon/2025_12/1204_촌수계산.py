# BOJ 2644
import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input())
m=int(input())
p={}
for i in range(m):
    x,y=map(int,input())
    if x not in p:
        p[x]=[y]
    else:
        p[x].append(y)
    if y not in p:
        p[y]=[x]
    else:
        p[y].append(x)

ans={}
st=[a]

while st:
    node=st.pop()
    if node in ans:
        continue
    st.extend(p[node])
    if node==a:
        ans[node]=a
    else:
        for x in p[node]:
            if x in ans:
                ans[node]=x

if b not in ans:
    print(-1)
else:
    r=0
    while 1:
        b=ans[b]
        r+=1
        if b==a:
            break
    print(r)