import sys
n=int(sys.stdin.readline())
lst=[]
if n==0:
    print(0)
else:
    for i in range(n):
        r=int(sys.stdin.readline())
        lst.append(r)
    lst.sort()
    q=int(n*0.15+0.5)
    print(int((sum(lst[q:n-q])/(n-2*q))+0.5))