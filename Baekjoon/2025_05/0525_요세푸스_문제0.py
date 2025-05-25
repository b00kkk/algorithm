import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())
n_list=list(range(1,n+1))
result=[]
index=0
while len(n_list)!=0:
    index+=(k-1)
    index=index%len(n_list)
    result.append(n_list.pop(index))
print("<",end='')
for i in range(n-1):
    print("%d,"%result[i],end=" ")
print("%d>"%result[-1])