# BOJ 1931
import sys
n=int(sys.stdin.readline())
time=[]

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    time.append((a,b))

time.sort(key=lambda x: (x[1],x[0]))

t=0
c=0
for a,b in time:
    if a>=t:
        t=b
        c+=1
print(c)