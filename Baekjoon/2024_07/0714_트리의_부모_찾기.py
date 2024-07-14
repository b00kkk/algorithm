#BOJ 11725
import sys
n=int(sys.stdin.readline())
tree=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=list(map(int,sys.stdin.readline().split()))
    tree[a].append(b)
    tree[b].append(a)

q=[1]
ans={}
check=[False for i in range(n+1)]

while len(q)>0:
    parent=q.pop(0)
    for i in tree[parent]:
        if check[i]==False:
            ans[i]=parent
            q.append(i)
            check[i]=True

for i in range(2,n+1):
    print(ans[i])