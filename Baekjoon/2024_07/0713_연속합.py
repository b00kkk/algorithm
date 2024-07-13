#BOJ 1912
import sys
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))

c=num[0]
r=num[0]

for i in range(1,n):
    c=max(num[i],c+num[i])
    r=max(r,c)
    
print(r)