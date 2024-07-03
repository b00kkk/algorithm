#BOJ 1654
import sys
k,n=map(int,sys.stdin.readline().split())
line=[]
for i in range(k):
    line.append(int(sys.stdin.readline()))
line_max=int(sum(line)/n)
line_min=1
while line_min<=line_max:
    c=0
    mid=(line_min+line_max)//2
    for i in line:
        c+=(i//mid)
    if c<n:
        line_max=mid-1
    else:
        line_min=mid+1
print(line_max)